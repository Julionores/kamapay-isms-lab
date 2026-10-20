---
id: INC-EX-01
titre: "Exercice sur table EX-2026-01 : vague de SIM swap"
version: "1.0"
statut: approuve
classification: confidentiel
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-04-08
prochaine_revue: 2027-04-08
controles_iso: ["5.24", "5.26"]
---

# Exercice sur table EX-2026-01 : vague de SIM swap

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2026-04-08 | RSSI | Compte rendu validé |

## 1. Contexte et objectifs

L'exercice a été organisé le **26 mars 2026** (09 h 00 à 12 h 30, heure de Douala) à la suite de l'incident réel [INC-2026-001](../../../data/incidents.yaml) (vague de SIM swap de février 2026). Il visait à valider la nouvelle version 2.0 de la [procédure de gestion des incidents](../procedure-gestion-incidents.md) avant la mise en production du gel automatique (mesure du risque R01).

Objectifs mesurables :

1. Qualifier un incident P1 en moins de 30 minutes après le premier inject.
2. Décider du gel préventif des comptes en moins de 1 heure.
3. Préparer l'information initiale au régulateur en moins de 24 heures (simulé : moins de 2 heures).
4. Identifier au moins trois améliorations de la procédure.

## 2. Participants

| Rôle | Participation |
|---|---|
| Animateur | RSSI |
| Observateur | Auditeur interne |
| Joueurs | Responsable Fraude, DSI, Directeur des Opérations, Responsable Conformité, Responsable Communication, chef du service client, représentant de KamaTel (opérateur P03) |
| Décideur | Directeur Général (joué par le Directeur Général adjoint) |

## 3. Scénario

Un groupe criminel obtient des duplicatas de SIM dans des boutiques partenaires de l'opérateur, en présentant de fausses pièces d'identité. Il cible des clients à fort solde identifiés grâce à une base de données achetée. Les OTP reçus sur les nouvelles SIM permettent de réinitialiser les PIN puis de transférer les fonds vers des comptes mules, retirés en cash-out chez des agents.

## 4. Injects et réponses

Les horaires sont ceux de l'exercice (temps simulé, UTC+1).

| Heure | Inject | Réponse attendue | Réponse observée | Écart |
|---|---|---|---|---|
| 09 h 10 | Le service client signale 4 appels de clients dont le solde est à zéro, tous ayant perdu le réseau mobile la veille | Ouverture d'un événement, transmission à l'analyste SOC | Événement ouvert à 09 h 14 | Aucun |
| 09 h 25 | Le SIEM remonte 11 réinitialisations de PIN suivies de transferts > 500 000 FCFA en moins de 2 h | Corrélation avec le changement de SIM, gravité P2 provisoire | Corrélation faite, mais les données de changement SIM n'étaient pas disponibles en temps réel | Dépendance à l'opérateur (flux SIM swap absent) |
| 09 h 40 | Le Responsable Fraude identifie 27 comptes touchés, 14 M FCFA débités | Passage en P1, activation de la cellule de crise | P1 déclaré à 09 h 46 (36 min après le 1er inject) | Objectif 1 dépassé de 6 min : critères P1 mal connus du N1 |
| 10 h 05 | Les fonds sont en cours de retrait chez 9 agents de deux villes | Gel des comptes mules, alerte aux agents, demande de gel aux banques partenaires | Gel décidé à 10 h 12 | Objectif 2 atteint |
| 10 h 30 | Un journaliste appelle le service communication | Message d'attente validé, pas de détails techniques | Message préparé, mais aucun modèle n'existait | Créer des messages pré-approuvés |
| 10 h 50 | KamaTel confirme 2 boutiques à l'origine des duplicatas | Demande de suspension des boutiques, préservation des preuves (vidéo, dossiers) | Demande faite ; la conservation des preuves chez l'opérateur n'était pas prévue au contrat | Clause contractuelle à ajouter (PA-02) |
| 11 h 20 | La Conformité demande les éléments de l'information initiale au régulateur | Fiche de synthèse : nature, impact, mesures | Fiche prête à 11 h 45 | Objectif 3 atteint |
| 11 h 40 | 6 clients publient sur les réseaux sociaux | Message public, procédure de remboursement | Message validé par le DG à 12 h 05 | Délai de validation long |

## 5. Constats

**Points forts**

- Les joueurs connaissaient leur rôle et la cellule de crise s'est réunie en 10 minutes.
- La décision de gel a été rapide et documentée.
- La fiche d'information au régulateur était complète.

**Points à améliorer**

1. Absence de flux temps réel des changements de SIM fourni par l'opérateur : la détection dépend de la plainte client.
2. Les critères de passage en P1 ne sont pas affichés pour l'analyste N1.
3. Aucun message de communication pré-approuvé pour les scénarios de fraude.
4. La conservation des preuves chez l'opérateur n'est pas prévue au contrat.
5. La réinitialisation de PIN après changement de SIM est encore possible par le service client à distance.

## 6. Plan d'action

| ID | Action | Responsable | Échéance | Statut |
|---|---|---|---|---|
| PA-01 | Intégrer l'API de notification SIM swap de l'opérateur et le gel automatique de 48 h | DSI | 2026-11-30 | En cours |
| PA-02 | Clause contractuelle : notification SIM swap en 5 min et conservation des preuves | Responsable Achats | 2026-12-15 | En cours |
| EX-01-A3 | Fiche réflexe « critères P1 » affichée au SOC | RSSI | 2026-04-30 | Terminé |
| EX-01-A4 | Bibliothèque de messages pré-approuvés (fraude, indisponibilité, fuite) | Responsable Communication | 2026-05-31 | Terminé |
| EX-01-A5 | Réinitialisation de PIN après changement de SIM uniquement en agence | Directeur des Opérations | 2026-05-15 | Terminé |

Les actions PA-01 et PA-02 sont suivies dans le [registre des risques](../../02-risques/registre-des-risques.md) (risque R01).

## 7. Évaluation globale

| Objectif | Résultat |
|---|---|
| 1. Qualification P1 < 30 min | Non atteint (36 min) |
| 2. Gel < 1 h | Atteint (62 min après le 1er inject, 26 min après la qualification P1) |
| 3. Information régulateur < 2 h (simulé) | Atteint (2 h 35 après le 1er inject, 1 h 59 après la qualification P1) |
| 4. Trois améliorations identifiées | Atteint (cinq) |

Prochain exercice : EX-2026-02, scénario rançongiciel sur le SI interne avec propagation (risque R06), programmé au second semestre 2026.
