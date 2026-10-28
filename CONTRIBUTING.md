# Contributing

Keep the skill conversational, tool-agnostic and proportionate. Do not turn a single incident into a global approval ceremony, add provider capabilities without evidence, or impose a website/runtime. Put conditional detail in directly linked references.

Include a synthetic request that demonstrates a behavior change and the actual outcome. Preserve user intent, existing authorization, provenance and the distinction between plan readiness and permission. Never include private dossiers or credentials in issues, tests or examples.

Before proposing a change, run `python tools/check_package.py` and `python -m unittest discover -s tests -v` in an environment with `requirements-dev.txt`. Exercise the affected conversation scenario; distinguish model evaluation from deterministic unit tests. Update both FR/EN docs if behavior changes. For schema changes, explain migration and update fixtures/tests.

Bug reports should include the skill version, host/version if known, minimal synthetic input, expected outcome and observed outcome. A host limitation is useful evidence; don't claim universal compatibility from one successful run.
