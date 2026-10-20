---
id: PROC-02
titre: Procédure de gestion des changements
version: "1.1"
statut: approuve
classification: interne
proprietaire: DSI
approbateur: Directeur Général
date_approbation: 2026-04-30
prochaine_revue: 2027-04-30
controles_iso: ["8.32", "5.37", "8.31"]
---

# Procédure de gestion des changements

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-08-18 | DSI | Création |
| 1.1 | 2026-04-30 | DSI | Contrôles de conformité automatisés comme critère d'acceptation ; changements des prestataires (INC-2026-004) |

## 1. Objet

Garantir que toute modification du système d'information en production est évaluée, approuvée, testée, tracée et réversible. La procédure traite le risque R10 (changement non maîtrisé) et s'aligne sur la pratique *Change enablement* d'ITIL 4.

## 2. Types de changements

| Type | Définition | Approbation | Exemples |
|---|---|---|---|
| Standard | Changement pré-approuvé, à faible risque, suivant un mode opératoire validé | Aucune au cas par cas | Ajout d'un marchand dans l'API, renouvellement de certificat |
| Normal | Tout changement non standard | Comité des changements (CAB) hebdomadaire | Nouvelle version de la plateforme, modification de pare-feu |
| Urgent | Changement requis pour rétablir le service ou corriger une vulnérabilité critique | CAB d'urgence : DSI + RSSI + propriétaire de l'actif (par téléphone possible) | Correctif d'une vulnérabilité activement exploitée |

## 3. Déroulement d'un changement normal

| Étape | Contenu | Responsable |
|---|---|---|
| 1. Demande | Ticket décrivant le besoin, le périmètre, les actifs concernés, la date souhaitée | Demandeur |
| 2. Évaluation | Impact métier, impact sécurité (le RSSI est consulté si A01, A02, A04 ou A06 sont touchés), plan de test, plan de retour arrière | Responsable technique |
| 3. Approbation | Décision du CAB, consignée dans le ticket | CAB |
| 4. Construction et test | Réalisé en environnement de recette, séparé de la production (8.31) ; aucune donnée de production réelle | Équipe projet |
| 5. Contrôles de conformité | Le pipeline exécute les contrôles automatisés : scan de vulnérabilités (CHK-VULN-01), analyse statique (CHK-SAST-01), absence de secrets (CHK-SECRET-01), tests d'authentification et d'autorisation (CHK-AUTH-01, CHK-AUTHZ-01). Un échec bloque la livraison | Pipeline CI |
| 6. Mise en production | Dans la fenêtre approuvée (hors fins de mois et jours de forte activité), par une personne différente du développeur | Exploitation |
| 7. Vérification | Tests de bon fonctionnement, surveillance renforcée pendant 24 h | Exploitation |
| 8. Clôture | Mise à jour de la documentation et de la configuration de référence | Responsable technique |

## 4. Changements urgents

- Documentés au plus tard le jour ouvré suivant.
- Présentés au CAB suivant pour revue a posteriori.
- Plus de 10 % de changements urgents sur un trimestre déclenche une analyse de cause par la DSI.

## 5. Retour arrière

Tout changement normal ou urgent doit avoir un plan de retour arrière testé. Pour la plateforme cœur A01, le retour arrière d'une évolution de schéma de base de données doit être validé sur une copie restaurée (voir [rapport de test de restauration](../../06-resilience/rapport-test-restauration.md)).

## 6. Changements réalisés par les prestataires

Les prestataires (P01 à P04) notifient tout changement affectant les services de KamaPay SA au moins **72 heures** à l'avance (exigence ajoutée après l'incident INC-2026-004). Les changements non notifiés sont traités comme des incidents et suivis dans la revue des fournisseurs ([POL-04](../politiques/POL-04-relations-fournisseurs.md)).

## 7. Gel des changements

Aucun changement normal n'est autorisé :

- les 3 derniers et 2 premiers jours ouvrés de chaque mois (pics de transactions, paiement des salaires) ;
- pendant les périodes de fêtes déclarées par la Direction des Opérations.

## 8. Indicateurs

- Taux de changements ayant provoqué un incident : cible < 5 %.
- Taux de changements urgents : cible < 10 %.
- Changements non autorisés détectés : cible 0.
