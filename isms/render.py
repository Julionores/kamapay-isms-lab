"""Génération des livrables lisibles à partir des référentiels (data/*.yaml).

Les fichiers produits commencent par GENERATED_MARKER : ils ne se modifient pas
à la main, la CI vérifie qu'ils sont à jour.
"""

from __future__ import annotations

import os
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from . import annexe_a, history, risk
from .data import GENERATED_MARKER, Isms
from .kpi import Kpi

STATUS_LABELS = {
    "implemente": "Implémentée",
    "partiel": "Partielle",
    "planifie": "Planifiée",
    "non_applicable": "Non applicable",
}
TREATMENT_LABELS = {"reduire": "Réduire", "accepter": "Accepter", "transferer": "Transférer", "eviter": "Éviter"}
HISTORY_ROWS = 12
ACTION_LABELS = {"planifie": "Planifiée", "en_cours": "En cours", "termine": "Terminée"}


def _header(source: str) -> str:
    return f"{GENERATED_MARKER} par `python -m isms render` à partir de {source}. Ne pas modifier. -->\n\n"


def _cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def _link(target: str, from_file: Path, root: Path) -> str:
    if target.startswith("ext:"):
        return _cell(target[4:].strip()) + " *(hors dépôt)*"
    rel = os.path.relpath(root / target, from_file.parent)
    return f"[{Path(target.rstrip('/')).name or target}]({rel})"


def soa(isms: Isms, out: Path) -> str:
    controls = sorted(isms.soa["controles"], key=lambda c: annexe_a.sort_key(c["id"]))
    counts = Counter(c["statut"] for c in controls)
    automated = sum(1 for c in controls if c.get("checks"))
    lines = [
        _header("data/soa.yaml et data/risques.yaml"),
        "# Déclaration d'applicabilité (SoA)\n",
        f"ISO/IEC 27001:2022, clause 6.1.3 d). Version {isms.soa['version']} du {isms.soa['date_revue']}, "
        f"approuvée par : {isms.soa['approbateur']}.\n",
        "## Synthèse\n",
        "| Statut | Nombre |",
        "|---|---:|",
    ]
    lines += [f"| {STATUS_LABELS[s]} | {counts.get(s, 0)} |" for s in STATUS_LABELS]
    lines += [
        f"| **Total** | **{len(controls)}** |\n",
        f"{automated} mesures sont vérifiées en continu par des contrôles automatisés (`checks/`).\n",
    ]

    by_theme = defaultdict(list)
    for c in controls:
        by_theme[annexe_a.theme_of(c["id"])].append(c)
    for theme, (label, _) in annexe_a.THEMES.items():
        lines += [
            f"## {theme}. {label}\n",
            "| Mesure | Intitulé | Statut | Justification | Preuves | Contrôle auto. |",
            "|---|---|---|---|---|---|",
        ]
        for c in by_theme[theme]:
            risks = isms.risks_for_control(c["id"])
            justification = "; ".join(
                part for part in (
                    c.get("justification", ""),
                    f"Risque{'s' if len(risks) > 1 else ''} {', '.join(risks)}" if risks else "",
                    f"Écart : {c['ecart']}" if c.get("ecart") else "",
                ) if part
            ) or "Mesure de base de la PSSI"
            proofs = "<br>".join(_link(p, out, isms.root) for p in c["preuves"]) or "-"
            lines.append(
                f"| {c['id']} | {_cell(c['titre'])} | {STATUS_LABELS[c['statut']]} | {_cell(justification)} "
                f"| {proofs} | {', '.join(c.get('checks', [])) or '-'} |"
            )
        lines.append("")
    return "\n".join(lines)


