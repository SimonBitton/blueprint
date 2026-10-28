# Compatibility and evidence

The package follows the [Agent Skills specification](https://agentskills.io/specification): a named directory with YAML-frontmatter `SKILL.md`, relative references, optional assets and product-specific UI metadata. Frontmatter uses standard `name`, `description`, `license` and string-valued `metadata`; it grants no tools. Main instructions stay below the recommended 500-line limit. References are directly discoverable from the entrypoint and read on demand.

| Surface | Supported approach | Evidence / boundary |
| --- | --- | --- |
| Codex | Native skill folder; optional `agents/openai.yaml` | Local format validation and installation can be checked; UI activation is separate |
| Skills CLI | Repository `skills/blueprint` discovery/install | Verify against the actual published revision before claiming remote installation |
| Other Agent Skills hosts | Use host's documented discovery mechanism | Format compatibility; no claim that every host/version was executed |
| ChatGPT, Claude, Gemini chat | Supply instructions and relevant references as context | Manual textual use; no native installer or memory guarantee |
| Cursor / repository agents | Skill or context according to host support; inspect repository rules | No model-specific tools or native installation assumed |
| Optional tools | Python 3.10+, jsonschema and PyYAML for contributor checks | Separate from the installed conversational skill; CI matrix is 3.10/3.12/3.14 |

The skill is multilingual by instruction; docs/templates are FR/EN. The optional CLI uses English labels and preserves Unicode. The main schema permits unknown dates as text and explicit unknown/proposed states; it is not a complete product domain model. Schema-valid imported reviews are not trusted approvals.

Compatibility is not certification. The [validation report](validation.md) records actual local and remote observations. No cross-model parity, provider privacy settings, tool availability or production security is implied.
