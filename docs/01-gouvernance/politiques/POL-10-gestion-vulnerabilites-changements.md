---
id: POL-10
titre: Politique de gestion des vulnérabilités et de la configuration
version: "1.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur Général
date_approbation: 2026-06-02
prochaine_revue: 2027-06-02
controles_iso: ["8.8", "8.9", "8.19", "8.32"]
---

# Politique de gestion des vulnérabilités et de la configuration

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 2025-10-01 | RSSI | Création |
| 1.1 | 2026-06-02 | RSSI | Intégration des contrôles automatisés en CI (CHK-VULN-01, CHK-CTR-01, CHK-HTTP-01) |

## 1. Objet

Réduire la fenêtre d'exposition aux vulnérabilités connues et garantir que les systèmes restent dans une configuration de sécurité maîtrisée. La politique traite principalement les risques R06 (rançongiciel), R07 (vulnérabilité de l'API) et R10 (changement non maîtrisé).

## 2. Identification des vulnérabilités (8.8)

| Source | Fréquence | Responsable |
|---|---|---|
| Scan des images de conteneurs (Trivy) | À chaque construction en CI | DSI |
| Scan d'infrastructure authentifié | Mensuel | RSSI |
| Bulletins éditeurs et alertes (voir [PROC-03](../procedures/PROC-03-veille-securite.md)) | Continue | RSSI |
| Test d'intrusion externe de l'API partenaires et des applications | Annuel et avant toute mise en service majeure | RSSI |
| Programme de signalement responsable (adresse dédiée) | Continue | RSSI |

## 3. Délais de correction

Les délais courent à partir de la publication du correctif ou, à défaut, de la détection.

| Sévérité (CVSS 3.1) | Exposé Internet ou A01/A02 | Interne |
|---|---|---|
| Critique (9,0 - 10) | 72 heures | 7 jours |
| Haute (7,0 - 8,9) | 7 jours | 30 jours |
| Moyenne (4,0 - 6,9) | 30 jours | 90 jours |
| Faible (< 4,0) | Prochain cycle de maintenance | Prochain cycle de maintenance |

Une vulnérabilité activement exploitée (catalogue d'exploitation connue ou alerte d'un CERT) est traitée comme critique quel que soit son score.

**Blocage en CI** : une image comportant une vulnérabilité **CRITICAL** corrigeable ne peut pas être livrée (contrôle **CHK-VULN-01**, workflow `.github/workflows/conformite.yml`). Le code applicatif ne doit présenter aucun constat **HIGH** de l'analyse statique (contrôle **CHK-SAST-01**).

## 4. Dérogations

Lorsqu'un correctif ne peut pas être appliqué dans les délais :

- le propriétaire de l'actif formule une demande de dérogation motivée ;
- des mesures compensatoires sont définies (filtrage, désactivation de la fonction, surveillance renforcée) ;
- la dérogation est validée par le RSSI pour 90 jours maximum, renouvelable une fois ; au-delà, par le Directeur Général ;
- les dérogations en cours sont présentées en revue de direction ([PIL-03](../../08-pilotage/revue-de-direction.md)).

## 5. Gestion de la configuration (8.9)

5.1. Chaque type de composant dispose d'une configuration de référence (« durcissement ») documentée et versionnée, dérivée des guides CIS et des recommandations des éditeurs.

5.2. Les configurations sont décrites sous forme de code (fichiers de déploiement, modèles) et stockées dans des dépôts à accès restreint. Exemple : [lab/docker-compose.yml](../../../lab/docker-compose.yml).

5.3. Exigences minimales vérifiées automatiquement dans le lab :

| Exigence | Contrôle |
|---|---|
| Conteneurs exécutés sans privilège, avec un utilisateur non root et un système de fichiers en lecture seule | CHK-CTR-01 |
| En-têtes de sécurité HTTP présents, version du serveur masquée | CHK-HTTP-01 |
| Base de données non exposée hors du réseau interne | CHK-NET-01 |

5.4. Toute dérive détectée par rapport à la référence est traitée comme un changement non autorisé et analysée selon la [procédure de gestion des incidents](../../05-incidents/procedure-gestion-incidents.md).

## 6. Installation de logiciels sur les systèmes en production (8.19)

- Seuls les composants issus du pipeline de déploiement peuvent être installés en production ; aucune installation manuelle n'est autorisée.
- Les images de conteneurs proviennent de registres approuvés et sont référencées par version précise.
- Les outils de diagnostic temporaires sont retirés à la fin de l'intervention et tracés dans le ticket.

## 7. Lien avec la gestion des changements (8.32)

Toute correction ou modification de configuration en production suit la [procédure de gestion des changements](../procedures/PROC-02-gestion-des-changements.md). Les correctifs critiques peuvent emprunter le circuit « changement urgent ».

## 8. Indicateurs

- Vulnérabilités critiques ouvertes au-delà du délai : cible 0.
- Contrôles automatisés au vert (KPI-02) : cible 100 %, voir le [tableau de bord](../../08-pilotage/tableau-de-bord.md).
