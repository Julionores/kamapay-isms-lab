---
id: POL-06
titre: Politique de journalisation et de surveillance
version: "1.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-04-14
prochaine_revue: 2027-04-14
controles_iso: ["8.15", "8.16", "8.17"]
---

# Politique de journalisation et de surveillance

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-11-20 | RSSI | Création |
| 1.1 | 2026-04-14 | RSSI | Format JSON obligatoire du journal d'audit, interdiction des données personnelles en clair (suite à INC-2026-003) |

## 1. Objet

Cette politique fixe les règles de production, de protection, de conservation et d'exploitation des journaux du système d'information de KamaPay SA. Elle vise à :

- détecter rapidement les événements de sécurité (fraude, compromission, indisponibilité) ;
- disposer de preuves exploitables pour l'investigation, le régulateur et la justice ;
- respecter les exigences de traçabilité des opérations de paiement.

Elle répond au risque R12 (journalisation insuffisante) et contribue au traitement de R01, R02 et R04.

## 2. Périmètre

Tous les actifs du périmètre SMSI, en priorité : plateforme cœur A01, base KYC A02, passerelle USSD/SMS A03, API partenaires A04, back-office A06, SI interne A07 et SIEM A09.

## 3. Événements à journaliser

| Catégorie | Événements minimaux | Actifs |
|---|---|---|
| Opérations financières | Toute transaction (cash-in, cash-out, transfert, paiement marchand, régularisation), avec identifiant de transaction, comptes masqués, montant, canal, résultat | A01, A04, A05 |
| Authentification | Succès et échecs de connexion, verrouillages, réinitialisation de PIN, changement de MFA | A01, A04, A06, A07 |
| Habilitations | Création, modification, suppression de comptes et de droits ; élévation de privilèges | A06, A07 |
| Administration | Sessions sur le bastion (enregistrement vidéo), commandes privilégiées, modification de plafonds | A01, A06 |
| Données sensibles | Consultation et export de dossiers KYC depuis le back-office | A02, A06 |
| Sécurité réseau | Refus du pare-feu, alertes IDS, limitation de débit (HTTP 429) sur le proxy | A04 |
| Événements opérateur | Notifications de changement de SIM reçues de P03 | A03 |

## 4. Format et contenu

4.1. Le journal d'audit applicatif doit être structuré en **JSON**, une ligne par événement, avec au minimum : `horodatage` (UTC, ISO 8601), `evenement`, `acteur` (identifiant technique), `resultat`, `id_correlation`.

4.2. Aucune donnée personnelle ne doit figurer **en clair** : les MSISDN sont masqués (exemple `2376****4521`), les numéros de pièce d'identité, PIN, OTP, mots de passe et jetons ne sont jamais journalisés. Ce point est vérifié en continu par le contrôle automatisé **CHK-LOG-01**.

4.3. Toute modification du format doit être validée par le RSSI et répercutée dans les règles du SIEM.

## 5. Protection et conservation

| Exigence | Règle |
|---|---|
| Centralisation | Envoi au SIEM (A09) en moins de 5 minutes |
| Intégrité | Stockage en écriture seule ; les administrateurs systèmes n'ont pas le droit de suppression |
| Accès | Lecture réservée à l'équipe sécurité, à l'audit interne et, sur demande tracée, à la fraude |
| Conservation en ligne | 12 mois |
| Archivage | 10 ans pour les journaux d'opérations financières (voir [POL-03](POL-03-sauvegarde-restauration.md)) |
| Perte de collecte | Alerte au RSSI si une source n'émet plus depuis 30 minutes |

## 6. Synchronisation des horloges (8.17)

6.1. Tous les serveurs, équipements réseau et conteneurs doivent se synchroniser sur deux serveurs NTP internes, eux-mêmes alignés sur des sources de strate 1.

6.2. Les horodatages sont enregistrés en **UTC**. L'écart maximal toléré est de 1 seconde ; au-delà, une alerte est levée.

## 7. Surveillance (8.16)

7.1. Le SIEM doit appliquer au minimum les règles de corrélation suivantes :

| Règle | Description | Risque |
|---|---|---|
| DET-01 | Changement de SIM + réinitialisation de PIN + retrait dans les 24 h | R01 |
| DET-02 | Fractionnement : plus de 10 cash-in identiques par un même agent en 1 h | R02 |
| DET-03 | Export de plus de 500 fiches clients par un même utilisateur sur 24 h | R03 |
| DET-04 | Connexion administrateur hors bastion ou hors plage horaire | R04 |
| DET-05 | Plus de 20 réponses HTTP 429 depuis une même adresse sur l'API partenaires en 5 min | R07 |
| DET-06 | Arrêt de la collecte d'une source critique | R12 |

7.2. Les alertes de gravité haute sont traitées 24 h/24 par la cellule de surveillance ; elles alimentent la procédure de gestion des incidents ([INC-01](../../05-incidents/procedure-gestion-incidents.md)).

7.3. La limitation de débit sur l'authentification de l'API (contrôle **CHK-RATE-01**) fait partie du dispositif de surveillance et de protection contre la force brute.

7.4. Les règles de détection sont revues chaque semestre et après chaque incident P1 ou P2.

## 8. Rôles

| Rôle | Responsabilité |
|---|---|
| RSSI | Propriétaire de la politique, des règles SIEM et de la revue des accès aux journaux |
| DSI | Mise en œuvre technique de la collecte, de la synchronisation et de la conservation |
| Responsable Fraude | Définition et revue des règles DET-01 à DET-03 |
| Audit interne | Vérification annuelle de l'application de la politique |

## 9. Indicateurs

- Part des sources critiques collectées : cible 100 %.
- Délai moyen de détection des incidents P1/P2 (KPI-05) : cible < 4 h, voir le [tableau de bord](../../08-pilotage/tableau-de-bord.md).

## 10. Non-respect

Toute désactivation volontaire d'une journalisation ou suppression de journal est une faute relevant du processus disciplinaire (contrôle 6.4).
