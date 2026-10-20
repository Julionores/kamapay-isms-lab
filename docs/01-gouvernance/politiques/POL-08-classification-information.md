---
id: POL-08
titre: Politique de classification et de manipulation de l'information
version: "1.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-03-05
prochaine_revue: 2027-03-05
controles_iso: ["5.12", "5.13", "5.14", "7.10", "7.14"]
---

# Politique de classification et de manipulation de l'information

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-06-12 | RSSI | Création |
| 1.1 | 2026-03-05 | RSSI | Règles de transfert vers les partenaires et de destruction des supports |

## 1. Objet

Toute information de KamaPay SA doit recevoir un niveau de classification qui détermine les règles de stockage, de transfert et de destruction. La classification de chaque actif figure dans l'[inventaire des actifs](../../../data/actifs.yaml).

## 2. Niveaux de classification (5.12)

| Niveau | Définition | Exemples |
|---|---|---|
| Public | Diffusion sans restriction | Tarifs, conditions générales, communiqués |
| Interne | Usage réservé aux salariés et prestataires sous contrat | Procédures, organigramme, liste des agents |
| Confidentiel | Divulgation pouvant causer un préjudice significatif | Transactions, soldes, configuration des systèmes, rapports d'audit |
| Secret | Divulgation pouvant causer un préjudice grave (financier, réglementaire, image) | Dossiers KYC (A02), sauvegardes (A08), clés cryptographiques, données d'authentification |

Le propriétaire de l'actif attribue la classification ; en cas de doute, le niveau supérieur s'applique. Un regroupement de données peut justifier un niveau plus élevé que chaque donnée isolée (un MSISDN seul est confidentiel, une base de MSISDN avec pièces d'identité est secrète).

## 3. Marquage (5.13)

- Les documents sont marqués en en-tête ou pied de page : `KAMAPAY - INTERNE`, `KAMAPAY - CONFIDENTIEL`, `KAMAPAY - SECRET`.
- Les documents de ce dépôt portent leur classification dans le champ `classification` de leur en-tête.
- Les exports de données confidentielles depuis le back-office portent automatiquement la mention dans le nom de fichier.
- **Écart connu** : le marquage automatique des documents bureautiques n'est pas encore déployé ; le marquage est manuel (statut « partiel » dans la [déclaration d'applicabilité](../../03-soa/declaration-applicabilite.md)).

## 4. Règles de manipulation

| Règle | Interne | Confidentiel | Secret |
|---|---|---|---|
| Stockage | Espaces de l'entreprise | Espaces à accès restreint | Systèmes chiffrés, accès nominatif et journalisé |
| Impression | Libre | Impression avec badge | Interdite sauf accord du propriétaire |
| Courriel interne | Libre | Liste de diffusion restreinte | Interdit ; partage via espace sécurisé |
| Transfert externe | Avec accord du manager | Canal chiffré et accord de confidentialité | Canal chiffré, accord du propriétaire et du RSSI, traçabilité |
| Supports amovibles | Déconseillé | Chiffré uniquement | Interdit |

## 5. Transfert des informations (5.14)

5.1. Les échanges avec les partenaires (banques, marchands, opérateur P03, agrégateurs) se font exclusivement par :

- l'API partenaires (A04) en TLS 1.2 minimum, vérifié par le contrôle **CHK-TLS-01** ;
- SFTP avec authentification par clé pour les fichiers de compensation ;
- un espace d'échange sécurisé pour les documents ponctuels.

5.2. Les codes OTP et les PIN ne sont jamais transmis par un agent ou par le service client. Les opérations sensibles sont validées par le PIN saisi par le client sur le canal USSD (traitement de R09).

5.3. Tout transfert de données personnelles hors du Cameroun doit être validé par le DPO (voir [POL-09](POL-09-protection-donnees-personnelles.md)).

5.4. Les règles de chiffrement sont définies dans la [politique de cryptographie](POL-02-cryptographie.md).

## 6. Supports de stockage (7.10)

- Les supports contenant des données confidentielles ou secrètes sont inventoriés et chiffrés.
- Le transport de supports de sauvegarde vers le site de secours se fait sous scellé, avec registre de remise.

## 7. Destruction et réutilisation (7.14)

| Support | Méthode |
|---|---|
| Papier confidentiel ou secret | Broyeur de niveau P-4 minimum ou prestataire avec certificat de destruction |
| Disques et SSD réutilisés en interne | Effacement cryptographique ou réécriture certifiée |
| Disques et SSD mis au rebut | Destruction physique par prestataire, certificat archivé 5 ans |
| Téléphones et terminaux d'agents | Réinitialisation via l'outil de gestion des mobiles avant restitution |

## 8. Responsabilités

- **Propriétaires d'actifs** : classifier et réviser la classification annuellement.
- **Utilisateurs** : appliquer les règles de manipulation.
- **RSSI** : maintenir la politique et contrôler son application lors des audits internes ([PIL-02](../../08-pilotage/programme-audit-interne.md)).
