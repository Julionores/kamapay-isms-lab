---
id: RES-02
titre: Plan de continuité et de reprise d'activité (PCA / PRA)
version: "1.3"
statut: approuve
classification: confidentiel
proprietaire: DSI
approbateur: Directeur Général
date_approbation: 2026-06-15
prochaine_revue: 2027-06-15
controles_iso: ["5.29", "5.30", "8.14"]
---

# Plan de continuité et de reprise d'activité (PCA / PRA)

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-10-10 | DSI | Création |
| 1.2 | 2026-03-01 | DSI | Ajout du scénario rançongiciel |
| 1.3 | 2026-06-15 | DSI | Retour d'expérience INC-2026-004 (panne USSD) |

## 1. Objet

Ce plan décrit comment KamaPay SA maintient ses activités critiques et restaure son système d'information après une perturbation majeure, dans le respect des objectifs fixés par le [BIA](bia.md) : **RTO 4 h et RPO 15 min** pour la plateforme cœur (A01) et les processus de paiement.

## 2. Architecture de résilience

| Composant | Site principal (P01) | Site de secours (P02) | Mécanisme |
|---|---|---|---|
| Base de la plateforme cœur (A01) | Primaire | Réplique synchrone en lecture seule | Réplication en continu des journaux de transactions (WAL) |
| Base KYC (A02) | Primaire | Réplique asynchrone | Réplication continue, retard surveillé < 5 min |
| API et proxy | Actif | Passif, images identiques | Déploiement par le même pipeline |
| Passerelle USSD / SMS | Liaison principale vers KamaTel | Liaison de secours | Deux liaisons opérateur, routage commutable |
| Sauvegardes (A08) | Quotidiennes, chiffrées | Copie immuable, copie hors ligne hebdomadaire | Voir [POL-03](../01-gouvernance/politiques/POL-03-sauvegarde-restauration.md) |

La réplication répond au RPO de 15 min ; les sauvegardes protègent contre la corruption logique et le rançongiciel (une réplique recopierait la corruption).

## 3. Scénarios couverts

| Scénario | Stratégie | Risques liés |
|---|---|---|
| S1 Perte du site principal | Bascule complète sur P02 | R05, R08 |
| S2 Corruption logique de la base | Restauration à un point antérieur (sauvegarde + journaux) | R10, R14 |
| S3 Rançongiciel | Isolement, reconstruction depuis images et sauvegardes immuables | R06 |
| S4 Indisponibilité de l'opérateur (USSD) | Communication clients vers l'application, liaison de secours | R05, R08 |
| S5 Indisponibilité du siège | Travail à distance, centre d'appels de secours | — |
| S6 Défaillance de l'éditeur P04 | Séquestre du code source, support d'un intégrateur tiers | R08 |

## 4. Organisation de crise

| Rôle | Titulaire | Suppléant |
|---|---|---|
| Directeur de crise | Directeur Général | Directeur des Opérations |
| Responsable de la reprise informatique | DSI | Responsable exploitation |
| Responsable sécurité | RSSI | Analyste SOC senior |
| Conformité et notifications | Responsable Conformité | DPO |
| Communication | Responsable Communication | Assistant(e) de direction |

La cellule se réunit en salle de crise du siège ou en visioconférence (pont permanent). L'annuaire de crise est imprimé et mis à jour chaque trimestre.

## 5. Procédure de bascule (scénario S1)

| Étape | Action | Responsable | Durée cible |
|---|---|---|---|
| 1 | Constater l'indisponibilité, décider la bascule (si durée prévisible > 1 h) | Directeur de crise | T0 + 30 min |
| 2 | Geler les écritures sur le primaire si accessible | DSI | + 10 min |
| 3 | Promouvoir la réplique P02 en primaire, vérifier le dernier numéro de transaction | DBA | + 30 min |
| 4 | Démarrer API et proxy sur P02, basculer le DNS et la liaison opérateur | Exploitation | + 45 min |
| 5 | Tests de non-régression : transfert, cash-out, paiement marchand avec comptes de test | Exploitation + Opérations | + 30 min |
| 6 | Réouverture du service, communication clients et régulateur | Directeur de crise | + 15 min |
| 7 | Surveillance renforcée, rapprochement comptable des transactions en suspens | Finance + Fraude | Continu |

Total cible : **2 h 40**, sous le RTO de 4 h.

## 6. Procédure de restauration (scénario S2)

1. Identifier l'heure de la corruption à partir des journaux d'audit.
2. Restaurer la dernière sauvegarde complète sur un environnement isolé.
3. Rejouer les journaux de transactions jusqu'à l'instant précédant la corruption.
4. Contrôler l'intégrité : nombre de comptes, somme des soldes, nombre et somme des transactions, comparés aux valeurs du grand livre.
5. Remplacer la base de production après validation par la Finance.

Le contrôle d'intégrité de l'étape 4 est automatisé dans le lab par [`lab/scripts/test-restauration.sh`](../../lab/scripts/test-restauration.sh) ; le résultat est publié dans le [rapport de test de restauration](rapport-test-restauration.md) et vérifié par le contrôle automatisé CHK-BKP-01.

## 7. Programme de tests

| Test | Fréquence | Dernier | Prochain |
|---|---|---|---|
| Test de restauration automatisé (lab, CI) | À chaque exécution du pipeline de conformité | Voir le rapport généré | Continu |
| Restauration réelle d'une base de production sur environnement isolé | Trimestriel | 2026-09-12 | 2026-12 |
| Bascule complète sur le site de secours | Semestriel | 2026-04-18 | 2026-11-15 (PA-05) |
| Exercice de crise sur table | Semestriel | 2026-03-26 (EX-2026-01) | 2026-S2 |
| Test de l'annuaire de crise (appel de tous les membres) | Trimestriel | 2026-09-30 | 2026-12 |

Chaque test donne lieu à un compte rendu : durée mesurée par étape, écarts au RTO / RPO, actions correctives.

## 8. Maintien en condition opérationnelle

Le plan est revu après chaque test, chaque incident P1 de disponibilité et chaque changement majeur d'architecture. La DSI vérifie chaque trimestre que les images de secours, les accès d'urgence et l'annuaire sont à jour.
