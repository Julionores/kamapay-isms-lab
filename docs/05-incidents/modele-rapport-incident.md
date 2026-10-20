---
id: INC-02
titre: Modèle de rapport d'incident et de retour d'expérience
version: "1.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-03-20
prochaine_revue: 2027-03-20
controles_iso: ["5.27"]
---

# Modèle de rapport d'incident et de retour d'expérience

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-10-01 | RSSI | Création |
| 1.1 | 2026-03-20 | RSSI | Ajout de la section notifications |

Ce modèle est obligatoire pour les incidents P1 et P2 (voir la [procédure de gestion des incidents](procedure-gestion-incidents.md)). Il est rempli sous 10 jours ouvrés après le confinement et présenté au comité sécurité. Le rapport est classé **confidentiel**.

---

## 1. Identification

| Champ | Valeur |
|---|---|
| Identifiant | INC-AAAA-NNN |
| Titre | |
| Gravité finale | P1 / P2 |
| Catégorie | |
| Gestionnaire d'incident | |
| Rédacteur, date | |

## 2. Résumé pour la direction

Cinq lignes au maximum : ce qui s'est passé, impact, état actuel, décision attendue.

## 3. Chronologie (UTC)

| Horodatage | Événement | Source | Acteur |
|---|---|---|---|
| | Début estimé | | |
| | Détection | | |
| | Qualification | | |
| | Confinement | | |
| | Restauration | | |
| | Clôture | | |

Délais : détection = détection − début ; confinement = confinement − détection.

## 4. Périmètre et impact

| Axe | Constat |
|---|---|
| Actifs touchés (A01 à A10) | |
| Clients / agents concernés (nombre) | |
| Impact financier (FCFA, perte brute et récupérée) | |
| Données personnelles concernées (catégories, volume) | |
| Durée d'indisponibilité | |
| Impact réglementaire et image | |

## 5. Analyse

- **Cause racine** (méthode des 5 pourquoi) :
- **Facteurs contributifs** (techniques, humains, organisationnels, fournisseurs) :
- **Contrôles qui ont fonctionné** :
- **Contrôles absents ou défaillants** (référence annexe A) :
- **Risques du registre concernés** (R01 à R14) et cotation à revoir :

## 6. Notifications réalisées

| Destinataire | Date et heure | Canal | Référence |
|---|---|---|---|
| Régulateur | | | |
| ANTIC | | | |
| Autorité de protection des données / DPO groupe | | | |
| Clients | | | |
| Groupe actionnaire | | | |

## 7. Enseignements et actions

| ID action | Description | Responsable | Échéance | Contrôle annexe A |
|---|---|---|---|---|
| PA-xx | | | | |

## 8. Preuves

Liste des pièces collectées avec empreinte SHA-256 et référence de la fiche de chaîne de conservation.

## 9. Validation

| Rôle | Nom | Date | Visa |
|---|---|---|---|
| RSSI | | | |
| Responsable Conformité | | | |
| Directeur Général (P1) | | | |

---

## Mise à jour du registre

À la validation du rapport, le gestionnaire met à jour l'entrée de [`data/incidents.yaml`](../../data/incidents.yaml) : `cloture`, `statut: clos`, `cause_racine`, `enseignements`, `actions`, `notification`.
