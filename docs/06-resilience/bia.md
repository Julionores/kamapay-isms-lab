---
id: RES-01
titre: Bilan d'impact sur l'activité (BIA)
version: "1.2"
statut: approuve
classification: confidentiel
proprietaire: DSI
approbateur: Directeur Général
date_approbation: 2026-05-28
prochaine_revue: 2027-05-28
controles_iso: ["5.29", "5.30"]
---

# Bilan d'impact sur l'activité (BIA)

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-09-15 | DSI | Création (méthode ISO 22301, clause 8.2.2) |
| 1.1 | 2026-02-28 | DSI | Ajout du canal USSD comme dépendance critique |
| 1.2 | 2026-05-28 | DSI | Révision après entretiens avec les directions métier |

## 1. Objet et méthode

Le BIA identifie les processus métier de KamaPay SA, l'impact de leur interruption dans le temps, et en déduit pour chacun :

- la **DMIA** (durée maximale d'interruption admissible), qui fixe l'objectif de reprise (RTO) ;
- la **PDMA** (perte de données maximale admissible), qui fixe l'objectif de point de reprise (RPO).

Les données ont été recueillies en entretiens avec les directions métier (Opérations, Fraude, Réseau de distribution, Conformité, Finance) puis validées par le comité de direction. L'échelle d'impact est celle de la [méthodologie des risques](../02-risques/methodologie-risques.md) (§ 4.2).

## 2. Impact dans le temps par processus

Notes d'impact de 1 (faible) à 4 (critique) selon la durée de l'interruption.

| Processus métier | Actifs | 1 h | 4 h | 24 h | 72 h | 1 sem. |
|---|---|---|---|---|---|---|
| P-01 Paiements et transferts clients (USSD, application) | A01, A03, A04 | 3 | 4 | 4 | 4 | 4 |
| P-02 Cash-in / cash-out en réseau d'agents | A01, A05 | 2 | 3 | 4 | 4 | 4 |
| P-03 Paiement marchand et API partenaires | A04, A01 | 2 | 3 | 4 | 4 | 4 |
| P-04 Détection et gestion de la fraude | A09, A06 | 2 | 3 | 3 | 4 | 4 |
| P-05 Service client et back-office | A06 | 1 | 2 | 3 | 3 | 4 |
| P-06 Ouverture de compte et KYC | A02 | 1 | 1 | 2 | 3 | 3 |
| P-07 Compensation et règlement avec les banques | A01, A10 | 1 | 2 | 3 | 4 | 4 |
| P-08 Reporting réglementaire | A01, A02 | 1 | 1 | 1 | 2 | 3 |
| P-09 Fonctions support (RH, paie, bureautique) | A07 | 1 | 1 | 2 | 2 | 3 |

## 3. Objectifs de reprise retenus

| Processus | DMIA (RTO) | PDMA (RPO) | Justification |
|---|---|---|---|
| P-01 Paiements et transferts | **4 h** | **15 min** | Au-delà de 4 h : impact 4 (régulateur, image). Toute transaction perdue crée un écart de grand livre |
| P-02 Cash-in / cash-out | 4 h | 15 min | Même plateforme que P-01 |
| P-03 Paiement marchand | 4 h | 15 min | Même plateforme que P-01 ; pénalités contractuelles marchands |
| P-04 Fraude | 8 h | 1 h | Mode dégradé possible : plafonds abaissés automatiquement |
| P-05 Service client | 24 h | 4 h | Mode dégradé : blocage de compte par procédure téléphonique |
| P-06 KYC | 72 h | 24 h | Ouvertures de comptes reportables |
| P-07 Compensation | 24 h | 15 min (données de transaction) | Règlement J+1 avec les banques |
| P-08 Reporting | 1 semaine | 24 h | Échéances mensuelles |
| P-09 Support | 72 h | 24 h | Travail possible depuis le service cloud de bureautique |

## 4. Dépendances critiques

| Dépendance | Processus | Mode dégradé / contournement |
|---|---|---|
| Opérateur mobile KamaTel (P03) : USSD, SMS, OTP | P-01, P-02 | Application mobile (données) ; aucun contournement pour les clients USSD seuls |
| Hébergeur principal (P01) | Tous | Bascule sur le site de secours P02 |
| Éditeur de la plateforme (P04) | P-01 à P-03 | Support contractuel 24 h/24 pour les P1 |
| Banques partenaires | P-07 | Règlement différé |
| Énergie au siège | P-05, P-09 | Onduleurs et groupe électrogène (autonomie 48 h) |
| Personnel clé (DSI, exploitation) | Tous | Astreinte, procédures documentées |

## 5. Ressources minimales en mode secours

| Ressource | Minimum requis pour P-01 à P-03 |
|---|---|
| Personnel | 2 exploitants, 1 administrateur base de données, 1 analyste fraude, 1 gestionnaire de crise |
| Infrastructure | Site P02 avec base répliquée, proxy, API, passerelle USSD |
| Accès | Bastion d'administration de secours, comptes d'urgence sous enveloppe scellée |

## 6. Conclusions

1. Les objectifs RTO 4 h et RPO 15 min pour la plateforme cœur A01 imposent une **réplication continue** vers le site de secours ; une sauvegarde quotidienne seule ne suffit pas.
2. Le canal USSD est un point de défaillance unique porté par un fournisseur : il est traité dans le risque R05 et le risque R08.
3. Les stratégies de continuité sont décrites dans le [PCA / PRA](pca-pra.md).
