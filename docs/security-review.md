# Independent package security/rights/compatibility review

Date: 2026-10-28. Scope: files in outputs/blueprint-v2 as inspected before publication. No product file or external service was changed by this evaluator. Local probes and reports were confined to work/forward-test; a temporary sparse file used for the resource test was removed after the probe.

## Confirmed finding

**P2 — Input size check occurs after unbounded read.** `tools/dossier.py`, `read_project`, initially used `Path(path).read_bytes()` before `len(raw) > MAX_BYTES`. The CLI rejects oversize data but allocates the whole file first. An untrusted oversized dossier can therefore exhaust process memory despite the advertised 2 MB input limit.

Reproduction: create a 16,000,000-byte sparse file under the evaluation directory, run `read_project` under tracemalloc, catch the expected ValueError. The actual peak allocation was 16,001,145 bytes; the configured cap was 2,000,000 bytes. This is a real resource-boundary issue, independent of scanner completeness or semantic model behavior.

Recommended fix: open the input in binary mode and read at most `MAX_BYTES + 1`; reject when the returned data exceeds MAX_BYTES, before JSON parsing. Add a regression that observes the requested read bound or peak memory; the existing oversize test only checks final rejection and does not detect unbounded allocation.

The probe is in adversarial_review.py; captured results are in adversarial-results.json. Parent notified immediately. This finding records the initially inspected implementation; parent may subsequently fix it and must record the rerun separately.

## Checks with no defect observed

- Ran all 12 current regression tests successfully.
- Additional malformed JSON, invalid UTF-8 and wrong-schema CLI probes returned code 2 without echoing payloads, private object keys, input names or source snippets.
- Added unique private reference content and false imported authorization; JSON, Markdown and handoff exports omitted both, and build handoff instructions retain trusted-context authority boundaries.
- Existing-file and dangling final-component symlink outputs were rejected. The dangling target was not created. No overwrite switch exists; exclusive create prevents replacing existing final files.
- JSON schema includes `decisions.source`, `decisions.reason`, `decisions.affects` and added `decisions.evidence`. Roundtrip tests preserve decision/review/test arrays. The main schema is intentionally an interchange envelope with technical prose, not OpenAPI or a complete domain schema; the docs say so.
- Markdown rendering escapes active HTML and special formatting; the docs correctly state that this is not an LLM sandbox or prompt-injection guarantee.
- Package format checker passed. Entry metadata, names, versions, relative references, bundled MIT license and UI metadata are consistent. No symlink, credential, private local absolute path, abandoned web source, font binary or third-party art observed in package.
- MIT licensing of installed jsonschema 4.26.0 and PyYAML 6.0.3 agrees with local installed package metadata. Dependencies are only for optional contributor tools; the installed conversational skill has no required runtime or executable install hook.
- CI permissions are read-only; the workflow uses pinned action commits and an explicit Python matrix. Docs distinguish specified remote jobs from actual remote execution and do not claim universal model/host testing.
- FR/EN docs agree on planning versus implementation authority, optional exports, migration limits and host-level privacy limitations. Product Hunt copy is labeled prepared and unsubmitted, and does not assert a live publication or certification.

## Bounded conclusions

The review is a local source inspection and small adversarial CLI probe, not penetration testing, dependency vulnerability scanning, legal advice, cryptographic verification of remote actions or a cross-model evaluation. Pattern scanner blind spots and arbitrary sensitive free text are documented limits rather than new findings. Other-host native installation and remote publication remain unverified by this evaluator.

## Fix verification

The parent changed read_project to `with Path(path).open('rb') as source: raw = source.read(MAX_BYTES + 1)`. I reran the same 16 MB sparse-file probe after observing that change. Peak allocation fell to approximately 2 MB (see current adversarial-results.json), while the oversized input was still rejected. The initial evidence is preserved in adversarial-results-before-fix.json. This resolves the confirmed resource-limit finding for this inspected revision. All current regression tests were rerun after the change and passed.
