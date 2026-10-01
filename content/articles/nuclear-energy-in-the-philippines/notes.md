# Editorial Notes

## Brief and intended reader

Issue #169 asked for a research-led executive explainer for Philippine executives, investors, and energy-sector decision-makers. The core brief was to explain why RA 12305 matters while making clear that regulatory readiness is not the same as project readiness or commercial viability.

## Content-type and taxonomy rationale

Content type: Article.

Category: Energy Transition, because the piece evaluates nuclear as part of the Philippine power-system transition, including cost, reliability, grid readiness, decarbonization, and capital structure.

Tags: `energy-markets`, `project-finance`, `capital-allocation`, `systems-thinking`, `long-term-thinking`. All are existing canonical tags.

## Research basis and citations

Public research basis plus the supplied general counsel notes in issue #169:

- RA 12305 from the Supreme Court E-Library and Lawphil PDF for the legal framework and PhilATOM authority.
- DOE milestone update for IAEA Milestones Approach status, PhilATOM implementation priorities, INIR follow-up progress, public acceptance trend, grid readiness, workforce, waste, and Phase 3 roadmap.
- DOE proposed nuclear-capacity tender rules for the 1,200 MW by 2032 planning assumption and the distinction between winning a tender and receiving PhilATOM authorization.
- IAEA December 2024 Phase 1 Follow-Up INIR Mission report for infrastructure-readiness framing.
- DOE/ERC-linked public reporting and IMF Philippines 2025 selected-issues report for electricity-cost context.
- PIA/DOE reporting on the SWS public-perception survey for public acceptance.
- Lazard 2025 LCOE+ for independent power-economics comparison context.

## Internal linking record

Internal linker helper was run with `--allow-draft-target`; its automated shortlist was weak because the scaffold had empty tags when it ran.

Selected outgoing links after reading local candidates:

- `articles/atoms-are-investable-again`: extends the demand-and-capital-allocation argument around energy hardware becoming strategically investable again.
- `articles/ev-mobility-sea`: reinforces the shared operating reality that energy transitions succeed or fail in financing, infrastructure, permitting, and grid execution, not in technology slogans.

Rejected:

- `articles/tokenization-is-the-capital-markets-upgrade`: strong infrastructure-governance theme, but too far from Philippine power-system economics for this reader path.
- `articles/strategy-prework`: useful executive-decision framing, but less directly relevant than the energy-market pieces.

## Featured image candidates and selected asset

Pixabay attempt: `uv run python .agents/skills/editorial-agent/scripts/find_pixabay_candidates.py "nuclear power plant philippines grid" --limit 3` failed with HTTP 403 even though `PIXABAY_API_KEY` exists in `.env`, so the search moved to licensed real photography.

Candidates:

1. Selected: "Bataan Nuclear Powerplant.jpg" by Jiru27. Source: Wikimedia Commons. URL: `https://commons.wikimedia.org/wiki/File:Bataan_Nuclear_Powerplant.jpg`. Rights basis: photographer offers CC BY-SA 3.0 / GFDL; depicted Philippine infrastructure also tagged PD-structure on Commons. Stored as `featured.jpg` after 16:9 crop.
2. "Kernkraftwerk Gundremmingen Kuehlturm.jpg" by Thilo Parg. Source: Wikimedia Commons. URL: `https://commons.wikimedia.org/wiki/File:Kernkraftwerk_Gundremmingen_Kuehlturm.jpg`. Rights basis: CC BY-SA 4.0.
3. "Doel Nuclear power plant and cooling tower.jpg" by Sally V. Source: Wikimedia Commons. URL: `https://commons.wikimedia.org/wiki/File:Doel_Nuclear_power_plant_and_cooling_tower.jpg`. Rights basis: CC BY-SA 4.0.

Selection rationale: BNPP is directly relevant to the Philippine executive question, sober in tone, and does not imply the plant is operating or ready to restart.

## Social draft archive

Saved under `docs/repurposed/2026-10-01-nuclear-energy-in-the-philippines.md`.

Validated campaign links generated with `.agents/skills/repurpose-social/scripts/generate_campaign_links.py`:

- X: `https://januszczak.org/articles/nuclear-energy-in-the-philippines/?utm_campaign=thought-leadership&utm_medium=social&utm_source=x`
- LinkedIn: `https://januszczak.org/articles/nuclear-energy-in-the-philippines/?utm_campaign=thought-leadership&utm_medium=social&utm_source=linkedin`

## Validation record

- Featured image downloaded from Wikimedia Commons and cropped to 960x540 with `sips`.
- Campaign URLs generated and validated through the repo campaign-link helper.
- Internal-linker helper rerun after real frontmatter existed; it ranked `articles/atoms-are-investable-again`, `articles/vc-atoms`, `articles/ev-mobility-sea`, and `articles/flatpeak`, confirming the selected outgoing links were relevant.
- Managing Editor eval passed for `content/articles/nuclear-energy-in-the-philippines/index.md`.
- Repurpose Social eval passed.
- Editorial Agent package validation passed.
- Hugo build passed via `uv run python .agents/skills/editorial-agent/evals/runner.py content/articles/nuclear-energy-in-the-philippines --social-draft docs/repurposed/2026-10-01-nuclear-energy-in-the-philippines.md`.
- Content Creator eval was run and failed only because its generic branch check expects `feature/article-nuclear-energy-in-the-philippines`; this issue-linked workflow correctly uses `feature/169-article-nuclear-energy-in-the-philippines`.

## Open questions and human decisions

None. The post remains `draft: true`; no publishing, merging, or social posting was performed.
