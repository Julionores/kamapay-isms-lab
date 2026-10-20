---
id: POL-04
titre: Politique de sécurité dans les relations avec les fournisseurs
version: "1.1"
statut: approuve
classification: interne
proprietaire: Responsable Achats
approbateur: Comité de sécurité
date_approbation: 2026-07-10
prochaine_revue: 2027-07-10
controles_iso: ["5.19", "5.20", "5.21", "5.22", "5.23", "8.21", "8.30"]
---

# Politique de sécurité dans les relations avec les fournisseurs

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2024-03-01 | Responsable Achats / RSSI | Création |
| 1.1 | 2026-07-10 | Responsable Achats / RSSI | Préavis de changement de 72 h (INC-2026-004), clause SIM swap (PA-02) |

## 1. Objet

Maîtriser les risques liés aux prestataires qui accèdent aux informations de KamaPay, les
traitent ou fournissent des services nécessaires à son activité (risque R08).

## 2. Classification des fournisseurs

| Niveau | Critère | Exemples |
|---|---|---|
| **Critique** | Son indisponibilité ou sa compromission affecte directement les paiements ou les données KYC | P01 hébergeur principal, P02 site de secours, P03 KamaTel (USSD, SMS, OTP), P04 éditeur de la plateforme |
| **Important** | Accès à des données internes ou confidentielles, sans effet direct sur les paiements | Service de bureautique en nuage, centre d'appels externalisé |
| **Standard** | Pas d'accès aux informations | Fournitures, entretien |

## 3. Exigences avant contractualisation

| Exigence | Critique | Important | Standard |
|---|---|---|---|
| Questionnaire de sécurité et analyse de risque par le RSSI | Oui | Oui | Non |
| Rapport ISAE 3402 type II, certificat ISO/IEC 27001 ou audit sur site | Oui | Recommandé | Non |
| Accord de confidentialité | Oui | Oui | Si accès aux locaux |
| Accord de sous-traitance des données personnelles (DPO) | Si données personnelles | Si données personnelles | Non |
| Plan de réversibilité | Oui | Recommandé | Non |

## 4. Clauses contractuelles obligatoires (contrôle 5.20)

Tout contrat avec un fournisseur critique doit comporter :

1. les exigences de sécurité applicables, avec un **plan d'assurance sécurité** (PAS)
   annexé ;
2. la **notification des incidents** de sécurité affectant KamaPay sous **4 heures** ;
3. un **préavis de 72 heures** pour tout changement susceptible d'affecter le service
   (ajout de la version 1.1, suite à l'incident INC-2026-004) ;
4. le **droit d'audit** de KamaPay ou d'un tiers mandaté, et la fourniture annuelle du
   rapport ISAE 3402 type II ;
5. les niveaux de service (disponibilité, délais de rétablissement) et des pénalités ;
6. la localisation des données et l'interdiction de sous-traiter sans accord écrit ;
7. la restitution puis la destruction attestée des données en fin de contrat ;
8. le respect de [POL-01](POL-01-controle-acces.md) pour les accès distants.

**Exigences spécifiques à l'opérateur KamaTel (P03)** :

- disponibilité du canal USSD ≥ 99,9 % par mois ;
- **notification en temps réel de tout changement de SIM** (délai cible ≤ 5 min), pour le
  gel automatique des opérations sortantes (risque R01). Cette clause est absente du
  contrat actuel ; l'avenant est en cours (action PA-02, écart sur le contrôle 5.20) ;
- pare-feu de signalisation SS7 / Diameter conforme aux recommandations **GSMA FS.11**
  (risque R09), et mesures de sécurité conformes aux spécifications 3GPP applicables
  (TS 33.102, 33.401, 33.501).

## 5. Chaîne d'approvisionnement TIC (contrôle 5.21)

- L'éditeur P04 doit fournir, pour chaque version, la liste des composants logiciels
  (SBOM) et le résultat de ses scans de vulnérabilités.
- Les correctifs de sécurité critiques doivent être livrés sous **15 jours**.
- Le code de la plateforme cœur est placé sous **séquestre** auprès d'un tiers.

## 6. Développement externalisé (contrôle 8.30)

Les livraisons de P04 sont soumises aux mêmes contrôles que les développements internes
([POL-05](POL-05-developpement-securise.md)) : analyse statique, scan de vulnérabilités et
tests de sécurité avant la recette.

## 7. Services en nuage (contrôle 5.23)

Avant d'adopter un service en nuage, il faut vérifier :

- la localisation des données ;
- le partage des responsabilités entre le fournisseur et KamaPay ;
- l'authentification unique et la MFA ;
- la journalisation disponible ;
- la réversibilité.

Les données classées « secret » (A02, A08) ne doivent pas être hébergées dans un service
en nuage public sans accord du comité de sécurité.

## 8. Surveillance des fournisseurs (contrôle 5.22)

| Activité | Critique | Important |
|---|---|---|
| Revue de performance et de sécurité | Trimestrielle | Annuelle |
| Revue du rapport ISAE 3402 type II (écarts, contrôles complémentaires à la charge du client) | Annuelle | Sur demande |
| Réévaluation du risque fournisseur | Annuelle | Tous les 2 ans |
| Audit sur site | Tous les 2 ans, ou après un incident majeur | Si nécessaire |

Les résultats sont présentés au comité de sécurité. Un écart non corrigé dans le délai
convenu est inscrit au registre des risques.

## 9. Fin de contrat

À la fin d'un contrat, la DSI révoque tous les accès le jour même. Le fournisseur restitue
puis détruit les données, et remet une attestation de destruction sous 30 jours.
