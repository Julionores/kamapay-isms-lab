---
id: POL-01
titre: Politique de contrôle d'accès
version: "1.2"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Comité de sécurité
date_approbation: 2026-05-20
prochaine_revue: 2027-05-20
controles_iso: ["5.3", "5.15", "5.16", "5.17", "5.18", "8.2", "8.3", "8.5", "8.18"]
---

# Politique de contrôle d'accès

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2024-03-01 | RSSI | Création |
| 1.1 | 2026-02-12 | RSSI | Alignement sur ISO/IEC 27001:2022 |
| 1.2 | 2026-05-20 | RSSI | Retrait automatique des droits lors d'une mobilité (INC-2026-003) |

## 1. Objet

Garantir que seules des personnes et des systèmes identifiés, authentifiés et autorisés
accèdent aux informations de KamaPay, au strict nécessaire de leur fonction.

## 2. Principes

1. **Moindre privilège** : un droit est accordé uniquement s'il est nécessaire à la fonction.
2. **Besoin d'en connaître** : un accès aux données KYC (A02) doit être justifié par une tâche.
3. **Refus par défaut** : tout ce qui n'est pas explicitement autorisé est interdit.
4. **Nominativité** : chaque compte est attribué à une personne identifiée. Les comptes
   génériques sont interdits, sauf les comptes techniques déclarés (point 6).
5. **Séparation des tâches** : selon la matrice de [GOV-01](../organisation-roles-raci.md).

## 3. Cycle de vie des accès

Le détail opérationnel figure dans [PROC-01](../procedures/PROC-01-gestion-des-acces.md).

| Étape | Exigence | Délai |
|---|---|---|
| Demande | Formulée par le manager, approuvée par le propriétaire de l'actif | Avant toute création |
| Création | Réalisée par la DSI à partir d'un profil type ; droits supplémentaires justifiés | 2 jours ouvrés |
| Mobilité | Les droits de l'ancien poste sont retirés automatiquement par l'outil RH | Le jour du changement |
| Départ | Désactivation de tous les comptes, révocation des jetons MFA et des certificats | Avant 18 h le dernier jour ; immédiat en cas de licenciement |
| Revue | Revue des droits par les propriétaires d'actifs | Trimestrielle (A01, A02, A04, A06), semestrielle (autres) |
| Comptes inactifs | Désactivation automatique | 45 jours sans connexion |

## 4. Authentification (contrôles 5.17 et 8.5)

| Population | Exigence |
|---|---|
| Salariés (SI interne) | Mot de passe d'au moins 14 caractères **et** MFA ; aucune rotation imposée sauf en cas de suspicion de compromission |
| Administrateurs | MFA matérielle (clé FIDO2) obligatoire, via le bastion |
| Back-office (A06) | MFA à chaque session ; session expirée après 15 min d'inactivité |
| Clients (USSD, application) | PIN de 4 chiffres plus possession de la SIM. Blocage après **3 PIN erronés** ; réinitialisation du PIN après un changement de SIM uniquement en agence, avec pièce d'identité (R01) |
| API partenaires (A04) | Jeton d'accès à durée de vie ≤ 1 h, secret client stocké dans un coffre ; limitation de débit sur `/v1/auth` (HTTP 429 au-delà du seuil) |
| Agents distributeurs | PIN agent et appareil enregistré |

Les secrets (mots de passe, clés, jetons) ne doivent **jamais** être stockés dans un dépôt
de code, un ticket ou une messagerie. Le contrôle `CHK-SECRET-01` vérifie l'absence de
secrets dans le code à chaque changement.

Le contrôle `CHK-AUTH-01` vérifie qu'aucune route sensible de l'API n'est accessible sans
authentification (réponse HTTP 401 attendue). Le contrôle `CHK-RATE-01` vérifie la
limitation de débit.

## 5. Accès privilégiés (contrôles 8.2 et 8.18)

- Les comptes à privilèges sont **distincts** des comptes bureautiques et ne lisent pas la
  messagerie.
- Toute administration de production passe par le **bastion**, qui enregistre les sessions.
  Les enregistrements sont conservés 12 mois.
- Les privilèges permanents sont limités. Les privilèges sur la plateforme cœur (A01) sont
  accordés **à la demande**, pour 8 h au maximum, avec un ticket de changement ou
  d'incident.
- Les comptes de service des applications n'ont **aucun privilège d'administration** sur
  les bases. Par exemple, le rôle `kamapay_app` de l'API n'est pas super-utilisateur et ne
  peut ni créer ni supprimer de tables (vérifié par `CHK-DB-01`).
- Les utilitaires à privilèges (outils de requêtage direct, consoles d'administration) ne
  sont installés que sur le bastion.
- La liste des comptes à privilèges est revue **chaque mois** par le RSSI.

## 6. Comptes techniques

Chaque compte technique a un propriétaire nommé, un usage documenté et un secret renouvelé
au moins une fois par an, ou immédiatement après le départ d'une personne qui le
connaissait.

## 7. Restriction d'accès aux informations (contrôle 8.3)

- Chaque requête de l'API doit vérifier que l'objet demandé (portefeuille, transaction)
  appartient bien à l'appelant. C'est la protection contre la faille d'autorisation au
  niveau objet (BOLA, risque R07), vérifiée par `CHK-AUTHZ-01`.
- Les données d'identité sont **masquées par défaut** dans le back-office et l'API
  (exemple : `2376****4521`). Le démasquage est réservé à des profils habilités et journalisé.
- Les exports de masse depuis le back-office nécessitent une habilitation spécifique,
  limitée à 5 personnes, et chaque export est journalisé.

## 8. Accès des tiers

Les accès des prestataires (éditeur P04 notamment) sont créés pour une durée limitée,
passent par le bastion et sont révoqués à la fin de l'intervention
([POL-04](POL-04-relations-fournisseurs.md)).

## 9. Contrôle et indicateurs

| Vérification | Fréquence | Responsable |
|---|---|---|
| Revue des droits A01, A02, A04, A06 (taux de réalisation suivi au comité de sécurité) | Trimestrielle | Propriétaires d'actifs / RSSI |
| Revue des comptes à privilèges | Mensuelle | RSSI |
| Rapprochement des comptes actifs avec la liste RH | Mensuel | DSI |
| Contrôles automatisés CHK-AUTH-01, CHK-AUTHZ-01, CHK-RATE-01, CHK-DB-01, CHK-SECRET-01 | À chaque changement | Pipeline de conformité |
