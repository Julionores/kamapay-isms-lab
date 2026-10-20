<!-- Document généré par `python -m isms render` à partir de reports/restauration.json (lab/scripts/test-restauration.sh). Ne pas modifier. -->


# Rapport de test de restauration

Preuve des mesures 8.13 (sauvegarde) et 5.30 (préparation des TIC pour la continuité) ; traitement du risque R14. Test exécuté sur le lab, pas sur la production.

| Élément | Résultat |
|---|---|
| Date d'exécution (UTC) | 2026-10-20T21:04:38+00:00 |
| Résultat | Test réussi |
| Méthode | pg_dump -Fc, chiffrement AES-256-CBC/PBKDF2, pg_restore sur instance isolée (--network none) |
| Durée de la sauvegarde | 0.66 s |
| Durée de la restauration (déchiffrement, instance vierge, pg_restore) | 5.6 s |
| Durée totale | 6.56 s |
| Empreinte d'intégrité de la source | `3:3:237000:2000:5a62056b12d5b2463352776157a741fc` |
| Empreinte d'intégrité de la copie restaurée | `3:3:237000:2000:5a62056b12d5b2463352776157a741fc` |
| SHA-256 de la sauvegarde chiffrée | `f8b2fbb2d392253ea2d436a777ababa16114265c74c07c0fcf3de84a620878f2` |

L'empreinte combine le nombre de clients et de portefeuilles, la somme des soldes, le nombre de transactions et un condensat MD5 de l'ensemble des transactions triées. Deux empreintes identiques prouvent que la copie restaurée est complète et intègre.

Le RTO de production (4 h pour A01, voir le [PCA/PRA](pca-pra.md)) inclut aussi la bascule réseau et la validation métier ; ce test mesure uniquement la partie technique de restauration des données.
