# Utiliser Blueprint

## Partir d’une idée

Quelques phrases suffisent : le problème rencontré, un usage concret et le résultat souhaité si tu les connais. L’agent doit reformuler ce qui est compris, préparer une première synthèse et demander seulement ce qui change la prochaine décision. « Je ne sais pas » est une réponse utile : il propose alors un choix réversible, clairement identifié comme proposition.

Un projet simple reçoit un dossier court. Un projet avec comptes, données sensibles ou intégrations mérite des contrats et vérifications plus précis. Tu peux demander une vue rapide ou un dossier complet sans changer de méthode.

## Fournir des références

Apporte une note, un croquis ou un lien accessible si cela aide. Une capture avec « j’aime la hiérarchie, pas les couleurs » est plus utile qu’une collection non commentée. L’agent précise ce qu’il a réellement lu, sépare observation et interprétation, et garde les droits d’utilisation visibles. Un lien inaccessible ne bloque pas tout le projet.

Sans préférence visuelle, demande deux directions et une structure textuelle. Pour une API ou un script, le pré-design devient un contrat : appelant, entrée, sortie, validation et erreurs. Il n’y a pas de maquette obligatoire.

## Valider sans bureaucratie

Relis les résultats concrets : brief, direction ou contrat, parcours et périmètre. Une confirmation globale peut couvrir plusieurs éléments présentés ensemble. L’agent conserve les validations existantes et ne redemande pas les mêmes informations.

« Le brief me va » valide le brief. « Je valide ce dossier, réalise le MVP décrit » peut valider le dossier et autoriser la réalisation. Publier, envoyer des données ou modifier les accès reste une action distincte. Un changement de public peut rouvrir parcours, données et tests ; un ajustement de texte ne doit pas invalider tout le projet.

## Obtenir un dossier ou transmettre

```text
Exporte maintenant le dossier en Markdown, même incomplet. Garde les
propositions, questions et limites visibles. Prépare un prompt pour un
agent de développement ; ne lui attribue aucune autorisation nouvelle.
```

Le dossier garde sa révision, les décisions, les exigences et preuves de test. Les références privées et secrets sont exclus du partage. Un export ne publie rien et ne déclenche pas un autre agent. La reprise dans une autre conversation utilise un résumé ou les fichiers réellement fournis, sans mémoire automatique promise.

## Outil JSON facultatif

Le [contrat v2](../skills/blueprint/assets/project.schema.json) accepte aussi les dossiers brouillons. Les champs vides et questions ouvertes restent visibles ; la validation prouve une structure, pas une approbation. Les identifiants sont uniques et les tests référencent des exigences existantes.

Après installation des dépendances de contribution, `python tools/dossier.py examples/reading-notes.json` contrôle la structure. Pour exporter, ajouter `--format markdown --output dossier.md --reviewed` après relecture locale. `--format handoff --target design`, `build`, `review` ou `generic` adapte le prompt. `--format json` produit un JSON conforme en supprimant les sources non publiques et l’autorisation importée.

Les sections techniques acceptent du texte structuré libre ; elles ne remplacent pas un schéma de base de données ou OpenAPI propre au projet. Aucun chemin, URL ou script du dossier n’est exécuté. Le contrôle de secrets reste partiel, notamment pour les secrets en langue naturelle ou encodés.

## Passer de V1 à V2

Sauvegarder le dossier du skill V1 avant remplacement. Copier uniquement `skills/blueprint`. L’ancien site et son stockage ne sont ni lus ni migrés. Les dossiers Markdown V1 restent utilisables : l’agent les reprend, ajoute les rubriques utiles et signale les informations absentes. Les anciens JSON du prototype web ne correspondent pas au contrat v2 ; il n’existe pas de migration automatique ni de réimport implicite.
