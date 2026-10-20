"""API de portefeuille mobile du lab KamaPay.

Volontairement minimale : elle sert de cible aux contrôles automatisés
(checks/) qui vérifient en continu les mesures de l'annexe A d'ISO 27001 :
authentification (8.5), autorisation au niveau objet (8.3), masquage (8.11)
et journal d'audit sans donnée personnelle en clair (8.15).
"""

import hashlib
import json
import logging
import os
import sys
from datetime import datetime, timezone

import psycopg
from flask import Flask, abort, g, jsonify, request
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from werkzeug.security import check_password_hash

TOKEN_TTL_SECONDS = 900

app = Flask(__name__)
serializer = URLSafeTimedSerializer(os.environ["API_SECRET_KEY"], salt="kamapay-token")

audit = logging.getLogger("audit")
audit.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter("%(message)s"))
audit.addHandler(_handler)
audit.propagate = False


def db():
    if "db" not in g:
        g.db = psycopg.connect(os.environ["DATABASE_URL"], autocommit=False)
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()


def pseudonymise(value: str) -> str:
    """Identifiant stable pour corréler les journaux sans exposer le MSISDN."""
    return hashlib.sha256(value.encode()).hexdigest()[:16]


def mask_msisdn(msisdn: str) -> str:
    return f"{msisdn[:4]}****{msisdn[-4:]}"


def mask_id_number(id_number: str) -> str:
    return f"{id_number[:3]}{'*' * (len(id_number) - 6)}{id_number[-3:]}"


def audit_event(event: str, outcome: str, **fields):
    record = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "type": "audit",
        "event": event,
        "outcome": outcome,
        "source_ip": request.headers.get("X-Real-IP", request.remote_addr),
        **fields,
    }
    audit.info(json.dumps(record, ensure_ascii=False))


def current_wallet_id() -> int:
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        abort(401)
    try:
        claims = serializer.loads(header[7:], max_age=TOKEN_TTL_SECONDS)
    except (BadSignature, SignatureExpired):
        abort(401)
    return claims["wallet_id"]


@app.errorhandler(401)
def unauthorized(_e):
    return jsonify(error="authentification requise"), 401


@app.errorhandler(403)
def forbidden(_e):
    return jsonify(error="accès refusé"), 403


@app.errorhandler(404)
def not_found(_e):
    return jsonify(error="ressource introuvable"), 404


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/v1/auth/token")
def issue_token():
    body = request.get_json(silent=True) or {}
    msisdn, pin = str(body.get("msisdn", "")), str(body.get("pin", ""))
    row = db().execute(
        "SELECT w.id, c.pin_hash FROM customers c JOIN wallets w ON w.customer_id = c.id "
        "WHERE c.msisdn = %s",
        (msisdn,),
    ).fetchone()
    if row is None or not check_password_hash(row[1], pin):
        audit_event("auth.token", "echec", subject=pseudonymise(msisdn))
        return jsonify(error="identifiants invalides"), 401
    audit_event("auth.token", "succes", subject=pseudonymise(msisdn), wallet_id=row[0])
    return jsonify(token=serializer.dumps({"wallet_id": row[0]}), expires_in=TOKEN_TTL_SECONDS)


@app.get("/v1/wallets/<int:wallet_id>")
def get_wallet(wallet_id: int):
    caller = current_wallet_id()
    if caller != wallet_id:
        # Autorisation au niveau objet : un client ne lit que son propre portefeuille.
        audit_event("wallet.read", "refus", wallet_id=wallet_id, caller_wallet=caller)
        abort(403)
    row = db().execute(
        "SELECT w.id, w.balance, w.currency, c.full_name, c.msisdn, c.id_number "
        "FROM wallets w JOIN customers c ON c.id = w.customer_id WHERE w.id = %s",
        (wallet_id,),
    ).fetchone()
    if row is None:
        abort(404)
    audit_event("wallet.read", "succes", wallet_id=wallet_id)
    return jsonify(
        wallet_id=row[0],
        balance=row[1],
        currency=row[2],
        owner={"name": row[3], "msisdn": mask_msisdn(row[4]), "id_number": mask_id_number(row[5])},
    )


@app.post("/v1/transfers")
def transfer():
    caller = current_wallet_id()
    body = request.get_json(silent=True) or {}
    to_msisdn = str(body.get("to_msisdn", ""))
    amount = body.get("amount")
    if not isinstance(amount, int) or amount <= 0:
        return jsonify(error="montant invalide"), 400

    conn = db()
    with conn.transaction():
        target = conn.execute(
            "SELECT w.id FROM wallets w JOIN customers c ON c.id = w.customer_id WHERE c.msisdn = %s",
            (to_msisdn,),
        ).fetchone()
        if target is None or target[0] == caller:
            return jsonify(error="bénéficiaire invalide"), 400
        debited = conn.execute(
            "UPDATE wallets SET balance = balance - %s WHERE id = %s AND balance >= %s RETURNING id",
            (amount, caller, amount),
        ).fetchone()
        if debited is None:
            audit_event("transfer", "refus_solde", from_wallet=caller, amount=amount)
            return jsonify(error="solde insuffisant"), 409
        conn.execute("UPDATE wallets SET balance = balance + %s WHERE id = %s", (amount, target[0]))
        tx_id = conn.execute(
            "INSERT INTO transactions (from_wallet, to_wallet, amount) VALUES (%s, %s, %s) RETURNING id",
            (caller, target[0], amount),
        ).fetchone()[0]
    audit_event("transfer", "succes", transaction_id=tx_id, from_wallet=caller,
                to_wallet=target[0], amount=amount)
    return jsonify(transaction_id=tx_id, status="execute"), 201
