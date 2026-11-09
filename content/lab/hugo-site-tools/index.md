---
title: "Hugo Sites Move Fast. Their Release Checks Should Too."
date: 2026-11-09
summary: "Hugo Site Tools gives teams and agents one dependable workflow for content operations, release checks, and distribution."
description: "A practical look at Hugo Site Tools, a Go toolkit for inspecting content, validating builds, comparing URLs, checking published sites, generating governed campaign links, and exporting EPUBs."
categories:
  - Technology
tags:
  - hugo
  - software-engineering
  - dev-ops
  - artificial-intelligence
  - open-source
showReadingTime: true
showTableOfContents: true
featuredImage: "featured-hugo-site-tools.jpg"
draft: false
status: agent-pending
about:
  - name: "Hugo"
    url: "https://gohugo.io/"
mentions:
  - name: "Pandoc"
    url: "https://pandoc.org/"
citations:
  - title: "Hugo Site Tools"
    url: "https://github.com/jjanuszczak/hugo-site-tools"
  - title: "Hugo Documentation"
    url: "https://gohugo.io/documentation/"
---

[Hugo](https://gohugo.io/) turns a content tree into a fast website. The release work around that build is less tidy: finding the right source, checking what will ship, catching broken links, comparing generated URLs with production, and preparing each post for distribution. Those jobs often end up split across shell commands, scripts, and manual checks.

[Hugo Site Tools](https://github.com/jjanuszczak/hugo-site-tools), or `hs`, gives those recurring jobs (and ideally your agent who is managing these jobs!) one interface. It works with the Hugo project already in place. Hugo still generates the site; `hs` helps people and agents inspect, validate, and operate it.

{{< quick-answer >}}
Hugo Site Tools is a Go toolkit for Hugo content operations and release checks. It can inspect local content, run production-equivalent builds in temporary destinations, audit source and generated output, compare local URLs with a deployed sitemap, and return findings as text, JSON, or SARIF.
{{< /quick-answer >}}

## Why add an operating layer around Hugo?

A small team may ask one person to write, review, release, investigate production, and prepare distribution. Agents can help with those jobs, but only when project facts are discoverable and the results can be checked.

Without a shared workflow, each task starts with assumptions about `content/`, URL rules, module mounts, or build output. A script written for one site may silently miss content mounted from a Hugo module. A browser check may confirm that a page loads without showing whether the deployed URL set matches the release.

`hs` turns common work into repeatable commands with useful exit codes and structured reports. The goal is simple: replace “I think this is ready” with the checks, findings, and status that support that decision.

## What can Hugo Site Tools do?

`hs` provides a command-line interface, an interactive terminal UI, and a local web workspace. The interfaces share the same domain behavior, so a content listing or audit does not take on a different meaning in each one.

- Find and inspect local content, including drafts, front matter, tags, word counts, sections, and generated paths.
- Run production-equivalent builds in a temporary destination, leaving the project’s `public/` directory untouched.
- Audit content, generated output, URLs, internal links, assets, SEO metadata, and Hugo warnings.
- Compare generated local URLs with a deployed sitemap to find missing, stale, or changed pages.
- Inspect a published site’s search index, sitemap, links, titles, descriptions, and canonical URLs.
- Create and validate GA4 campaign links against the project’s approved campaigns, sources, and media.
- Export local Markdown as an EPUB with front matter metadata, covers, local images, custom CSS, footnotes, and project-defined replacements.
- Return human-readable text, JSON for programs, or SARIF for CI and code-scanning workflows.

The work spans the release: source inspection before a build, validation during release review, and checks against the published site afterward.

## How does it help editors and site operators?

An editor can search for a page, review its source and metadata, then create a campaign link from the project’s own policy. That avoids rebuilding a URL by hand or guessing which tracking fields the team allows.

The same Markdown source can become a web post and a reader-ready EPUB. Front matter supplies the book metadata. A bundle can provide its cover, images, and styles, while controlled replacements handle edition-specific wording.

Developers get one bounded audit instead of a collection of site-specific checks. Reports can point to the source path, generated path, public URL, warning, and suggested next action. Maintainers can keep policy in version control and use strict mode when a quality gap should block release.

## What does an agent need from a Hugo tool?

An agent needs more than permission to execute a command. It needs to discover project state, take a bounded action, verify the result, and report evidence that a person can trace.

`hs` supports that loop:

1. **Discover:** Read Hugo configuration, including custom content directories and content-targeted module mounts. List content, inspect front matter, and resolve generated paths from project settings.
2. **Act:** Run a build, audit, URL comparison, search, or campaign-link operation through a stable command. State-changing operations use explicit options.
3. **Verify:** Review findings, exit codes, warnings, generated output, and deployed-site checks. Local release builds use temporary destinations and leave `public/` alone.
4. **Report:** Return a concise summary or pass JSON and SARIF to another system. Findings can be traced to a file, generated path, or public URL.

That gives an agent evidence for questions such as “What changed?”, “What will ship?”, and “What should I fix next?” The answer comes from the configured project and its outputs, rather than an agent’s memory or a visual guess.

This Discover, Act, Verify, Report sequence follows the same contract-first approach I use when [designing reliable workflow agents]({{< ref "lab/developing-effective-agents" >}}): keep repeatable checks explicit and make the result easy to inspect.

## What does a release workflow look like?

An agent preparing a release can search changed content, inspect its front matter, run `hs doctor . --format json`, review the findings, then run `hs urls .` and compare the generated URL set with the deployed sitemap. If checks pass, it can return the commands and exit status. If they fail, it can name the affected file and the smallest useful next step.

For distribution, an agent can select a page, create a policy-compliant campaign link, validate it, and return the URL with its tracking fields. The campaign policy stays visible in the repository.

For repurposing, an agent can export a finished Markdown post to EPUB and report the output path, metadata source, and conversion status. EPUB export requires Pandoc 3.0 or later, will not overwrite an existing EPUB, and refuses to write into Hugo’s `public/` directory.

The same behavior is available through the CLI, TUI, and web workspace. People and agents can use the interface that fits the task and still follow the same operating rules.

## Where does `hs` fit in the stack?

Hugo Site Tools does not replace Hugo, CI, analytics, or editorial judgment. Hugo remains responsible for generation, routing, templates, and archetypes. CI still runs the checks a team chooses. Analytics still measures what happens after publication.

`hs` connects that work to project-aware inspection and evidence. Editors spend less time hunting through directories. Developers can run a bounded audit. Agents can return findings a reviewer can reproduce. The release decision stays with the team.

For teams building agent workflows, this is the same discipline used in [deterministic evaluations for AI skills]({{< ref "lab/deterministic-evals-for-ai-skills" >}}): make the requirements explicit, then return results another person or system can inspect.

## How do I get started?

Install the CLI with Go:

```sh
go install github.com/jjanuszczak/hugo-site-tools/cmd/hs@latest
```

Start by listing content and running the doctor:

```sh
hs content list .
hs doctor .
hs doctor . --format json
```

Export a post with:

```sh
hs content epub content/articles/example.md . \
  --output private/example.epub
```

The EPUB command requires Pandoc 3.0 or later. In the local TUI, select a content item and press `e` to export it.

{{< faq >}}
{{% faq-item question="Does Hugo Site Tools replace Hugo?" %}}
No. Hugo remains the source of truth for site generation, routing, templates, and archetypes. `hs` adds project-aware inspection, validation, and content operations around it.
{{% /faq-item %}}

{{% faq-item question="Can `hs doctor` block a release?" %}}
Yes. Teams can keep site policy in version control and use strict mode when configured quality gaps should produce a failing status for release or CI workflows.
{{% /faq-item %}}

{{% faq-item question="Does a local release build overwrite `public/`?" %}}
No. Local build and doctor workflows use temporary destinations so the project’s `public/` directory is left untouched.
{{% /faq-item %}}

{{% faq-item question="What does EPUB export require?" %}}
It requires Pandoc 3.0 or later. It uses local Markdown content and refuses to overwrite an existing EPUB or write the output into Hugo’s `public/` directory.
{{% /faq-item %}}
{{< /faq >}}

Image by [Chris Reading](https://pixabay.com/users/chrisreadingfoto-2723427/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3013129) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3013129)
