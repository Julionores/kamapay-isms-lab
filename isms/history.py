"""Historique des indicateurs (clause 9.1 : conserver les résultats de la surveillance).

Chaque relevé fige, à une date donnée, la valeur des indicateurs et le résultat des
contrôles automatisés. La CI ajoute un relevé chaque lundi (data/historique-kpi.yaml) ;
un relevé n'est jamais modifié a posteriori, sauf s'il est refait le même jour.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml

from .kpi import Kpi

HEADER = """\
# Historique des indicateurs du SMSI (clause 9.1 d'ISO/IEC 27001:2022).
# Fichier alimenté par `python -m isms history` (chaque lundi par la CI) : ne pas modifier à la main.
# Définitions des indicateurs : docs/08-pilotage/indicateurs-smsi.md
"""


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data.get("releves", [])


def entry(kpis: list[Kpi], checks_report: dict | None, today: date, source: str, commit: str | None) -> dict:
    record = {"date": today.isoformat(), "source": source}
    if commit:
        record["commit"] = commit[:12]
    record["indicateurs"] = {k.id: k.valeur for k in kpis}
    if checks_report:
        results = checks_report["resultats"]
        record["controles"] = {
            "conformes": sum(1 for r in results if r["statut"] == "PASS"),
            "total": len(results),
            "non_conformes": sorted(r["id"] for r in results if r["statut"] != "PASS"),
        }
    return record


def record(path: Path, new: dict) -> list[dict]:
    """Ajoute le relevé ; un relevé existant à la même date est remplacé."""
    entries = [e for e in load(path) if e["date"] != new["date"]] + [new]
    entries.sort(key=lambda e: e["date"])
    body = yaml.safe_dump({"releves": entries}, allow_unicode=True, sort_keys=False, default_flow_style=None)
    path.write_text(HEADER + body, encoding="utf-8")
    return entries


def direction(kpi: Kpi) -> int:
    """+1 si une hausse est une amélioration, -1 si c'est une baisse."""
    return -1 if kpi.cible.startswith("<") or kpi.cible.strip() == "0" else 1


def trend(kpi: Kpi, previous: float | None) -> str:
    if kpi.valeur is None or previous is None:
        return "-"
    delta = kpi.valeur - previous
    if abs(delta) < 1e-9:
        return "stable"
    sign = "+" if delta > 0 else "-"
    label = "amélioration" if delta * direction(kpi) > 0 else "**dégradation**"
    return f"{label} ({sign}{abs(delta):g})"
