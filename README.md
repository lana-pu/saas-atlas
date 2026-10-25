# SaaS Atlas — Visual UX Reference Library

Independent, shareable website for SaaS interface research. Each UX pattern is paired with a real screenshot, concise analysis and an original source.

## Website

Expected GitHub Pages address after setup: https://lana-pu.github.io/saas-atlas/
Do not share it as verified until the deployment succeeds.

## Site files

- index.html — responsive site: search, filters, favorites, image viewer, annotation, ?pattern=<id> deep links.
- catalog-source.json — 22 candidate patterns with source URLs and UX explanations.
- scripts/build.py — downloads images, validates dimensions and actual decoding, removes unavailable/duplicate screenshots.
- .github/workflows/pages.yml — automated GitHub Pages build and deployment.
- dist/catalog.json — machine-readable records for *verified* images.
- AGENTS.md — instructions for AI agents using these references.

Unlike earlier versions, the published pages serve image files locally from /assets; they do not hotlink screenshots from third-party sites. The workflow deliberately refuses to publish if fewer than 8 screens or 4 products have verified images.

Some screenshots are from 2021 and are useful as UX-pattern history rather than evidence of current design.

## Enable GitHub Pages

Go to repository Settings → Pages → Build and deployment. Choose **Source: GitHub Actions**. In Actions check the workflow **Publish verified SaaS Atlas**. Only share the site URL once the deployment succeeds and you have seen actual screenshots.

## For agents

Read /AGENTS.md and /catalog.json; for image health read /validation-report.json.

## Local preview

Install Python and Pillow, then run:

\`\`\`bash
python -m pip install Pillow
python scripts/build.py
python -m http.server 8000 --directory dist
\`\`\`

Visit http://localhost:8000.

## Competitive UX scenario matrix

[Interactive scenario benchmark](https://lana-pu.github.io/saas-atlas/ionta-ux-benchmark.html) · [Open JSON rubric](https://lana-pu.github.io/saas-atlas/ionta-ux-benchmark.json)

Fifteen published competitor profiles are compared against one fictional, anonymized freelancer-client journey across nine stages. Evidence cells distinguish described mechanisms, partial analogies, and missing evidence. All hands-on walkthrough result fields remain empty until tested. No private design manuals, personal messages or internal screenshots are published with this research.
