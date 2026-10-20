---
id: PRJ-01
titre: Intégration de la sécurité dans les projets IT et réseaux
version: "1.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-03-20
prochaine_revue: 2027-03-20
controles_iso: ["5.8", "8.26", "8.27"]
---

# Intégration de la sécurité dans les projets IT et réseaux

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-09-05 | RSSI | Création |
| 1.1 | 2026-03-20 | RSSI | Fiche d'analyse de risque projet, exigences mobile money, jalon prestataires |

## 1. Objet

Tout projet qui crée ou modifie un service, une application, une interconnexion ou une infrastructure de KamaPay SA doit intégrer la sécurité dès son lancement, et non au moment de la mise en production. Ce document définit :

- les **jalons sécurité** du cycle projet ;
- la **fiche d'analyse de risque projet** ;
- la **check-list des exigences de sécurité** à reprendre dans les cahiers des charges.

## 2. Classement du projet

Au lancement, le chef de projet et le correspondant sécurité classent le projet :

| Classe | Critères (au moins un) | Exigences |
|---|---|---|
| S1 - Sensible | Touche A01, A02, A04 ou A06 ; manipulation de fonds ; nouvelle interconnexion externe ; données KYC | Tous les jalons, test d'intrusion obligatoire, avis formel du RSSI |
| S2 - Standard | Touche le SI interne ou des données internes | Jalons J0, J2, J4 ; scans automatisés |
| S3 - Mineur | Aucun impact sur les données ou l'exposition | Check-list simplifiée |

## 3. Jalons sécurité

