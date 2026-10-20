"""Contrôles de cohérence du SMSI.

Chaque règle traduit une exigence d'ISO/IEC 27001:2022 ; une erreur bloque la CI.
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from . import annexe_a, risk
from .data import Isms, parse_date, parse_datetime

SCHEMAS = {
    "actifs": "actifs.schema.json",
    "risques": "risques.schema.json",
    "soa": "soa.schema.json",
    "incidents": "incidents.schema.json",
    "sensibilisation": "sensibilisation.schema.json",
    "historique": "historique-kpi.schema.json",
}

_LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def _schema(root: Path, name: str) -> Draft202012Validator:
    schema = json.loads((root / "schemas" / name).read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_errors(validator: Draft202012Validator, instance, label: str) -> list[str]:
    return [
        f"{label} : {'/'.join(map(str, e.absolute_path)) or '(racine)'} : {e.message}"
        for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    ]


def _duplicates(ids: list[str]) -> set[str]:
    return {i for i in ids if ids.count(i) > 1}


def check_schemas(isms: Isms) -> list[str]:
    errors = []
    for attr, schema in SCHEMAS.items():
        errors += _schema_errors(_schema(isms.root, schema), getattr(isms, attr), f"data/{attr}.yaml")
    return errors


def check_soa(isms: Isms, known_checks: set[str]) -> list[str]:
    """Clause 6.1.3 d) : les 93 mesures, avec statut, justification et preuves."""
    errors = []
    ids = [c["id"] for c in isms.soa["controles"]]
    for dup in sorted(_duplicates(ids)):
        errors.append(f"SoA : mesure {dup} déclarée plusieurs fois")
    missing = set(annexe_a.CONTROL_IDS) - set(ids)
    unknown = set(ids) - set(annexe_a.CONTROL_IDS)
    errors += [f"SoA : mesure {c} de l'annexe A absente" for c in sorted(missing, key=annexe_a.sort_key)]
    errors += [f"SoA : mesure {c} inconnue de l'annexe A" for c in sorted(unknown)]

    for c in isms.soa["controles"]:
        cid, statut = c["id"], c["statut"]
        if statut == "non_applicable" and not c.get("justification"):
            errors.append(f"SoA {cid} : une exclusion doit être justifiée")
        if statut in ("partiel", "planifie") and not c.get("ecart"):
            errors.append(f"SoA {cid} : statut {statut} sans description de l'écart")
        if statut == "implemente" and not c["preuves"]:
            errors.append(f"SoA {cid} : mesure implémentée sans preuve")
        for proof in c["preuves"]:
            if not proof.startswith("ext:") and not (isms.root / proof).exists():
                errors.append(f"SoA {cid} : preuve introuvable : {proof}")
        for chk in c.get("checks", []):
            if chk not in known_checks:
                errors.append(f"SoA {cid} : contrôle automatisé inconnu : {chk}")
    return errors


def check_risks(isms: Isms, today: date) -> list[str]:
    """Clauses 6.1.2 et 6.1.3 : actifs, mesures et acceptation des risques résiduels."""
    errors = []
    assets, controls = isms.assets, isms.controls
    errors += [f"Risques : identifiant {d} en double" for d in _duplicates([r["id"] for r in isms.risks])]
    errors += [f"Plan d'actions : identifiant {d} en double" for d in _duplicates([a["id"] for a in isms.actions])]

    for r in isms.risks:
        rid = r["id"]
        for a in r["actifs"]:
            if a not in assets:
                errors.append(f"Risque {rid} : actif inconnu {a}")
        for cid in r["controles"]:
            if cid not in controls:
                errors.append(f"Risque {rid} : mesure {cid} absente de la SoA")
            elif controls[cid]["statut"] == "non_applicable":
                errors.append(f"Risque {rid} : traité par la mesure {cid} pourtant exclue de la SoA")
        if risk.score(r["residuel"]) > risk.score(r["brut"]):
            errors.append(f"Risque {rid} : le risque résiduel dépasse le risque brut")
        if risk.needs_acceptance(r) and "acceptation" not in r:
            errors.append(
                f"Risque {rid} : résiduel {risk.score(r['residuel'])} > appétence {risk.APPETITE} "
                "sans acceptation formelle de la direction"
            )
    return errors


def check_incidents(isms: Isms) -> list[str]:
    """Contrôles 5.24 à 5.27 : registre cohérent et chronologie plausible."""
    errors = []
    assets, risk_ids = isms.assets, {r["id"] for r in isms.risks}
    action_ids = {a["id"] for a in isms.actions}
    incidents = isms.incidents["incidents"]
    errors += [f"Incidents : identifiant {d} en double" for d in _duplicates([i["id"] for i in incidents])]

    for inc in incidents:
        iid = inc["id"]
        errors += [f"Incident {iid} : actif inconnu {a}" for a in inc["actifs"] if a not in assets]
        errors += [f"Incident {iid} : risque inconnu {r}" for r in inc["risques"] if r not in risk_ids]
        errors += [f"Incident {iid} : action inconnue {a}" for a in inc.get("actions", []) if a not in action_ids]
        steps = [(k, inc.get(k)) for k in ("debut", "detection", "confinement", "cloture")]
        stamps = [(k, parse_datetime(v)) for k, v in steps if v]
        for (k1, t1), (k2, t2) in zip(stamps, stamps[1:]):
            if t2 < t1:
                errors.append(f"Incident {iid} : {k2} antérieur à {k1}")
        if inc["statut"] == "clos" and not inc.get("cloture"):
            errors.append(f"Incident {iid} : clos sans date de clôture")
        if inc["statut"] == "clos" and not inc.get("enseignements"):
            errors.append(f"Incident {iid} : clos sans retour d'expérience (5.27)")
    return errors


def check_history(isms: Isms, today: date) -> list[str]:
    """Clause 9.1 : relevés datés, uniques et chronologiques."""
    dates = [r["date"] for r in isms.historique["releves"]]
    errors = [f"Historique : plusieurs relevés le {d}" for d in sorted(_duplicates(dates))]
    if dates != sorted(dates):
        errors.append("Historique : relevés hors ordre chronologique")
    errors += [f"Historique : relevé daté dans le futur ({d})" for d in dates if parse_date(d) > today]
    return errors


def check_documents(isms: Isms, today: date) -> list[str]:
    """Clause 7.5 : informations documentées identifiées, approuvées, revues et liées."""
    errors = []
    validator = _schema(isms.root, "document.schema.json")
    controls = isms.controls
    seen_ids: dict[str, str] = {}

    for doc in isms.documents:
        for target in _LINK.findall(doc.body):
            if "://" in target or target.startswith("mailto:"):
                continue
            if not (doc.path.parent / target).resolve().exists():
                errors.append(f"{doc.rel} : lien cassé vers {target}")
        if doc.generated:
            continue
        if doc.meta is None:
            errors.append(f"{doc.rel} : en-tête de métadonnées absent")
            continue
        schema_errors = _schema_errors(validator, doc.meta, doc.rel)
        errors += schema_errors
        if schema_errors:
            continue
        if doc.meta["id"] in seen_ids:
            errors.append(f"{doc.rel} : identifiant {doc.meta['id']} déjà utilisé par {seen_ids[doc.meta['id']]}")
        seen_ids[doc.meta["id"]] = doc.rel
        for cid in doc.meta["controles_iso"]:
            if cid not in controls:
                errors.append(f"{doc.rel} : mesure {cid} absente de la SoA")
        approved, review = parse_date(doc.meta["date_approbation"]), parse_date(doc.meta["prochaine_revue"])
        if review <= approved:
            errors.append(f"{doc.rel} : prochaine revue antérieure à l'approbation")
        if approved > today:
            errors.append(f"{doc.rel} : date d'approbation dans le futur")
    return errors


def overdue_documents(isms: Isms, today: date) -> list[str]:
    return [
        doc.rel for doc in isms.documents
        if doc.meta and "prochaine_revue" in doc.meta and parse_date(doc.meta["prochaine_revue"]) < today
    ]


def validate(isms: Isms, known_checks: set[str], today: date) -> list[str]:
    errors = check_schemas(isms)
    if errors:  # les règles suivantes supposent des données bien formées
        return errors
    return (
        check_soa(isms, known_checks)
        + check_risks(isms, today)
        + check_incidents(isms)
        + check_history(isms, today)
        + check_documents(isms, today)
    )
