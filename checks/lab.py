"""Contrôles exécutés contre le lab démarré (make lab-up)."""

from __future__ import annotations

import http.client
import json
import os
import re
import socket
import ssl
import subprocess
import time
from datetime import datetime, timezone
from functools import lru_cache

from isms import ROOT

from .registry import Result, Skip, check

HOST = os.environ.get("LAB_HOST", "127.0.0.1")
PORT = int(os.environ.get("LAB_PORT", "8443"))
PROJECT = "kamapay-lab"
CA_FILE = ROOT / "lab/proxy/certs/server.crt"

# Comptes fictifs du jeu de données de test (lab/db/init/02-donnees-fictives.sql).
CLIENT_1 = {"msisdn": "237690004521", "pin": "1357", "wallet": 1, "id_number": "CMR100000451"}
CLIENT_2 = {"msisdn": "237690007788", "wallet": 2, "id_number": "CMR100000788"}

PII_PATTERNS = [re.compile(r"\b2376\d{8}\b"), re.compile(r"\bCMR\d{9}\b")]


def _tls_context(minimum=None, maximum=None) -> ssl.SSLContext:
    if not CA_FILE.exists():
        raise Skip("certificat du lab absent (make lab-up)")
    ctx = ssl.create_default_context(cafile=str(CA_FILE))
    if minimum:
        # Autorise le client à proposer d'anciennes versions pour tester le refus côté serveur.
        ctx.set_ciphers("DEFAULT:@SECLEVEL=0")
        ctx.minimum_version = minimum
    if maximum:
        ctx.maximum_version = maximum
    return ctx


