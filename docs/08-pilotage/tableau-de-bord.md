<!-- Document généré par `python -m isms render` à partir de data/*.yaml et reports/checks.json. Ne pas modifier. -->


# Tableau de bord du SMSI

Situation au 2026-10-26. Définitions : [indicateurs du SMSI](indicateurs-smsi.md). Tendance : depuis le 2026-10-20.

## Indicateurs

| Indicateur | Libellé | Valeur | Cible | État | Tendance | Détail |
|---|---|---:|---|---|---|---|
| KPI-01 | Mesures applicables implémentées | 92.5 % | ≥ 85 % | Atteint | stable | 86 sur 93 |
| KPI-02 | Contrôles automatisés conformes | 100.0 % | 100 % | Atteint | stable | 16 sur 16 (exécution du 2026-10-26) |
| KPI-03 | Risques au-delà de l'appétence non acceptés | 0 | 0 | Atteint | stable | aucun |
| KPI-04 | Actions de traitement en retard | 0 | 0 | Atteint | stable | aucune |
| KPI-05 | Délai moyen de détection (P1/P2) | 14.91 h | < 4 h | **Non atteint** | stable | 4 incidents |
| KPI-06 | Délai moyen de confinement (P1/P2) | 1.21 h | < 4 h | Atteint | stable | 4 incidents |
| KPI-07 | Taux de formation (toutes campagnes) | 76.5 % | ≥ 90 % | **Non atteint** | stable | 3489 sur 4562 |
| KPI-08 | Taux de clic, dernier hameçonnage simulé | 6.1 % | < 10 % | Atteint | stable | PHISH-2026-03 |
| KPI-09 | Taux de signalement, dernier hameçonnage simulé | 38.1 % | ≥ 30 % | Atteint | stable | PHISH-2026-03 |
| KPI-10 | Documents dont la revue est à jour | 100.0 % | 100 % | Atteint | stable | 32 sur 32 |

## Incidents de l'année

8 incidents enregistrés, 1 non clos, 3 déclarés au régulateur.

| Gravité | Nombre |
|---|---:|
| P1 | 1 |
| P2 | 3 |
| P3 | 3 |
| P4 | 1 |

| Catégorie | Nombre |
|---|---:|
| fraude | 2 |
| compromission compte | 1 |
| fuite donnees | 1 |
| disponibilite | 1 |
| attaque applicative | 1 |
| logiciel malveillant | 1 |
| configuration | 1 |

## Contrôles automatisés (exécution du 2026-10-26T11:09:23+00:00)

| Contrôle | Mesures | Intitulé | Résultat | Détail |
|---|---|---|---|---|
| CHK-DOC-01 | 5.1, 5.36, 5.37 | Documents du SMSI identifiés, approuvés et revus dans les délais | PASS | 32 documents maîtrisés, revues à jour |
| CHK-SAST-01 | 8.25, 8.28 | Analyse statique du code de l'API sans défaut de sévérité haute | PASS | 137 lignes analysées ; sévérité haute : 0, moyenne : 0, basse : 0 |
| CHK-SECRET-01 | 5.17, 8.4 | Aucun secret dans les fichiers versionnés | PASS | 83 fichiers analysés, aucun secret |
| CHK-BKP-01 | 8.13, 5.30 | Test de restauration réussi depuis moins de 7 jours | PASS | test du 2026-10-26 : intègre, restauration en 3.63 s |
| CHK-VULN-01 | 8.8 | Image de l'API sans vulnérabilité critique corrigeable (Trivy) | PASS | scan du 2026-10-26 : 0 critique(s), 0 haute(s) (correctifs disponibles uniquement) |
| CHK-AUTH-01 | 8.5, 5.15, 8.29 | Les routes protégées refusent l'accès sans jeton valide | PASS | sans jeton : 401, jeton forgé : 401, virement sans jeton : 401 |
| CHK-AUTHZ-01 | 8.3, 5.18, 8.28, 8.29 | Un client ne peut pas lire le portefeuille d'un autre client (BOLA) | PASS | son portefeuille : 200, portefeuille d'un tiers : 403 |
| CHK-CTR-01 | 8.9, 8.19 | Conteneurs durcis : non-root, lecture seule, sans capacité | PASS | 3 conteneurs conformes |
| CHK-DB-01 | 8.2, 8.3 | Le rôle applicatif n'a ni privilège d'administration ni droit de suppression | PASS | privilège d'administration : f, droits interdits : aucun, modification du PIN : f |
| CHK-HTTP-01 | 8.9 | En-têtes de sécurité présents, version du serveur masquée | PASS | conforme |
| CHK-LOG-01 | 8.15, 5.28 | Journal d'audit structuré, sans donnée personnelle en clair | PASS | 3 événements d'audit, 0 incomplets, 0 non JSON, 0 avec donnée personnelle en clair |
| CHK-MASK-01 | 8.11, 5.34 | MSISDN et numéro de pièce d'identité masqués dans l'API | PASS | msisdn=2376****4521, id_number=CMR******451 |
| CHK-NET-01 | 8.20, 8.22 | La base n'est joignable que depuis le réseau interne | PASS | services publiés : proxy ; réseaux de la base internes : True ; port 5432 joignable depuis l'hôte : False |
| CHK-TLS-01 | 8.24, 5.14, 8.21 | Seuls TLS 1.2 et TLS 1.3 sont acceptés | PASS | acceptés : TLS 1.2, TLS 1.3 ; refusés : TLS 1.0, TLS 1.1 |
| CHK-TLS-02 | 8.24, 8.21 | HSTS actif et certificat valide plus de 14 jours | PASS | HSTS max-age=31536000 s ; certificat valide encore 89 jours |
| CHK-RATE-01 | 8.5, 8.16 | La force brute sur l'authentification est limitée (HTTP 429) | PASS | 7 réponses 429 sur 12 essais, blocage dès la tentative 6 |

## Historique des relevés

2 relevé(s) dans [data/historique-kpi.yaml](../../data/historique-kpi.yaml), complété chaque lundi par la CI ; les 12 plus récents sont affichés.

| Date | K01 | K02 | K03 | K04 | K05 | K06 | K07 | K08 | K09 | K10 | Contrôles |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2026-10-26 | 92.5 | 100 | 0 | 0 | 14.91 | 1.21 | 76.5 | 6.1 | 38.1 | 100 | 16/16 |
| 2026-10-20 | 92.5 | 100 | 0 | 0 | 14.91 | 1.21 | 76.5 | 6.1 | 38.1 | 100 | 16/16 |
