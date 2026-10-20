---
id: SEN-02
titre: Quiz annuel hameçonnage et ingénierie sociale
version: "2026.1"
statut: approuve
classification: interne
proprietaire: RSSI
approbateur: Directeur des Ressources Humaines
date_approbation: 2026-09-20
prochaine_revue: 2027-09-20
controles_iso: ["6.3"]
---

# Quiz annuel hameçonnage et ingénierie sociale

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 2026.1 | 2026-09-20 | RSSI | Édition 2026 |

12 questions, une seule bonne réponse par question. Score attendu : 10 / 12 au minimum (≥ 80 %). Durée : 10 minutes. Ce quiz est utilisé au T4 du [programme de sensibilisation](programme-sensibilisation.md).

## Questions

**1.** Vous recevez un courriel « Votre boîte de messagerie est pleine, cliquez ici pour conserver vos messages ». L'adresse de l'expéditeur est `support@kamapay-mail.com`. Que faites-vous ?
- A. Je clique, c'est le support informatique.
- B. Je transfère à mes collègues pour vérifier s'ils l'ont reçu.
- C. J'utilise le bouton « Signaler » de la messagerie sans cliquer.
- D. Je réponds pour demander si c'est sérieux.

**2.** Quel indice est le plus fiable pour reconnaître un lien piégé ?
- A. Le logo de l'entreprise dans le message.
- B. Le domaine réel affiché au survol du lien.
- C. La présence de fautes d'orthographe.
- D. L'heure d'envoi.

**3.** Un appelant se présente comme technicien de l'éditeur de la plateforme et vous demande votre code MFA « pour une maintenance urgente ». Que faites-vous ?
- A. Je le donne, c'est un prestataire connu.
- B. Je refuse, je raccroche et je signale l'appel au RSSI.
- C. Je le donne seulement s'il connaît mon nom.
- D. Je lui demande de rappeler plus tard.

**4.** Vous avez cliqué sur un lien suspect et saisi votre mot de passe. Quelle est la première chose à faire ?
- A. Attendre de voir s'il se passe quelque chose.
- B. Supprimer le courriel.
- C. Signaler immédiatement l'incident (poste 4444 ou securite@) et changer le mot de passe.
- D. Éteindre l'ordinateur et rentrer chez soi.

**5.** Un client appelle le service client : « J'ai perdu ma SIM hier, je veux réinitialiser mon PIN par téléphone. » Quelle est la bonne réponse ?
- A. Réinitialiser après avoir vérifié la date de naissance.
- B. Réinitialiser si le client est poli et pressé.
- C. Bloquer les opérations sortantes et orienter le client vers une agence avec sa pièce d'identité.
- D. Lui envoyer le nouveau PIN par SMS.

**6.** Pourquoi la MFA a-t-elle empêché la compromission lors de l'incident d'hameçonnage de mars 2026 ?
- A. Parce que le mot de passe était trop long.
- B. Parce que le second facteur n'était pas en possession de l'attaquant.
- C. Parce que le courriel avait été bloqué.
- D. Parce que le compte était désactivé.

**7.** Un collègue vous demande de lui exporter une liste de clients sur une clé USB pour « travailler chez lui ce week-end ». Que faites-vous ?
- A. J'accepte, c'est un collègue.
- B. J'exporte sur ma messagerie personnelle à la place.
- C. Je refuse : l'export de données clients est soumis à habilitation et la clé USB est interdite.
- D. J'accepte si la clé est neuve.

**8.** Quel mot de passe respecte le mieux la politique de KamaPay ?
- A. `KamaPay2026!`
- B. Une phrase de passe de plus de 14 caractères, unique, stockée dans le gestionnaire de mots de passe.
- C. Le même mot de passe que la messagerie personnelle, avec un chiffre ajouté.
- D. La date de naissance de son enfant.

**9.** Un SMS indique : « KamaPay : votre compte sera suspendu, confirmez votre PIN au 6xx xx xx xx ». Que doit-on dire aux clients ?
- A. De confirmer leur PIN pour éviter la suspension.
- B. Que KamaPay ne demande jamais le PIN, et de signaler ce SMS au service client.
- C. De rappeler le numéro pour vérifier.
- D. D'ignorer tous les SMS de KamaPay.

**10.** Vous trouvez une clé USB marquée « Salaires 2026 » sur le parking. Que faites-vous ?
- A. Je la branche pour trouver son propriétaire.
- B. Je la remets au service informatique sans la brancher.
- C. Je la jette.
- D. Je la garde.

**11.** Un fournisseur habituel écrit : « Nos coordonnées bancaires changent, merci de payer la prochaine facture sur ce nouveau compte. » Que faites-vous ?
- A. Je mets à jour les coordonnées.
- B. Je réponds au courriel pour confirmer.
- C. Je vérifie par un appel au contact connu du fournisseur (numéro du contrat) avant tout changement.
- D. Je paie sur les deux comptes.

**12.** Lequel de ces comportements augmente le taux de signalement (KPI-09) et protège le plus l'entreprise ?
- A. Supprimer discrètement les courriels suspects.
- B. Signaler chaque courriel suspect, même en cas de doute.
- C. Signaler uniquement les courriels qui contiennent une pièce jointe.
- D. Attendre qu'un collègue signale le premier.

## Corrigé

| Question | Réponse | Explication |
|---|---|---|
| 1 | C | Domaine imitant KamaPay ; signaler sans cliquer permet au SOC de bloquer le message pour tous. |
| 2 | B | Le domaine réel du lien est l'indice décisif ; logos et orthographe s'imitent facilement. |
| 3 | B | Aucun prestataire ne demande un code MFA. C'est le scénario type de contournement de la MFA. |
| 4 | C | La rapidité du signalement réduit le délai de confinement (KPI-06). |
| 5 | C | La réinitialisation de PIN après perte de SIM se fait en agence uniquement (mesure du risque R01). |
| 6 | B | Le mot de passe seul ne suffisait pas sans le second facteur. |
| 7 | C | Contrôles 5.14 et 7.10 : transfert et supports amovibles encadrés ; voir l'incident INC-2026-003. |
| 8 | B | Longueur, unicité et gestionnaire de mots de passe (POL-01). |
| 9 | B | Message central de la campagne clients (risque R13). |
| 10 | B | Une clé inconnue peut contenir un logiciel malveillant (incident INC-2026-006). |
| 11 | C | Fraude au changement de coordonnées bancaires : toujours vérifier par un canal connu. |
| 12 | B | Un signalement, même erroné, ne coûte rien ; un message non signalé peut toucher toute l'entreprise. |
