"""Point d'entrée : python -m isms {validate,render,kpi}."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from checks.registry import REGISTRY

from . import ROOT, history, kpi, render
from .data import load
from .validate import validate

CHECKS_REPORT = ROOT / "reports" / "checks.json"
RESTORE_REPORT = ROOT / "reports" / "restauration.json"
HISTORY = ROOT / "data" / "historique-kpi.yaml"


def _checks_report() -> dict | None:
    return json.loads(CHECKS_REPORT.read_text(encoding="utf-8")) if CHECKS_REPORT.exists() else None


def _write(path: Path, content: str, check_only: bool) -> bool:
    """Écrit le fichier ; en mode --check, signale seulement s'il n'est pas à jour."""
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return True
    if check_only:
        print(f"PAS À JOUR : {path.relative_to(ROOT)} (lancer `make render`)")
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"généré : {path.relative_to(ROOT)}")
    return True


def cmd_validate(args) -> int:
    errors = validate(load(), set(REGISTRY), args.date)
    for e in errors:
        print(f"ERREUR : {e}")
    if errors:
        print(f"\n{len(errors)} erreur(s) de cohérence.")
        return 1
    print("SMSI cohérent : schémas, SoA (93 mesures), risques, incidents et documents valides.")
    return 0


def cmd_render(args) -> int:
    isms = load()
    soa_path = ROOT / "docs/03-soa/declaration-applicabilite.md"
    outputs = {
        soa_path: render.soa(isms, soa_path),
        ROOT / "docs/03-soa/correspondance-referentiels.md": render.mapping(isms),
        ROOT / "docs/02-risques/registre-des-risques.md": render.risk_register(isms),
    }
    ok = all(_write(path, content, args.check) for path, content in outputs.items())
    if not args.check:
        # Livrables dépendant d'une exécution (date, résultats du lab) : non vérifiés en mode --check.
        report = _checks_report()
        _write(ROOT / "docs/08-pilotage/tableau-de-bord.md",
               render.dashboard(isms, kpi.compute(isms, args.date, report), report, args.date,
                                history.load(HISTORY)), False)
        if RESTORE_REPORT.exists():
            result = json.loads(RESTORE_REPORT.read_text(encoding="utf-8"))
            _write(ROOT / "docs/06-resilience/rapport-test-restauration.md", render.restore_report(result), False)
    return 0 if ok else 1


def cmd_kpi(args) -> int:
    kpis = kpi.compute(load(), args.date, _checks_report())
    if args.json:
        print(kpi.to_json(kpis))
        return 0
    for k in kpis:
        state = {True: "OK ", False: "KO ", None: "-- "}[k.atteint]
        print(f"{state} {k.id}  {k.libelle:<48} {k.formatted():>10}  (cible {k.cible})  {k.detail}")
    return 0


def cmd_history(args) -> int:
    report = _checks_report()
    if report is None and args.source == "ci":
        print("ERREUR : reports/checks.json absent ; exécuter les contrôles avant d'enregistrer un relevé.")
        return 1
    kpis = kpi.compute(load(), args.date, report)
    entries = history.record(HISTORY, history.entry(kpis, report, args.date, args.source, args.commit))
    print(f"relevé du {args.date.isoformat()} enregistré dans data/historique-kpi.yaml ({len(entries)} relevés)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="isms", description="Outillage du SMSI KamaPay")
    parser.add_argument("--date", type=date.fromisoformat, default=date.today(),
                        help="date de référence (AAAA-MM-JJ), par défaut aujourd'hui")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="vérifier la cohérence du SMSI").set_defaults(func=cmd_validate)
    p_render = sub.add_parser("render", help="générer la SoA, le registre des risques et le tableau de bord")
    p_render.add_argument("--check", action="store_true", help="échouer si un livrable généré n'est pas à jour")
    p_render.set_defaults(func=cmd_render)
    p_kpi = sub.add_parser("kpi", help="calculer les indicateurs du SMSI")
    p_kpi.add_argument("--json", action="store_true")
    p_kpi.set_defaults(func=cmd_kpi)
    p_history = sub.add_parser("history", help="enregistrer un relevé daté des indicateurs")
    p_history.add_argument("--source", choices=["ci", "manuel"], default="manuel")
    p_history.add_argument("--commit", help="commit évalué (traçabilité du relevé)")
    p_history.set_defaults(func=cmd_history)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
