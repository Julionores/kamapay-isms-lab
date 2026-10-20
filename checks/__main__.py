"""Exécution des contrôles automatisés : python -m checks [--strict] [--cible lab|depot|rapport]."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone

from isms import ROOT

from .registry import REGISTRY, Result, Skip

ORDER = ["depot", "rapport", "lab"]


def run(targets: set[str]) -> list[dict]:
    results = []
    # CHK-RATE-01 déclenche la limitation de débit : il passe en dernier.
    selected = sorted((c for c in REGISTRY.values() if c.cible in targets),
                      key=lambda c: (ORDER.index(c.cible), c.id == "CHK-RATE-01", c.id))
    for c in selected:
        try:
            outcome: Result = c.func()
            statut, detail = ("PASS" if outcome.ok else "FAIL"), outcome.detail
        except Skip as exc:
            statut, detail = "SKIP", str(exc)
        except Exception as exc:  # un contrôle défaillant ne doit pas masquer les autres
            statut, detail = "ERREUR", f"{type(exc).__name__} : {exc}"
        results.append({"id": c.id, "controles": c.controles, "titre": c.titre, "cible": c.cible,
                        "statut": statut, "detail": detail})
        print(f"{statut:<6} {c.id:<13} [{', '.join(c.controles)}] {c.titre}\n       {detail}")
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="checks", description="Contrôles automatisés ISO/IEC 27001 du lab KamaPay")
    parser.add_argument("--cible", action="append", choices=ORDER, help="limiter à une cible (répétable)")
    parser.add_argument("--strict", action="store_true", help="un contrôle non exécuté (SKIP) est un échec")
    args = parser.parse_args(argv)

    results = run(set(args.cible or ORDER))
    report = {"date": datetime.now(timezone.utc).isoformat(timespec="seconds"), "resultats": results}
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports" / "checks.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    failing = {"FAIL", "ERREUR"} | ({"SKIP"} if args.strict else set())
    counts = {s: sum(1 for r in results if r["statut"] == s) for s in ("PASS", "FAIL", "SKIP", "ERREUR")}
    print("\n" + ", ".join(f"{n} {s}" for s, n in counts.items()) + " -> reports/checks.json")
    return 1 if any(r["statut"] in failing for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
