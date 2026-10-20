---
id: PROC-03
titre: Procédure de veille sécurité et de renseignement sur les menaces
version: "1.0"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-06-15
prochaine_revue: 2027-06-15
controles_iso: ["5.6", "5.7"]
---

# Procédure de veille sécurité et de renseignement sur les menaces

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2026-06-15 | RSSI | Création |

## 1. Objet

Organiser la collecte, l'analyse et la diffusion des informations sur les menaces et vulnérabilités qui concernent KamaPay SA, pour anticiper les attaques (fraude au mobile money, rançongiciels, vulnérabilités de nos composants) et alimenter l'appréciation des risques.

## 2. Niveaux de renseignement

| Niveau | Contenu | Destinataires | Fréquence |
|---|---|---|---|
| Stratégique | Tendances de la fraude et de la cybercriminalité dans la zone CEMAC, évolutions réglementaires | Direction générale, comité sécurité | Trimestrielle |
| Tactique | Modes opératoires des attaquants (SIM swap, faux service client, hameçonnage ciblé) | Fraude, service client, DSI | Mensuelle |
| Opérationnel | Vulnérabilités de nos composants, indicateurs de compromission | DSI, cellule de surveillance | Continue |

## 3. Sources

| Source | Type | Usage |
|---|---|---|
| CIRT national (ANTIC) | Alertes et bulletins nationaux | Menaces visant les organisations camerounaises |
| CERT-FR (ANSSI) | Alertes et avis de sécurité | Vulnérabilités des produits courants |
| Catalogue CISA KEV | Vulnérabilités activement exploitées | Priorisation des correctifs (voir [POL-10](../politiques/POL-10-gestion-vulnerabilites-changements.md)) |
| Bases NVD et avis des éditeurs (dont l'éditeur P04) | Vulnérabilités | Correspondance avec l'inventaire des composants |
| GSMA (publications sur la fraude et la sécurité de la signalisation, FS.11) | Sécurité télécom et mobile money | Risques R01 et R09 |
| OWASP (API Security Top 10) | Sécurité applicative | Risque R07 |
| Groupe KamaTel (P03) : équipe sécurité du groupe | Partage interne d'indicateurs | Menaces visant l'opérateur et ses filiales |
| Groupe de travail fraude des émetteurs de monnaie électronique (5.6) | Partage d'information entre pairs | Numéros et modes opératoires de fraude |
| Alertes de la cellule fraude interne | Signaux faibles internes | Détection de nouvelles campagnes |

Le partage avec des groupes externes respecte la classification de l'information ([POL-08](../politiques/POL-08-classification-information.md)) : aucune donnée personnelle de client n'est partagée, sauf obligation légale.

## 4. Processus

1. **Collecte** : abonnement aux flux listés ; revue quotidienne par l'analyste de veille (30 minutes par jour ouvré).
2. **Qualification** : l'information concerne-t-elle un actif de l'[inventaire](../../../data/actifs.yaml) ou un scénario du [registre des risques](../../02-risques/registre-des-risques.md) ?
3. **Priorisation** :

   | Priorité | Critère | Action |
   |---|---|---|
   | Urgente | Vulnérabilité exploitée affectant un actif exposé, ou campagne de fraude en cours | Alerte immédiate à la DSI ou à la Fraude ; ouverture d'un événement selon la [procédure incidents](../../05-incidents/procedure-gestion-incidents.md) |
   | Normale | Menace pertinente sans exploitation constatée | Inscription au bulletin hebdomadaire et ticket de suivi |
   | Information | Tendance générale | Bulletin mensuel ou trimestriel |

4. **Diffusion** : bulletin selon le modèle ci-dessous.
5. **Suivi** : chaque action demandée est tracée dans un ticket jusqu'à clôture.
6. **Retour vers le SMSI** : une menace nouvelle ou en hausse déclenche la mise à jour du registre des risques et, si besoin, des règles de détection ([POL-06](../politiques/POL-06-journalisation-surveillance.md)).

## 5. Modèle de bulletin de veille

```
KAMAPAY - INTERNE                              Bulletin de veille n° 2026-S42
Période : 12/10/2026 - 18/10/2026        Rédacteur : analyste de veille, équipe RSSI

1. À retenir cette semaine (3 lignes maximum)
   - ...

2. Alertes urgentes
   | Réf. | Sujet | Actifs concernés | Action demandée | Responsable | Échéance |
   |------|-------|------------------|-----------------|-------------|----------|

3. Vulnérabilités à corriger
   | CVE | Produit / version | CVSS | Exploitée (KEV) | Actif | Délai POL-10 |
   |-----|-------------------|------|-----------------|-------|--------------|

4. Fraude et ingénierie sociale
   - Mode opératoire observé, canaux, recommandations au service client et aux agents

5. Réglementation et écosystème
   - Évolutions du régulateur, publications GSMA, autres émetteurs

6. Impact sur le registre des risques
   - Risque concerné (R..), proposition de réévaluation

Diffusion : DSI, Fraude, Conformité, Service client (sections 4 et 5)
```

## 6. Indicateurs

- Délai entre publication d'une vulnérabilité KEV touchant un actif et ouverture du ticket : cible < 24 h.
- Bulletins hebdomadaires publiés : cible 100 %.
- Nombre de mises à jour du registre des risques issues de la veille (suivi en revue de direction).
