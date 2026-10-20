---
id: SEN-01
titre: Programme de sensibilisation et de formation à la sécurité
version: "2026.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-01-15
prochaine_revue: 2027-01-15
controles_iso: ["6.3"]
---

# Programme de sensibilisation et de formation à la sécurité

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 2025.1 | 2025-01-20 | RSSI | Programme 2025 |
| 2026.1 | 2026-01-15 | RSSI | Programme 2026 : ajout du réseau d'agents et des campagnes clients |

## 1. Objectifs

1. Chaque salarié suit au moins un module par trimestre ; taux de formation ≥ 90 % (KPI-07).
2. Le taux de clic aux campagnes d'hameçonnage simulé passe sous 10 % (KPI-08).
3. Le taux de signalement de ces campagnes dépasse 30 % (KPI-09).
4. Les 4 200 agents distributeurs reçoivent chaque année la formation anti-fraude.
5. Les clients sont informés en continu des escroqueries courantes (risque R13).

## 2. Publics et contenus

| Public | Effectif | Contenu | Format | Fréquence |
|---|---|---|---|---|
| Tous les salariés | 180 | Charte, hameçonnage, mots de passe et MFA, signalement, données clients | E-learning de 20 min + quiz | Trimestrielle |
| Nouveaux arrivants | ~25 / an | Charte, règles d'accès, classification, signalement | Présentiel de 1 h, avant ouverture des accès | À l'arrivée |
| Administrateurs et développeurs | 22 | Gestion des privilèges, développement sécurisé (OWASP API Top 10), secrets | Atelier de 3 h | Semestrielle |
| Service client et back-office | 45 | Ingénierie sociale, vérification d'identité, SIM swap, exports | Atelier de 2 h avec jeux de rôle | Semestrielle |
| Direction | 9 | Responsabilités, gestion de crise, exercice sur table | Exercice | Annuelle |
| Agents distributeurs | 4 200 | [Kit agents](kit-agents-distributeurs.md) : fraude, PIN, signalement | Session de 30 min par les superviseurs, fiche papier, SMS de rappel | Annuelle + rappels |
| Clients | ~1,9 M | « KamaPay ne vous demandera jamais votre PIN » | SMS, radio, réseaux sociaux (PA-07) | Continue |

## 3. Calendrier 2026

| Trimestre | Thème principal salariés | Hameçonnage simulé | Autres actions |
|---|---|---|---|
| T1 | Hameçonnage et MFA (SEN-2026-T1) | PHISH-2026-01 (février) | Module dédié après INC-2026-002 |
| T2 | Protection des données clients (SEN-2026-T2) | PHISH-2026-02 (mai) | Suite à INC-2026-003 |
| T3 | Fraude et ingénierie sociale (SEN-2026-T3, agents) | PHISH-2026-03 (août) | Kit agents diffusé |
| T4 | Bilan, quiz annuel ([quiz hameçonnage](quiz-phishing.md)) | PHISH-2026-04 (novembre) | Campagne radio clients |

## 4. Résultats 2026 à date

Les résultats sont tenus dans [`data/sensibilisation.yaml`](../../data/sensibilisation.yaml) et calculés par `python -m isms kpi`.

| Campagne | Public | Formés / cible | Taux |
|---|---|---|---|
| SEN-2026-T1 | Salariés | 171 / 180 | 95,0 % |
| SEN-2026-T2 | Salariés | 168 / 182 | 92,3 % |
| SEN-2026-T3 | Agents | 3 150 / 4 200 | 75,0 % |

| Hameçonnage simulé | Envoyés | Clics | Taux de clic | Signalements | Taux de signalement |
|---|---|---|---|---|---|
| PHISH-2026-01 | 180 | 31 | 17,2 % | 22 | 12,2 % |
| PHISH-2026-02 | 182 | 19 | 10,4 % | 47 | 25,8 % |
| PHISH-2026-03 | 181 | 11 | 6,1 % | 69 | 38,1 % |

Lecture : la progression est nette sur l'hameçonnage. La couverture du réseau d'agents (75 %) reste sous la cible : les superviseurs régionaux de l'Est et du Nord n'ont pas terminé les sessions ; rattrapage prévu au T4.

## 5. Règles

- Un salarié qui clique lors d'une campagne simulée reçoit un module court de 5 minutes ; il n'est pas sanctionné.
- Un salarié qui n'a pas suivi le module trimestriel après deux relances est signalé à son manager.
- Les accès aux applications sensibles (A01, A02, A06) ne sont ouverts qu'après la formation d'arrivée.

## 6. Mesure de l'efficacité

Au-delà de la participation, l'efficacité est mesurée par : l'évolution des taux de clic et de signalement, le nombre d'incidents d'origine humaine (catégories `compromission_compte` et `fuite_donnees`), le délai de signalement des incidents par les salariés, et le score moyen au quiz annuel (cible ≥ 80 %).