def mapping(isms: Isms) -> str:
    controls = sorted(isms.soa["controles"], key=lambda c: annexe_a.sort_key(c["id"]))
    lines = [
        _header("data/soa.yaml"),
        "# Correspondance entre référentiels\n",
        "Une mesure ISO/IEC 27001, plusieurs exigences couvertes : cette table permet de réutiliser une même "
        "preuve pour un audit ISO 27001, une revue COBIT for SOX ou ISAE 3402, une évaluation PCI DSS ou un "
        "contrôle RGPD. Les correspondances sont indicatives et doivent être confirmées par l'auditeur.\n",
        "## Par mesure de l'annexe A\n",
        "| Mesure | Intitulé | COBIT 2019 | ITIL 4 | PCI DSS v4.0 | RGPD (articles) |",
        "|---|---|---|---|---|---|",
    ]
    for c in controls:
        lines.append(
            f"| {c['id']} | {_cell(c['titre'])} | {', '.join(c.get('cobit', [])) or '-'} "
            f"| {', '.join(c.get('itil', [])) or '-'} | {', '.join(c.get('pci', [])) or '-'} "
            f"| {', '.join(c.get('rgpd', [])) or '-'} |"
        )

    for key, title in (("cobit", "Par objectif COBIT 2019"), ("pci", "Par exigence PCI DSS v4.0")):
        reverse = defaultdict(list)
        for c in controls:
            for ref in c.get(key, []):
                reverse[ref].append(c["id"])
        lines += ["", f"## {title}\n", "| Référence | Mesures ISO/IEC 27001 |", "|---|---|"]
        for ref in sorted(reverse, key=lambda r: [int(p) if p.isdigit() else p for p in r.replace(".", " ").split()]):
            lines.append(f"| {ref} | {', '.join(reverse[ref])} |")
    lines.append("")
    return "\n".join(lines)


def _heatmap(isms: Isms, key: str) -> list[str]:
    cells = defaultdict(list)
    for r in isms.risks:
        cells[(r[key]["V"], r[key]["I"])].append(r["id"])
    lines = ["| Vraisemblance \\ Impact | 1 | 2 | 3 | 4 |", "|---|---|---|---|---|"]
    for v in range(4, 0, -1):
        row = [", ".join(cells[(v, i)]) or "·" for i in range(1, 5)]
        lines.append(f"| **{v}** | " + " | ".join(row) + " |")
    return lines


