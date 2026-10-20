---
id: PSSI
titre: Politique de sécurité des systèmes d'information
version: "2.0"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-02-12
prochaine_revue: 2027-02-12
controles_iso: ["5.1", "5.4"]
---

# Politique de sécurité des systèmes d'information (PSSI)

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2024-03-01 | RSSI | Première version |
| 2.0 | 2026-02-12 | RSSI | Refonte sur ISO/IEC 27001:2022, ajout des objectifs mesurables |

## 1. Engagement de la direction

KamaPay SA conserve la monnaie électronique et les données personnelles de près de
2 millions de clients. La confiance de ces clients, du régulateur et de nos partenaires
repose sur notre capacité à protéger leurs fonds et leurs informations.

La Direction Générale s'engage à :

1. établir, mettre en œuvre, tenir à jour et améliorer en continu un SMSI conforme à
   ISO/IEC 27001:2022 ;
2. respecter les exigences légales, réglementaires et contractuelles recensées dans le
   [registre des exigences](../00-contexte/parties-interessees-exigences.md) ;
3. fournir les ressources nécessaires : budget annuel validé en revue de direction,
   effectif de l'équipe sécurité, formation ;
4. présider la revue de direction au moins une fois par an.

Signé : le Directeur Général, le 12 février 2026.

## 2. Objet et domaine d'application

Cette politique fixe les principes de sécurité que doivent respecter **tous les salariés,
prestataires, stagiaires et agents distributeurs** qui accèdent aux informations ou aux
systèmes de KamaPay. Elle s'applique au domaine défini dans
[CTX-02](../00-contexte/perimetre-smsi.md).

## 3. Objectifs de sécurité 2026 (clause 6.2)

| N° | Objectif | Indicateur | Cible | Pilote |
|---|---|---|---|---|
| O1 | Protéger les fonds des clients contre la fraude | Montant net perdu par fraude / volume traité | < 0,01 % | Responsable Fraude |
| O2 | Garantir la disponibilité des paiements | Disponibilité mensuelle de A01 et A03 | ≥ 99,9 % | DSI |
| O3 | Mettre en œuvre les contrôles de la SoA | KPI-01 : contrôles applicables mis en œuvre | ≥ 85 % | RSSI |
| O4 | Détecter et contenir rapidement les incidents | KPI-05 et KPI-06 : délais moyens pour les P1 / P2 | < 4 h | RSSI |
| O5 | Maîtriser les risques | KPI-03 : risques au-delà de l'appétence non acceptés | 0 | RSSI |
| O6 | Développer la culture de sécurité | KPI-07 : taux de formation ; KPI-08 : taux de clic | ≥ 90 % ; < 10 % | RSSI / RH |

Les indicateurs sont définis dans les [indicateurs du SMSI](../08-pilotage/indicateurs-smsi.md)
et suivis dans le [tableau de bord](../08-pilotage/tableau-de-bord.md).

## 4. Principes de sécurité

1. **Gestion par les risques.** Toute décision de sécurité s'appuie sur l'analyse des
   risques ([méthodologie](../02-risques/methodologie-risques.md)). Un risque résiduel
   supérieur à l'appétence (niveau > 6) doit être accepté par écrit par le Directeur
   Général.
2. **Moindre privilège et besoin d'en connaître.** Les droits d'accès sont accordés au
   minimum nécessaire et revus chaque trimestre ([POL-01](politiques/POL-01-controle-acces.md)).
3. **Séparation des tâches.** Aucune personne ne peut, seule, initier et valider une
   opération qui crée ou déplace de la monnaie électronique.
4. **Défense en profondeur.** Aucun contrôle unique ne doit protéger un actif critique :
   cloisonnement réseau, authentification forte, journalisation et détection se cumulent.
5. **Sécurité dès la conception.** Les exigences de sécurité sont intégrées dès le début
   de chaque projet ([PRJ-01](../04-securite-projets/securite-dans-les-projets.md)).
6. **Traçabilité.** Toute opération financière et toute action privilégiée est journalisée
   et conservée selon [POL-06](politiques/POL-06-journalisation-surveillance.md).
7. **Vérification continue.** Dès que c'est possible, la conformité est vérifiée par des
   contrôles automatisés, exécutés à chaque changement (pipeline `conformite.yml`).
8. **Maîtrise des tiers.** Un prestataire ne reçoit des accès qu'après signature
   d'exigences de sécurité ([POL-04](politiques/POL-04-relations-fournisseurs.md)).

## 5. Cadre documentaire

| Niveau | Documents | Approbation |
|---|---|---|
| 1. Politique générale | Cette PSSI | Directeur Général |
| 2. Politiques thématiques | POL-01 à POL-10 | Comité de sécurité |
| 3. Procédures | PROC-01 à PROC-03, procédures incidents et continuité | RSSI |
| 4. Enregistrements | Registres (actifs, risques, incidents), SoA, rapports | Propriétaire du registre |

Chaque document porte une fiche d'identification : identifiant, version, propriétaire,
approbateur, date d'approbation, prochaine revue. Il est revu **au moins une fois par an**.
Le contrôle automatisé `CHK-DOC-01` signale tout document incomplet ou dont la date de
revue est dépassée.

## 6. Organisation

Les rôles et responsabilités sont décrits dans [GOV-01](organisation-roles-raci.md).
Le **comité de sécurité** se réunit chaque mois. Il réunit le Directeur Général (ou son
représentant), le RSSI, le DSI, le Directeur des Opérations, le Responsable Conformité,
le DPO et le Responsable Fraude.

## 7. Sensibilisation

Chaque salarié suit la sensibilisation à l'embauche puis chaque année. Chaque agent
distributeur reçoit le kit de sécurité à l'ouverture de son contrat
([programme de sensibilisation](../07-sensibilisation/programme-sensibilisation.md)).

## 8. Non-respect et dérogations

- Tout manquement à cette politique peut entraîner des sanctions disciplinaires (contrôle
  6.4) ou, pour un prestataire ou un agent, des pénalités et la résiliation du contrat.
- Une dérogation doit être demandée par écrit au RSSI. Elle précise le risque, la mesure
  compensatoire et une durée limitée à **6 mois**, renouvelable une fois. Les dérogations
  sont inscrites au registre des risques.

## 9. Révision

La PSSI est revue chaque année en revue de direction, et après tout changement majeur :
nouvelle activité, incident P1, évolution réglementaire.
