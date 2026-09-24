# Editorial Notes

## Brief and intended reader

Issue #160 asked for a long-form analysis for founders, operators, angels, and seed investors asking whether startup success is inversely proportional to funds raised. The draft keeps the answer qualified: more funding is not automatically bad, but large early checks can damage experimentation and capital efficiency before product-market fit is clear.

## Content-type and taxonomy rationale

Content type: Article. The brief is strategic analysis rather than technical lab, video, or research note.

Category: Venture Building. The piece is about venture funding, startup operating discipline, capital allocation, and founder decision-making.

Tags: `venture-building`, `venture-capital`, `capital-allocation`, `go-to-market`, `saas`, `systems-thinking`. All are existing approved tags.

## Research basis and citations

Primary and supporting sources used in frontmatter and body:

- Founder Collective, "Don't Overdose on VC: Lessons from 166 startup IPOs."
- TechCrunch, "Do more startups die of indigestion or starvation?"
- Crunchbase News, "What Are The Odds Of Success For A US Seed Funded Startup?"
- Ketkar and Roche, "Too Soon? Early Funding, Technological Unconventionality, and Innovation Capabilities."
- Los Angeles Times, "Quibi is shutting down after subscriber struggles."
- TechCrunch source articles on Atlassian, Veeva, WhatsApp/Sequoia, and Color were used for case-study cross-checks.

## Internal linking record

Ran:

```bash
uv run python .agents/skills/internal-linker/scripts/find_link_candidates.py content/articles/does-more-venture-funding-make-startups-worse/index.md --limit 4 --allow-draft-target
```

Selected contextual outgoing links:

- `articles/cvc-vs-cvb`: Used in the founder guidance section because the post explains matching capital structure to the operating job.
- `articles/atoms-are-investable-again`: Used in the sector caveat because some categories genuinely require large capital when physical deployment, regulation, or infrastructure are the constraint.

Shortlisted but not used:

- `articles/building-an-audience`: Relevant to manual learning loops, but the draft already had stronger capital-structure links.
- `articles/vc-atoms`: Relevant, but `Atoms Are Investable Again` covered the more current capital-intensity point.

## Featured image candidates and selected asset

Pixabay API path:

- `python3 .agents/skills/editorial-agent/scripts/find_pixabay_candidates.py "startup founder funding venture capital boardroom"` failed with sandbox DNS, then returned HTTP 403 with the project `.env` key. Fallback used public Pixabay search/source pages.

Candidates:

1. Selected: StartupStockPhotos, "Startup, Start-up, People", https://pixabay.com/photos/startup-start-up-people-593341/. Real photo, Pixabay Content License visible on source page, relevant to early-stage planning and experimentation. Downloaded from Pixabay CDN and cropped to `featured.jpg` at 1280x720.
2. TheDigitalArtist, "Handshake, Business, Deal", https://pixabay.com/photos/handshake-business-deal-agreement-3198019/. Real photo, Pixabay Content License visible on source page, relevant to financing and agreements but less specific to startup learning.
3. Search candidate: business meeting category result featuring mwitt1337 on Pixabay business meeting search pages. Relevant to boardroom/investor discussion, but no stable source page was needed after selecting #593341.

## Social draft archive

Saved draft-only X and LinkedIn candidates at:

`docs/repurposed/2026-09-24-does-more-venture-funding-make-startups-worse.md`

Validated campaign URLs:

- X: `https://januszczak.org/articles/does-more-venture-funding-make-startups-worse/?utm_campaign=thought-leadership&utm_medium=social&utm_source=x`
- LinkedIn: `https://januszczak.org/articles/does-more-venture-funding-make-startups-worse/?utm_campaign=thought-leadership&utm_medium=social&utm_source=linkedin`

## Validation record

- Managing Editor eval: PASS.
- Repurpose Social eval: PASS.
- Editorial Agent package validation: PASS.
- Hugo build through Editorial Agent runner: PASS.

Known provisioning eval exception: `content-creator` expected `feature/article-does-more-venture-funding-make-startups-worse`, while this workflow correctly reused issue #160 and created `feature/160-article-does-more-venture-funding-make-startups-worse`.

## Open questions and human decisions

None. The article remains `draft: true` and is ready for editorial review after validation and PR handoff.
