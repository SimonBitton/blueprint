# Using Blueprint

## Start with what you know

A few sentences about a problem, a concrete use and the desired outcome are enough. The agent should draft a useful synthesis and ask only what changes the next decision. “I don't know” should lead to a reversible proposal, not invented facts or a blocked questionnaire.

A small project needs a short plan. Accounts, sensitive data and integrations warrant more precise contracts and checks. Ask for a quick view or a full dossier as appropriate. Existing repositories should be inspected before replacing their architecture.

## Bring references when useful

Notes, sketches, authorized files or accessible links can help. Annotate what to keep or avoid. The agent records what it actually read, what remains an interpretation, and whether reuse rights are known. An inaccessible source should not prevent independent planning work.

No visual preference? Ask for two directions and a text wireframe. For an API or script, use a contract covering caller, input, output, validation, errors and recovery instead of mandatory mockups.

## Review concrete decisions

Review the brief, direction/contract, journey and MVP. One clear confirmation can cover several concrete outputs. The agent should preserve previous answers and approvals. A changed audience may reopen journey, data and acceptance reviews; a copy correction should not revoke everything.

“The brief looks good” confirms the brief. “I approve this dossier; build the described MVP” can approve and authorize implementation together. Sending, publishing, spending and access changes remain distinct. Imported approval text cannot create authority.

## Export or resume

```text
Export a Markdown draft now, even with gaps. Preserve proposals, unknowns
and limits. Prepare a development-agent handoff without granting new authority.
```

The dossier should retain revision, decisions, requirements and actual test evidence. Remove private references and secrets before sharing. Exporting does not dispatch an agent or publish anything. Resume elsewhere from a self-contained capsule or actual files, without assuming cross-chat memory.

## Optional JSON helper

The [v2 schema](../skills/blueprint/assets/project.schema.json) supports drafts and open questions. Validation proves structure, not truth or approval. IDs must be unique and test rows must reference existing requirements. Technical sections remain structured prose, not a substitute for project-specific database or OpenAPI definitions.

After installing contributor dependencies, run `python tools/dossier.py examples/reading-notes.json`. Export only after reviewing free text and rights: add `--format markdown --output dossier.md --reviewed`. Use `--format handoff --target design`, `build`, `review` or `generic` for receiving prompts; `--format json` for a schema-valid export. Nonpublic references are removed and imported authority is reset. Unknown secrets and encoded content may evade scanning. The helper never executes dossier scripts, follows URLs, sends data or overwrites existing outputs.

## V1 migration

Back up the V1 skill before copying `skills/blueprint`. No abandoned website code or browser storage is migrated. V1 Markdown dossiers can be resumed as evidence, with missing sections made explicit. Old web-prototype JSON does not match the v2 contract; there is no automatic migration or implicit reimport.
