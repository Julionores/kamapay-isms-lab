---
id: POL-05
titre: Politique de développement sécurisé
version: "1.1"
statut: approuve
classification: interne
proprietaire: DSI
approbateur: Comité de sécurité
date_approbation: 2026-06-02
prochaine_revue: 2027-06-02
controles_iso: ["8.4", "8.25", "8.26", "8.27", "8.28", "8.29", "8.30", "8.31", "8.33"]
---

# Politique de développement sécurisé

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2024-03-01 | DSI | Création |
| 1.1 | 2026-06-02 | DSI / RSSI | Contrôles de sécurité automatisés obligatoires dans le pipeline |

## 1. Objet

Garantir que les applications développées ou paramétrées par KamaPay ou ses prestataires
(API partenaires, back-office, intégrations, scripts) sont sécurisées dès leur conception.
Cible principale : le risque R07 (exploitation de l'API).

## 2. Cycle de développement sécurisé (contrôle 8.25)

| Phase | Activité de sécurité obligatoire | Responsable |
|---|---|---|
| Expression du besoin | Exigences de sécurité et de protection des données ([PRJ-01](../../04-securite-projets/securite-dans-les-projets.md)) | Chef de projet, RSSI |
| Conception | Analyse de menaces (méthode STRIDE) pour toute nouvelle API ou tout nouveau flux financier | Architecte, ingénieur sécurité |
| Développement | Règles de codage du point 4 ; revue de code par un pair | Développeurs |
| Intégration continue | Contrôles automatisés du point 5, bloquants | Pipeline |
| Recette | Tests de sécurité fonctionnels (autorisation, plafonds, séparation des tâches) | Équipe de test |
| Mise en production | Approbation du CAB ([PROC-02](../procedures/PROC-02-gestion-des-changements.md)) | DSI |
| Exploitation | Test d'intrusion annuel par un tiers, et avant toute exposition Internet majeure | RSSI |

## 3. Exigences de sécurité des applications (contrôle 8.26)

Chaque API qui manipule des fonds ou des données personnelles doit, au minimum :

1. authentifier l'appelant et refuser tout accès anonyme aux routes métier (HTTP 401) ;
2. vérifier **à chaque requête** que l'objet demandé appartient à l'appelant (protection
   BOLA, OWASP API Security Top 10 : API1) ;
3. valider toutes les entrées (type, longueur, format, montants positifs, plafonds) ;
4. masquer les données d'identité dans les réponses (MSISDN `2376****4521`) ;
5. produire un journal d'audit structuré, sans donnée personnelle en clair
   ([POL-06](POL-06-journalisation-surveillance.md)) ;
6. rendre les opérations financières idempotentes, grâce à une clé d'idempotence, pour
   éviter les doubles débits ;
7. renvoyer des messages d'erreur génériques, sans trace technique.

## 4. Codage sécurisé (contrôle 8.28)

- Requêtes SQL **paramétrées uniquement**. La concaténation de chaînes dans une requête
  est interdite.
- Pas de secrets dans le code : ils sont lus depuis l'environnement ou le coffre.
- Les dépendances proviennent de dépôts officiels, avec des versions **figées**.
- Les avertissements de sécurité de l'analyse statique ne sont jamais ignorés sans
  justification écrite dans le code et validation du RSSI.

## 5. Contrôles automatisés bloquants (contrôle 8.29)

Le pipeline `.github/workflows/conformite.yml` doit réussir avant toute fusion :

| Contrôle | Outil | Critère de blocage |
|---|---|---|
| CHK-SAST-01 | Bandit (analyse statique Python) | Au moins un défaut de sévérité HIGH |
| CHK-VULN-01 | Trivy (image de conteneur) | Au moins une vulnérabilité CRITICAL corrigeable |
| CHK-SECRET-01 | Recherche de secrets | Au moins un secret détecté |
| CHK-AUTH-01 / CHK-AUTHZ-01 | Tests dynamiques de l'API | Accès sans authentification, ou à l'objet d'un tiers |
| CHK-MASK-01 / CHK-LOG-01 | Tests dynamiques de l'API | Donnée personnelle non masquée dans une réponse ou un journal |

## 6. Accès au code source (contrôle 8.4)

- Les dépôts sont privés. L'accès en écriture est limité aux développeurs du projet.
- La branche principale est protégée : pas de poussée directe, une revue est obligatoire
  et le pipeline doit être au vert.
- Les accès aux dépôts sont revus chaque trimestre ([PROC-01](../procedures/PROC-01-gestion-des-acces.md)).

## 7. Séparation des environnements (contrôle 8.31)

- Développement, recette et production sont des environnements distincts : réseaux,
  comptes et secrets différents.
- Les développeurs n'ont **aucun accès en écriture** à la production.
- Aucun déploiement ne se fait en production depuis un poste de travail : seul le pipeline
  déploie.

## 8. Données de test (contrôle 8.33)

- Il est **interdit** d'utiliser des données réelles de clients en développement ou en
  recette.
- Les jeux de données sont fictifs (voir `lab/db/init/02-donnees-fictives.sql`) ou
  anonymisés de manière irréversible, après validation du DPO.

## 9. Développement externalisé

Les livraisons de l'éditeur P04 suivent les mêmes contrôles
([POL-04](POL-04-relations-fournisseurs.md), contrôle 8.30).

## 10. Principes d'architecture (contrôle 8.27)

Les architectures appliquent les principes suivants :

- **cloisonnement** : la base n'est jamais exposée, seul le proxy l'est (vérifié par
  `CHK-NET-01`) ;
- **moindre privilège** : conteneurs sans root et en lecture seule (`CHK-CTR-01`), rôle de
  base de données limité (`CHK-DB-01`) ;
- **défense en profondeur** : TLS, puis limitation de débit, puis authentification, puis
  autorisation, puis journalisation ;
- **échec sécurisé** : en cas d'erreur, l'opération est refusée.