| Jalon | Phase projet | Livrables sécurité | Décision |
|---|---|---|---|
| **J0 - Cadrage** | Note de cadrage | Classe S1/S2/S3, actifs concernés, premières contraintes réglementaires (KYC, protection des données, régulateur) | Correspondant sécurité désigné |
| **J1 - Analyse de risque** | Expression de besoin | Fiche d'analyse de risque projet (section 4) ; analyse d'impact sur la protection des données si données personnelles ([POL-09](../01-gouvernance/politiques/POL-09-protection-donnees-personnelles.md)) | Exigences retenues validées par le RSSI |
| **J2 - Conception** | Architecture et spécifications | Dossier d'architecture conforme aux principes de la section 6 ; exigences de la check-list intégrées aux spécifications et au contrat du prestataire ([POL-04](../01-gouvernance/politiques/POL-04-relations-fournisseurs.md)) | Revue d'architecture sécurité |
| **J3 - Réalisation et recette** | Développement, intégration | Pipeline avec contrôles automatisés (CHK-SAST-01, CHK-VULN-01, CHK-SECRET-01), tests d'authentification et d'autorisation (CHK-AUTH-01, CHK-AUTHZ-01), test d'intrusion pour S1 | Vulnérabilités critiques et hautes corrigées ([POL-10](../01-gouvernance/politiques/POL-10-gestion-vulnerabilites-changements.md)) |
| **J4 - Mise en production** | Passage en exploitation | Configuration durcie, journalisation raccordée au SIEM, comptes de test supprimés, procédures d'exploitation, mise à jour de l'inventaire et du registre des risques | **Avis sécurité** : favorable, favorable avec réserves (plan d'action daté) ou défavorable |
| **J5 - Bilan** | Clôture | Réserves levées, risques résiduels acceptés par le propriétaire (ou le DG si > 6) | Clôture sécurité |

Un avis défavorable du RSSI au jalon J4 ne peut être levé que par le Directeur Général, avec acceptation formelle et écrite du risque résiduel.

## 4. Fiche d'analyse de risque projet

La fiche reprend la méthode du SMSI ([méthodologie des risques](../02-risques/methodologie-risques.md)) sous une forme allégée.

```
FICHE D'ANALYSE DE RISQUE PROJET                         KAMAPAY - CONFIDENTIEL
Projet : ......................      Classe : S1 / S2 / S3      Version : ...
Chef de projet : ...........         Correspondant sécurité : ...........
Date : ..../..../......

1. Description fonctionnelle (5 lignes)
2. Actifs concernés (référence inventaire : A01..A10) et nouveaux actifs créés
3. Besoins de sécurité (1 à 4)
   | Actif | Disponibilité | Intégrité | Confidentialité | Traçabilité |
4. Données personnelles traitées : oui / non  -> si oui, analyse d'impact (DPO)
5. Interconnexions et prestataires (sens des flux, protocole, authentification)
6. Scénarios de risque
   | N° | Scénario | Lien registre (R..) | V (1-4) | I (1-4) | Niveau | Mesures proposées | Résiduel |
7. Exigences de sécurité retenues (références de la check-list, section 5)
8. Risques résiduels et acceptation
   | N° | Niveau résiduel | Accepté par | Date |
9. Avis du RSSI : favorable / favorable avec réserves / défavorable
```

### Exemple rempli (extrait) : ouverture de l'API de paiement à un nouvel agrégateur

| N° | Scénario | Lien | V | I | Niveau | Mesures | Résiduel |
|---|---|---|---|---|---|---|---|
| 1 | L'agrégateur consulte les portefeuilles d'autres clients en modifiant l'identifiant dans la requête | R07 | 3 | 4 | 12 critique | Contrôle d'autorisation au niveau objet, test CHK-AUTHZ-01 en CI | 1 x 4 = 4 modéré |
| 2 | Vol de la clé API de l'agrégateur et transactions frauduleuses | R07 | 2 | 4 | 8 élevé | Authentification mutuelle TLS, liste blanche d'adresses, plafonds par partenaire | 1 x 3 = 3 faible |
| 3 | Force brute sur l'authentification | R07 | 3 | 3 | 9 élevé | Limitation de débit (CHK-RATE-01), alerte SIEM DET-05 | 1 x 3 = 3 faible |
| 4 | Indisponibilité de l'agrégateur entraînant des transactions en suspens | R08 | 2 | 3 | 6 modéré | Délais d'expiration, rapprochement quotidien | 2 x 2 = 4 modéré |

## 5. Check-list des exigences de sécurité (8.26)

Chaque exigence retenue est reprise dans les spécifications ou le contrat, avec sa méthode de vérification.

| Réf. | Domaine | Exigence | Vérification |
|---|---|---|---|
| EX-01 | Authentification | MFA pour tout accès d'administration ou de back-office ; PIN client de 4 à 6 chiffres verrouillé après 3 échecs | Recette, CHK-AUTH-01 |
| EX-02 | Authentification | Limitation du nombre de tentatives sur toute interface d'authentification exposée | CHK-RATE-01 |
| EX-03 | Autorisation | Contrôle d'autorisation côté serveur, au niveau de chaque objet (compte, transaction) | CHK-AUTHZ-01, test d'intrusion |
| EX-04 | Opérations sensibles | Réinitialisation de PIN, changement de MSISDN ou plafond : double validation ou contrôle renforcé ; prise en compte des notifications de changement de SIM | Recette fonctionnelle |
| EX-05 | Données | Masquage des MSISDN et numéros de pièce dans les réponses et écrans | CHK-MASK-01 |
| EX-06 | Cryptographie | TLS 1.2 minimum, HSTS, algorithmes de [POL-02](../01-gouvernance/politiques/POL-02-cryptographie.md) | CHK-TLS-01, CHK-TLS-02 |
| EX-07 | Journalisation | Journal d'audit JSON des opérations, sans donnée personnelle en clair, raccordé au SIEM | CHK-LOG-01 |
| EX-08 | Configuration | Conteneurs non root, lecture seule, sans privilège ; en-têtes de sécurité HTTP | CHK-CTR-01, CHK-HTTP-01 |
| EX-09 | Réseau | Bases de données sur réseau interne non exposé ; flux ouverts au strict nécessaire | CHK-NET-01 |
| EX-10 | Comptes techniques | Comptes applicatifs sans privilège d'administration | CHK-DB-01 |
| EX-11 | Code | Analyse statique sans constat HIGH ; aucun secret dans le code | CHK-SAST-01, CHK-SECRET-01 |
| EX-12 | Composants | Aucune vulnérabilité CRITICAL corrigeable dans les images livrées | CHK-VULN-01 |
| EX-13 | Continuité | RTO et RPO définis dans le [BIA](../06-resilience/bia.md) ; sauvegarde et restauration testées | CHK-BKP-01 |
| EX-14 | Réversibilité | Contrat prestataire avec clauses de sécurité, d'audit et de réversibilité | Revue du contrat |
| EX-15 | Télécom | Pour les interconnexions opérateur : pare-feu de signalisation et exigences des spécifications 3GPP applicables | Plan d'assurance sécurité |

## 6. Principes d'architecture sécurisée (8.27)

1. **Défense en profondeur** : proxy inverse TLS en frontal, application, base de données sur réseau interne ; aucun composant de données exposé directement.
2. **Moindre privilège** : chaque composant et chaque compte technique n'a que les droits nécessaires.
3. **Cloisonnement** : séparation stricte entre SI bureautique et production, entre environnements (développement, recette, production).
4. **Sécurité par défaut** : les fonctions sensibles sont désactivées tant qu'elles ne sont pas explicitement configurées.
5. **Traçabilité** : toute opération financière est attribuable et horodatée.
6. **Résilience** : pas de point unique de défaillance sur la chaîne de paiement.

L'architecture du [lab](../../lab/docker-compose.yml) illustre ces principes : seul le proxy est exposé, l'API et la base de données sont sur un réseau interne.

## 7. Indicateurs

- Projets S1 mis en production avec avis sécurité : cible 100 %.
- Réserves de jalon J4 levées dans les délais : cible ≥ 90 %.
