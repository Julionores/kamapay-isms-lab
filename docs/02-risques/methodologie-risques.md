---
id: RSK-00
titre: Méthodologie d'appréciation et de traitement des risques
version: "2.0"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-07-10
prochaine_revue: 2027-07-10
controles_iso: []
---

# Méthodologie d'appréciation et de traitement des risques

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-11-20 | RSSI | Création (alignement ISO/IEC 27005:2022) |
| 2.0 | 2026-07-10 | RSSI | Ajout de l'appétence au risque formalisée et des scénarios mobile money |

## 1. Objet et références

Ce document décrit la méthode utilisée par KamaPay SA pour répondre aux clauses 6.1.2 (appréciation des risques), 6.1.3 (traitement des risques), 8.2 et 8.3 (réalisation) d'ISO/IEC 27001:2022. Il s'appuie sur ISO/IEC 27005:2022 (approche par scénarios) et reprend, pour l'identification des sources de risque, la logique « sources de risque / objectifs visés » d'EBIOS Risk Manager.

Le registre opérationnel est tenu dans [`data/risques.yaml`](../../data/risques.yaml). Sa version lisible est générée dans le [registre des risques](registre-des-risques.md).

## 2. Périmètre

La méthode s'applique à tous les actifs inventoriés dans [`data/actifs.yaml`](../../data/actifs.yaml) (A01 à A10), aux projets (voir [la sécurité dans les projets](../04-securite-projets/securite-dans-les-projets.md)) et aux changements significatifs.

## 3. Processus

| Étape | Activité | Responsable | Livrable |
|---|---|---|---|
| 1 | Établir le contexte : actifs, besoins DICT, exigences légales | RSSI | Inventaire des actifs à jour |
| 2 | Identifier les scénarios : source de risque, menace, vulnérabilité, actif touché | RSSI + propriétaires d'actifs | Fiche risque (id, titre, scénario) |
| 3 | Analyser : coter la vraisemblance et l'impact bruts | Propriétaire du risque | Cotation brute V × I |
| 4 | Évaluer : comparer au seuil d'appétence | RSSI | Priorisation |
| 5 | Traiter : choisir l'option, les contrôles de l'annexe A et le plan d'action | Propriétaire du risque | Mesures, actions PA-xx, cotation résiduelle |
| 6 | Accepter le risque résiduel | Propriétaire, ou DG si > 6 | Champ `acceptation` |
| 7 | Surveiller et revoir | RSSI | Revue du registre, KPI-03 et KPI-04 |

## 4. Échelles de cotation

### 4.1 Vraisemblance (V)

| Note | Libellé | Critère |
|---|---|---|
| 1 | Rare | Pas d'occurrence connue dans le secteur en 5 ans ; attaque nécessitant des moyens étatiques |
| 2 | Possible | Occurrence connue dans le secteur, pas chez KamaPay |
| 3 | Probable | Déjà survenu chez KamaPay, ou tentatives observées chaque trimestre |
| 4 | Quasi certain | Tentatives observées chaque semaine |

### 4.2 Impact (I)

L'impact retenu est **le maximum** des quatre axes.

| Note | Financier | Réglementaire | Image | Opérationnel |
|---|---|---|---|---|
| 1 | < 1 M FCFA | Aucun | Plainte isolée | Dégradation < 30 min |
| 2 | 1 à 10 M FCFA | Demande d'information du régulateur | Presse locale | Interruption < 2 h |
| 3 | 10 à 100 M FCFA | Mise en demeure, notification obligatoire | Presse nationale, réseaux sociaux | Interruption 2 à 4 h |
| 4 | > 100 M FCFA | Sanction, suspension ou retrait d'agrément | Perte de confiance durable | Interruption > 4 h (au-delà du RTO) |

### 4.3 Niveau de risque

Niveau = V × I.

| Niveau | Plage | Traitement attendu |
|---|---|---|
| Faible | 1 à 3 | Acceptable, revue annuelle |
| Modéré | 4 à 6 | Acceptable par le propriétaire du risque, surveillance |
| Élevé | 8 à 9 | Plan de traitement obligatoire |
| Critique | 12 à 16 | Plan de traitement obligatoire, suivi mensuel en comité sécurité |

Matrice :

| V \ I | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **4** | 4 | 8 | 12 | 16 |
| **3** | 3 | 6 | 9 | 12 |
| **2** | 2 | 4 | 6 | 8 |
| **1** | 1 | 2 | 3 | 4 |

## 5. Appétence au risque

Le Directeur Général a fixé l'appétence au risque au **niveau 6**.

- Un risque résiduel ≤ 6 peut être accepté par son propriétaire.
- Un risque résiduel > 6 doit faire l'objet d'une **acceptation formelle du Directeur Général**, datée et motivée (champ `acceptation` du registre). Sans cette acceptation, il est compté dans l'indicateur KPI-03 (cible : 0).
- Une acceptation est valable 12 mois au maximum.

## 6. Options de traitement

| Option | Valeur dans le registre | Usage |
|---|---|---|
| Réduire | `reduire` | Mettre en œuvre des contrôles de l'annexe A |
| Transférer | `transferer` | Assurance, clause contractuelle (le risque résiduel reste suivi) |
| Éviter | `eviter` | Arrêt de l'activité ou du service concerné |
| Accepter | `accepter` | Risque déjà dans l'appétence |

Chaque risque traité par réduction référence les contrôles de l'annexe A dans le champ `controles`. Le lien inverse (contrôle vers risques) est calculé automatiquement pour la [déclaration d'applicabilité](../03-soa/declaration-applicabilite.md). L'outil `python -m isms validate` refuse un registre qui cite un contrôle inexistant.

## 7. Plan de traitement

Chaque action porte un identifiant `PA-xx`, un responsable, une échéance et un statut (`planifie`, `en_cours`, `termine`). Une action non terminée dont l'échéance est dépassée est comptée dans KPI-04 (cible : 0).

## 8. Fréquence de revue

| Déclencheur | Action |
|---|---|
| Trimestriel | Revue des risques élevés et critiques en comité sécurité |
| Annuel | Revue complète du registre, présentée en [revue de direction](../08-pilotage/revue-de-direction.md) |
| Incident P1 ou P2 | Réévaluation des risques liés (champ `risques` du registre des incidents) sous 30 jours |
| Nouveau projet ou changement majeur | Analyse de risque projet |
| Évolution réglementaire | Réévaluation de R11 |

## 9. Exemple de cotation : R01 (SIM swap)

- **Brut** : V = 4 (tentatives hebdomadaires dans le secteur, incident INC-2026-001), I = 4 (pertes financières et notification au régulateur), niveau **16, critique**.
- **Mesures** : gel de 48 h après changement de SIM, réinitialisation de PIN en agence uniquement, règle SIEM.
- **Résiduel** : V = 2, I = 3, niveau **6, modéré**, dans l'appétence.
