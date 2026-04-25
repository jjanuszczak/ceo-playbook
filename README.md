# CEO Playbook

Personal branding and strategy platform for John Januszczak, focusing on Fintech, Innovation Strategy, and C-Suite leadership.

## Overview

This site is a static website built with **Hugo** and the **Blowfish** theme. It serves as a digital garden and professional portfolio for sharing insights on strategy, technology, and venture building.

## Tech Stack

- **Static Site Generator:** [Hugo](https://gohugo.io/) (Extended version)
- **Theme:** [Blowfish](https://blowfish.page/)
- **Styling:** Tailwind CSS (via Hugo Pipes)
- **Hosting:** GitHub Pages

## Project Structure

- `/articles`: Long-form strategy and technology essays.
- `/videos`: Curated video content and lectures.
- `/lab`: Technical overviews, experiments, and project documentation.
- `/portfolio`: Investment and project showcase.
- `/signals`: Weekly synthesized insights and bookmarks.
- `/.policies`: Governance documentation for categories and tags.
- `/.gemini`: Custom AI coding skills and agent configurations.

## Development

### Prerequisites

- Hugo Extended (latest version recommended)
- Git

### Local Setup

1. Clone the repository:
   ```bash
   git clone --recursive https://github.com/jjanuszczak/ceo-playbook.git
   ```
2. Run the development server:
   ```bash
   hugo server -D
   ```
3. Open `http://localhost:1313` in your browser.

## Content Governance

The site follows strict taxonomy policies to ensure long-term discoverability:

- **Categories:** See `.policies/category_governance_policy.md` (Strategy, Leadership, Fintech, etc.)
- **Tags:** See `.policies/tag_governance_policy.md` (Singular, hyphenated, lowercase).

## License

All rights reserved © 2026 John Januszczak.
