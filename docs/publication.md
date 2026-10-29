# Distribution verification — 2026-10-29

Release skill version: **2.0.0**. Release source commit: `8c69cc8d645a8e397b5d38e385d33efda4c6d2f5`. The author explicitly approved public distribution under MIT before publication.

| Destination | Verified state | Link |
| --- | --- | --- |
| GitHub | Public repository, MIT license recognized; release published, not draft or prerelease | [Repository](https://github.com/SimonBitton/blueprint), [v2.0.0 release](https://github.com/SimonBitton/blueprint/releases/tag/v2.0.0) |
| Skills.sh | Public skill detail page displays the installed skill text and installation command | [Blueprint listing](https://www.skills.sh/simonbitton/blueprint/blueprint) |
| Product Hunt | Launch submission completed; success confirmation and dashboard show **Scheduled** | [Launch destination](https://www.producthunt.com/products/blueprint-2-0?launch=blueprint-2-0) |

Product Hunt's first offered date was **2026-10-30 at 00:01 PDT**, equivalent to **09:01 Asia/Jerusalem (UTC+2)**. This was selected for the requested publication. At verification time the creator's page shows the scheduled date and disables upvoting until the launch is live. The launch is scheduled, not yet observed live. Anonymous access to the prelaunch page was not established by the web reader.

The existing Product Hunt draft was completed rather than duplicated: original logo and three gallery cards, approved description and maker comment, Free pricing, Open Source / Developer Tools / Artificial Intelligence launch tags, Prompt Engineering Tools category, GitHub primary URL and Skills.sh additional URL. No paid promotion or outreach was performed.

## Installation and integrity

Skills CLI 1.7.4 successfully installed `SimonBitton/blueprint` into an isolated Codex project. SHA-256 comparison matched every installed skill file to the validated source. One telemetry-enabled remote installation was used as the requested distribution check; local authoring tests had telemetry disabled. No repeated installation was used to inflate counts.

The three attached GitHub release files are uploaded. Downloaded archives matched their published sums:

```text
a7c4aac8847caf7688954471311e98d2975239fac8910a4975747cdd4cff5ab4  Blueprint-2.0.0-skill.zip
5f56a534558e892f753d9c4ab8dd7ec0f77fb0fe397fb6b5e48aadeb1d1581a2  Blueprint-2.0.0-source.zip
```

The [release-commit CI run](https://github.com/SimonBitton/blueprint/actions/runs/40765004255) passed package checks and the thirteen regression tests on Python 3.10, 3.12 and 3.14. The tag-triggered run also passed. See [local validation](validation.md) and [independent review](security-review.md) for scope and limitations.

On 2026-10-29 the Skills.sh listing displayed one installation and PASS indicators for Gen Agent Trust Hub, Socket and Snyk. These are observed platform indicators at that time, not a universal security certification or a guarantee of future status.

The release archives remain frozen to the validated release commit; later distribution documentation on `main` does not change the skill's 2.0.0 payload.
