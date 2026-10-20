---
id: POL-02
titre: Politique d'utilisation de la cryptographie
version: "1.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Comité de sécurité
date_approbation: 2026-03-18
prochaine_revue: 2027-03-18
controles_iso: ["5.14", "8.24"]
---

# Politique d'utilisation de la cryptographie

| Version | Date | Auteur | Objet |
|---|---|---|---|
| 1.0 | 2024-03-01 | RSSI | Création |
| 1.1 | 2026-03-18 | RSSI | Abandon de TLS 1.0 / 1.1, durée maximale des certificats, inventaire des clés |

## 1. Objet

Définir quand et comment chiffrer, signer et hacher les informations de KamaPay, et
comment gérer les clés tout au long de leur cycle de vie.

## 2. Quand chiffrer

| Situation | Exigence |
|---|---|
| Flux sur Internet (API partenaires, application mobile) | TLS 1.2 ou 1.3 **uniquement** |
| Flux interbancaires et vers l'opérateur | TLS mutuel (certificats client) ou liaison dédiée chiffrée |
| Flux internes en production | TLS entre zones ; en clair autorisé seulement à l'intérieur d'un même segment cloisonné, après analyse de risque |
| Bases de production (A01, A02) | Chiffrement des volumes (AES-256) |
| Sauvegardes (A08) | Chiffrement AES-256 avant transfert ; clés séparées des sauvegardes |
| PIN clients | Jamais stockés en clair : hachage avec sel par une fonction lente (Argon2id ou bcrypt) ou traitement dans un HSM |
| Supports amovibles et ordinateurs portables | Chiffrement intégral du disque |
| Courriels contenant des données « secret » | Interdits sans chiffrement de bout en bout |

## 3. Algorithmes et paramètres autorisés

| Usage | Autorisé | Interdit |
|---|---|---|
| Transport | TLS 1.3 ; TLS 1.2 avec suites ECDHE et AES-GCM ou ChaCha20-Poly1305 | SSL, TLS 1.0, TLS 1.1, RC4, 3DES, suites sans confidentialité persistante |
| Chiffrement symétrique | AES-256-GCM, ChaCha20-Poly1305 | DES, 3DES, AES-ECB |
| Asymétrique | RSA ≥ 3072 bits, ECDSA P-256 / P-384, Ed25519 | RSA < 2048 bits |
| Hachage | SHA-256, SHA-384, SHA-3 | MD5, SHA-1 (sauf usage non sécuritaire) |
| Mots de passe et PIN | Argon2id, bcrypt (coût ≥ 12), PBKDF2-SHA256 (≥ 600 000 itérations) | Hachage simple, même avec sel |
| Signature de jetons (API) | ES256, EdDSA, RS256 avec clé ≥ 3072 bits | `alg: none`, HS256 avec secret partagé entre partenaires |

## 4. Configuration TLS de référence (exposition Internet)

- Versions : `TLSv1.2 TLSv1.3`.
- En-tête **HSTS** : `Strict-Transport-Security: max-age=31536000; includeSubDomains`.
- Certificats émis par une autorité de confiance publique, durée ≤ 398 jours,
  renouvellement automatisé à J-30, alerte à J-14 (voir INC-2026-008).
- Agrafage OCSP activé quand l'autorité le permet.

La configuration du lab (`lab/proxy/nginx.conf`) applique ce profil. Le contrôle
`CHK-TLS-01` vérifie que TLS 1.0 et 1.1 sont refusés et que TLS 1.2 et 1.3 sont acceptés ;
`CHK-TLS-02` vérifie la présence et la durée de l'en-tête HSTS.

## 5. Gestion des clés

| Étape | Exigence |
|---|---|
| Génération | Dans un HSM ou un coffre de secrets ; jamais sur un poste de travail |
| Stockage | Clés maîtresses en HSM ; clés applicatives dans le coffre ; jamais dans le code ni dans un fichier de configuration versionné |
| Accès | Double contrôle (deux personnes) pour les clés maîtresses |
| Rotation | Clés de chiffrement de données : annuelle ; clés de signature de jetons : 6 mois ; immédiate en cas de suspicion de compromission |
| Destruction | Destruction attestée et inscrite à l'inventaire |
| Inventaire | Le RSSI tient l'inventaire des clés et certificats (propriétaire, usage, expiration) et le revoit chaque trimestre |

## 6. Transfert d'informations (contrôle 5.14)

- Les fichiers échangés avec les banques sont **signés et chiffrés** ; la signature est
  vérifiée avant tout traitement.
- Les OTP envoyés par SMS ne doivent servir qu'en complément du PIN, jamais seuls, pour
  une opération sensible (risque R09).
- Tout transfert de données « secret » vers un tiers exige un accord écrit qui précise le
  chiffrement utilisé ([POL-08](POL-08-classification-information.md)).

## 7. Contrôle

| Vérification | Fréquence | Responsable |
|---|---|---|
| CHK-TLS-01, CHK-TLS-02 | À chaque changement de configuration | Pipeline de conformité |
| Scan TLS des points d'exposition Internet | Mensuel | Ingénieurs sécurité |
| Revue de l'inventaire des clés et certificats | Trimestrielle | RSSI |
