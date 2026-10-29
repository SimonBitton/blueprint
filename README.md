# Blueprint 2.0

**From a rough idea to a reviewed, testable project plan — in the conversation.**

Blueprint helps an AI agent ask useful questions, gather references, propose a direction, define a realistic MVP and prepare an implementation handoff. You explain what you want; the agent does the structuring. No website, account or API key is required by the skill.

[Français](README.fr.md) · [English guide](docs/guide.en.md) · [Guide français](docs/guide.fr.md) · [Security](SECURITY.md) · [Validation](docs/validation.md)

Available on [GitHub Releases](https://github.com/SimonBitton/blueprint/releases/tag/v2.0.0) and [Skills.sh](https://www.skills.sh/simonbitton/blueprint/blueprint). The [Product Hunt launch](https://www.producthunt.com/products/blueprint-2-0?launch=blueprint-2-0) is scheduled for October 30, 2026 at 00:01 PDT. See the [distribution verification](docs/publication.md) for the observed status and integrity checks.

## Try it

```text
Use $blueprint. I want an app for my reading notes. Help me clarify the
first useful version, tell me what references would help, and prepare
a plan before implementation. I don't have a design yet.
```

Or bring a detailed brief, an existing repository or a dossier to resume. Blueprint should use what is already settled instead of repeating a questionnaire. A specified bug fix does not need a new discovery workshop.

## What you get

- Adaptive discovery with a few consequential questions at a time.
- Reference provenance, observed versus unread material, rights and sensitivity.
- Pre-design with text wireframes and alternatives, or an input/output contract for nonvisual products.
- MVP boundaries, journeys, failure states and testable acceptance criteria.
- Proportionate architecture, data/API, security, privacy and operational decisions.
- Decisions, assumptions, open questions, scoped reviews and change impact.
- FR/EN dossier templates, optional JSON interchange and design/build/review handoff.

The agent responds in your language. The skill instructions are in English for portability; French and English usage documentation and dossier templates are included. Readiness and authority stay separate: a reviewed brief does not automatically authorize coding or publication. Existing user authorization is respected without repeated permission requests.

## Install

The repository uses the standard `skills/blueprint/SKILL.md` layout.

```sh
npx skills add SimonBitton/blueprint --skill blueprint
```

This uses the third-party Skills CLI. Inspect its proposed destination before accepting installation; an existing local skill may need a backup. To opt out of its telemetry, prefix the command with `DISABLE_TELEMETRY=1`. Blueprint itself includes no telemetry or runtime.

Manual Codex installation: copy `skills/blueprint` to your Codex skills directory, normally `~/.codex/skills/blueprint`, preserving an existing version first. Other Agent Skills hosts use their own discovery/installation conventions. Plain chat tools can use the instructions and relevant reference files manually; this is not a claim of native installation support everywhere. See [compatibility and limits](docs/compatibility.md).

## Repository contents

| Path | Purpose |
| --- | --- |
| [skills/blueprint](skills/blueprint/SKILL.md) | Installable text skill, guides, templates, schema, license |
| [docs](docs/guide.en.md) | Usage, migration, security/rights and validation evidence |
| [examples](examples/reading-notes.json) | Synthetic draft, not an approved customer project |
| [tools/dossier.py](tools/dossier.py) | Optional offline JSON validation and export helper |
| [tests](tests/test_dossier.py) | Regression tests for export and validation boundaries |
| [launch](launch/product-hunt.md) | Reviewable launch copy and release materials |

The abandoned web prototype is not included. No account system, server, model API, project database or autonomous multi-agent runtime is installed.

## Optional contributor tools

The conversational skill needs no Python or package installation. To work on the optional checker/exporter:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/check_package.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/dossier.py examples/reading-notes.json
```

After reviewing every free-text field for privacy and rights, an example export is:

```sh
.venv/bin/python tools/dossier.py examples/reading-notes.json \
  --format handoff --target build --output reading-handoff.md --reviewed
```

Outputs are local; existing files are never overwritten. Only references marked public are included. The exporter resets imported authorization, escapes Markdown content, and refuses some recognizable credential patterns. Human review remains essential: arbitrary sensitive text cannot be reliably identified by a pattern scanner. `--reviewed` records your local review, not a security guarantee or approval to send anything.

## Honest limits

Results depend on the agent, its context and its available tools. Blueprint does not provide persistent memory, encryption, legal compliance or a sandbox. A plan and a planned test are not tested software. Format checks and a bounded same-family agent evaluation do not prove behavior on all models or in all products. The validation report states what was actually run and what remains unverified.

MIT licensed. See [LICENSE](LICENSE), [third-party notices](THIRD_PARTY_NOTICES.md) and [contributing](CONTRIBUTING.md).
