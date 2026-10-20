---
id: PIL-01
titre: Indicateurs de performance du SMSI
version: "1.3"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-10-20
prochaine_revue: 2027-10-20
controles_iso: []
---

# Indicateurs de performance du SMSI

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-12-01 | RSSI | Création (clause 9.1) |
| 1.2 | 2026-07-10 | RSSI | Calcul automatisé des indicateurs depuis les registres |
| 1.3 | 2026-10-20 | RSSI | Conservation de l'historique des relevés hebdomadaires |

## 1. Objet

Ce document définit les indicateurs utilisés pour surveiller et mesurer la performance du SMSI, conformément à la clause 9.1 d'ISO/IEC 27001:2022 : quoi mesurer, comment, quand, par qui, et qui analyse.

Les indicateurs sont **calculés automatiquement** à partir des registres du dépôt par la commande :

```bash
python -m isms kpi
```

Le résultat est publié dans le [tableau de bord](tableau-de-bord.md). Les données sources ne sont jamais ressaisies : une valeur de tableau de bord est toujours traçable jusqu'à une ligne d'un registre ou d'un rapport de contrôle.

**Conservation des résultats.** La clause 9.1 impose de conserver les résultats de la surveillance comme preuves. Chaque lundi, la CI exécute tous les contrôles puis enregistre un relevé daté (valeur des 10 indicateurs, contrôles conformes et non conformes, commit évalué) dans [data/historique-kpi.yaml](../../data/historique-kpi.yaml) avec `python -m isms history --source ci`, et le committe. Une semaine non conforme est enregistrée comme les autres. Le tableau de bord affiche la tendance par rapport au relevé précédent et les douze derniers relevés. Un relevé manuel se fait avec `python -m isms history`.

## 2. Synthèse

| ID | Indicateur | Cible | Fréquence | Propriétaire |
|---|---|---|---|---|
| KPI-01 | Taux de mise en œuvre des contrôles applicables | ≥ 85 % | Mensuelle | RSSI |
| KPI-02 | Contrôles automatisés au vert | 100 % | À chaque exécution du pipeline | RSSI |
| KPI-03 | Risques résiduels au-dessus de l'appétence non acceptés | 0 | Mensuelle | RSSI |
| KPI-04 | Actions du plan de traitement en retard | 0 | Mensuelle | RSSI |
| KPI-05 | Délai moyen de détection des incidents P1 / P2 | < 4 h | Mensuelle | Responsable SOC |
| KPI-06 | Délai moyen de confinement des incidents P1 / P2 | < 4 h | Mensuelle | RSSI |
| KPI-07 | Taux de formation | ≥ 90 % | Trimestrielle | RSSI |
| KPI-08 | Taux de clic à la dernière campagne d'hameçonnage simulé | < 10 % | Trimestrielle | RSSI |
| KPI-09 | Taux de signalement à la dernière campagne d'hameçonnage simulé | ≥ 30 % | Trimestrielle | RSSI |
| KPI-10 | Documents du SMSI à jour | 100 % | Mensuelle | RSSI |

## 3. Fiches indicateurs

### KPI-01 - Taux de mise en œuvre des contrôles applicables

- **Formule** : nombre de contrôles au statut `implemente` / nombre de contrôles applicables (statut différent de `non_applicable`) × 100.
- **Source** : [`data/soa.yaml`](../../data/soa.yaml).
- **Interprétation** : mesure l'avancement du SMSI. Les contrôles `partiel` et `planifie` sont listés avec leur écart dans la [déclaration d'applicabilité](../03-soa/declaration-applicabilite.md).

### KPI-02 - Contrôles automatisés au vert

- **Formule** : nombre de contrôles automatisés au statut « conforme » / nombre de contrôles automatisés exécutés × 100.
- **Source** : `reports/checks.json`, produit par le pipeline de conformité (`.github/workflows/conformite.yml`) à partir des contrôles CHK-xxx du dossier `checks/`.
- **Interprétation** : tout contrôle en échec crée un incident P4 (ou plus selon l'impact) et bloque la livraison.

### KPI-03 - Risques résiduels au-dessus de l'appétence non acceptés

- **Formule** : nombre de risques dont le niveau résiduel (V × I) est > 6 et qui n'ont pas d'acceptation formelle du Directeur Général.
- **Source** : [`data/risques.yaml`](../../data/risques.yaml), champs `residuel` et `acceptation`.
- **Interprétation** : doit rester à 0. Voir la [méthodologie des risques](../02-risques/methodologie-risques.md), § 5.

### KPI-04 - Actions du plan de traitement en retard

- **Formule** : nombre d'actions `PA-xx` dont le statut n'est pas `termine` et dont l'échéance est antérieure à la date du calcul.
- **Source** : [`data/risques.yaml`](../../data/risques.yaml), champ `actions`.

### KPI-05 - Délai moyen de détection des incidents P1 / P2

- **Formule** : moyenne, sur les incidents de gravité P1 ou P2 de l'année en cours, de (`detection` − `debut`), en heures.
- **Source** : [`data/incidents.yaml`](../../data/incidents.yaml).
- **Limite** : l'heure de début est une estimation établie lors de l'analyse ; elle est revue à la clôture.

### KPI-06 - Délai moyen de confinement des incidents P1 / P2

- **Formule** : moyenne, sur les incidents P1 ou P2 de l'année en cours, de (`confinement` − `detection`), en heures.
- **Source** : [`data/incidents.yaml`](../../data/incidents.yaml).

### KPI-07 - Taux de formation

- **Formule** : somme des personnes formées / somme des effectifs cibles, sur les campagnes de l'année, × 100.
- **Source** : [`data/sensibilisation.yaml`](../../data/sensibilisation.yaml), section `campagnes`.
- **Interprétation** : le taux est également suivi séparément pour les salariés et pour les agents distributeurs.

### KPI-08 - Taux de clic à l'hameçonnage simulé

- **Formule** : clics / courriels envoyés × 100, pour la campagne la plus récente.
- **Source** : [`data/sensibilisation.yaml`](../../data/sensibilisation.yaml), section `hameconnage_simule`.

### KPI-09 - Taux de signalement à l'hameçonnage simulé

- **Formule** : signalements / courriels envoyés × 100, pour la campagne la plus récente.
- **Source** : [`data/sensibilisation.yaml`](../../data/sensibilisation.yaml).

### KPI-10 - Documents du SMSI à jour

- **Formule** : nombre de documents de `docs/` dont la date `prochaine_revue` n'est pas dépassée / nombre de documents soumis à revue × 100. Les documents générés sont exclus.
- **Source** : en-têtes (front matter) des documents de `docs/`, vérifiés par le contrôle automatisé CHK-DOC-01.

## 4. Analyse et communication

| Instance | Fréquence | Indicateurs présentés | Décisions attendues |
|---|---|---|---|
| Comité sécurité (RSSI, DSI, Fraude, Conformité, Opérations) | Mensuelle | Tous | Actions correctives, arbitrages de priorité |
| Comité de direction | Trimestrielle | KPI-01, 03, 05, 06, 07 | Ressources, acceptation de risques |
| [Revue de direction](revue-de-direction.md) | Annuelle | Tous, avec tendances sur 12 mois | Décisions de la clause 9.3.3 |
| Groupe actionnaire | Semestrielle | KPI-01, 03, 06 | Information |

Un indicateur hors cible deux mois de suite fait l'objet d'une action corrective inscrite au plan de traitement.