def request(method: str, path: str, body: dict | None = None, token: str | None = None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    conn = http.client.HTTPSConnection(HOST, PORT, context=_tls_context(), timeout=10)
    try:
        conn.request(method, path, body=json.dumps(body) if body is not None else None, headers=headers)
        resp = conn.getresponse()
        raw = resp.read()
    except (ConnectionError, socket.timeout, OSError) as exc:
        raise Skip(f"lab injoignable sur {HOST}:{PORT} ({exc})") from exc
    finally:
        conn.close()
    try:
        payload = json.loads(raw) if raw else None
    except ValueError:
        payload = None
    return resp.status, {k.lower(): v for k, v in resp.getheaders()}, payload


@lru_cache(maxsize=1)
def client_token() -> str:
    """Jeton du client de test ; patiente si la limitation de débit est active."""
    deadline = time.monotonic() + 75
    while True:
        status, _, payload = request("POST", "/v1/auth/token",
                                     {"msisdn": CLIENT_1["msisdn"], "pin": CLIENT_1["pin"]})
        if status == 200:
            return payload["token"]
        if status != 429 or time.monotonic() > deadline:
            raise Skip(f"impossible d'obtenir un jeton de test (HTTP {status})")
        time.sleep(5)


def docker(*args: str) -> str:
    try:
        return subprocess.run(["docker", *args], check=True, capture_output=True, text=True).stdout
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise Skip(f"docker indisponible ou lab arrêté ({exc})") from exc


def containers() -> list[dict]:
    ids = docker("ps", "-q", "--filter", f"label=com.docker.compose.project={PROJECT}").split()
    if not ids:
        raise Skip("aucun conteneur du lab en cours d'exécution")
    return json.loads(docker("inspect", *ids))


def service(info: dict) -> str:
    return info["Config"]["Labels"]["com.docker.compose.service"]


# --- Cryptographie et configuration du point d'entrée ------------------------

@check("CHK-TLS-01", ["8.24", "5.14", "8.21"], "Seuls TLS 1.2 et TLS 1.3 sont acceptés", "lab")
def tls_versions() -> Result:
    accepted, refused = [], []
    for label, version in [("TLS 1.0", ssl.TLSVersion.TLSv1), ("TLS 1.1", ssl.TLSVersion.TLSv1_1),
                           ("TLS 1.2", ssl.TLSVersion.TLSv1_2), ("TLS 1.3", ssl.TLSVersion.TLSv1_3)]:
        ctx = _tls_context(minimum=version, maximum=version)
        try:
            with socket.create_connection((HOST, PORT), timeout=5) as sock:
                with ctx.wrap_socket(sock, server_hostname=HOST):
                    accepted.append(label)
        except ssl.SSLError:
            refused.append(label)
        except OSError as exc:
            raise Skip(f"lab injoignable ({exc})") from exc
    ok = accepted == ["TLS 1.2", "TLS 1.3"]
    return Result(ok, f"acceptés : {', '.join(accepted) or 'aucun'} ; refusés : {', '.join(refused) or 'aucun'}")


@check("CHK-TLS-02", ["8.24", "8.21"], "HSTS actif et certificat valide plus de 14 jours", "lab")
def hsts_and_certificate() -> Result:
    _, headers, _ = request("GET", "/health")
    hsts = headers.get("strict-transport-security", "")
    max_age = int(m.group(1)) if (m := re.search(r"max-age=(\d+)", hsts)) else 0
    with socket.create_connection((HOST, PORT), timeout=5) as sock:
        with _tls_context().wrap_socket(sock, server_hostname=HOST) as tls:
            not_after = ssl.cert_time_to_seconds(tls.getpeercert()["notAfter"])
    days_left = int((not_after - datetime.now(timezone.utc).timestamp()) // 86400)
    ok = max_age >= 15552000 and days_left > 14
    return Result(ok, f"HSTS max-age={max_age} s ; certificat valide encore {days_left} jours")


@check("CHK-HTTP-01", ["8.9"], "En-têtes de sécurité présents, version du serveur masquée", "lab")
def security_headers() -> Result:
    _, headers, _ = request("GET", "/health")
    expected = {
        "x-content-type-options": "nosniff",
        "x-frame-options": "DENY",
        "content-security-policy": "default-src 'none'",
        "referrer-policy": "no-referrer",
        "cache-control": "no-store",
    }
    missing = [h for h, v in expected.items() if v not in headers.get(h, "")]
    server = headers.get("server", "")
    if re.search(r"\d", server):
        missing.append(f"server divulgue sa version ({server})")
    return Result(not missing, "conforme" if not missing else "manquant : " + ", ".join(missing))


# --- Authentification et autorisation ----------------------------------------

@check("CHK-AUTH-01", ["8.5", "5.15", "8.29"], "Les routes protégées refusent l'accès sans jeton valide", "lab")
def authentication_required() -> Result:
    no_token, _, _ = request("GET", f"/v1/wallets/{CLIENT_1['wallet']}")
    forged, _, _ = request("GET", f"/v1/wallets/{CLIENT_1['wallet']}", token="eyJ3YWxsZXRfaWQiOjF9.forge.forge")
    transfer, _, _ = request("POST", "/v1/transfers", {"to_msisdn": CLIENT_2["msisdn"], "amount": 100})
    ok = (no_token, forged, transfer) == (401, 401, 401)
    return Result(ok, f"sans jeton : {no_token}, jeton forgé : {forged}, virement sans jeton : {transfer}")


@check("CHK-AUTHZ-01", ["8.3", "5.18", "8.28", "8.29"],
       "Un client ne peut pas lire le portefeuille d'un autre client (BOLA)", "lab")
def object_level_authorization() -> Result:
    token = client_token()
    own, _, _ = request("GET", f"/v1/wallets/{CLIENT_1['wallet']}", token=token)
    other, _, _ = request("GET", f"/v1/wallets/{CLIENT_2['wallet']}", token=token)
    return Result(own == 200 and other == 403, f"son portefeuille : {own}, portefeuille d'un tiers : {other}")


@check("CHK-MASK-01", ["8.11", "5.34"], "MSISDN et numéro de pièce d'identité masqués dans l'API", "lab")
def data_masking() -> Result:
    status, _, payload = request("GET", f"/v1/wallets/{CLIENT_1['wallet']}", token=client_token())
    if status != 200:
        return Result(False, f"lecture du portefeuille impossible (HTTP {status})")
    owner = payload["owner"]
    raw = json.dumps(payload)
    leaks = [p.pattern for p in PII_PATTERNS if p.search(raw)]
    ok = not leaks and "*" in owner["msisdn"] and "*" in owner["id_number"]
    return Result(ok, f"msisdn={owner['msisdn']}, id_number={owner['id_number']}"
                  + (f" ; fuite : {leaks}" if leaks else ""))


@check("CHK-RATE-01", ["8.5", "8.16"], "La force brute sur l'authentification est limitée (HTTP 429)", "lab")
def brute_force_limited() -> Result:
    statuses = [request("POST", "/v1/auth/token", {"msisdn": CLIENT_2["msisdn"], "pin": f"{n:04d}"})[0]
                for n in range(12)]
    first_429 = statuses.index(429) + 1 if 429 in statuses else None
    ok = first_429 is not None and first_429 <= 7
    return Result(ok, f"{statuses.count(429)} réponses 429 sur 12 essais"
                  + (f", blocage dès la tentative {first_429}" if first_429 else ""))


# --- Journalisation ------------------------------------------------------------

@check("CHK-LOG-01", ["8.15", "5.28"], "Journal d'audit structuré, sans donnée personnelle en clair", "lab")
def audit_log() -> Result:
    client_token()  # garantit au moins un événement d'authentification
    api = next((c for c in containers() if service(c) == "api"), None)
    if api is None:
        raise Skip("conteneur api absent")
    logs = docker("logs", "--since", "30m", api["Id"])
    events, invalid = [], 0
    for line in logs.splitlines():
        if '"type": "audit"' not in line:
            continue
        try:
            events.append(json.loads(line))
        except ValueError:
            invalid += 1
    incomplete = [e for e in events if not {"ts", "event", "outcome", "source_ip"} <= e.keys()]
    leaks = sum(1 for e in events if any(p.search(json.dumps(e)) for p in PII_PATTERNS))
    ok = bool(events) and not incomplete and not invalid and not leaks
    return Result(ok, f"{len(events)} événements d'audit, {len(incomplete)} incomplets, "
                      f"{invalid} non JSON, {leaks} avec donnée personnelle en clair")


# --- Base de données et conteneurs ---------------------------------------------

@check("CHK-DB-01", ["8.2", "8.3"], "Le rôle applicatif n'a ni privilège d'administration ni droit de suppression", "lab")
def database_least_privilege() -> Result:
    db = next((c for c in containers() if service(c) == "db"), None)
    if db is None:
        raise Skip("conteneur db absent")
    sql = """
      SELECT rolsuper OR rolcreaterole OR rolcreatedb OR rolreplication OR rolbypassrls,
             (SELECT string_agg(t || ':' || p, ',')
                FROM unnest(ARRAY['customers','wallets','transactions']) AS t,
                     unnest(ARRAY['DELETE','TRUNCATE']) AS p
               WHERE has_table_privilege('kamapay_app', t, p)),
             has_column_privilege('kamapay_app', 'wallets', 'balance', 'UPDATE'),
             has_column_privilege('kamapay_app', 'customers', 'pin_hash', 'UPDATE')
        FROM pg_roles WHERE rolname = 'kamapay_app'"""
    out = docker("exec", db["Id"], "psql", "-U", "kamapay_admin", "-d", "kamapay", "-At", "-F", ";", "-c", sql).strip()
    admin, forbidden, balance_update, pin_update = out.split(";")
    ok = admin == "f" and not forbidden and balance_update == "t" and pin_update == "f"
    return Result(ok, f"privilège d'administration : {admin}, droits interdits : {forbidden or 'aucun'}, "
                      f"modification du PIN : {pin_update}")


@check("CHK-NET-01", ["8.20", "8.22"], "La base n'est joignable que depuis le réseau interne", "lab")
def network_segmentation() -> Result:
    infos = containers()
    db = next((c for c in infos if service(c) == "db"), None)
    if db is None:
        raise Skip("conteneur db absent")
    published = {s: [p for p, b in (c["NetworkSettings"]["Ports"] or {}).items() if b] for c in infos
                 for s in [service(c)]}
    networks = list(db["NetworkSettings"]["Networks"])
    internal = all(json.loads(docker("network", "inspect", n))[0]["Internal"] for n in networks)
    try:
        with socket.create_connection(("127.0.0.1", 5432), timeout=2):
            reachable = True
    except OSError:
        reachable = False
    exposed = sorted(s for s, ports in published.items() if ports)
    ok = exposed == ["proxy"] and internal and not reachable
    return Result(ok, f"services publiés : {', '.join(exposed)} ; réseaux de la base internes : {internal} ; "
                      f"port 5432 joignable depuis l'hôte : {reachable}")


@check("CHK-CTR-01", ["8.9", "8.19"], "Conteneurs durcis : non-root, lecture seule, sans capacité", "lab")
def container_hardening() -> Result:
    problems, infos = [], containers()
    for c in infos:
        name, host = service(c), c["HostConfig"]
        user = c["Config"]["User"].split(":")[0]
        if user in ("", "0", "root"):
            problems.append(f"{name} : exécuté en root")
        if host["Privileged"]:
            problems.append(f"{name} : privilégié")
        if not host["ReadonlyRootfs"]:
            problems.append(f"{name} : système de fichiers inscriptible")
        if "ALL" not in (host.get("CapDrop") or []):
            problems.append(f"{name} : capacités non retirées")
        if not any("no-new-privileges" in o for o in host.get("SecurityOpt") or []):
            problems.append(f"{name} : no-new-privileges absent")
    return Result(not problems, f"{len(infos)} conteneurs conformes" if not problems else "; ".join(problems))
