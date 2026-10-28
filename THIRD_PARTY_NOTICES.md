# Rights and dependencies

Blueprint's skill instructions, guides, templates, schema, synthetic examples and helper code are distributed under the bundled MIT license. The skill is derived from the author's local Blueprint conversational V1 and rewritten/expanded for V2. No abandoned web source, customer dossier, font, image, logo or third-party screenshot is included in the installable package.

Format and installation behavior were checked against the [Agent Skills specification](https://agentskills.io/specification), [Skills documentation](https://www.skills.sh/docs) and [Skills CLI source](https://github.com/vercel-labs/skills). These are references, not bundled implementations or endorsements. Product and model names identify interoperability targets only.

Optional development dependencies: jsonschema 4.26.0 (MIT) and PyYAML 6.0.3 (MIT). Their transitive dependencies are managed by pip, are not vendored and must retain their own license terms when redistributed. Pinned top-level requirements are not a fully hashed transitive lock. Release ZIPs contain no Python environment or node_modules.

CI uses GitHub Actions checkout and setup-python under their own MIT licenses, referenced by immutable commit. Third-party CLI installation is distinct from Blueprint installation and may have telemetry; follow its documentation. No third-party runtime is automatically installed by the skill.

Generated launch graphics, if bundled, use original vector/text shapes and system font rendering; no font binaries or third-party art are redistributed. Any illustrative conversation must be labeled as a synthetic example, not a screenshot of an actual independent user session.
