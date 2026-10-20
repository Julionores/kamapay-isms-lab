---
id: CTX-02
titre: Domaine d'application du SMSI
version: "1.0"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-02-10
prochaine_revue: 2027-02-10
controles_iso: ["5.9", "5.23"]
---

# Domaine d'application du SMSI

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2026-02-10 | RSSI | Création, validée en comité de sécurité du 2026-02-05 |

Ce document répond à la clause **4.3 d'ISO/IEC 27001:2022** : il fixe les limites et
l'applicabilité du système de management de la sécurité de l'information (SMSI).

## 1. Énoncé du domaine d'application

> Le SMSI de KamaPay SA couvre **la conception, l'exploitation et le support des services
> de monnaie électronique mobile** (portefeuille client, paiement marchand, interopérabilité
> bancaire, réseau d'agents), **les systèmes d'information qui les supportent** et **les
> processus de gestion associés**. Il s'applique au siège de Douala et aux centres de
> données hébergés chez les prestataires P01 et P02. Il est conforme à la déclaration
> d'applicabilité en vigueur.

Cet énoncé figurera sur le certificat ISO/IEC 27001.

## 2. Périmètre organisationnel

| Inclus | Exclus |
|---|---|
| Toutes les directions de KamaPay SA (180 salariés) | Les activités propres de l'actionnaire KamaTel (téléphonie, données mobiles) |
| Les prestataires, pour les services rendus à KamaPay (contrôles 5.19 à 5.23) | Les systèmes internes des banques partenaires |
| Les agents distributeurs, pour l'usage de l'application agent et leurs obligations contractuelles | Les terminaux personnels des clients |

Les prestataires et les agents sont **dans le périmètre par leurs interfaces** : KamaPay
maîtrise les exigences contractuelles et leur contrôle, pas leurs systèmes internes.

## 3. Périmètre physique

| Site | Rôle | Maîtrise |
|---|---|---|
| Siège, Douala | Bureaux, service client, salle de supervision | Directe |
| Centre de données principal (P01) | Production | Contractuelle, avec rapport ISAE 3402 type II |
| Site de secours (P02) | Reprise d'activité, sauvegardes | Contractuelle, avec rapport ISAE 3402 type II |

## 4. Périmètre technique

Tous les actifs de l'inventaire `data/actifs.yaml` (A01 à A10) sont dans le périmètre.

## 5. Interfaces et dépendances

| Interface | Partie externe | Flux | Mesure de sécurité principale |
|---|---|---|---|
| USSD, SMS, OTP | KamaTel (P03) | Sessions USSD, OTP, notifications de changement de SIM | Liaison dédiée chiffrée, pare-feu de signalisation (GSMA FS.11) |
| API partenaires | Marchands, agrégateurs | REST / HTTPS | TLS 1.2 minimum, authentification, limitation de débit |
| Interopérabilité bancaire | Banques partenaires | Fichiers et API | TLS mutuel, signature des fichiers |
| Compte de cantonnement | Banque teneuse du compte | Rapprochement quotidien | Contrôle d'intégrité et double validation |
| Régulateur | COBAC / BEAC | Rapports réglementaires, déclarations d'incidents | Canal désigné, validation par la Conformité |
| Plateforme cœur | Éditeur P04 | Maintenance, correctifs | Accès via bastion, enregistrement des sessions |

## 6. Exclusions et justification

Aucun contrôle de l'annexe A n'est exclu (voir la
[déclaration d'applicabilité](../03-soa/declaration-applicabilite.md)). Les contrôles
physiques des centres de données (7.1 à 7.13) sont mis en œuvre **par les prestataires**.
KamaPay en vérifie l'efficacité par la revue annuelle de leurs rapports ISAE 3402 type II.

## 7. Révision

Le domaine d'application doit être revu :

- à chaque revue de direction (au moins une fois par an) ;
- avant tout nouveau produit, nouveau pays, changement d'hébergeur ou nouvelle activité
  agréée ;
- après tout incident de gravité P1 qui révèle une dépendance non couverte.
