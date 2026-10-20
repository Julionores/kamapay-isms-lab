---
id: PIL-03
titre: Revue de direction du SMSI - modèle d'ordre du jour et de compte rendu
version: "1.1"
statut: approuve
classification: confidentiel
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-02-10
prochaine_revue: 2027-02-10
controles_iso: ["5.4"]
---

# Revue de direction du SMSI - modèle d'ordre du jour et de compte rendu

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-12-05 | RSSI | Création |
| 1.1 | 2026-02-10 | RSSI | Alignement strict sur la clause 9.3.2 (a à g) |

## 1. Objet

La revue de direction permet à la direction de KamaPay SA de s'assurer que le SMSI reste pertinent, adéquat et efficace (clause 9.3 d'ISO/IEC 27001:2022). Elle a lieu **au moins une fois par an**, et en plus après un incident P1 ou un changement majeur (réglementation, organisation, périmètre).

## 2. Participants

| Rôle | Statut |
|---|---|
| Directeur Général | Président, décideur |
| RSSI | Rapporteur, secrétariat |
| DSI, Directeur des Opérations, Responsable Conformité, DPO, Responsable Fraude, Directeur Financier, Responsable Audit interne | Membres |
| Représentant sécurité du groupe actionnaire | Invité |

## 3. Préparation

Deux semaines avant la séance, le RSSI diffuse le dossier : [tableau de bord](tableau-de-bord.md) (généré par `python -m isms kpi`), [registre des risques](../02-risques/registre-des-risques.md), [déclaration d'applicabilité](../03-soa/declaration-applicabilite.md), rapports d'audit interne, synthèse du registre des incidents.

---

## 4. Modèle d'ordre du jour

| N° | Point | Élément d'entrée (clause 9.3.2) | Présentateur | Durée |
|---|---|---|---|---|
| 1 | Suivi des décisions de la revue précédente | a) | RSSI | 10 min |
| 2 | Changements des enjeux internes et externes : réglementation des paiements, menaces, organisation | b) | Conformité, RSSI | 15 min |
| 3 | Changements des besoins et attentes des parties intéressées : régulateur, groupe, partenaires, clients | c) | Conformité | 10 min |
| 4 | Retours sur la performance de la sécurité : | d) | | |
| 4.1 | Non-conformités et actions correctives | d) 1 | Audit interne | 10 min |
| 4.2 | Résultats de la surveillance et de la mesure (KPI-01 à KPI-10) | d) 2 | RSSI | 15 min |
| 4.3 | Résultats d'audit | d) 3 | Audit interne | 10 min |
| 4.4 | Atteinte des objectifs de sécurité | d) 4 | RSSI | 10 min |
| 5 | Retours des parties intéressées (plaintes clients, remarques du régulateur, du groupe) | e) | Opérations, Conformité | 10 min |
| 6 | Résultats de l'appréciation des risques et état du plan de traitement | f) | RSSI | 20 min |
| 7 | Opportunités d'amélioration continue | g) | Tous | 10 min |
| 8 | Décisions et ressources | Sortie 9.3.3 | Directeur Général | 15 min |

## 5. Modèle de compte rendu

**Revue de direction n° RD-AAAA-NN** - Date : ____ - Lieu : ____

**Présents** : ____ - **Excusés** : ____

### 5.1 Suivi des décisions précédentes (a)

| Décision | Responsable | Échéance | État |
|---|---|---|---|
| | | | Réalisée / en cours / abandonnée (motif) |

### 5.2 Évolution du contexte (b, c)

- Enjeux externes : ____
- Enjeux internes : ____
- Parties intéressées : ____
- Impact sur le périmètre ou la politique : oui / non. Si oui : ____

### 5.3 Performance de la sécurité (d)

| Indicateur | Valeur | Cible | Tendance 12 mois | Commentaire |
|---|---|---|---|---|
| KPI-01 à KPI-10 | | | | |

Non-conformités ouvertes : ____ (dont majeures : ____). Résultats d'audit : ____. Objectifs atteints : ____ / ____.

### 5.4 Retours des parties intéressées (e)

____

### 5.5 Risques (f)

- Risques critiques ou élevés en résiduel : ____
- Risques au-dessus de l'appétence et acceptations à renouveler : ____
- Actions du plan de traitement en retard : ____

### 5.6 Opportunités d'amélioration (g)

____

### 5.7 Décisions (clause 9.3.3)

| N° | Décision | Type (amélioration / changement du SMSI / ressources) | Responsable | Échéance |
|---|---|---|---|---|
| | | | | |

**Conclusion de la direction sur l'adéquation et l'efficacité du SMSI** : ____

Signature du Directeur Général : ____

---

## 6. Conservation

Le compte rendu est conservé comme information documentée pendant 5 ans au minimum. Les décisions sont reportées dans le plan de traitement (`PA-xx`) ou dans le plan d'action du SMSI, et suivies au point 1 de la revue suivante.
