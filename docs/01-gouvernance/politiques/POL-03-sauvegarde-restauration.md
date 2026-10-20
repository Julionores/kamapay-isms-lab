---
id: POL-03
titre: Politique de sauvegarde et de restauration
version: "1.1"
statut: approuve
classification: interne
proprietaire: DSI
approbateur: Comité de sécurité
date_approbation: 2026-04-15
prochaine_revue: 2027-04-15
controles_iso: ["5.33", "8.13"]
---

# Politique de sauvegarde et de restauration

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2024-03-01 | DSI | Création |
| 1.1 | 2026-04-15 | DSI / RSSI | Sauvegardes immuables, test de restauration automatisé (risque R14) |

## 1. Objet

Garantir que les données de KamaPay peuvent être restaurées dans des délais compatibles
avec les objectifs de continuité, y compris après un rançongiciel (R06) ou la perte du
site principal (R05).

## 2. Objectifs de restauration

Ils sont issus de l'[analyse d'impact sur l'activité](../../06-resilience/bia.md).

| Actif | RPO (perte de données maximale) | RTO (délai de reprise maximal) |
|---|---|---|
| A01 Plateforme cœur (grand livre) | 15 min | 4 h |
| A02 Base clients et KYC | 15 min | 8 h |
| A04 API partenaires (configuration) | 24 h | 4 h |
| A06 Back-office | 24 h | 24 h |
| A09 Journaux et SIEM | 24 h | 72 h |
| A07 SI interne | 24 h | 72 h |

## 3. Règles de sauvegarde

| Élément | Exigence |
|---|---|
| Bases A01 / A02 | Réplication continue vers P02 (RPO 15 min), plus une sauvegarde complète quotidienne et l'archivage continu des journaux de transactions (WAL) |
| Règle 3-2-1-1 | 3 copies, sur 2 supports différents, dont 1 hors site (P02) et 1 **hors ligne ou immuable** |
| Chiffrement | AES-256 avant transfert ([POL-02](POL-02-cryptographie.md)) ; clés conservées hors du système de sauvegarde |
| Accès | Console de sauvegarde accessible depuis le bastion uniquement ; comptes distincts des administrateurs de production |
| Suppression | Impossible pendant la période d'immuabilité, même pour un administrateur |
| Surveillance | Tout échec de sauvegarde génère une alerte traitée sous 1 jour ouvré |

## 4. Durées de conservation

| Données | Conservation |
|---|---|
| Sauvegardes quotidiennes | 35 jours |
| Sauvegardes mensuelles | 12 mois |
| Archives des opérations de paiement et dossiers KYC | 10 ans après la clôture du compte (exigences LBC/FT et du régulateur ; contrôle 5.33) |
| Journaux de sécurité | 12 mois en ligne, puis archivés selon [POL-06](POL-06-journalisation-surveillance.md) |

## 5. Tests de restauration

Une sauvegarde qui n'a jamais été restaurée ne compte pas comme une sauvegarde.

| Test | Fréquence | Critère de réussite |
|---|---|---|
| Restauration automatisée d'une base dans un environnement isolé, avec contrôle d'intégrité (nombre de lignes et totaux des soldes identiques) | **Hebdomadaire**, et à chaque exécution du pipeline de conformité | Succès, et durée compatible avec le RTO |
| Restauration d'un fichier ou d'une table à la demande | Trimestrielle | Délai < 4 h |
| Bascule complète vers P02 | Semestrielle (PA-05) | RTO et RPO respectés |

Le lab met en œuvre le test automatisé avec le script `lab/scripts/test-restauration.sh` :
sauvegarde logique, restauration dans un conteneur vierge, comparaison des données et
mesure du temps de restauration. Le résultat est publié dans le
[rapport de test de restauration](../../06-resilience/rapport-test-restauration.md) et
contrôlé par `CHK-BKP-01`.

## 6. Responsabilités

- **DSI** : exécute les sauvegardes et les tests, tient le journal des tests.
- **RSSI** : vérifie chaque trimestre les résultats et l'immuabilité.
- **Propriétaires d'actifs** : valident les RPO / RTO lors de la revue annuelle de la BIA.