def risk_register(isms: Isms) -> str:
    lines = [
        _header("data/risques.yaml"),
        "# Registre des risques\n",
        f"Version {isms.risques['version']} du {isms.risques['date_revue']}. Méthode : "
        "[méthodologie](methodologie-risques.md). Niveau = vraisemblance × impact ; "
        f"appétence : résiduel ≤ {risk.APPETITE}.\n",
        "## Cartographie des risques bruts\n",
        *_heatmap(isms, "brut"),
        "",
        "## Cartographie des risques résiduels\n",
        *_heatmap(isms, "residuel"),
        "",
        "## Registre\n",
        "| Risque | Intitulé | Actifs | Propriétaire | Brut | Traitement | Mesures ISO 27001 | Résiduel | Acceptation |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in isms.risks:
        brut, res = risk.score(r["brut"]), risk.score(r["residuel"])
        acceptance = r.get("acceptation")
        accepted = f"{acceptance['par']}, {acceptance['date']}" if acceptance else (
            "requise" if risk.needs_acceptance(r) else "non requise")
        lines.append(
            f"| {r['id']} | {_cell(r['titre'])} | {', '.join(r['actifs'])} | {r['proprietaire']} "
            f"| {brut} ({risk.level(brut)}) | {TREATMENT_LABELS[r['traitement']]} | {', '.join(r['controles'])} "
            f"| {res} ({risk.level(res)}) | {accepted} |"
        )
    lines += [
        "",
        "## Plan de traitement des risques\n",
        "| Action | Risque | Libellé | Responsable | Échéance | Statut |",
        "|---|---|---|---|---|---|",
    ]
    for a in sorted(isms.actions, key=lambda a: a["id"]):
        lines.append(
            f"| {a['id']} | {a['risque']} | {_cell(a['libelle'])} | {a['responsable']} | {a['echeance']} "
            f"| {ACTION_LABELS[a['statut']]} |"
        )
    lines += ["", "## Scénarios\n"]
    for r in isms.risks:
        lines += [f"### {r['id']} - {r['titre']}\n", r["scenario"].strip(), "", "Mesures :", ""]
        lines += [f"- {m}" for m in r.get("mesures", [])]
        if r.get("acceptation"):
            lines += ["", f"Acceptation du risque résiduel : {r['acceptation']['motif']}"]
        lines.append("")
    return "\n".join(lines)


def dashboard(isms: Isms, kpis: list[Kpi], checks_report: dict | None, today: date,
              releves: list[dict] = ()) -> str:
    state = {True: "Atteint", False: "**Non atteint**", None: "n.d."}
    previous = next((r for r in reversed(releves) if r["date"] < today.isoformat()), None)
    since = f"depuis le {previous['date']}" if previous else "aucun relevé antérieur"
    lines = [
        _header("data/*.yaml et reports/checks.json"),
        "# Tableau de bord du SMSI\n",
        f"Situation au {today.isoformat()}. Définitions : [indicateurs du SMSI](indicateurs-smsi.md). "
        f"Tendance : {since}.\n",
        "## Indicateurs\n",
        "| Indicateur | Libellé | Valeur | Cible | État | Tendance | Détail |",
        "|---|---|---:|---|---|---|---|",
    ]
    lines += [
        f"| {k.id} | {k.libelle} | {k.formatted()} | {k.cible} | {state[k.atteint]} "
        f"| {history.trend(k, previous['indicateurs'].get(k.id) if previous else None)} | {_cell(k.detail)} |"
        for k in kpis
    ]

    incidents = isms.incidents["incidents"]
    by_severity = Counter(i["gravite"] for i in incidents)
    by_category = Counter(i["categorie"] for i in incidents)
    notified = sum(1 for i in incidents if i["notification"]["regulateur"])
    lines += [
        "",
        "## Incidents de l'année\n",
        f"{len(incidents)} incidents enregistrés, {sum(1 for i in incidents if i['statut'] != 'clos')} non clos, "
        f"{notified} déclarés au régulateur.\n",
        "| Gravité | Nombre |",
        "|---|---:|",
        *[f"| {g} | {by_severity.get(g, 0)} |" for g in ("P1", "P2", "P3", "P4")],
        "",
        "| Catégorie | Nombre |",
        "|---|---:|",
        *[f"| {c.replace('_', ' ')} | {n} |" for c, n in by_category.most_common()],
    ]

    if checks_report:
        lines += [
            "",
            f"## Contrôles automatisés (exécution du {checks_report['date']})\n",
            "| Contrôle | Mesures | Intitulé | Résultat | Détail |",
            "|---|---|---|---|---|",
        ]
        lines += [
            f"| {r['id']} | {', '.join(r['controles'])} | {_cell(r['titre'])} | {r['statut']} | {_cell(r['detail'])} |"
            for r in checks_report["resultats"]
        ]

    if releves:
        ids = [k.id for k in kpis]
        recent = list(releves)[-HISTORY_ROWS:]
        lines += [
            "",
            "## Historique des relevés\n",
            f"{len(releves)} relevé(s) dans [data/historique-kpi.yaml](../../data/historique-kpi.yaml), "
            f"complété chaque lundi par la CI ; les {HISTORY_ROWS} plus récents sont affichés.\n",
            "| Date | " + " | ".join(i.replace("KPI-", "K") for i in ids) + " | Contrôles |",
            "|---|" + "---:|" * len(ids) + "---|",
        ]
        for r in reversed(recent):
            values = ["n.d." if r["indicateurs"].get(i) is None else f"{r['indicateurs'][i]:g}" for i in ids]
            ctl = r.get("controles")
            checks = f"{ctl['conformes']}/{ctl['total']}" if ctl else "n.d."
            lines.append(f"| {r['date']} | " + " | ".join(values) + f" | {checks} |")
    lines.append("")
    return "\n".join(lines)


def restore_report(result: dict) -> str:
    verdict = "réussi" if result["succes"] else "**échoué**"
    return "\n".join([
        _header("reports/restauration.json (lab/scripts/test-restauration.sh)"),
        "# Rapport de test de restauration\n",
        "Preuve des mesures 8.13 (sauvegarde) et 5.30 (préparation des TIC pour la continuité) ; "
        "traitement du risque R14. Test exécuté sur le lab, pas sur la production.\n",
        "| Élément | Résultat |",
        "|---|---|",
        f"| Date d'exécution (UTC) | {result['date']} |",
        f"| Résultat | Test {verdict} |",
        f"| Méthode | {result['methode']} |",
        f"| Durée de la sauvegarde | {result['duree_sauvegarde_s']} s |",
        f"| Durée de la restauration (déchiffrement, instance vierge, pg_restore) | {result['duree_restauration_s']} s |",
        f"| Durée totale | {result['duree_totale_s']} s |",
        f"| Empreinte d'intégrité de la source | `{result['empreinte_source']}` |",
        f"| Empreinte d'intégrité de la copie restaurée | `{result['empreinte_restauree']}` |",
        f"| SHA-256 de la sauvegarde chiffrée | `{result['sha256_sauvegarde_chiffree']}` |",
        "",
        "L'empreinte combine le nombre de clients et de portefeuilles, la somme des soldes, le nombre de "
        "transactions et un condensat MD5 de l'ensemble des transactions triées. Deux empreintes identiques "
        "prouvent que la copie restaurée est complète et intègre.\n",
        "Le RTO de production (4 h pour A01, voir le [PCA/PRA](pca-pra.md)) inclut aussi la bascule réseau "
        "et la validation métier ; ce test mesure uniquement la partie technique de restauration des données.\n",
    ])
