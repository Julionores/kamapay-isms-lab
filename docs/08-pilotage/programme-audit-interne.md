---
id: PIL-02
titre: Programme d'audit interne du SMSI 2026-2027
version: "1.0"
statut: approuve
classification: interne
proprietaire: Responsable Audit interne
approbateur: Directeur Général
date_approbation: 2026-01-20
prochaine_revue: 2027-01-20
controles_iso: ["5.35", "5.36", "8.34"]
---

# Programme d'audit interne du SMSI 2026-2027

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2026-01-20 | Responsable Audit interne | Programme pluriannuel |

## 1. Objet

Ce programme met en œuvre la clause 9.2 d'ISO/IEC 27001:2022 et les contrôles 5.35 (révision indépendante) et 5.36 (conformité aux politiques). Il couvre l'ensemble des clauses 4 à 10 et des contrôles applicables de la [déclaration d'applicabilité](../03-soa/declaration-applicabilite.md) sur un cycle de deux ans, avant l'audit de certification.

## 2. Principes

- **Indépendance** : l'auditeur n'audite pas son propre travail. Le RSSI n'audite pas le SMSI ; l'audit est conduit par l'audit interne, avec l'appui d'un auditeur externe certifié ISO/IEC 27001 Lead Auditor pour les domaines techniques.
- **Approche par les risques** : les domaines liés aux risques critiques bruts (R01) et élevés sont audités chaque année.
- **Preuves** : chaque constat s'appuie sur une preuve (document, enregistrement, entretien, test).
- **Référentiel** : ISO/IEC 27001:2022, ISO/IEC 27002:2022, politiques internes, exigences réglementaires du [registre des exigences](../00-contexte/parties-interessees-exigences.md). Lignes directrices : ISO 19011 et ISO/IEC 27007.

## 3. Planning

| Mission | Périmètre | Contrôles / clauses | Période | Statut |
|---|---|---|---|---|
| AI-2026-01 | Gouvernance du SMSI | Clauses 4, 5, 6 ; 5.1 à 5.4, 5.31 | Avril 2026 | Réalisée |
| AI-2026-02 | Gestion des accès et privilèges | 5.15 à 5.18, 8.2, 8.3, 8.5, 8.18 | Juin 2026 | Réalisée |
| AI-2026-03 | Incidents et fraude | 5.24 à 5.28, 6.8 | Septembre 2026 | Réalisée |
| AI-2026-04 | Continuité et sauvegardes | 5.29, 5.30, 8.13, 8.14 | Novembre 2026 | Planifiée |
| AI-2027-01 | Fournisseurs et cloud | 5.19 à 5.23, 8.30 | Février 2027 | Planifiée |
| AI-2027-02 | Développement et changements | 8.25 à 8.33, 8.8, 8.9 | Avril 2027 | Planifiée |
| AI-2027-03 | Personnes et sécurité physique | 6.1 à 6.7, 7.1 à 7.14 | Juin 2027 | Planifiée |
| AI-2027-04 | Mesure, amélioration, revue de direction | Clauses 7, 9, 10 ; 5.35, 5.36 | Septembre 2027 | Planifiée |

## 4. Déroulement d'une mission

1. **Lettre de mission** envoyée au moins 3 semaines avant : périmètre, critères, audités, calendrier.
2. **Revue documentaire** : politiques, procédures, registres (`data/`), résultats des contrôles automatisés (`reports/checks.json`).
3. **Réunion d'ouverture**.
4. **Entretiens et tests** : échantillonnage (par exemple 25 départs de salariés sur 12 mois pour vérifier le retrait des accès sous 24 h).
5. **Réunion de clôture** : présentation des constats.
6. **Rapport** sous 15 jours ouvrés.
7. **Suivi** des actions correctives jusqu'à leur clôture.

## 5. Classement des constats

| Classement | Définition | Délai de traitement |
|---|---|---|
| Non-conformité majeure | Absence ou défaillance totale d'une exigence ; mettrait en cause la certification | Plan d'action sous 15 jours, correction sous 3 mois |
| Non-conformité mineure | Défaillance ponctuelle d'une exigence | Correction sous 6 mois |
| Observation | Risque de non-conformité future | Analyse par le propriétaire |
| Piste de progrès | Bonne pratique possible | Facultatif |

Chaque non-conformité fait l'objet d'une analyse de cause et d'une action corrective (clause 10.2), suivie dans le plan de traitement.

## 6. Constats des missions réalisées en 2026

| Mission | Constat | Classement | Action |
|---|---|---|---|
| AI-2026-01 | Le registre des exigences légales n'avait pas été revu depuis 9 mois (exigence semestrielle) | Mineure | Revue réalisée en mai 2026 |
| AI-2026-02 | Revue trimestrielle des accès du back-office non réalisée au T1 (cause de INC-2026-003) | Majeure | Revue automatisée, suivie en comité sécurité ; levée en septembre 2026 |
| AI-2026-02 | 3 comptes à privilèges partagés sur l'outil de supervision | Mineure | Comptes nominatifs créés |
| AI-2026-03 | Absence d'outillage forensique interne | Observation | Écart accepté, recours au prestataire (SoA 5.28) |
| AI-2026-03 | Les critères de passage en P1 étaient mal connus du SOC | Mineure | Fiche réflexe (exercice EX-2026-01) |

## 7. Protection des systèmes pendant l'audit (8.34)

- Les tests techniques (scans, tests d'intrusion) sont planifiés avec la DSI, en dehors des pics d'activité (fin de mois, jours de fête), et autorisés par écrit.
- Les accès des auditeurs sont en **lecture seule**, nominatifs, limités à la durée de la mission et retirés à la clôture.
- Les extractions de données personnelles sont interdites ; les échantillons sont pseudonymisés.
- Les tests d'intrusion en production sont exécutés depuis des adresses déclarées et peuvent être arrêtés à tout moment par la DSI.

## 8. Compétences des auditeurs

Les auditeurs doivent justifier d'une formation ISO/IEC 27001 (Lead Auditor ou équivalent) et d'une connaissance du secteur des paiements. Les compétences sont conservées comme information documentée (clause 7.2).
