# Project Context: ceo-playbook

## Overview
This is a static website built with Hugo, using the Blowfish theme, and deployed to Github Pages. It is the personal branding site for John Januszczak, a C-Suite executive specializing in Fintech & Innovation Strategy.

## Tech Stack
- **Engine:** Hugo Extended
- **Theme:** Blowfish
- **Scripting:** Vanilla JS

## Directory Structure
- `/archetypes`: Contains templates for new content files created with `hugo new`.
- `/assets`: Stores files that will be processed by Hugo Pipes, like CSS or JS.
  - `/images`: Contains site-level images (e.g., backgrounds, logos).
- `/config/_default`: Main configuration files for the Hugo site.
  - `hugo.toml`: The main configuration file for the site.
  - `languages.en.toml`: Language-specific settings.
  - `markup.toml`: Markdown rendering settings.
  - `menus.en.toml`: Defines the site's menus.
  - `module.toml`: Hugo modules configuration.
  - `params.toml`: Theme-specific and custom site parameters.
- `/content`: Contains the markdown content for the site.
  - `/articles`: Blog posts and articles.
  - `/lab`: Technical overviews and projects.
  - `/portfolio`: Showcase of projects and investments.
  - `/videos`: Content that includes embedded videos.
  - `_index.md`: The home page content.
  - `about.md`: The about page.
  - `contact.md`: The contact page.
- `/layouts`: Holds templates that override the theme's default layouts.
  - `/shortcodes`: Custom Hugo shortcodes.
- `/public`: The output directory where the generated static site is placed. This directory is usually not tracked in git.
- `/resources`: Caches for processed assets. This directory is usually not tracked in git.
- `/static`: Contains static assets that are copied directly to the `public` directory without processing.
- `/themes/blowfish`: The Blowfish theme used for the site, included as a git submodule.

## Coding Standards
1. **Frontmatter:** Use YML format. Always include `title`, `date`, `summary`, `description`, `draft`, and `tags`.
2. **Images:** Place images in content bundles or `/static/images` if used outside of content. Reference them as `/images/filename.jpg`.
3. **Shortcodes:** Prefer built-in Hugo shortcodes over raw HTML where possible.
4. **Categories:** Articles and Videos in `/content/articles` and `/content/videos` always include `categories` in the frontmatter. Each post will set `categories` to one of the following values:
* Strategy
* Leadership
* Fintech
* Energy Transition
* Technology
* Venture Building
* Essays

## Common Commands
- **Dev Server:** `hugo server -D` (renders drafts)
- **Build:** `hugo --minify`
- **New Post:** `hugo new articles/my-new-post.md`