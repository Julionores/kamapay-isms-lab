---
id: CTX-03
titre: Parties intéressées et registre des exigences
version: "1.1"
statut: approuve
classification: interne
proprietaire: Responsable Conformité
approbateur: Directeur Général
date_approbation: 2026-07-10
prochaine_revue: 2027-01-10
controles_iso: ["5.5", "5.6", "5.31"]
---

# Parties intéressées et registre des exigences

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2026-02-10 | Responsable Conformité | Création |
| 1.1 | 2026-07-10 | Responsable Conformité | Revue semestrielle : ajout des exigences contractuelles de l'opérateur sur le SIM swap |

Ce document répond aux clauses **4.1 et 4.2 d'ISO/IEC 27001:2022** et au contrôle **5.31**.
Il est revu **chaque semestre** par le Responsable Conformité, avec l'appui du RSSI et du
DPO.

> Les références aux textes locaux sont données au niveau du texte, sans citer d'articles.
> Avant tout usage opérationnel, la Direction Juridique doit valider la version en vigueur
> et les dispositions applicables.

## 1. Enjeux externes et internes (clause 4.1)

| Type | Enjeu | Effet sur le SMSI |
|---|---|---|
| Externe | Hausse de la fraude par SIM swap et ingénierie sociale dans la zone CEMAC | Risques R01 et R13 en priorité |
| Externe | Exigences croissantes du régulateur des services de paiement | Reporting des incidents, audits, continuité |
| Externe | Délestages électriques et qualité variable des liaisons | Contrôles 7.11 et 8.14, PCA |
| Externe | Peu d'hébergeurs certifiés dans la zone | Risque R08 accepté et suivi |
| Interne | Plateforme cœur dépendante d'un éditeur unique (P04) | Contrôles 5.21 et 8.30 |
| Interne | Équipe sécurité réduite (RSSI et 3 ingénieurs) | Priorité à l'automatisation des contrôles |
| Interne | Exigences de sécurité de l'actionnaire, alignées sur le RGPD | Politique POL-09 |

## 2. Parties intéressées (clause 4.2)

| Partie intéressée | Attentes principales | Comment le SMSI y répond | Responsable du suivi |
|---|---|---|---|
| Clients particuliers | Fonds disponibles et protégés, données confidentielles | Contrôles anti-fraude, masquage, continuité | Directeur des Opérations |
| Marchands et agrégateurs | Disponibilité de l'API, intégrité des paiements | SLA, limitation de débit, tests de sécurité | Directeur des Opérations |
| Agents distributeurs | Outils fiables, protection contre la fraude | Kit de sensibilisation, plafonds, détection | Resp. Réseau de distribution |
| Régulateur (COBAC / BEAC) | Respect de l'agrément, déclarations d'incidents, continuité, protection des fonds | Registre des incidents, PCA, audits | Responsable Conformité |
| Autorités nationales (ANTIC, autorité de protection des données) | Respect du droit national de la cybersécurité et des données personnelles | Déclarations, coopération lors des incidents | Responsable Conformité / DPO |
| Actionnaire KamaTel | Respect des politiques de sécurité du groupe, reporting | PSSI alignée, tableau de bord trimestriel | RSSI |
| Banques partenaires et banque de cantonnement | Sécurité des échanges, rapprochement fiable | TLS mutuel, double validation | DSI |
| Prestataires P01 à P04 | Exigences claires, accès maîtrisés | POL-04, plans d'assurance sécurité | Responsable Achats |
| Salariés | Règles claires, formation | Charte, programme de sensibilisation | RH / RSSI |
| Auditeurs externes et commissaires aux comptes | Preuves de l'efficacité des contrôles | SoA, preuves, contrôles automatisés | RSSI |

## 3. Registre des exigences légales, réglementaires et contractuelles (contrôle 5.31)

| Réf. | Source | Exigence principale | Contrôles liés | Preuve de conformité |
|---|---|---|---|---|
| EX-01 | Règlement n°04/18/CEMAC/UMAC/COBAC relatif aux services de paiement dans la CEMAC | Agrément, protection des fonds de la clientèle, sécurité et continuité des services, information du régulateur | 5.29, 5.30, 5.31, 8.13, 8.14 | PCA / PRA, rapports au régulateur |
| EX-02 | Loi n°2010/012 du 21 décembre 2010 relative à la cybersécurité et à la cybercriminalité au Cameroun | Sécurité des réseaux et des systèmes, conservation des données de connexion, coopération avec les autorités (ANTIC) | 5.5, 8.15, 5.28 | POL-06, procédure incidents |
| EX-03 | Réglementation nationale de protection des données personnelles | Licéité des traitements, sécurité, droits des personnes | 5.34, 8.10, 8.11 | POL-09, registre des traitements |
| EX-04 | RGPD (règlement (UE) 2016/679), imposé par la politique de l'actionnaire | Principes de l'article 5, sécurité (art. 32), notification des violations (art. 33 et 34), AIPD (art. 35) | 5.34, 5.26, 8.11 | POL-09, registre des incidents |
| EX-05 | Réglementation de lutte contre le blanchiment (LBC/FT) en vigueur dans la CEMAC | Connaissance du client (KYC), conservation des pièces, déclarations de soupçon | 5.33, 5.12 | Dossiers KYC, procédure Conformité |
| EX-06 | PCI DSS v4.0 (contractuel, pour l'émission de cartes virtuelles) | 12 exigences de sécurité des données de carte | voir la SoA (colonne PCI) | Rapport de conformité annuel |
| EX-07 | Contrat opérateur KamaTel (P03) | Disponibilité USSD 99,9 %, notification de changement de SIM, pare-feu de signalisation | 5.20, 8.21 | Plan d'assurance sécurité P03 ; écart PA-02 ouvert |
| EX-08 | Contrats d'hébergement P01 / P02 | Rapport ISAE 3402 type II annuel, droit d'audit, réversibilité | 5.19, 5.22, 7.1 à 7.13 | Rapports ISAE 3402 2025 |
| EX-09 | Politique de sécurité du groupe actionnaire | SMSI ISO/IEC 27001, reporting trimestriel, gestion des risques | 5.1, 5.4, 5.35 | Tableau de bord, revue de direction |

## 4. Relations avec les autorités (contrôle 5.5)

| Autorité | Motif de contact | Interlocuteur KamaPay | Délai cible |
|---|---|---|---|
| Régulateur des services de paiement (COBAC / BEAC) | Incident majeur, indisponibilité prolongée, fraude significative | Responsable Conformité | Dans le délai réglementaire en vigueur, au plus tard 24 h pour un P1 |
| ANTIC / CIRT national | Cyberattaque, demande d'assistance, partage d'indicateurs | RSSI | 24 h pour un P1 |
| Autorité de protection des données | Violation de données personnelles | DPO | 72 h (référence RGPD, art. 33) |
| Police judiciaire | Plainte pour fraude ou intrusion | Direction Juridique | Selon la procédure de plainte |

La liste des contacts, avec noms et numéros, est tenue hors dépôt par le Responsable
Conformité. Elle est vérifiée **chaque trimestre** par un appel test.

## 5. Groupes d'intérêt spécifiques (contrôle 5.6)

- Groupe de travail fraude des émetteurs de monnaie électronique de la zone (réunion mensuelle).
- Communauté sécurité de l'actionnaire (partage d'indicateurs de compromission).
- Associations professionnelles de la sécurité (OWASP, ISACA) pour la veille technique.

Les informations reçues sont exploitées selon la
[procédure de veille](../01-gouvernance/procedures/PROC-03-veille-securite.md).
