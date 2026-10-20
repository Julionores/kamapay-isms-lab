---
id: PROC-01
titre: Procédure de gestion des identités et des accès
version: "1.2"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: DSI
date_approbation: 2026-05-28
prochaine_revue: 2027-05-28
controles_iso: ["5.11", "5.16", "5.18", "6.5", "8.2"]
---

# Procédure de gestion des identités et des accès

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-07-01 | RSSI | Création |
| 1.1 | 2025-12-10 | RSSI | Comptes à privilèges et bastion |
| 1.2 | 2026-05-28 | RSSI | Retrait automatique des droits déclenché par l'outil RH (retour d'expérience INC-2026-003) |

## 1. Objet

Décrire le cycle de vie des identités et des droits d'accès (arrivée, changement de poste, départ, revue) pour les salariés, prestataires et comptes techniques. Cette procédure met en œuvre la [politique de contrôle d'accès](../politiques/POL-01-controle-acces.md).

## 2. Acteurs

| Acteur | Rôle |
|---|---|
| Responsable RH | Déclare les arrivées, mobilités et départs dans l'outil RH |
| Manager | Demande et valide les droits nécessaires à la fonction |
| Propriétaire d'application | Valide les droits sur son application (A01, A04, A06...) |
| DSI (équipe identités) | Crée, modifie, désactive les comptes |
| RSSI | Valide les droits à privilèges, pilote la revue des accès |

## 3. Arrivée (5.16)

| Étape | Action | Responsable | Délai |
|---|---|---|---|
| 1 | Création de la fiche salarié dans l'outil RH (contrat signé, vérifications préalables réalisées, voir contrôle 6.1) | RH | J-5 |
| 2 | Création automatique de l'identité unique dans l'annuaire, rattachée au profil métier | DSI | J-3 |
| 3 | Demande de droits complémentaires au profil, avec justification | Manager | J-3 |
| 4 | Validation par le propriétaire d'application ; validation RSSI pour tout droit à privilèges | Propriétaire, RSSI | J-1 |
| 5 | Remise des moyens d'authentification (activation MFA en présentiel), signature de la [politique d'usage acceptable](../politiques/POL-07-usage-acceptable.md) | DSI | J0 |

Règles :

- un identifiant unique et nominatif par personne ; aucun compte partagé ;
- les comptes de prestataires portent une date d'expiration (maximum 6 mois, renouvelable) ;
- les profils métier intègrent la séparation des tâches : un même compte ne peut pas saisir et valider une régularisation (traitement de R02).

## 4. Changement de poste

1. Le RH enregistre la mobilité ; l'outil RH déclenche la **suppression automatique** des droits liés à l'ancien profil à la date d'effet.
2. Le nouveau manager demande les droits du nouveau poste (étapes 3 et 4 ci-dessus).
3. Aucun cumul de droits n'est conservé sans dérogation validée par le RSSI pour 30 jours maximum.

## 5. Départ (5.11, 6.5)

| Étape | Action | Responsable | Délai |
|---|---|---|---|
| 1 | Enregistrement de la date de départ | RH | Dès connaissance |
| 2 | Pendant le préavis : retrait des droits d'export et des accès à privilèges | DSI | J+1 après notification |
| 3 | Désactivation de tous les comptes et révocation des jetons MFA, certificats et accès VPN | DSI | Jour du départ, avant 18 h |
| 4 | Restitution du matériel, des badges et des documents (procès-verbal signé) | Manager | Jour du départ |
| 5 | Rappel écrit des obligations de confidentialité qui perdurent après le départ | RH | Jour du départ |
| 6 | Suppression des comptes désactivés | DSI | J+90 |

En cas de départ conflictuel ou de licenciement, les étapes 2 et 3 sont réalisées **avant** l'annonce à la personne.

## 6. Comptes à privilèges (8.2)

- Comptes d'administration nominatifs (préfixe `adm-`), distincts du compte bureautique.
- Utilisation uniquement depuis le bastion d'administration avec MFA matérielle ; sessions enregistrées.
- Comptes génériques (`root`, `postgres`, comptes d'urgence) : mots de passe dans le coffre-fort, extraction tracée et changement après usage.
- Les comptes techniques applicatifs disposent du strict minimum : par exemple, le rôle `kamapay_app` de la base de données n'est pas super-utilisateur et n'a pas le droit de modifier le schéma (vérifié par **CHK-DB-01**).
- Liste des comptes à privilèges revue **mensuellement** par le RSSI.

## 7. Revue des accès (5.18)

| Périmètre | Fréquence | Réviseur |
|---|---|---|
| Comptes à privilèges | Mensuelle | RSSI |
| Back-office A06 (dont droits d'export) | Trimestrielle | Directeur des Opérations |
| Plateforme A01, API A04 (comptes partenaires) | Trimestrielle | Propriétaires d'application |
| Annuaire et SI interne A07 | Semestrielle | Managers |

Déroulement :

1. La DSI extrait la liste des comptes et droits (J-5 avant la campagne).
2. Chaque réviseur confirme ou retire chaque droit dans un délai de 10 jours ouvrés.
3. Les retraits sont appliqués sous 48 heures ; les comptes sans réponse du réviseur sont suspendus.
4. Le RSSI archive les preuves de revue et présente le taux de réalisation en revue de direction.

## 8. Enregistrements

Tickets de demande et de validation, procès-verbaux de restitution, extractions et validations de revue des accès : conservés 3 ans.
