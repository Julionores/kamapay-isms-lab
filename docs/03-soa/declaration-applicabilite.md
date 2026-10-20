<!-- Document généré par `python -m isms render` à partir de data/soa.yaml et data/risques.yaml. Ne pas modifier. -->


# Déclaration d'applicabilité (SoA)

ISO/IEC 27001:2022, clause 6.1.3 d). Version 1.4 du 2026-10-05, approuvée par : Directeur Général.

## Synthèse

| Statut | Nombre |
|---|---:|
| Implémentée | 86 |
| Partielle | 6 |
| Planifiée | 1 |
| Non applicable | 0 |
| **Total** | **93** |

27 mesures sont vérifiées en continu par des contrôles automatisés (`checks/`).

## 5. Mesures organisationnelles

| Mesure | Intitulé | Statut | Justification | Preuves | Contrôle auto. |
|---|---|---|---|---|---|
| 5.1 | Politiques de sécurité de l'information | Implémentée | Exigence clause 5.2 et politique du groupe actionnaire. | [PSSI.md](../01-gouvernance/PSSI.md) | CHK-DOC-01 |
| 5.2 | Fonctions et responsabilités liées à la sécurité de l'information | Implémentée | Rôles requis par la clause 5.3. | [organisation-roles-raci.md](../01-gouvernance/organisation-roles-raci.md) | - |
| 5.3 | Séparation des tâches | Implémentée | Risque R02 | [organisation-roles-raci.md](../01-gouvernance/organisation-roles-raci.md)<br>[POL-01-controle-acces.md](../01-gouvernance/politiques/POL-01-controle-acces.md) | - |
| 5.4 | Responsabilités de la direction | Implémentée | Engagement de la direction (clause 5.1). | [PSSI.md](../01-gouvernance/PSSI.md)<br>[revue-de-direction.md](../08-pilotage/revue-de-direction.md) | - |
| 5.5 | Relations avec les autorités | Implémentée | Risque R11 | [parties-interessees-exigences.md](../00-contexte/parties-interessees-exigences.md)<br>[procedure-gestion-incidents.md](../05-incidents/procedure-gestion-incidents.md) | - |
| 5.6 | Relations avec des groupes d'intérêt spécifiques | Implémentée | Partage d'information sur la fraude avec les acteurs du mobile money. | [PROC-03-veille-securite.md](../01-gouvernance/procedures/PROC-03-veille-securite.md) | - |
| 5.7 | Renseignement sur les menaces | Implémentée | Exigence de veille de la fiche de poste RSSI. | [PROC-03-veille-securite.md](../01-gouvernance/procedures/PROC-03-veille-securite.md) | - |
| 5.8 | Sécurité de l'information dans la gestion de projet | Implémentée | Mesure de base de la PSSI | [securite-dans-les-projets.md](../04-securite-projets/securite-dans-les-projets.md) | - |
| 5.9 | Inventaire des informations et autres actifs associés | Implémentée | Mesure de base de la PSSI | [actifs.yaml](../../data/actifs.yaml) | - |
| 5.10 | Utilisation correcte des informations et autres actifs associés | Implémentée | Mesure de base de la PSSI | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md) | - |
| 5.11 | Restitution des actifs | Implémentée | Mesure de base de la PSSI | [PROC-01-gestion-des-acces.md](../01-gouvernance/procedures/PROC-01-gestion-des-acces.md) | - |
| 5.12 | Classification des informations | Implémentée | Risque R03 | [POL-08-classification-information.md](../01-gouvernance/politiques/POL-08-classification-information.md)<br>[actifs.yaml](../../data/actifs.yaml) | - |
| 5.13 | Marquage des informations | Partielle | Écart : Marquage automatique des documents bureautiques non déployé ; marquage manuel uniquement. | [POL-08-classification-information.md](../01-gouvernance/politiques/POL-08-classification-information.md) | - |
| 5.14 | Transfert des informations | Implémentée | Risques R01, R09 | [POL-08-classification-information.md](../01-gouvernance/politiques/POL-08-classification-information.md)<br>[POL-02-cryptographie.md](../01-gouvernance/politiques/POL-02-cryptographie.md) | CHK-TLS-01 |
| 5.15 | Contrôle d'accès | Implémentée | Mesure de base de la PSSI | [POL-01-controle-acces.md](../01-gouvernance/politiques/POL-01-controle-acces.md) | CHK-AUTH-01 |
| 5.16 | Gestion des identités | Implémentée | Mesure de base de la PSSI | [PROC-01-gestion-des-acces.md](../01-gouvernance/procedures/PROC-01-gestion-des-acces.md) | - |
| 5.17 | Informations d'authentification | Implémentée | Risque R04 | [POL-01-controle-acces.md](../01-gouvernance/politiques/POL-01-controle-acces.md) | CHK-SECRET-01 |
| 5.18 | Droits d'accès | Implémentée | Risque R02 | [PROC-01-gestion-des-acces.md](../01-gouvernance/procedures/PROC-01-gestion-des-acces.md) | CHK-AUTHZ-01 |
| 5.19 | Sécurité de l'information dans les relations avec les fournisseurs | Implémentée | Risques R01, R08 | [POL-04-relations-fournisseurs.md](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md) | - |
| 5.20 | La sécurité de l'information dans les accords conclus avec les fournisseurs | Partielle | Risques R01, R08; Écart : Clause de notification SIM swap absente du contrat opérateur (PA-02). | [POL-04-relations-fournisseurs.md](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md) | - |
| 5.21 | Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC | Implémentée | Risque R08 | [POL-04-relations-fournisseurs.md](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md) | - |
| 5.22 | Surveillance, révision et gestion des changements des services fournisseurs | Implémentée | Risque R08 | [POL-04-relations-fournisseurs.md](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md)<br>Rapports ISAE 3402 type II 2025 de P01 et P02 *(hors dépôt)* | - |
| 5.23 | Sécurité de l'information dans l'utilisation de services en nuage | Implémentée | Risque R08 | [POL-04-relations-fournisseurs.md](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md) | - |
| 5.24 | Planification et préparation de la gestion des incidents liés à la sécurité de l'information | Implémentée | Risques R01, R13 | [procedure-gestion-incidents.md](../05-incidents/procedure-gestion-incidents.md)<br>[EX-2026-01-sim-swap.md](../05-incidents/exercices/EX-2026-01-sim-swap.md) | - |
| 5.25 | Évaluation des événements liés à la sécurité de l'information et prise de décision | Implémentée | Mesure de base de la PSSI | [procedure-gestion-incidents.md](../05-incidents/procedure-gestion-incidents.md)<br>[incidents.yaml](../../data/incidents.yaml) | - |
| 5.26 | Réponse aux incidents liés à la sécurité de l'information | Implémentée | Mesure de base de la PSSI | [procedure-gestion-incidents.md](../05-incidents/procedure-gestion-incidents.md)<br>[incidents.yaml](../../data/incidents.yaml) | - |
| 5.27 | Tirer des enseignements des incidents liés à la sécurité de l'information | Implémentée | Mesure de base de la PSSI | [modele-rapport-incident.md](../05-incidents/modele-rapport-incident.md)<br>[incidents.yaml](../../data/incidents.yaml) | - |
| 5.28 | Recueil de preuves | Partielle | Risque R12; Écart : Chaîne de conservation des preuves formalisée mais aucun outil d'acquisition forensique en interne (recours à un prestataire). | [procedure-gestion-incidents.md](../05-incidents/procedure-gestion-incidents.md) | - |
| 5.29 | Sécurité de l'information durant une perturbation | Implémentée | Risque R05 | [pca-pra.md](../06-resilience/pca-pra.md) | - |
| 5.30 | Préparation des TIC pour la continuité d'activité | Implémentée | Risques R05, R14 | [bia.md](../06-resilience/bia.md)<br>[pca-pra.md](../06-resilience/pca-pra.md)<br>[rapport-test-restauration.md](../06-resilience/rapport-test-restauration.md) | CHK-BKP-01 |
| 5.31 | Exigences légales, statutaires, réglementaires et contractuelles | Implémentée | Risque R11 | [parties-interessees-exigences.md](../00-contexte/parties-interessees-exigences.md) | - |
| 5.32 | Droits de propriété intellectuelle | Implémentée | Licences logicielles et code de l'éditeur P04. | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md) | - |
| 5.33 | Protection des enregistrements | Implémentée | Conservation légale des opérations de paiement (10 ans). | [POL-03-sauvegarde-restauration.md](../01-gouvernance/politiques/POL-03-sauvegarde-restauration.md) | - |
| 5.34 | Protection de la vie privée et des données à caractère personnel | Implémentée | Risques R03, R11 | [POL-09-protection-donnees-personnelles.md](../01-gouvernance/politiques/POL-09-protection-donnees-personnelles.md) | CHK-MASK-01 |
| 5.35 | Révision indépendante de la sécurité de l'information | Implémentée | Risque R11 | [programme-audit-interne.md](../08-pilotage/programme-audit-interne.md) | - |
| 5.36 | Conformité aux politiques, règles et normes de sécurité de l'information | Implémentée | Risque R11 | [programme-audit-interne.md](../08-pilotage/programme-audit-interne.md) | CHK-DOC-01 |
| 5.37 | Procédures d'exploitation documentées | Implémentée | Mesure de base de la PSSI | [PROC-01-gestion-des-acces.md](../01-gouvernance/procedures/PROC-01-gestion-des-acces.md)<br>[PROC-02-gestion-des-changements.md](../01-gouvernance/procedures/PROC-02-gestion-des-changements.md) | CHK-DOC-01 |

