---
id: CTX-01
titre: Présentation de KamaPay SA
version: "1.0"
statut: approuve
classification: public
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-02-10
prochaine_revue: 2027-02-10
controles_iso: []
---

# Présentation de KamaPay SA

> **Avertissement.** KamaPay SA est une entreprise **fictive**, créée pour ce laboratoire
> de démonstration. Toute ressemblance avec un établissement existant serait fortuite.
> Les chiffres, incidents et prestataires sont inventés mais réalistes.

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2026-02-10 | RSSI | Création |

## 1. Identité

| Élément | Valeur |
|---|---|
| Raison sociale | KamaPay SA |
| Statut | Établissement de paiement agréé pour l'émission de monnaie électronique dans la zone CEMAC |
| Siège | Douala, Cameroun |
| Actionnaire majoritaire | KamaTel SA, opérateur de téléphonie mobile (prestataire P03) |
| Effectif | 180 salariés |
| Clients actifs (90 jours) | environ 1,9 million |
| Réseau de distribution | 4 200 agents et sous-distributeurs |
| Volume mensuel | environ 21 millions de transactions |

## 2. Activités

KamaPay exploite un service de **monnaie électronique mobile**. Ses principaux produits sont :

1. **Portefeuille client** : ouverture de compte avec vérification d'identité (KYC), dépôt
   (cash-in) et retrait (cash-out) chez un agent, transfert entre particuliers.
2. **Paiement marchand** : paiement de factures, de commerçants et de services publics,
   par USSD (`*126#`), par l'application mobile et par l'API partenaires.
3. **Interopérabilité bancaire** : virements entre un portefeuille et un compte bancaire,
   via des banques partenaires et des agrégateurs.
4. **Réseau d'agents** : animation, commissionnement et contrôle des agents distributeurs.

## 3. Organisation

```
                        Conseil d'administration
                                  |
                          Directeur Général
                                  |
   +-----------+-----------+------+------+-----------+--------------+
   |           |           |             |           |              |
  DSI     Dir. Opérations  Conformité   Fraude      RH / Achats   RSSI (*)
   |           |           (DPO)         |
 Exploitation  Service client          Analyse
 Projets       Back-office             transactionnelle
 Réseaux       Réseau d'agents
```

(*) Le RSSI est rattaché directement au Directeur Général. Il est indépendant de la DSI,
ce qui évite que la même personne soit à la fois juge et partie (voir
[GOV-01](../01-gouvernance/organisation-roles-raci.md)).

## 4. Système d'information

| Composant | Actif | Hébergement |
|---|---|---|
| Plateforme cœur de portefeuille | A01 | Centre de données principal (P01), secours actif / passif (P02) |
| Base clients et KYC | A02 | P01, réplication vers P02 |
| Passerelle USSD / SMS / OTP | A03 | Opérateur KamaTel (P03) |
| API partenaires | A04 | P01, derrière le reverse proxy et le WAF |
| Application agent | A05 | Terminaux des agents |
| Back-office | A06 | P01, accès depuis le réseau interne uniquement |
| SI interne | A07 | Siège et service de bureautique en nuage |
| Sauvegardes | A08 | P02 et copie hors ligne |
| Journaux et SIEM | A09 | P01 |

La plateforme cœur est un progiciel de l'éditeur **P04**, paramétré et intégré par la DSI.

L'inventaire complet des actifs, avec leurs besoins de sécurité, se trouve dans
`data/actifs.yaml`. Il est évalué sur quatre critères : disponibilité, intégrité,
confidentialité et traçabilité (DICT).

## 5. Enjeux de sécurité

Pour un établissement de paiement, la sécurité de l'information **est le produit** :

- **Disponibilité** : chaque heure d'interruption bloque les paiements de centaines de
  milliers de clients et doit être déclarée au régulateur.
- **Intégrité** : le grand livre de monnaie électronique doit toujours correspondre au
  compte de cantonnement tenu en banque.
- **Confidentialité** : les dossiers KYC (pièces d'identité) sont des données personnelles
  sensibles et une cible de fraude.
- **Traçabilité** : chaque opération doit pouvoir être prouvée devant le régulateur, un
  juge ou un client.

Les menaces dominantes en 2026 sont la fraude par SIM swap, l'ingénierie sociale envers
les clients, la fraude d'agents et la compromission de comptes à privilèges. Elles sont
analysées dans le [registre des risques](../02-risques/registre-des-risques.md).

## 6. Documents liés

- [Périmètre du SMSI](perimetre-smsi.md)
- [Parties intéressées et exigences](parties-interessees-exigences.md)
- [Politique de sécurité des systèmes d'information](../01-gouvernance/PSSI.md)
