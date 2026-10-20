---
id: REF-01
titre: Référentiels normatifs et réglementaires
version: "1.1"
statut: approuve
classification: public
proprietaire: Responsable Conformité
approbateur: RSSI
date_approbation: 2026-10-05
prochaine_revue: 2027-10-05
controles_iso: []
---

# Référentiels normatifs et réglementaires

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2026-01-15 | Responsable Conformité | Création |
| 1.1 | 2026-10-05 | Responsable Conformité | Ajout ISAE 3402 et spécifications 3GPP |

> **Avertissement.** KamaPay SA est une entreprise fictive créée pour ce laboratoire. Les textes cités ci-dessous existent, mais leur interprétation dans ce dépôt est pédagogique ; toute mise en œuvre réelle doit être validée par un juriste et par le service conformité de l'établissement concerné.

## 1. Normes de sécurité de l'information

| Référence | Objet | Usage dans le SMSI |
|---|---|---|
| ISO/IEC 27001:2022 | Exigences d'un SMSI (clauses 4 à 10, annexe A de 93 contrôles) | Référentiel de certification ; structure de la [déclaration d'applicabilité](03-soa/declaration-applicabilite.md) |
| ISO/IEC 27002:2022 | Recommandations de mise en œuvre des contrôles | Rédaction des politiques et procédures |
| ISO/IEC 27005:2022 | Gestion des risques de sécurité de l'information | [Méthodologie des risques](02-risques/methodologie-risques.md) |
| ISO/IEC 27035 (série) | Gestion des incidents de sécurité | [Procédure de gestion des incidents](05-incidents/procedure-gestion-incidents.md) |
| ISO 22301:2019 | Management de la continuité d'activité | [BIA](06-resilience/bia.md) et [PCA / PRA](06-resilience/pca-pra.md) |

## 2. Cadres de gouvernance et de gestion des services

| Référence | Objet | Usage |
|---|---|---|
| COBIT 2019 (ISACA) | Gouvernance et gestion du SI ; référentiel utilisé pour les contrôles informatiques généraux de type SOX | Correspondance des contrôles (colonne COBIT de la SoA) |
| ITIL 4 | Pratiques de gestion des services (les processus ITIL V3 cités dans certains référentiels d'audit y sont repris sous forme de pratiques) | Correspondance des contrôles (colonne ITIL de la SoA), [gestion des changements](01-gouvernance/procedures/PROC-02-gestion-des-changements.md) |
| ISAE 3402 | Norme d'assurance sur les contrôles d'un prestataire de services (rapports type I et type II) | Revue annuelle des rapports des hébergeurs P01 et P02 ([POL-04](01-gouvernance/politiques/POL-04-relations-fournisseurs.md)) |
| SOX (contrôles informatiques généraux) | Accès logiques, changements, exploitation, sauvegardes | Exigences de reporting du groupe actionnaire |

## 3. Secteur des paiements

| Référence | Objet | Usage |
|---|---|---|
| Règlement n°04/18/CEMAC/UMAC/COBAC relatif aux services de paiement dans la CEMAC | Cadre des services de paiement et de l'émission de monnaie électronique dans la zone CEMAC (agrément, protection des fonds, gestion des risques, exigences de sécurité) | [Exigences légales et parties intéressées](00-contexte/parties-interessees-exigences.md), risque R11 |
| Instructions et exigences de la BEAC et de la COBAC | Déclarations, reporting et contrôles du régulateur | Notifications d'incidents, audits |
| PCI DSS v4.0 | Sécurité des données de cartes de paiement | Bonnes pratiques retenues (colonne PCI de la SoA) pour les flux de cartes des partenaires bancaires |

## 4. Protection des données et cybersécurité

| Référence | Objet | Usage |
|---|---|---|
| Loi n°2010/012 du 21 décembre 2010 relative à la cybersécurité et à la cybercriminalité au Cameroun | Obligations de sécurité des réseaux et systèmes, rôle de l'ANTIC | Exigences légales, relations avec les autorités (contrôle 5.5) |
| ANTIC (Agence Nationale des Technologies de l'Information et de la Communication) et son CIRT | Autorité nationale de cybersécurité, alertes | [Veille sécurité](01-gouvernance/procedures/PROC-03-veille-securite.md), signalement d'incidents |
| Règlement (UE) 2016/679 (RGPD) | Protection des données personnelles | Standard imposé par le groupe actionnaire ; colonne RGPD de la SoA ; [POL-09](01-gouvernance/politiques/POL-09-protection-donnees-personnelles.md) |
| Législation camerounaise applicable à la protection des données personnelles | Droits des personnes, obligations des responsables de traitement | À suivre par le DPO dans le registre des exigences légales |

## 5. Télécommunications et mobile money

| Référence | Objet | Usage |
|---|---|---|
| 3GPP TS 33.102 | Architecture de sécurité des réseaux 3G | Exigences envers l'opérateur P03 (canal USSD et SMS) |
| 3GPP TS 33.401 | Architecture de sécurité 4G (EPS) | Idem |
| 3GPP TS 33.501 | Architecture de sécurité 5G | Idem, évolutions futures |
| GSMA FS.11 | Surveillance et filtrage de la signalisation SS7 | Risque R09 (interception des OTP) |
| OWASP API Security Top 10 | Principales vulnérabilités des API | Risque R07, [sécurité dans les projets](04-securite-projets/securite-dans-les-projets.md) |
| Guides CIS (benchmarks) | Configurations de référence | [POL-10](01-gouvernance/politiques/POL-10-gestion-vulnerabilites-changements.md) |

## 6. Mise à jour

Le Responsable Conformité revoit ce document chaque année et à chaque évolution réglementaire signalée par la veille. Toute nouvelle exigence est répercutée dans le registre des exigences légales et, si nécessaire, dans la déclaration d'applicabilité.
