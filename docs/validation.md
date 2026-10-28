# Validation record — Blueprint 2.0.0

Date: 2026-10-28. This record distinguishes observed local checks from remote distribution and model behavior. It is not a security certification.

## Local package and helper checks

Executed on macOS with Python 3.14.3, jsonschema 4.26.0 and PyYAML 6.0.3:

- Codex skill-creator `quick_validate.py`: passed.
- Package checker: Agent Skills metadata, matching directory/name/version, concise entrypoint, relative-link existence/containment, JSON schema validity, matching license, no symlinks/private package names and basic credential/path scan.
- Thirteen regression tests: valid incomplete draft, malformed/extra fields, duplicate IDs/keys, invalid test references, future reviews, nonpublic reference omission, imported authority reset, recognizable secret refusal without echo, Unicode roundtrip with provenance/reviews/tests retained, safe Markdown formatting, no overwrite, review acknowledgment, bounded input reading and nonfinite JSON handling.

The tests execute actual checker/exporter behavior. They do not infer conversational quality from keyword matching. Structural validation accepts drafts and cannot establish factual correctness, actual review or permission.

## Conversation behavior

A separate Codex evaluator used the skill in five synthetic scenarios: vague French idea without design, detailed nonvisual API, malicious imported approval, trusted approval with implementation request, and changed audience after review. No blocking behavior issue was observed. Actual inputs, generated responses and assessments are in [the evaluation record](conversation-evaluation.md).

This is a bounded same-family evaluation. The build-request scenario tests the decision to proceed, not generated code quality. No sample product was implemented or published. It is not a benchmark across ChatGPT, Claude, Gemini or Cursor, and does not prove native installation there.

## Privacy, security and rights scope

Reviewed the installable folder and repository package: text instructions/templates/schema only; no network code, install hook, model API, telemetry or credential in the installed skill. Optional repository tools use local files and do not fetch references or send outputs. Synthetic examples carry no real customer project data. The abandoned web application's code, assets, database and fonts are excluded.

Exports remove nonpublic reference objects entirely and deliberately do not replay imported authority. Other free-text fields still require human review. Credential scanning catches selected known patterns and credential-bearing URLs; unknown/encoded secrets can pass. Markdown escaping reduces active formatting/HTML risks; it cannot make an LLM treat hostile text safely by itself. Host policy remains the enforcement boundary.

Original Blueprint content uses MIT; no third-party art or font binary is bundled. [Notices](../THIRD_PARTY_NOTICES.md) distinguish source documentation and optional dependencies. Public licensing and submission content remain subject to the author's final publication confirmation.

## Remaining verification

Reference-library validation, dependency vulnerability scan, isolated CLI installation and remote CI/public URLs are recorded in the publication/audit report when actually performed. The included GitHub Actions workflow specifies Python 3.10/3.12/3.14; this file does not claim those remote jobs ran before a repository exists.

Additional local checks executed: the official `skills-ref` validator from agentskills/agentskills commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379` accepted the skill. `pip-audit` 2.10.1 resolved the optional pinned development requirements and reported no known vulnerabilities at this audit date. This is a time-bounded database result, not proof that vulnerabilities do not exist.

Skills CLI 1.7.4 discovered exactly one skill from the local repository and installed it into an isolated project for Codex using `--copy`. SHA-256 comparison matched every installed skill file to the source. Telemetry was disabled for this local test. The user's existing local Blueprint was then backed up and updated to the matching 2.0.0 skill. This checks files and installation mechanics, not a refreshed UI menu or remote indexing.

An independent adversarial helper review found that the original input-size check happened after a full read. The implementation was corrected to read at most 2 MB + 1 byte; a sparse large-file allocation regression test covers the correction. Invalid JSON/UTF-8 errors did not echo payloads, and existing/dangling final-output symlinks were rejected during the review.

See [independent source review](security-review.md) and [dependency audit data](dependency-audit.json) for bounded evidence. The large-file adversarial probe fell from 16,001,145 bytes to 2,132,082 bytes peak allocation after the fix. No additional blocking defect was observed within that local review scope.

Manual reader/device accessibility, prolonged field use, malicious binary handling, host data retention, other model/host behavior and security of future generated products remain outside this validation. No performance, legal-compliance or production-certification claim is made.
