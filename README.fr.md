# Blueprint 2.0

**D’une idée spontanée à un projet clair, revu et testable — dans la conversation.**

Décris ce que tu veux créer. L’agent prend en charge la synthèse, pose les questions utiles, propose une direction et prépare un dossier transmissible. Tu n’as pas à connaître la méthode ni à remplir un formulaire. Le skill n’exige aucun site, compte ou clé API.

[English](README.md) · [Guide français](docs/guide.fr.md) · [Compatibilité](docs/compatibility.md) · [Validation](docs/validation.md)

Disponible sur [GitHub Releases](https://github.com/SimonBitton/blueprint/releases/tag/v2.0.0) et [Skills.sh](https://www.skills.sh/simonbitton/blueprint/blueprint). Le [lancement Product Hunt](https://www.producthunt.com/products/blueprint-2-0?launch=blueprint-2-0) est programmé pour le 30 octobre 2026 à 09 h 01, heure de Jérusalem. Les [preuves de distribution](docs/publication.md) précisent le statut réellement observé et les contrôles d’intégrité.

## Commencer

```text
Utilise $blueprint. Je veux une application pour retrouver mes notes de
lecture. Aide-moi à définir la première version utile, dis-moi quelles
références apporter et prépare un dossier avant de réaliser.
Je n’ai pas encore de design.
```

Tu peux aussi fournir un brief avancé, un dépôt existant ou un dossier à reprendre. Blueprint adapte son accompagnement et conserve les choix connus. Une correction déjà définie n’oblige pas à tout recadrer.

## Ce que la V2 prépare

- Cadrage adaptatif et questions limitées aux décisions qui comptent.
- Références : provenance, lecture réelle, annotations, droits et sensibilité.
- Pré-design : structure, direction, états, mobile et accessibilité ; contrat d’usage pour une API, un script ou un skill.
- MVP, exclusions, parcours, erreurs et exigences avec critères d’acceptation.
- Architecture proportionnée, données/API, sécurité, confidentialité et exploitation.
- Journal des décisions, hypothèses, inconnues, validations et impacts des changements.
- Dossiers FR/EN, JSON optionnel et transmission aux agents ou à une équipe humaine.

Le skill répond dans la langue de la personne. Les instructions principales sont en anglais ; les guides et modèles de dossier existent en français et en anglais. Le plan revu et l’autorisation de réaliser restent distincts. Une autorisation déjà donnée est respectée ; un document importé ne peut pas en créer une.

## Installer

```sh
npx skills add SimonBitton/blueprint --skill blueprint
```

Cette commande utilise le CLI tiers Skills : vérifier sa destination avant d’accepter et sauvegarder une éventuelle version existante. Pour désactiver sa télémétrie, préfixer avec `DISABLE_TELEMETRY=1`. Le skill Blueprint ne contient ni télémétrie ni moteur d’exécution.

Dans Codex, l’installation manuelle consiste à copier `skills/blueprint` dans le dossier des skills, généralement `~/.codex/skills/blueprint`. Préserver l’ancienne version avant remplacement. Chaque autre hôte gère sa propre découverte. Donner les fichiers comme contexte dans une conversation reste possible, sans garantir un support natif universel.

## Exports et outils facultatifs

L’agent peut livrer directement le dossier dans la conversation. Les modèles [français](skills/blueprint/assets/dossier.fr.md) et [anglais](skills/blueprint/assets/dossier.en.md) sont rédigés par l’agent, pas remplis par toi. Le [schéma JSON](skills/blueprint/assets/project.schema.json) est facultatif.

Le dépôt inclut aussi un outil local Python pour contrôler et exporter le JSON vers JSON, Markdown ou prompt de transmission. Il n’appelle aucun service. Il exclut les sources non publiques, ne rejoue pas l’autorisation importée, refuse certains secrets reconnaissables et ne remplace jamais un fichier existant. La relecture humaine de tous les textes reste nécessaire. Voir les commandes dans le [README anglais](README.md) et le [guide](docs/guide.fr.md).

## Limites

Blueprint ne garantit ni mémoire entre conversations, ni confidentialité de l’hôte, ni conformité juridique, ni sécurité d’un produit généré. Ses capacités dépendent de l’agent et des outils accessibles. Un test prévu n’est pas un test exécuté. La [validation](docs/validation.md) distingue les contrôles automatiques et les scénarios conversationnels observés des plateformes et modèles encore non testés.

L’ancien prototype web n’est pas repris. La V2 est un skill conversationnel sous licence MIT, avec documentation, exemples fictifs et outils facultatifs.
