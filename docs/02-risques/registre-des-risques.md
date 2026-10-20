<!-- Document généré par `python -m isms render` à partir de data/risques.yaml. Ne pas modifier. -->


# Registre des risques

Version 2.1 du 2026-10-05. Méthode : [méthodologie](methodologie-risques.md). Niveau = vraisemblance × impact ; appétence : résiduel ≤ 6.

## Cartographie des risques bruts

| Vraisemblance \ Impact | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **4** | · | · | R13 | R01 |
| **3** | · | · | R10, R12 | R02, R03, R04, R06, R07 |
| **2** | · | · | · | R05, R08, R09, R11, R14 |
| **1** | · | · | · | · |

## Cartographie des risques résiduels

| Vraisemblance \ Impact | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **4** | · | · | · | · |
| **3** | · | · | R13 | · |
| **2** | · | · | R01, R02, R03, R06 | R08 |
| **1** | · | · | R10, R12, R14 | R04, R05, R07, R09, R11 |

## Registre

| Risque | Intitulé | Actifs | Propriétaire | Brut | Traitement | Mesures ISO 27001 | Résiduel | Acceptation |
|---|---|---|---|---|---|---|---|---|
| R01 | Prise de contrôle de comptes clients par SIM swap frauduleux | A03, A01, A06 | Responsable Fraude | 16 (critique) | Réduire | 5.14, 5.19, 5.20, 8.5, 8.16, 5.24 | 6 (modéré) | non requise |
| R02 | Fraude interne ou collusion d'agents distributeurs | A05, A06, A01 | Responsable Fraude | 12 (critique) | Réduire | 5.3, 5.18, 8.2, 8.15, 8.16, 6.4 | 6 (modéré) | non requise |
| R03 | Fuite de données KYC | A02, A04, A06, A08 | Responsable Conformité | 12 (critique) | Réduire | 5.12, 5.34, 8.3, 8.11, 8.12, 8.24 | 6 (modéré) | non requise |
| R04 | Compromission d'un compte administrateur de la plateforme | A01, A06, A07 | RSSI | 12 (critique) | Réduire | 8.2, 8.5, 8.18, 6.3, 5.17 | 4 (modéré) | non requise |
| R05 | Indisponibilité prolongée de la plateforme de paiement | A01, A03, A04, A10 | DSI | 8 (élevé) | Réduire | 5.29, 5.30, 8.6, 8.14, 8.20 | 4 (modéré) | non requise |
| R06 | Rançongiciel sur le SI interne avec propagation vers la production | A07, A01, A08 | RSSI | 12 (critique) | Réduire | 8.7, 8.22, 8.13, 8.1, 8.8 | 6 (modéré) | non requise |
| R07 | Exploitation d'une vulnérabilité de l'API partenaires | A04, A01 | Directeur des Opérations | 12 (critique) | Réduire | 8.25, 8.26, 8.28, 8.29, 8.8, 8.3 | 4 (modéré) | non requise |
| R08 | Défaillance d'un prestataire critique | A10, A01 | Responsable Achats | 8 (élevé) | Réduire | 5.19, 5.20, 5.21, 5.22, 5.23 | 8 (élevé) | Directeur Général, 2026-07-10 |
| R09 | Interception des OTP via les failles de signalisation (SS7) | A03 | DSI | 8 (élevé) | Réduire | 5.14, 8.5, 8.21 | 4 (modéré) | non requise |
| R10 | Changement non maîtrisé en production | A01 | DSI | 9 (élevé) | Réduire | 8.32, 8.31, 8.9, 8.29 | 3 (faible) | non requise |
| R11 | Non-conformité réglementaire | A02, A01 | Responsable Conformité | 8 (élevé) | Réduire | 5.31, 5.34, 5.35, 5.36, 5.5 | 4 (modéré) | non requise |
| R12 | Journalisation insuffisante empêchant l'investigation | A09, A01, A06 | RSSI | 9 (élevé) | Réduire | 8.15, 8.16, 8.17, 5.28 | 3 (faible) | non requise |
| R13 | Escroquerie des clients par faux service client | A01 | Responsable Fraude | 12 (critique) | Réduire | 6.3, 8.16, 5.24 | 9 (élevé) | Directeur Général, 2026-07-10 |
| R14 | Restauration impossible des sauvegardes | A08, A01 | DSI | 8 (élevé) | Réduire | 8.13, 5.30 | 3 (faible) | non requise |

## Plan de traitement des risques

