---
id: INC-01
titre: Procédure de gestion des incidents de sécurité de l'information
version: "2.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-03-20
prochaine_revue: 2027-03-20
controles_iso: ["5.5", "5.24", "5.25", "5.26", "5.27", "5.28", "6.8"]
---

# Procédure de gestion des incidents de sécurité de l'information

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-10-01 | RSSI | Création |
| 2.0 | 2026-02-25 | RSSI | Retour d'expérience INC-2026-001 (SIM swap) : ajout du gel préventif |
| 2.1 | 2026-03-20 | RSSI | Circuit de notification précisé |

## 1. Objet

Cette procédure organise la détection, la qualification, la réponse, la notification et le retour d'expérience pour tout événement ou incident de sécurité de l'information touchant le périmètre du SMSI. Elle met en œuvre les contrôles 5.24 à 5.28 et 6.8 d'ISO/IEC 27001:2022.

## 2. Définitions

- **Événement** : occurrence observée pouvant indiquer une atteinte à la sécurité (alerte SIEM, signalement d'un agent, plainte client).
- **Incident** : événement qualifié qui porte atteinte, ou risque fortement de porter atteinte, à la disponibilité, l'intégrité, la confidentialité ou la traçabilité d'un actif.
- **Cellule de crise** : instance activée pour les incidents P1 (voir § 5).

## 3. Rôles

| Rôle | Responsabilités |
|---|---|
| Tout salarié, agent ou prestataire | Signaler sans délai tout événement (§ 4) |
| Analyste SOC (N1) | Recevoir, enregistrer, qualifier en première analyse sous 30 min |
| RSSI (gestionnaire d'incident) | Valider la gravité, piloter la réponse, tenir le registre, décider des notifications avec la Conformité |
| DSI | Mesures techniques de confinement et de restauration |
| Responsable Fraude | Gel des comptes et des flux, coordination avec les partenaires |
| Responsable Conformité / DPO | Qualification réglementaire, notifications régulateur et autorité de protection des données |
| Directeur Général | Décisions de crise P1, communication externe |
| Responsable Communication | Messages clients et presse, validés par le DG |

## 4. Canaux de signalement

| Public | Canal |
|---|---|
| Salariés | Adresse dédiée securite@ (interne), bouton « Signaler » de la messagerie, poste 4444 |
| Agents distributeurs | Ligne agents, option « fraude » ; voir le [kit agents](../07-sensibilisation/kit-agents-distributeurs.md) |
| Clients | Service client, motif « fraude / compte piraté » |
| Prestataires (P01 à P04) | Contact sécurité défini au contrat, délai contractuel de signalement de 4 h au maximum |
| Outils | Alertes SIEM, EDR, contrôles automatisés (`checks/`) |

Aucune sanction n'est appliquée pour un signalement de bonne foi, y compris d'une erreur personnelle.

## 5. Matrice de gravité

| Gravité | Critères (un seul suffit) | Exemples | Délai de prise en charge | Escalade |
|---|---|---|---|---|
| **P1 critique** | Perte financière > 10 M FCFA ; fuite de données KYC massive ; indisponibilité du service de paiement > 1 h ; compromission d'un compte à privilèges confirmée | Vague de SIM swap, rançongiciel en production | 15 min, 24 h/24 | Cellule de crise, DG informé sous 1 h |
| **P2 majeur** | Perte 1 à 10 M FCFA ; fuite limitée de données personnelles ; indisponibilité d'un canal < 1 h sur le service global ; tentative de compromission privilégiée | Export non autorisé, panne USSD | 1 h | RSSI, DSI, Conformité |
| **P3 modéré** | Attaque bloquée sans impact durable ; fraude client isolée ; poste infecté isolé | Force brute bloquée, logiciel malveillant isolé | 4 h ouvrées | RSSI |
| **P4 mineur** | Écart de configuration sans exploitation, non-conformité détectée par un contrôle | Certificat proche de l'expiration | 2 jours ouvrés | Analyste SOC |

La gravité peut être relevée à tout moment de la vie de l'incident.

## 6. Déroulement

### 6.1 Détection et enregistrement

1. Tout événement reçu est enregistré dans l'outil de ticketing avec l'horodatage UTC de début estimé et de détection.
2. Tout événement qualifié en incident est reporté dans le registre [`data/incidents.yaml`](../../data/incidents.yaml) avec un identifiant `INC-AAAA-NNN`.

### 6.2 Qualification et décision

L'analyste N1 qualifie en 30 min : actifs touchés (A01 à A10), catégorie (`fraude`, `compromission_compte`, `fuite_donnees`, `disponibilite`, `attaque_applicative`, `logiciel_malveillant`, `configuration`), gravité provisoire. Le RSSI confirme la gravité et désigne le gestionnaire d'incident.

### 6.3 Confinement

Mesures types, à appliquer sans attendre l'analyse complète :

| Scénario | Mesures de confinement |
|---|---|
| Fraude sur comptes (SIM swap, faux service client) | Gel des opérations sortantes des comptes concernés, demande de gel aux partenaires bénéficiaires, blocage des MSISDN suspects |
| Compromission de compte | Désactivation du compte, révocation des sessions et jetons, rotation des secrets |
| Fuite de données | Coupure de l'accès ou de l'export, préservation des journaux |
| Logiciel malveillant | Isolement réseau par l'EDR, pas d'extinction avant acquisition |
| Indisponibilité | Activation du [PCA/PRA](../06-resilience/pca-pra.md) si la durée prévisible dépasse 1 h |

L'horodatage de confinement est consigné (champ `confinement`). L'indicateur KPI-06 mesure le délai détection → confinement pour P1/P2 (cible < 4 h).

### 6.4 Éradication et restauration

Suppression de la cause, correction, restauration contrôlée, surveillance renforcée pendant 72 h. La clôture technique est prononcée par le RSSI.

### 6.5 Clôture et retour d'expérience

- P1 et P2 : rapport selon le [modèle de rapport d'incident](modele-rapport-incident.md) sous 10 jours ouvrés, réunion de retour d'expérience, réévaluation des risques liés sous 30 jours (voir la [méthodologie des risques](../02-risques/methodologie-risques.md)).
- P3 et P4 : synthèse dans le registre (champs `cause_racine`, `enseignements`).
- Les actions correctives sont créées dans le plan de traitement (`PA-xx`).

## 7. Notifications

| Destinataire | Déclencheur | Délai cible | Responsable | Contenu |
|---|---|---|---|---|
| Régulateur des services de paiement (COBAC / BEAC) | Incident P1, ou P2 avec impact clients ou financier | Information initiale sous 24 h, rapport détaillé selon les exigences du régulateur | Responsable Conformité | Nature, impact, mesures, calendrier |
| ANTIC (CIRT national) | Incident de cybersécurité significatif (attaque, intrusion) | Dès qualification | RSSI | Indicateurs techniques |
| Autorité de protection des données / DPO du groupe (exigence RGPD du groupe) | Violation de données personnelles | 72 h maximum après prise de connaissance | DPO | Catégories et volume de données, conséquences, mesures |
| Clients concernés | Atteinte à leurs fonds ou à leurs données avec risque élevé | Sans délai injustifié | Communication, validé DG | Message clair, mesures à prendre |
| Groupe actionnaire (KamaTel) | P1 et P2 | 24 h | RSSI | Fiche de synthèse |
| Assureur | Sinistre couvert | Selon contrat | Direction financière | Déclaration de sinistre |

Le champ `notification` du registre trace les notifications effectuées. Les obligations exactes et leurs délais sont tenus à jour dans le [registre des exigences](../00-contexte/parties-interessees-exigences.md).

## 8. Recueil et conservation des preuves (5.28)

1. **Identifier** les sources : journaux applicatifs JSON, SIEM, EDR, captures réseau, tickets, enregistrements d'appels.
2. **Acquérir** sans altérer : export en lecture seule, calcul d'une empreinte SHA-256 au moment de la collecte, horodatage UTC.
3. **Consigner** chaque manipulation dans une fiche de chaîne de conservation : pièce, empreinte, collecteur, date, lieu de stockage, transferts successifs avec signature.
4. **Stocker** les preuves dans un espace chiffré à accès restreint (RSSI et DPO), conservation au minimum jusqu'à la clôture judiciaire.
5. **Acquisition forensique avancée** (mémoire, disque) : réalisée par le prestataire de réponse à incident sous contrat (écart connu, voir la SoA 5.28).

## 9. Exercices

Un exercice sur table est réalisé au moins par semestre, et un exercice technique par an. Le premier exercice 2026 est documenté dans [EX-2026-01](exercices/EX-2026-01-sim-swap.md).

## 10. Indicateurs

KPI-05 (délai de détection P1/P2) et KPI-06 (délai de confinement P1/P2) sont calculés depuis le registre par `python -m isms kpi`. Voir les [indicateurs du SMSI](../08-pilotage/indicateurs-smsi.md).
