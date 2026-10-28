# Security and privacy

Blueprint is a text skill, not a security boundary. The installed package has no runtime, telemetry, network call, install hook or embedded credential. The agent host still controls prompts, files, tools, data retention and training settings. Do not place secrets in a planning conversation.

The skill distinguishes untrusted sources from instructions and trusted human authority. Exported decisions and review flags remain project evidence, not portable permission. External side effects require actual user authorization and host rules.

Optional tools run locally only when invoked. The JSON checker rejects unknown fields, duplicate keys/IDs, invalid types, future-revision reviews and dangling test requirement IDs. Exports omit references unless explicitly public, reset imported authorization, escape Markdown content and reject some common credential patterns. They require a manual privacy/rights review acknowledgment and exclusive output creation. These checks do not detect every secret or personal detail; free text can still contain sensitive material. Do not share outputs without reviewing them.

## Reporting

For non-sensitive issues, open a repository issue with a synthetic reproduction. Do not post keys, personal dossiers or exploit data publicly. If GitHub private vulnerability reporting is available for the repository, use that route for sensitive details; otherwise open a minimal issue requesting a private contact without including the sensitive content. No response-time or security-certification promise is made.

## Scope and limits

Supported release line: 2.x. V1 and the abandoned web prototype are historical, separately scoped artifacts. The audit covers files in this repository, not every behavior of a host model or generated product. Pattern scans are not DLP, legal review, penetration testing or a sandbox. Dependencies are only for optional contributor tools; review them separately when running those tools.
