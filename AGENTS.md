# SaaS Atlas — Instructions for AI agents

SaaS Atlas is an independent, curated UX reference site for SaaS product screens and design patterns. Product screenshots remain copyrighted by their owners. It is not an official website of the products.

## Machine-readable access

- Live dataset: /catalog.json (only successfully downloaded and validated screenshots).
- Validation summary: /validation-report.json.
- Deep link: /?pattern=attio-saved-views (or any published ID).
- Screenshot path: patterns[].image_local, relative to the website root. All listed images are served from the website itself.
- Original provenance: patterns[].source_url and patterns[].image_url.
- Core fields: id, product, title, tag, year, what, why, apply, focus, note, origin.

## How to analyze

1. Read /catalog.json.
2. Select a relevant real screen/pattern. Compare what, why, and apply notes to your user's goals.
3. View the locally hosted screenshot. Ground visual claims in the actual image.
4. Cite original URLs and year. Archived screens, particularly 2019–2022, are NOT representative of current versions.
5. Do not invent screenshots. If an image failed to validate, the publishing pipeline excludes its pattern.

## Updating

Edit catalog-source.json and commit. GitHub Actions downloads screenshots, verifies image decoding/dimensions, removes unavailable patterns and deploys dist/ to Pages. Never ship remote-URL placeholders.


## UX scenario benchmark (Ionta competitors)

- /ionta-ux-benchmark.html — interactive evidence matrix for 15 SaaS competitors across nine standardized user tasks.
- /ionta-ux-benchmark.json — machine-readable tasks, source-linked preliminary assessments, and hands-on research protocol.
- Evidence levels are **documented / partial / unknown**. A documented mechanism means the feature was described in a source, NOT verified by an account-based usability test.
- `hands_on_tests_completed: 0` is deliberate. Do not invent timing, task-success results, competitor absences or UX ranking.
- An **unknown** cell is missing evidence, not a negative finding.
- Distinguish an email reply status from the state of a user commitment, a task or an approval.
- For visual reference, follow the external `ionta-competitive-deep-dive.json` evidence and locally verified `catalog.json` screenshots.
- No internal product files, private source materials or user screenshots are included in this public benchmark.
