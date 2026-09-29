# Editorial Notes

## Brief and intended reader

Issue #165 asked for a long-form leadership essay helping mid-to-senior managers and operators question the five-day / 40-hour default as a design choice, not a law of nature. The article is skeptical of slogans, especially the viral Microsoft Japan 40% productivity framing, and practical about AI surplus allocation.

## Content-type and taxonomy rationale

Content type: Article.

Category: Leadership, because the piece is about management choices, organizational design, and executive allocation of productivity gains.

Tags: `productivity`, `organizational-design`, `artificial-intelligence`, `systems-thinking`, `long-term-thinking`. All are existing canonical tags.

## Research basis and citations

Public sources only. Core research basis:

- Microsoft Japan Work-Life Choice Challenge Summer 2019 official results, including the later caveat that the 39.9% sales-per-employee figure was not caused by the challenge alone.
- 2022 UK four-day week pilot results report.
- 2025 Nature Human Behaviour paper on work time reduction and worker wellbeing.
- U.S. Department of Labor FLSA FAQ and related public labor-history material for the 40-hour/overtime distinction.
- NBER and UC Berkeley material on generative AI time savings and workload intensification.

## Internal linking record

Selected outgoing links:

- `articles/human-pain-as-an-optimizer`: links the AI productivity-surplus section to the existing argument that faster output still needs human judgment and system discipline.
- `articles/values`: links the final leadership-choice section to an existing piece on values as defended operating choices rather than wall text.

Shortlisted but rejected:

- `articles/acqui-hiring-as-a-people-strategy`: shared AI and organizational-design tags, but the reader path was too indirect.
- `articles/responsiveness`: related to productivity and async work, but the article did not need a tactical responsiveness detour.

## Featured image candidates and selected asset

Pixabay attempt: `python3 .agents/skills/editorial-agent/scripts/find_pixabay_candidates.py "1920s factory assembly line workers"` failed with HTTP 403 after network approval, so the image search moved to public-domain Library of Congress/Wikimedia sources.

Candidates:

1. Selected: "Assembly line at the Ford Motor Company's Highland Park plant", 1913. Source: Library of Congress via Wikimedia Commons. URL: `https://commons.wikimedia.org/wiki/File:Assembly_line_at_the_Ford_Motor_Company%27s_Highland_Park_plant_LCCN2011661021.jpg`. Rights basis: public domain / no known restrictions on publication. Stored as `featured.jpg` after a 16:9 crop.
2. "Change of work shift at Ford Motor Company", Detroit, 1910s. Source: Detroit Publishing Company / Library of Congress via Wikimedia Commons. URL: `https://commons.wikimedia.org/wiki/File:Change_of_work_shift_at_Ford_Motor_Company.jpg`. Rights basis: public domain / no known copyright restrictions.
3. "Factory workers on assembly line for bearings", 1924. Source: Library of Congress. URL: `https://www.loc.gov/item/2016817039/`. Rights basis: public domain or no known copyright restrictions according to the Detroit Publishing Company collection notice.

Selection rationale: the Highland Park assembly-line image is directly tied to Ford-era industrial work design, which matches the article argument and avoids modern office stock imagery.

## Social draft archive

Saved under `docs/repurposed/2026-09-29-four-day-workweek.md`.

Validated campaign URL pattern used from the existing repository convention:

- X: `https://januszczak.org/articles/four-day-workweek/?utm_campaign=thought-leadership&utm_medium=social&utm_source=x`
- LinkedIn: `https://januszczak.org/articles/four-day-workweek/?utm_campaign=thought-leadership&utm_medium=social&utm_source=linkedin`

## Validation record

- Featured image dimensions verified at 1536x864.
- Managing Editor eval passed for `content/articles/four-day-workweek/index.md`.
- Editorial Agent package validation passed.
- Hugo build passed via `uv run python .agents/skills/editorial-agent/evals/runner.py content/articles/four-day-workweek --social-draft docs/repurposed/2026-09-29-four-day-workweek.md`.

## Open questions and human decisions

None. The post remains `draft: true`; no publishing, merging, or social posting was performed.