## 6. Mesures liées aux personnes

| Mesure | Intitulé | Statut | Justification | Preuves | Contrôle auto. |
|---|---|---|---|---|---|
| 6.1 | Sélection des candidats | Implémentée | Postes à accès privilégié et manipulation de fonds. | Procédure RH de recrutement RH-PR-02 (vérification casier judiciaire) *(hors dépôt)* | - |
| 6.2 | Termes et conditions du contrat de travail | Implémentée | Mesure de base de la PSSI | Modèle de contrat de travail avec clause de sécurité et charte annexée *(hors dépôt)* | - |
| 6.3 | Sensibilisation, enseignement et formation en sécurité de l'information | Implémentée | Risques R04, R13 | [programme-sensibilisation.md](../07-sensibilisation/programme-sensibilisation.md)<br>[quiz-phishing.md](../07-sensibilisation/quiz-phishing.md)<br>[kit-agents-distributeurs.md](../07-sensibilisation/kit-agents-distributeurs.md)<br>[sensibilisation.yaml](../../data/sensibilisation.yaml) | - |
| 6.4 | Processus disciplinaire | Implémentée | Risque R02 | Règlement intérieur, article relatif aux manquements à la charte informatique *(hors dépôt)* | - |
| 6.5 | Responsabilités consécutivement à la fin ou à la modification du contrat de travail | Implémentée | Mesure de base de la PSSI | [PROC-01-gestion-des-acces.md](../01-gouvernance/procedures/PROC-01-gestion-des-acces.md) | - |
| 6.6 | Accords de confidentialité ou de non-divulgation | Implémentée | Mesure de base de la PSSI | Modèles d'accords de confidentialité salariés et prestataires *(hors dépôt)* | - |
| 6.7 | Travail à distance | Implémentée | Mesure de base de la PSSI | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md) | - |
| 6.8 | Déclaration des événements liés à la sécurité de l'information | Implémentée | Mesure de base de la PSSI | [procedure-gestion-incidents.md](../05-incidents/procedure-gestion-incidents.md)<br>[kit-agents-distributeurs.md](../07-sensibilisation/kit-agents-distributeurs.md) | - |

