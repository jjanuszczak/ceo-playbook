# CEO Playbook

My profesisonal branding and strategy platform, focusing on Fintech, Innovation Strategy, and C-Suite leadership. Includes a lot of what I have been up to, including and stuff I am interested in. I made this repo public so that people can suggest edits to articles using github.

## Overview

This site is a static website built with **Hugo** and the **Blowfish** theme. It serves as a digital garden and professional portfolio for sharing insights on strategy, technology, and venture building.

## Tech Stack

- **Static Site Generator:** [Hugo](https://gohugo.io/) (Extended version)
- **Theme:** [Blowfish](https://blowfish.page/)
- **Styling:** Tailwind CSS (via Hugo Pipes)
- **Hosting:** GitHub Pages
- **Python Tooling:** [uv](https://docs.astral.sh/uv/) managed project environment for repo automation

## Local Setup

This repository is primarily a Hugo site, but it also includes Python-based automation under `.agents/skills/`.

### Prerequisites

- Install `uv`
- Install Hugo Extended

### Python Tooling Setup

From the repository root:

```bash
uv sync
```

This creates or updates the local `.venv` from the committed `pyproject.toml` and `uv.lock`.

Run repository Python tooling through `uv` so commands use the managed environment:

```bash
uv run python .agents/skills/github-issue-manager/scripts/manage_issue.py "Title" "Description" --type enhancement
```

### Internal Linking Skill

Use the internal-linker helper to rank local cross-link candidates for an article:

```bash
uv run python .agents/skills/internal-linker/scripts/find_link_candidates.py \
  content/articles/the-next-compiler/index.md --limit 4
```

Run its deterministic eval after changing the skill or applying its suggestions:

```bash
uv run python .agents/skills/internal-linker/evals/runner.py \
  content/articles/the-next-compiler/index.md
```

Eval fixtures are version-controlled test data. Generated evaluation reports are ignored by Git.

## Project Structure

- `/content/articles`: Long-form strategy and technology essays.
- `/content/videos`: Curated video content and lectures.
- `/content/lab`: Technical overviews, experiments, and project documentation.
- `/content/portfolio`: Investment and project showcase.
- `/content/signals`: Weekly synthesized insights and bookmarks.
- `/.policies`: Governance documentation for categories and tags.
- `/.agents`: Custom AI skills, agent guidance, and deterministic skill evals.

## Content Governance

The site follows strict taxonomy policies to ensure long-term discoverability:

- **Categories:** See `.policies/category_governance_policy.md` (Strategy, Leadership, Fintech, etc.)
- **Tags:** See `.policies/tag_governance_policy.md` (Singular, hyphenated, lowercase).

## License

All rights reserved © 2026 John Januszczak.
