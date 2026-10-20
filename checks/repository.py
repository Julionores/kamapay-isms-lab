"""Contrôles exécutés sur le dépôt et sur les rapports produits par les outils."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone

from isms import ROOT
from isms.data import load
from isms.validate import check_documents, overdue_documents

from .registry import Result, Skip, check

REPORTS = ROOT / "reports"

SECRET_PATTERNS = {
    "clé privée": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "clé d'accès AWS": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "jeton GitHub": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    "jeton Slack": re.compile(r"\bxox[abpr]-[A-Za-z0-9-]{10,}\b"),
    "mot de passe en dur": re.compile(
        # ":'variable'" est une interpolation psql, pas une valeur en dur.
        r"(?i)\b(?:password|passwd|secret|api_key)\b['\"]?\s*(?:=|:(?!'))\s*['\"][^'\"$\s{}]{8,}['\"]"),
    "chaîne de connexion avec mot de passe": re.compile(r"postgres(?:ql)?://[^:\s/]+:(?!\$\{)[^@\s]{6,}@"),
}
MUST_BE_IGNORED = ["lab/.env", "lab/proxy/certs/server.key"]


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


@check("CHK-SECRET-01", ["5.17", "8.4"], "Aucun secret dans les fichiers versionnés", "depot")
def no_secrets() -> Result:
    listing = _git("ls-files", "--cached", "--others", "--exclude-standard")
    if listing.returncode != 0:
        raise Skip("dépôt git introuvable")
    findings = []
    for rel in listing.stdout.splitlines():
        path = ROOT / rel
        if not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{rel}:{line} ({label})")
    not_ignored = [p for p in MUST_BE_IGNORED if _git("check-ignore", "-q", p).returncode != 0]
    findings += [f"{p} n'est pas exclu par .gitignore" for p in not_ignored]
    files = len(listing.stdout.splitlines())
    return Result(not findings, f"{files} fichiers analysés, aucun secret" if not findings else "; ".join(findings))


@check("CHK-DOC-01", ["5.1", "5.36", "5.37"], "Documents du SMSI identifiés, approuvés et revus dans les délais", "depot")
def documentation_governance() -> Result:
    isms, today = load(), date.today()
    errors = check_documents(isms, today)
    overdue = overdue_documents(isms, today)
    managed = sum(1 for d in isms.documents if d.meta)
    problems = errors + [f"revue échue : {p}" for p in overdue]
    return Result(not problems, f"{managed} documents maîtrisés, revues à jour" if not problems
                  else f"{len(problems)} écart(s) : " + "; ".join(problems[:5]))


@check("CHK-SAST-01", ["8.25", "8.28"], "Analyse statique du code de l'API sans défaut de sévérité haute", "depot")
def static_analysis() -> Result:
    proc = subprocess.run([sys.executable, "-m", "bandit", "-r", str(ROOT / "lab/api"), "-f", "json", "-q"],
                          capture_output=True, text=True)
    if not proc.stdout.strip():
        raise Skip("bandit non installé (pip install -r requirements-dev.txt)")
    report = json.loads(proc.stdout)
    REPORTS.mkdir(exist_ok=True)
    (REPORTS / "bandit.json").write_text(proc.stdout, encoding="utf-8")
    by_severity = {s: sum(1 for r in report["results"] if r["issue_severity"] == s) for s in ("HIGH", "MEDIUM", "LOW")}
    return Result(by_severity["HIGH"] == 0,
                  f"{report['metrics']['_totals']['loc']} lignes analysées ; sévérité haute : {by_severity['HIGH']}, "
                  f"moyenne : {by_severity['MEDIUM']}, basse : {by_severity['LOW']}")


@check("CHK-VULN-01", ["8.8"], "Image de l'API sans vulnérabilité critique corrigeable (Trivy)", "rapport")
def vulnerabilities() -> Result:
    path = REPORTS / "trivy.json"
    if not path.exists():
        raise Skip("reports/trivy.json absent (make scan)")
    report = json.loads(path.read_text(encoding="utf-8"))
    vulns = [v for r in report.get("Results", []) for v in r.get("Vulnerabilities") or []]
    critical = sorted({v["VulnerabilityID"] for v in vulns if v["Severity"] == "CRITICAL"})
    high = {v["VulnerabilityID"] for v in vulns if v["Severity"] == "HIGH"}
    scanned = report.get("CreatedAt", "")[:10]
    return Result(not critical, f"scan du {scanned} : {len(critical)} critique(s), {len(high)} haute(s) "
                                f"(correctifs disponibles uniquement)" + (f" : {', '.join(critical)}" if critical else ""))


@check("CHK-BKP-01", ["8.13", "5.30"], "Test de restauration réussi depuis moins de 7 jours", "rapport")
def restore_test() -> Result:
    path = REPORTS / "restauration.json"
    if not path.exists():
        raise Skip("reports/restauration.json absent (make restore-test)")
    result = json.loads(path.read_text(encoding="utf-8"))
    age = datetime.now(timezone.utc) - datetime.fromisoformat(result["date"])
    ok = result["succes"] and age < timedelta(days=7) and result["duree_totale_s"] < 900
    return Result(ok, f"test du {result['date'][:10]} : {'intègre' if result['succes'] else 'ÉCHEC'}, "
                      f"restauration en {result['duree_restauration_s']} s")
