# Editorial Notes

## Brief and intended reader

Issue #119 asked for an executive article on why capital-intensive businesses are investable again, using Base Power and Valar Atomics as the core examples while preserving the counterpoint that enterprise SaaS is not dead.

## Content-type and taxonomy rationale

Content type: Article.

Category: Energy Transition, because the draft centers on power demand, distributed storage, nuclear, and the investability of energy infrastructure.

Tags: capital-allocation, energy-markets, project-finance, artificial-intelligence, saas, venture-capital, systems-thinking.

## Research basis and citations

Research used public web sources only. The supplied X post was not retrievable as a reliable source during drafting, so the SaaS rebound point was supported with Meritech, Gartner, Deloitte, and S&P Global instead.

Primary or high-authority sources used:

- Base Power, Business Wire release on the $1B Series C and distributed storage model.
- U.S. Department of Energy, Valar Ward 250 criticality announcement.
- U.S. Department of Energy, Reactor Pilot Program overview.
- International Energy Agency, Energy and AI data center electricity demand forecast.
- U.S. Energy Information Administration, data center load growth analysis.
- Gartner, 2026 IT spending forecast.
- Meritech, 2026 SaaS rebound analysis.
- Deloitte, 2026 Global Software Industry Outlook.
- S&P Global Market Intelligence, software sell-off analysis.

## Internal linking record

Ran `uv run python .agents/skills/internal-linker/scripts/find_link_candidates.py content/articles/atoms-are-investable-again/index.md --limit 4 --allow-draft-target`.

Selected contextual links:

- `articles/vc-atoms`: direct precursor on AI forcing venture capital back toward physical infrastructure.
- `articles/flatpeak`: useful adjacent energy-transition link on the digital coordination layer for distributed assets.
- `articles/moats-vibe-coding`: supports the enterprise software survival argument with a moat framework.
- `articles/cvc-vs-cvb`: supports the executive capital-allocation section on whether to invest, buy, or build.

Rejected shortlist items:

- `articles/bdc`: relevant to patient capital, but less directly useful to the article's energy and software argument.
- `articles/ev-mobility-sea`: relevant to energy transition and infrastructure density, but less precise than Flatpeak for this draft.

Incoming links were not edited because the Editorial Agent authority is scoped to the owned draft.

## Featured image candidates and selected asset

Pixabay searches were run with the project key from `.env`.

Candidates:

1. `https://pixabay.com/photos/solar-panels-energy-green-power-2836846/`, creator `bertbraet`, 5616x3744, real-photo solar/storage proxy. Rights basis: Pixabay Content License, source recorded at selection time.
2. `https://pixabay.com/photos/solar-battery-clean-energy-pillar-2602980/`, creator `Aleksandr1984`, 4608x3456, solar battery installation. Rights basis: Pixabay Content License, source recorded at selection time.
3. `https://pixabay.com/photos/photovoltaic-photovoltaic-system-2138992/`, creator `andreas160578`, 4288x2820, photovoltaic field. Rights basis: Pixabay Content License, source recorded at selection time.

Selected: Candidate 1. It is a clean real-photo landscape proxy for distributed energy storage and avoids text, logos, and watermarks. Downloaded, center-cropped, and resized to `featured.jpg` at 1600x900.

## Social draft archive

Saved draft-only X and LinkedIn candidates to `docs/repurposed/2026-08-05-atoms-are-investable-again.md`.

## Validation record

Provisioning eval ran and returned a known branch-name false failure because the content-creator issue-reuse path creates `feature/119-article-atoms-are-investable-again`, while the eval expects `feature/article-atoms-are-investable-again`.

Managing Editor eval passed:

- `uv run python .agents/skills/managing-editor/evals/runner.py content/articles/atoms-are-investable-again/index.md`

Editorial Agent package and Hugo validation passed:

- `uv run python .agents/skills/editorial-agent/evals/runner.py content/articles/atoms-are-investable-again --social-draft docs/repurposed/2026-08-05-atoms-are-investable-again.md`

## Open questions and human decisions

None. Draft remains `draft: true`.
