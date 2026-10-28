# From decisions to an implementable specification

Scale the dossier to the product. These are decision prompts for the agent, not mandatory questions for the person. “Not applicable, because …” is better than invented infrastructure. Inspect an existing implementation before choosing a stack.

## MVP and acceptance

State the smallest complete user outcome, included capabilities, explicit exclusions and next-version candidates. Rank by necessity for that outcome, not by how easy code generation looks. Estimates are proposals with assumptions; do not invent commitments.

Give requirements stable IDs. For each critical R-ID include behavior, actor, preconditions, observable success/failure, priority and a verification method. Example: “R-03: Given an expired import session, submitting a file shows a recoverable session error, stores no new file and allows sign-in then retry.” Link relevant decisions, data boundaries and tests. Avoid acceptance criteria such as “secure”, “modern” or “fast” without measurable meaning.

## Architecture

Describe a small system boundary and the flow from caller/UI through application logic to storage/providers. Compare at most a few realistic options where the choice matters. Explain fit with current code, deployment, offline needs, team capability, cost and reversibility. Identify dependency ownership and failure modes. Don't introduce microservices, authentication or AI unless the need requires it.

For an AI feature specify the human goal, allowed tools, data sent, provider/configuration unknowns, fallbacks, evaluation cases, time/cost caps and behavior on unsupported output. Do not claim deterministic answers or universal model compatibility.

## Data and API

For important entities specify identifiers, fields/types/constraints, ownership, relationships, source of truth, lifecycle, retention/deletion, backups and migration. Distinguish application data from secrets and audit logs. Describe offline/concurrent editing and conflict resolution only if relevant.

For each critical API/action specify method or trigger, path/name, authentication, object-level authorization, request and response examples with synthetic values, validation, error contract, idempotency/retries/timeouts, pagination/rate limits if relevant and side effects. Mark provider contracts as unverified until actual documentation/connection was inspected. A planned connector is not a working integration.

Example contract:

```text
POST /imports (proposed)
Actor: signed-in owner; server checks workspace membership.
Input: source_id, client_request_id; source must belong to actor's workspace.
202: job_id, status=pending; repeating same request ID returns same job.
400: malformed input; 401: no session; 403/404: unavailable resource;
409: incompatible source state; 429: retry after backoff.
No document text or access token in logs. Upload size and parser limits
are proposed values to settle from real usage, not assumed requirements.
```

## Quality and operations

Define relevant latency/size/concurrency targets with their source; leave unknown targets explicit. Include keyboard/screen reader paths, contrast, reduced motion and responsive states for interfaces. Distinguish local capability from external connectivity. Plan configuration, environment separation, dependency/license checks, logging without sensitive payloads, backup/restore exercise, rollout/rollback and support ownership proportionate to impact.

Make a test matrix connecting critical R-IDs and risks to:

- Unit or domain tests for rules and edge cases.
- Integration tests for real contracts, permission boundaries and failure behavior.
- End-to-end tests for primary outcome and recovery.
- Accessibility/manual/device tests where automation is insufficient.
- Security/privacy cases such as cross-owner access, deletion across backups and injected source instructions.

Record **planned / executed / passed / failed / blocked**, environment, version and evidence. Don't generate trivial tests for prose or make claims about execution from a test plan alone.

## Review and implementation sequence

Summarize settled scope, proposals, blockers and deferred risks. Mark each blocker as resolved, isolated from the first increment, or explicitly deferred by the user with its consequence. Then propose small verifiable increments with prerequisites, acceptance and rollback. Start implementation when actual authorization and a sufficient reviewed plan are present; don't keep extending the dossier indefinitely.
