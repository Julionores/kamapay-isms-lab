"""Indicateurs du SMSI (clause 9.1). Définitions : docs/08-pilotage/indicateurs-smsi.md"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from statistics import mean

from . import risk
from .data import Isms, parse_date, parse_datetime
from .validate import overdue_documents


@dataclass
class Kpi:
    id: str
    libelle: str
    valeur: float | None
    unite: str
    cible: str
    atteint: bool | None
    detail: str = ""

    def formatted(self) -> str:
        if self.valeur is None:
            return "n.d."
        if self.unite == "%":
            return f"{self.valeur:.1f} %"
        if self.unite == "h":
            return f"{self.valeur:.2f} h"
        return f"{self.valeur:g}"


def _pct(num: int, den: int) -> float | None:
    return round(100 * num / den, 1) if den else None


def _hours(start: str, end: str) -> float:
    return (parse_datetime(end) - parse_datetime(start)).total_seconds() / 3600


def compute(isms: Isms, today: date, checks_report: dict | None) -> list[Kpi]:
    applicable = [c for c in isms.soa["controles"] if c["statut"] != "non_applicable"]
    implemented = [c for c in applicable if c["statut"] == "implemente"]

    kpis = [
        Kpi("KPI-01", "Mesures applicables implémentées", _pct(len(implemented), len(applicable)), "%", "≥ 85 %",
            None, f"{len(implemented)} sur {len(applicable)}"),
    ]

    if checks_report:
        results = checks_report["resultats"]
        passed = sum(1 for r in results if r["statut"] == "PASS")
        kpis.append(Kpi("KPI-02", "Contrôles automatisés conformes", _pct(passed, len(results)), "%", "100 %",
                        None, f"{passed} sur {len(results)} (exécution du {checks_report['date'][:10]})"))
    else:
        kpis.append(Kpi("KPI-02", "Contrôles automatisés conformes", None, "%", "100 %", None,
                        "reports/checks.json absent : lancer `make checks`"))

    unaccepted = [r["id"] for r in isms.risks if risk.needs_acceptance(r) and "acceptation" not in r]
    kpis.append(Kpi("KPI-03", "Risques au-delà de l'appétence non acceptés", len(unaccepted), "", "0", None,
                    ", ".join(unaccepted) or "aucun"))

    late = sorted(a["id"] for a in isms.actions if a["statut"] != "termine" and parse_date(a["echeance"]) < today)
    kpis.append(Kpi("KPI-04", "Actions de traitement en retard", len(late), "", "0", None, ", ".join(late) or "aucune"))

    major = [i for i in isms.incidents["incidents"] if i["gravite"] in ("P1", "P2")]
    detect = [_hours(i["debut"], i["detection"]) for i in major]
    contain = [_hours(i["detection"], i["confinement"]) for i in major if i.get("confinement")]
    kpis.append(Kpi("KPI-05", "Délai moyen de détection (P1/P2)", round(mean(detect), 2) if detect else None, "h",
                    "< 4 h", None, f"{len(detect)} incidents"))
    kpis.append(Kpi("KPI-06", "Délai moyen de confinement (P1/P2)", round(mean(contain), 2) if contain else None, "h",
                    "< 4 h", None, f"{len(contain)} incidents"))

    campaigns = isms.sensibilisation["campagnes"]
    trained, target = sum(c["formes"] for c in campaigns), sum(c["cible"] for c in campaigns)
    kpis.append(Kpi("KPI-07", "Taux de formation (toutes campagnes)", _pct(trained, target), "%", "≥ 90 %", None,
                    f"{trained} sur {target}"))

    last = max(isms.sensibilisation["hameconnage_simule"], key=lambda p: p["date"])
    kpis.append(Kpi("KPI-08", "Taux de clic, dernier hameçonnage simulé", _pct(last["clics"], last["envoyes"]), "%",
                    "< 10 %", None, last["id"]))
    kpis.append(Kpi("KPI-09", "Taux de signalement, dernier hameçonnage simulé",
                    _pct(last["signalements"], last["envoyes"]), "%", "≥ 30 %", None, last["id"]))

    managed = [d for d in isms.documents if d.meta]
    overdue = overdue_documents(isms, today)
    kpis.append(Kpi("KPI-10", "Documents dont la revue est à jour", _pct(len(managed) - len(overdue), len(managed)),
                    "%", "100 %", None, f"{len(managed) - len(overdue)} sur {len(managed)}"))

    for k in kpis:
        k.atteint = _target_met(k)
    return kpis


def _target_met(k: Kpi) -> bool | None:
    if k.valeur is None:
        return None
    match = re.match(r"^(≥|<)?\s*([0-9.]+)", k.cible)
    op, threshold = match.group(1), float(match.group(2))
    if op == "≥":
        return k.valeur >= threshold
    if op == "<":
        return k.valeur < threshold
    return k.valeur == threshold


def to_json(kpis: list[Kpi]) -> str:
    return json.dumps([asdict(k) for k in kpis], indent=2, ensure_ascii=False)
