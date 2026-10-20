---
id: GOV-01
titre: Organisation de la sécurité, rôles et matrice RACI
version: "1.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-05-20
prochaine_revue: 2027-05-20
controles_iso: ["5.2", "5.3", "5.4"]
---

# Organisation de la sécurité, rôles et matrice RACI

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2026-02-12 | RSSI | Création |
| 1.1 | 2026-05-20 | RSSI | Séparation saisie / validation des régularisations, suite à l'incident INC-2026-003 |

## 1. Rôles

| Rôle | Responsabilités principales en sécurité |
|---|---|
| **Directeur Général** | Porte le SMSI, approuve la PSSI et la SoA, accepte les risques résiduels supérieurs à l'appétence, préside la revue de direction. |
| **RSSI** | Pilote le SMSI : politiques, analyse de risques, SoA, contrôles, veille, gestion des incidents, sensibilisation, indicateurs. Il est rattaché au DG et dispose d'un droit d'alerte direct auprès du Conseil d'administration. |
| **Ingénieurs sécurité (3)** | Mettent en œuvre les contrôles techniques (SIEM, vulnérabilités, contrôles automatisés), répondent aux incidents, apportent l'expertise sécurité aux projets. |
| **DSI** | Exploite le SI de manière sécurisée : changements, sauvegardes, continuité, correctifs, configuration. |
| **Directeur des Opérations** | Propriétaire de l'API partenaires et du back-office ; garantit la séparation des tâches dans les opérations. |
| **Responsable Conformité** | Tient le registre des exigences, assure la relation avec le régulateur, déclare les incidents réglementaires. |
| **DPO** | Veille à la conformité des traitements de données personnelles, notifie les violations, conseille sur les analyses d'impact (AIPD). |
| **Responsable Fraude** | Détecte et traite la fraude ; propriétaire des risques R01, R02 et R13. |
| **Responsable Achats** | Intègre les clauses de sécurité dans les contrats, organise la revue des prestataires. |
| **RH** | Vérifie les antécédents à l'embauche, gère les départs et les mobilités, applique le processus disciplinaire. |
| **Audit interne** | Évalue de manière indépendante l'efficacité du SMSI (contrôle 5.35). |
| **Propriétaires d'actifs** | Classent leurs actifs, valident les droits d'accès, participent à l'analyse de risques. |
| **Tous les utilisateurs** | Respectent la charte, signalent tout événement suspect (contrôle 6.8). |

## 2. Indépendance et séparation des tâches (contrôle 5.3)

Les combinaisons suivantes sont **interdites** pour une même personne, ou pour un même
compte technique :

| Activité A | Activité B | Mesure de contrôle |
|---|---|---|
| Saisir une régularisation de solde | Valider cette régularisation | Validation par un second profil dans le back-office (principe des quatre yeux) |
| Développer une modification | La déployer en production | Pipeline de déploiement, approbation du CAB |
| Administrer un système | Administrer les journaux de ce système | Journaux transférés vers le SIEM, géré par l'équipe sécurité |
| Créer un compte utilisateur | Approuver les droits de ce compte | Approbation par le propriétaire de l'actif |
| Piloter le SMSI (RSSI) | Exploiter le SI (DSI) | Rattachements hiérarchiques distincts |
| Mettre en œuvre un contrôle | L'auditer | Audit interne ou cabinet externe |

Quand l'effectif ne permet pas la séparation (astreintes de nuit), une **revue a
posteriori sous 1 jour ouvré** par une seconde personne est obligatoire.

Le respect de ces règles est vérifié lors de la revue trimestrielle des accès
([PROC-01](procedures/PROC-01-gestion-des-acces.md)).

## 3. Instances

| Instance | Fréquence | Participants | Livrables |
|---|---|---|---|
| Comité de sécurité | Mensuelle | DG ou représentant, RSSI, DSI, Dir. Opérations, Conformité, DPO, Fraude | Suivi des risques, des incidents, des actions et des indicateurs |
| Comité des changements (CAB) | Hebdomadaire | DSI, RSSI ou délégué, demandeurs | Changements approuvés |
| Cellule de crise | Sur déclenchement (incident P1) | DG, RSSI, DSI, Conformité, Communication | Décisions, communication, déclarations |
| Revue de direction | Annuelle, ou après une crise majeure | Comité de direction | [Compte rendu PIL-03](../08-pilotage/revue-de-direction.md) |

## 4. Matrice RACI des processus du SMSI

R = réalise, A = rend compte (un seul A par ligne), C = consulté, I = informé.

| Processus | DG | RSSI | DSI | Dir. Ops | Conformité | DPO | Fraude | Achats | RH |
|---|---|---|---|---|---|---|---|---|---|
| PSSI et politiques | A | R | C | C | C | C | C | I | I |
| Analyse et traitement des risques | A | R | C | C | C | C | C | I | I |
| Acceptation des risques résiduels > 6 | R/A | C | I | I | I | I | I | I | I |
| Déclaration d'applicabilité | A | R | C | C | C | C | I | I | I |
| Gestion des accès | I | C | R | A | I | I | I | I | C |
| Revue trimestrielle des accès | I | A | R | R | I | I | C | I | I |
| Gestion des changements | I | C | A/R | C | I | I | I | I | I |
| Gestion des vulnérabilités | I | A | R | I | I | I | I | I | I |
| Gestion des incidents | I | A/R | R | R | C | C | R | I | I |
| Déclaration au régulateur | I | C | I | C | A/R | C | C | I | I |
| Notification de violation de données | I | C | I | I | C | A/R | I | I | I |
| Continuité et tests de PRA | A | C | R | R | I | I | I | I | I |
| Sécurité des fournisseurs | I | C | C | C | C | C | I | A/R | I |
| Sensibilisation | I | A/R | I | C | I | C | C | I | R |
| Arrivées, départs, mobilités | I | I | R | C | I | I | I | I | A/R |
| Audit interne | I | C | C | C | C | C | I | I | I |
| Revue de direction | A/R | R | C | C | C | C | C | I | I |

L'audit interne (non représenté en colonne) est **A/R** sur la ligne « Audit interne ».

## 5. Compétences (clause 7.2)

| Rôle | Compétences requises | Moyen de preuve |
|---|---|---|
| RSSI | Gouvernance ISO/IEC 27001, gestion des risques, connaissance de la réglementation des paiements | Diplôme Bac + 5 ; certification ISO 27001 Lead Implementer ou équivalent |
| Ingénieurs sécurité | Sécurité réseau et applicative, SIEM, réponse aux incidents | Certifications techniques, plan de formation annuel |
| Membres du CAB | Évaluation des risques d'un changement | Formation interne annuelle |

Les preuves de compétence sont conservées par les RH et vérifiées lors de l'audit interne.
