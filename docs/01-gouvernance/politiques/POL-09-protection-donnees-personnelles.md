---
id: POL-09
titre: Politique de protection des données à caractère personnel
version: "1.2"
statut: approuve
classification: interne
proprietaire: DPO
approbateur: Directeur Général
date_approbation: 2026-05-20
prochaine_revue: 2027-05-20
controles_iso: ["5.34", "8.10", "8.11"]
---

# Politique de protection des données à caractère personnel

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-05-02 | DPO | Création |
| 1.1 | 2025-12-01 | DPO | Masquage dans les API et le back-office |
| 1.2 | 2026-05-20 | DPO | Retour d'expérience INC-2026-003 (export non autorisé) |

## 1. Objet

KamaPay SA traite les données personnelles de près de 1,9 million de clients et de 4 200 agents. Cette politique fixe les principes de protection applicables, conformément au cadre légal camerounais applicable, aux exigences du régulateur des services de paiement de la CEMAC et aux standards du groupe actionnaire KamaTel, qui s'alignent sur le RGPD.

## 2. Données traitées

| Catégorie | Exemples | Actif | Classification |
|---|---|---|---|
| Identification | Nom, date de naissance, MSISDN | A02 | Secret (en base) |
| Pièces justificatives KYC | Numéro et copie de pièce d'identité, photo | A02 | Secret |
| Données financières | Solde, historique des transactions | A01 | Confidentiel |
| Données d'authentification | PIN (stocké haché), MFA des salariés | A01, A07 | Secret |
| Données des agents | Identité, localisation du point de vente, commissions | A05 | Confidentiel |

## 3. Principes

3.1. **Finalité et minimisation** : seules les données exigées par la réglementation KYC et par la fourniture du service sont collectées.

3.2. **Registre des traitements** : le DPO tient le registre des traitements, revu chaque semestre ; il est rapproché de l'[inventaire des actifs](../../../data/actifs.yaml).

3.3. **Protection dès la conception** : tout nouveau projet traitant des données personnelles passe le jalon « analyse d'impact » de la [démarche sécurité projet](../../04-securite-projets/securite-dans-les-projets.md).

3.4. **Sous-traitants** : les contrats comportent les clauses de sous-traitance définies dans la [politique fournisseurs](POL-04-relations-fournisseurs.md).

3.5. **Transferts hors du Cameroun** : soumis à l'avis préalable du DPO et aux garanties contractuelles requises.

## 4. Masquage des données (8.11)

4.1. Le MSISDN est masqué dans toutes les réponses d'API et dans les écrans du back-office, sauf habilitation spécifique : seuls les 4 premiers et 4 derniers chiffres sont visibles (exemple `2376****4521`).

4.2. Le numéro de pièce d'identité n'est jamais renvoyé par l'API ; dans le back-office, seuls les 3 derniers caractères sont visibles.

4.3. Les journaux ne contiennent aucune donnée personnelle en clair ([POL-06](POL-06-journalisation-surveillance.md)).

4.4. Les environnements de développement et de test utilisent des données fictives ou pseudonymisées ; la copie de données de production y est interdite (voir [POL-05](POL-05-developpement-securise.md)).

4.5. Le respect des règles 4.1 et 4.2 est vérifié automatiquement par le contrôle **CHK-MASK-01**.

## 5. Durées de conservation et suppression (8.10)

| Donnée | Durée | Action à échéance |
|---|---|---|
| Dossier KYC d'un compte clos | 10 ans après la clôture | Suppression définitive |
| Historique des transactions | 10 ans | Suppression ou anonymisation |
| Enregistrements d'appels du service client | 6 mois | Suppression automatique |
| Candidatures non retenues | 2 ans | Suppression |

**Écart connu** : la purge automatique des dossiers KYC des comptes clos depuis plus de 10 ans n'est pas encore développée (statut « partiel » dans la [déclaration d'applicabilité](../../03-soa/declaration-applicabilite.md)).

## 6. Droits des personnes

Les demandes d'accès, de rectification ou d'opposition sont reçues par le service client, transmises au DPO et traitées en 30 jours maximum. Toute demande est enregistrée dans un registre dédié.

## 7. Violations de données

7.1. Toute violation suspectée est déclarée immédiatement selon la [procédure de gestion des incidents](../../05-incidents/procedure-gestion-incidents.md).

7.2. Le DPO évalue, avec le RSSI et le Responsable Conformité, l'obligation de notifier l'autorité compétente, le régulateur et les personnes concernées. L'objectif interne est une décision en moins de 72 heures après la détection.

7.3. Exemple : INC-2026-003 (export non autorisé de 2 300 fiches) a donné lieu à notification du régulateur et de l'autorité de protection des données.

## 8. Rôles

| Rôle | Responsabilité |
|---|---|
| DPO | Propriétaire de la politique, registre des traitements, analyses d'impact, notifications |
| RSSI | Mesures de sécurité techniques et organisationnelles |
| Responsable Conformité | Propriétaire de la base KYC (A02), lien avec le régulateur |
| DSI | Mise en œuvre du masquage, de la purge et du chiffrement |
