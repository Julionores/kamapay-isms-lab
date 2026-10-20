---
id: POL-07
titre: Politique d'usage acceptable des ressources informatiques
version: "1.2"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-02-10
prochaine_revue: 2027-02-10
controles_iso: ["5.10", "5.32", "6.7", "7.7", "7.9", "8.1", "8.7", "8.23"]
---

# Politique d'usage acceptable des ressources informatiques

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-03-01 | RSSI | Création (ancienne charte informatique) |
| 1.1 | 2025-09-15 | RSSI | Ajout du travail à distance |
| 1.2 | 2026-02-10 | RSSI | Supports amovibles, filtrage web des postes nomades |

## 1. Objet et portée

Cette politique, annexée au règlement intérieur, définit ce que les salariés, stagiaires et prestataires de KamaPay SA peuvent et ne peuvent pas faire avec les ressources informatiques (postes, téléphones, messagerie, accès Internet, applications). Chaque utilisateur la signe à son arrivée et reconfirme chaque année lors de la campagne de sensibilisation.

## 2. Principes généraux (5.10)

2.1. Les ressources sont fournies pour un usage professionnel. Un usage personnel limité est toléré s'il ne nuit ni à la sécurité ni à l'activité.

2.2. Chaque utilisateur est responsable des actions réalisées avec ses identifiants. Il est interdit de prêter son compte, son badge ou son jeton MFA.

2.3. Sont notamment interdits :

- la consultation de données clients sans besoin lié à une tâche (consultation « par curiosité ») ;
- l'envoi de données clients ou de pièces d'identité vers une messagerie personnelle ou une application de messagerie instantanée ;
- le contournement des dispositifs de sécurité (EDR, proxy, filtrage, verrouillage) ;
- l'installation de logiciels non autorisés.

## 3. Postes de travail et terminaux (8.1, 8.7)

| Exigence | Règle |
|---|---|
| Gestion | Postes masterisés et gérés par la DSI ; utilisateurs sans droits d'administration |
| Protection | EDR obligatoire, mises à jour automatiques, chiffrement intégral du disque |
| Verrouillage | Automatique après 5 minutes d'inactivité |
| Supports amovibles | Bloqués par défaut ; exception accordée par le RSSI pour une durée limitée (suite à INC-2026-006) |
| Téléphones professionnels | Enrôlés dans l'outil de gestion des mobiles, code de 6 chiffres minimum, effacement à distance |
| Terminaux personnels | Accès à la messagerie seulement via l'application gérée ; aucun accès au back-office |

## 4. Messagerie et Internet (8.23)

4.1. Le filtrage web bloque les catégories à risque (logiciels malveillants, hameçonnage, partage de fichiers non approuvé). Au siège, le filtrage DNS est actif ; l'extension aux postes nomades est en cours (écart suivi dans la [déclaration d'applicabilité](../../03-soa/declaration-applicabilite.md)).

4.2. Tout courriel suspect doit être signalé avec le bouton « Signaler » de la messagerie, sans cliquer sur les liens.

4.3. Les transferts automatiques de courriels vers l'extérieur sont désactivés.

## 5. Bureau propre et écran vide (7.7)

- Aucun document classé confidentiel ou secret ne reste sur un bureau en l'absence de son utilisateur.
- Les documents imprimés sont récupérés immédiatement (impression avec badge).
- L'écran est verrouillé à chaque départ du poste (Windows + L).
- Contrôle inopiné trimestriel par l'équipe sécurité, avec retour individuel.

## 6. Travail à distance et actifs hors des locaux (6.7, 7.9)

6.1. Le travail à distance est autorisé pour les fonctions validées par le manager et la DSI. L'accès au SI se fait exclusivement via le VPN de l'entreprise avec MFA.

6.2. L'accès au back-office (A06) et aux outils d'administration est **interdit** hors des locaux, sauf astreinte via le bastion.

6.3. Le matériel emporté ne doit jamais être laissé sans surveillance dans un véhicule ou un lieu public. La perte ou le vol doit être déclaré à la DSI dans l'heure (procédure [INC-01](../../05-incidents/procedure-gestion-incidents.md)).

6.4. Les réseaux Wi-Fi publics ne sont utilisables qu'avec le VPN actif.

## 7. Propriété intellectuelle (5.32)

- Seuls des logiciels sous licence valide ou des logiciels libres approuvés par la DSI peuvent être utilisés.
- Le code source et la documentation de la plateforme fournis par l'éditeur P04 sont soumis au contrat de licence : interdiction de les copier hors des dépôts autorisés.
- L'inventaire des licences est rapproché annuellement de l'inventaire des actifs.

## 8. Contrôle et sanctions

KamaPay SA peut contrôler l'usage des ressources dans le respect de la législation, de manière proportionnée et après information des représentants du personnel. Tout manquement peut entraîner les sanctions prévues par le règlement intérieur (contrôle 6.4).

## 9. Engagement de l'utilisateur

> Je reconnais avoir lu la politique d'usage acceptable des ressources informatiques de KamaPay SA et m'engage à la respecter.
>
> Nom, fonction, date, signature : ____________________