## 7. Mesures physiques

| Mesure | Intitulé | Statut | Justification | Preuves | Contrôle auto. |
|---|---|---|---|---|---|
| 7.1 | Périmètres de sécurité physique | Implémentée | Siège de Douala ; centres de données hébergés chez P01 / P02. | Rapports ISAE 3402 type II 2025 de P01 et P02 *(hors dépôt)*<br>Plan de zonage du siège *(hors dépôt)* | - |
| 7.2 | Les entrées physiques | Implémentée | Mesure de base de la PSSI | Registre des badges et journaux du contrôle d'accès du siège *(hors dépôt)* | - |
| 7.3 | Sécurisation des bureaux, des salles et des installations | Implémentée | Mesure de base de la PSSI | Plan de zonage du siège *(hors dépôt)* | - |
| 7.4 | Surveillance de la sécurité physique | Partielle | Écart : Vidéoprotection du siège sans conservation centralisée des enregistrements au-delà de 7 jours. | Contrat de télésurveillance du siège *(hors dépôt)* | - |
| 7.5 | Protection contre les menaces physiques et environnementales | Implémentée | Mesure de base de la PSSI | Rapports ISAE 3402 type II 2025 de P01 et P02 *(hors dépôt)* | - |
| 7.6 | Travail dans les zones sécurisées | Implémentée | Mesure de base de la PSSI | Procédure d'accès aux salles techniques de P01 *(hors dépôt)* | - |
| 7.7 | Bureau propre et écran vide | Implémentée | Mesure de base de la PSSI | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md) | - |
| 7.8 | Emplacement et protection du matériel | Implémentée | Mesure de base de la PSSI | Rapports ISAE 3402 type II 2025 de P01 et P02 *(hors dépôt)* | - |
| 7.9 | Sécurité des actifs hors des locaux | Implémentée | Mesure de base de la PSSI | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md) | - |
| 7.10 | Supports de stockage | Implémentée | Mesure de base de la PSSI | [POL-08-classification-information.md](../01-gouvernance/politiques/POL-08-classification-information.md) | - |
| 7.11 | Services généraux | Implémentée | Délestages électriques fréquents ; groupes électrogènes et onduleurs. | Contrats de maintenance onduleurs et groupes électrogènes du siège *(hors dépôt)* | - |
| 7.12 | Sécurité du câblage | Implémentée | Mesure de base de la PSSI | Rapports ISAE 3402 type II 2025 de P01 et P02 *(hors dépôt)* | - |
| 7.13 | Maintenance du matériel | Implémentée | Mesure de base de la PSSI | Contrats de maintenance matériel *(hors dépôt)* | - |
| 7.14 | Élimination ou recyclage sécurisé(e) du matériel | Implémentée | Mesure de base de la PSSI | [POL-08-classification-information.md](../01-gouvernance/politiques/POL-08-classification-information.md) | - |