| Action | Risque | Libellé | Responsable | Échéance | Statut |
|---|---|---|---|---|---|
| PA-01 | R01 | Intégrer l'API de notification SIM swap de l'opérateur | DSI | 2026-11-30 | En cours |
| PA-02 | R01 | Ajouter la clause SIM swap dans le contrat opérateur (SLA 5 min) | Responsable Achats | 2026-12-15 | En cours |
| PA-03 | R02 | Déployer les règles de détection de fractionnement | Responsable Fraude | 2026-10-31 | Terminée |
| PA-04 | R03 | Mettre en place la DLP sur la messagerie (pièces jointes d'identité) | RSSI | 2027-02-28 | Planifiée |
| PA-05 | R05 | Réaliser le test de bascule du second semestre | DSI | 2026-11-15 | Planifiée |
| PA-06 | R08 | Étudier un second hébergeur dans la zone CEMAC | DSI | 2027-06-30 | Planifiée |
| PA-07 | R13 | Campagne radio nationale de sensibilisation clients | Responsable Fraude | 2026-12-31 | En cours |
| PA-08 | R03 | Alerte SIEM en temps réel sur les exports volumineux du back-office (retour d'expérience INC-2026-003, détecté en 55 h) | RSSI | 2026-12-15 | En cours |

## Scénarios

### R01 - Prise de contrôle de comptes clients par SIM swap frauduleux

Un fraudeur obtient un duplicata de carte SIM (complicité ou usurpation en boutique), reçoit les OTP du client, réinitialise le PIN et vide le portefeuille.

Mesures :

- Flux temps réel de changement de SIM fourni par l'opérateur et gel automatique de 48 h des opérations sortantes.
- Réinitialisation de PIN après changement de SIM uniquement en agence avec pièce d'identité.
- Règle de détection SIEM "changement SIM + réinitialisation PIN + retrait < 24 h".

### R02 - Fraude interne ou collusion d'agents distributeurs

Des agents réalisent des cash-in fictifs ou fractionnés pour capter des commissions, avec la complicité d'un employé du back-office qui valide les régularisations.

Mesures :

- Séparation des tâches saisie / validation des régularisations (principe des quatre yeux).
- Plafonds par agent et alertes sur les schémas de fractionnement.
- Revue trimestrielle des droits du back-office.

### R03 - Fuite de données KYC

Exfiltration de pièces d'identité et de MSISDN via une API mal protégée, un export du back-office ou une sauvegarde non chiffrée.

Mesures :

- Masquage des MSISDN et numéros de pièce dans les API et le back-office.
- Chiffrement des sauvegardes et des volumes de base de données.
- Exports du back-office soumis à habilitation et journalisés.

### R04 - Compromission d'un compte administrateur de la plateforme

Hameçonnage ciblé d'un administrateur, vol de session et exécution d'opérations privilégiées (création de monnaie, modification de plafonds).

Mesures :

- Bastion d'administration avec MFA matérielle et enregistrement des sessions.
- Comptes à privilèges nominatifs, séparés des comptes bureautiques.
- Campagnes d'hameçonnage simulé trimestrielles.

### R05 - Indisponibilité prolongée de la plateforme de paiement

Panne du centre de données principal ou attaque par déni de service sur l'API et le canal USSD, rendant les paiements impossibles plus de 4 heures.

Mesures :

- Site de secours actif / passif avec réplication des bases (RPO 15 min, RTO 4 h).
- Protection anti-DDoS du fournisseur de transit et limitation de débit sur le proxy.
- Test de bascule semestriel.

### R06 - Rançongiciel sur le SI interne avec propagation vers la production

Un poste infecté chiffre les partages réseau puis atteint les serveurs de production par réutilisation d'identifiants.

Mesures :

- EDR sur tous les postes et serveurs.
- Cloisonnement strict bureautique / production (aucun flux direct).
- Sauvegardes immuables et copie hors ligne testées.

### R07 - Exploitation d'une vulnérabilité de l'API partenaires

Un partenaire ou un attaquant exploite une faille d'autorisation au niveau objet (BOLA) pour consulter ou débiter le portefeuille d'un autre client.

Mesures :

- Contrôle d'autorisation au niveau objet sur chaque route (test automatisé en CI).
- Analyse statique et scan de vulnérabilités à chaque livraison.
- Test d'intrusion annuel par un tiers.

### R08 - Défaillance d'un prestataire critique

L'hébergeur principal ou l'éditeur de la plateforme subit un incident majeur, fait faillite ou ne respecte pas ses engagements de sécurité.

Mesures :

- Clauses de sécurité, de réversibilité et d'audit dans les contrats.
- Revue annuelle des rapports ISAE 3402 type II des prestataires.

Acceptation du risque résiduel : Pas d'hébergeur alternatif certifié au Cameroun à coût acceptable ; réévaluation en 2027.

### R09 - Interception des OTP via les failles de signalisation (SS7)

Un attaquant ayant accès au réseau de signalisation intercepte les SMS contenant les codes OTP de validation.

Mesures :

- Pare-feu de signalisation SS7 chez l'opérateur (exigence contractuelle, recommandations GSMA FS.11).
- Validation des opérations sensibles par PIN côté réseau USSD plutôt que par SMS.

### R10 - Changement non maîtrisé en production

Une mise en production sans test ni retour arrière provoque des écritures erronées dans le grand livre.

Mesures :

- Comité des changements (CAB) pour les changements normaux et urgents.
- Environnements séparés et pipeline de déploiement avec validations.

### R11 - Non-conformité réglementaire

Manquement aux obligations du régulateur des services de paiement (COBAC / BEAC) ou de protection des données personnelles, entraînant sanctions ou retrait d'agrément.

Mesures :

- Registre des exigences légales revu chaque semestre.
- Audit interne annuel du SMSI et audit externe de certification.

### R12 - Journalisation insuffisante empêchant l'investigation

Les journaux ne couvrent pas les opérations sensibles ou ne sont pas conservés, rendant impossibles la preuve et la remontée au régulateur.

Mesures :

- Journal d'audit structuré (JSON) pour toute opération financière, sans donnée personnelle en clair.
- Conservation 12 mois en ligne, 10 ans en archive.

### R13 - Escroquerie des clients par faux service client

Des fraudeurs se font passer pour le service client par appel ou SMS et obtiennent le PIN du client.

Mesures :

- Campagnes de sensibilisation clients (SMS, radio) "KamaPay ne vous demandera jamais votre PIN".
- Détection des comportements anormaux après appel entrant.

Acceptation du risque résiduel : Risque principalement porté par le comportement client ; réduction progressive par la sensibilisation.

### R14 - Restauration impossible des sauvegardes

Les sauvegardes existent mais sont corrompues, incomplètes ou trop lentes à restaurer pour respecter le RTO.

Mesures :

- Test de restauration automatisé avec contrôle d'intégrité des données (voir lab/scripts/test-restauration.sh).