## 8. Mesures technologiques

| Mesure | Intitulé | Statut | Justification | Preuves | Contrôle auto. |
|---|---|---|---|---|---|
| 8.1 | Terminaux finaux des utilisateurs | Implémentée | Risque R06 | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md) | - |
| 8.2 | Droits d'accès privilégiés | Implémentée | Risques R02, R04 | [POL-01-controle-acces.md](../01-gouvernance/politiques/POL-01-controle-acces.md)<br>[PROC-01-gestion-des-acces.md](../01-gouvernance/procedures/PROC-01-gestion-des-acces.md) | CHK-DB-01 |
| 8.3 | Restriction d'accès aux informations | Implémentée | Risques R03, R07 | [POL-01-controle-acces.md](../01-gouvernance/politiques/POL-01-controle-acces.md) | CHK-AUTHZ-01 |
| 8.4 | Accès aux codes source | Implémentée | Mesure de base de la PSSI | [POL-05-developpement-securise.md](../01-gouvernance/politiques/POL-05-developpement-securise.md) | CHK-SECRET-01 |
| 8.5 | Authentification sécurisée | Implémentée | Risques R01, R04, R09 | [POL-01-controle-acces.md](../01-gouvernance/politiques/POL-01-controle-acces.md) | CHK-AUTH-01, CHK-RATE-01 |
| 8.6 | Dimensionnement | Implémentée | Pics de transactions en fin de mois et jours de fête.; Risque R05 | Rapport mensuel de capacité de la DSI *(hors dépôt)* | - |
| 8.7 | Protection contre les programmes malveillants | Implémentée | Risque R06 | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md)<br>Console EDR - rapport de couverture *(hors dépôt)* | - |
| 8.8 | Gestion des vulnérabilités techniques | Implémentée | Risques R06, R07 | [POL-10-gestion-vulnerabilites-changements.md](../01-gouvernance/politiques/POL-10-gestion-vulnerabilites-changements.md)<br>[conformite.yml](../../.github/workflows/conformite.yml) | CHK-VULN-01 |
| 8.9 | Gestion de la configuration | Implémentée | Risque R10 | [POL-10-gestion-vulnerabilites-changements.md](../01-gouvernance/politiques/POL-10-gestion-vulnerabilites-changements.md)<br>[docker-compose.yml](../../lab/docker-compose.yml) | CHK-HTTP-01, CHK-CTR-01 |
| 8.10 | Suppression des informations | Partielle | Écart : Purge automatique des dossiers KYC des comptes clos depuis plus de 10 ans non encore développée. | [POL-09-protection-donnees-personnelles.md](../01-gouvernance/politiques/POL-09-protection-donnees-personnelles.md) | - |
| 8.11 | Masquage des données | Implémentée | Risque R03 | [POL-09-protection-donnees-personnelles.md](../01-gouvernance/politiques/POL-09-protection-donnees-personnelles.md)<br>[app.py](../../lab/api/app.py) | CHK-MASK-01 |
| 8.12 | Prévention de la fuite de données | Planifiée | Risque R03; Écart : DLP messagerie prévue (PA-04, février 2027). | - | - |
| 8.13 | Sauvegarde des informations | Implémentée | Risques R06, R14 | [POL-03-sauvegarde-restauration.md](../01-gouvernance/politiques/POL-03-sauvegarde-restauration.md)<br>[test-restauration.sh](../../lab/scripts/test-restauration.sh)<br>[rapport-test-restauration.md](../06-resilience/rapport-test-restauration.md) | CHK-BKP-01 |
| 8.14 | Redondance des moyens de traitement de l'information | Implémentée | Risque R05 | [pca-pra.md](../06-resilience/pca-pra.md) | - |
| 8.15 | Journalisation | Implémentée | Risques R02, R12 | [POL-06-journalisation-surveillance.md](../01-gouvernance/politiques/POL-06-journalisation-surveillance.md)<br>[app.py](../../lab/api/app.py) | CHK-LOG-01 |
| 8.16 | Activités de surveillance | Implémentée | Risques R01, R02, R12, R13 | [POL-06-journalisation-surveillance.md](../01-gouvernance/politiques/POL-06-journalisation-surveillance.md) | CHK-RATE-01 |
| 8.17 | Synchronisation des horloges | Implémentée | Risque R12 | [POL-06-journalisation-surveillance.md](../01-gouvernance/politiques/POL-06-journalisation-surveillance.md) | - |
| 8.18 | Utilisation de programmes utilitaires à privilèges | Implémentée | Risque R04 | [POL-01-controle-acces.md](../01-gouvernance/politiques/POL-01-controle-acces.md) | - |
| 8.19 | Installation de logiciels sur des systèmes opérationnels | Implémentée | Mesure de base de la PSSI | [POL-10-gestion-vulnerabilites-changements.md](../01-gouvernance/politiques/POL-10-gestion-vulnerabilites-changements.md) | CHK-CTR-01 |
| 8.20 | Sécurité des réseaux | Implémentée | Risque R05 | [docker-compose.yml](../../lab/docker-compose.yml)<br>[nginx.conf](../../lab/proxy/nginx.conf) | CHK-NET-01 |
| 8.21 | Sécurité des services réseau | Implémentée | Interconnexion avec l'opérateur mobile et les banques.; Risque R09 | [POL-04-relations-fournisseurs.md](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md) | CHK-TLS-01, CHK-TLS-02 |
| 8.22 | Cloisonnement des réseaux | Implémentée | Risque R06 | [docker-compose.yml](../../lab/docker-compose.yml) | CHK-NET-01 |
| 8.23 | Filtrage web | Partielle | Écart : Filtrage DNS déployé au siège mais pas sur les postes nomades. | [POL-07-usage-acceptable.md](../01-gouvernance/politiques/POL-07-usage-acceptable.md) | - |
| 8.24 | Utilisation de la cryptographie | Implémentée | Risque R03 | [POL-02-cryptographie.md](../01-gouvernance/politiques/POL-02-cryptographie.md)<br>[nginx.conf](../../lab/proxy/nginx.conf) | CHK-TLS-01, CHK-TLS-02 |
| 8.25 | Cycle de développement sécurisé | Implémentée | Risque R07 | [POL-05-developpement-securise.md](../01-gouvernance/politiques/POL-05-developpement-securise.md)<br>[conformite.yml](../../.github/workflows/conformite.yml) | CHK-SAST-01 |
| 8.26 | Exigences de sécurité des applications | Implémentée | Risque R07 | [securite-dans-les-projets.md](../04-securite-projets/securite-dans-les-projets.md) | - |
| 8.27 | Principes d'ingénierie et d'architecture des systèmes sécurisés | Implémentée | Mesure de base de la PSSI | [securite-dans-les-projets.md](../04-securite-projets/securite-dans-les-projets.md)<br>[docker-compose.yml](../../lab/docker-compose.yml) | - |
| 8.28 | Codage sécurisé | Implémentée | Risque R07 | [POL-05-developpement-securise.md](../01-gouvernance/politiques/POL-05-developpement-securise.md) | CHK-SAST-01, CHK-AUTHZ-01 |
| 8.29 | Tests de sécurité dans le développement et l'acceptation | Implémentée | Risques R07, R10 | [conformite.yml](../../.github/workflows/conformite.yml)<br>[checks](../../checks) | CHK-AUTHZ-01, CHK-AUTH-01 |
| 8.30 | Développement externalisé | Implémentée | La plateforme cœur est développée par l'éditeur P04. | [POL-04-relations-fournisseurs.md](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md) | - |
| 8.31 | Séparation des environnements de développement, de test et de production | Implémentée | Risque R10 | [POL-05-developpement-securise.md](../01-gouvernance/politiques/POL-05-developpement-securise.md) | - |
| 8.32 | Gestion des changements | Implémentée | Risque R10 | [PROC-02-gestion-des-changements.md](../01-gouvernance/procedures/PROC-02-gestion-des-changements.md) | - |
| 8.33 | Informations de test | Implémentée | Mesure de base de la PSSI | [POL-05-developpement-securise.md](../01-gouvernance/politiques/POL-05-developpement-securise.md)<br>[02-donnees-fictives.sql](../../lab/db/init/02-donnees-fictives.sql) | - |
| 8.34 | Protection des systèmes d'information en cours d'audit et de test | Implémentée | Mesure de base de la PSSI | [programme-audit-interne.md](../08-pilotage/programme-audit-interne.md) | - |
