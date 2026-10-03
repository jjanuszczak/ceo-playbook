---
title: "Marp Made Markdown Slides Easy. Margo Treats Them as a Product."
date: 2026-10-03
summary: "Marp is an excellent Markdown-to-slides format. Margo is a structured presentation project system for decks that need to grow, repeat, and survive agent-assisted maintenance."
description: "A practical comparison of Marp and Margo, focused on the difference between exporting a Markdown document and maintaining a presentation as a structured product."
categories:
  - "Technology"
tags:
  - "artificial-intelligence"
  - "knowledge-management"
  - "open-source"
  - "software-engineering"
  - "design-systems"
  - "systems-thinking"
  - "productivity"
showReadingTime: false
showTableOfContents: true
featuredImage: "featured.png"
draft: false
status: published
about:
  - name: "Markdown"
    url: "https://en.wikipedia.org/wiki/Markdown"
  - name: "Marp"
    url: "https://marp.app/"
  - name: "Margo"
    url: "https://github.com/jjanuszczak/margo"
mentions:
  - name: "Andrej Karpathy"
    url: "https://github.com/karpathy"
  - name: "Obsidian"
    url: "https://obsidian.md/"
citations:
  - title: "Marp official site"
    url: "https://marp.app/"
  - title: "Margo source repository"
    url: "https://github.com/jjanuszczak/margo"
---

Andrej Karpathy recently described a compelling workflow for [LLM-maintained knowledge bases](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw material goes into a Markdown wiki, the LLM organizes and updates it, and useful outputs come back as documents, charts, or slide decks. In that workflow, he suggested Marp for presentations.

That recommendation makes sense.

[Marp](https://github.com/marp-team/marp) is simple, capable, and widely understood. Its core idea is straightforward: write Markdown, separate slides with `---`, add a few directives, and export to HTML, PDF, PowerPoint, or images. Marp also has a mature ecosystem, including a VS Code extension and a dedicated CLI.

But Marp solves a narrower problem than the one many teams now have.

Marp turns a Markdown file into slides.

[Margo](https://github.com/jjanuszczak/margo) treats a presentation as a maintained, structured project.

That difference matters when an LLM, a team, or a company needs to create more than one disposable deck.

This is the narrower technical comparison behind my broader argument in [The Presentation Is Not the Product. The System Is.]({{< relref "lab/presentation-system-not-product" >}}): the durable value sits in the system that preserves the work, not only in the first export.

{{< quick-answer >}}
Marp is an excellent Markdown slide format for quick, self-contained decks. Margo is the stronger fit when a presentation needs addressable slides, local assets and notes, reusable layouts, brand rules, draft states, and repeatable agent-assisted maintenance.
{{< /quick-answer >}}

## Why does Marp remain a strong choice?

Marp is an excellent choice for quick, self-contained presentations.

A basic deck can be one Markdown file:

```markdown
---
marp: true
theme: default
paginate: true
---

# First slide

Some content.

---

# Second slide

More content.
```

That simplicity has real value.

Marp is easy to explain to an LLM. It is easy to edit in Obsidian or VS Code. It requires very little project structure. It supports custom themes, speaker notes, PDF export, PowerPoint export, and image export. Its CLI can run directly through `npx`, and its VS Code extension provides live preview and export workflows.

If you need to produce a quick visual summary from a Markdown note, Marp may be the right answer.

The problem begins when the deck becomes a real artifact.

## What changes when a deck becomes a product?

A serious presentation usually contains more than slide text:

- slide-specific assets
- speaker notes
- research notes
- draft slides
- hidden slides
- reusable layouts
- brand rules
- section metadata
- deck-wide configuration
- multiple output formats
- version history
- generated files that should not be edited by hand

A single Markdown file can contain some of this information. It does not provide a particularly strong model for managing it.

Marp’s basic authoring model is document-oriented. Slides are sections inside a Markdown document, usually separated by horizontal rules. That is elegant for a short deck. It becomes less comfortable when an LLM needs to revise slide 17, replace its image, update its research notes, preserve its speaker script, and insert a new slide before it without rewriting the whole file.

Margo uses slide bundles instead:

```text
my-deck/
  margo.yaml
  slides/
    01-title/
      index.md
      notes/
        speaker-script.md
        research.md
      hero.svg
    02-problem/
      index.md
  assets/
  themes/
  archetypes/
```

Each slide is an addressable unit. Content, notes, and assets can live together. An agent can modify one slide without treating the entire deck as a single text blob.

That is a small architectural decision with large consequences.

## How does Margo turn a deck into a project?

Margo borrows the useful parts of Hugo’s mental model and applies them to presentations.

A deck has:

- a root configuration file
- an explicit slide directory
- themes
- layouts
- reusable partials
- shortcodes
- archetypes
- assets
- build outputs
- local development commands

The project structure tells both humans and agents where things belong.

The content stays in Markdown. The visual behavior stays in themes. The engine handles parsing, validation, sequencing, asset resolution, and output generation.

That separation matters. It prevents every deck from becoming a collection of ad hoc CSS fragments and one-off HTML patches.

Margo’s default workflow is closer to this:

```bash
margo new my-deck
cd my-deck
margo serve
margo build
```

Creating a new slide can use an archetype:

```bash
margo new slide market-size --archetype metric
```

The archetype can provide the initial front matter and content structure. The author then fills in the actual material.

This is more opinionated than Marp. That is intentional.

## Why is the project model useful for LLM-authored decks?

LLMs are good at writing Markdown. They are less reliable at maintaining large, fragile documents whose meaning depends on position, formatting, and implicit conventions.

Margo gives an agent more explicit handles:

```yaml
---
title: Market size
order: 5
section: Strategy
layout: metric
draft: false
---
```

The agent can reason about a slide as a structured object:

- title
- order
- section
- layout
- visibility
- background
- notes
- local assets

That makes common operations safer:

- create a slide
- move a slide
- draft a slide without publishing it
- hide a slide from normal output
- change the layout without rewriting its content
- keep research notes separate from rendered content
- preserve local assets beside the slide that uses them

Margo also generates project-local agent guidance when scaffolding a deck. The deck can carry instructions about its own structure, commands, theme rules, and authoring conventions. That gives an LLM more context than a bare `.md` file provides.

This is the strongest argument for Margo.

Not that it produces prettier slides automatically. Marp can produce attractive decks.

The stronger argument is that Margo gives an agent a better workspace.

## What does Margo add for reusable brand systems?

Marp themes are largely CSS-based. That is powerful, but it puts much of the authoring burden on the person writing the deck.

Margo treats themes as reusable presentation systems. A theme can define:

- slide layouts
- deck shells
- typography
- color options
- reusable partials
- shortcodes
- assets
- print behavior
- optional PowerPoint metadata

The deck author can then select approved options in `margo.yaml`:

```yaml
theme:
  name: default
  color_mode: dark
  typography: executive
  accent_color: "#4db6ac"
```

The distinction is between changing the content and changing the presentation system.

A writer should not need to understand every CSS selector in a company theme to create a new metric slide. They should choose the metric archetype, provide the data, and let the theme own the composition.

That model is better suited to teams. One person can maintain the theme while others write decks against it.

## Why does a living deck repository need more than export?

The LLM wiki idea changes the job from “make a presentation” to “maintain a growing body of knowledge.”

That calls for more than export.

The same logic appears in [the Markdown-native CRM experiment]({{< relref "lab/crm-llm" >}}), where structured files act as the durable record and agents operate on top of them.

A useful presentation repository needs to support:

- incremental edits
- reviewable Git diffs
- reusable conventions
- source and research notes
- multiple deck versions
- draft content
- generated artifacts
- predictable builds
- agent handoffs

Marp can participate in that workflow. Its files are plain Markdown, and its ecosystem works well with Obsidian, VS Code, and Git.

Margo is designed around that workflow from the start.

It treats the deck as a small software project with a content model, build process, theme contract, and local development loop. That may be unnecessary for a five-slide summary. It becomes useful when a deck is updated every week, maintained by several people, or generated and revised by agents.

## Is Margo actually better than Marp?

Not universally.

Marp may be better when:

- you want the smallest possible setup
- the deck belongs in one Markdown file
- you are working inside an Obsidian or VS Code workflow
- you need a quick export
- you want the existing Marp ecosystem
- you do not need a structured project model

Margo is better when:

- the deck will be maintained over time
- an LLM will create and revise it repeatedly
- slides need their own assets and notes
- you need draft and hidden slide states
- you want reusable layouts and archetypes
- a team needs a shared brand system
- you want explicit separation between content and presentation
- the deck is closer to a product than a document

The honest positioning is not “Marp is obsolete.”

Marp is still active and useful. The Marp team maintains the core ecosystem, CLI, and VS Code integration.

The better claim is narrower:

> Marp is an excellent Markdown slide format. Margo is a presentation project system designed for decks that need to grow, repeat, and survive agent-assisted maintenance.

Karpathy’s recommendation points toward a future where Markdown becomes a durable working format for both knowledge and generated outputs.

Marp is a strong answer for the output format.

Margo is an attempt to answer the next question:

What should the repository look like when the slide deck becomes part of the knowledge system itself?

That is where Margo has a credible advantage.

It is not better because it has more configuration. It is better when structure, reuse, branding, notes, assets, and agent maintenance matter more than getting from one Markdown file to one PDF as quickly as possible.

Margo is still evolving. It does not yet have Marp’s ecosystem or maturity, and its PowerPoint and PDF workflows still have sharper edges. But its direction is different.

Marp treats slides as Markdown with presentation syntax.

Margo treats slides as content inside a maintainable presentation system.

For disposable decks, use Marp.

For living decks, Margo is the better bet.

*Featured image source: [Unsplash desktop publishing collection](https://unsplash.com/s/photos/desktop-publishing).*

{{< faq >}}
  {{% faq-item question="Is Marp obsolete?" %}}
  Marp is not obsolete. It remains a strong choice for quick, self-contained Markdown presentations and has a mature ecosystem around themes, the CLI, and VS Code.
  {{% /faq-item %}}

  {{% faq-item question="When should a team choose Margo over Marp?" %}}
  Choose Margo when the deck needs to be maintained over time, when slides need their own assets and notes, or when agents and multiple contributors need explicit project structure.
  {{% /faq-item %}}

  {{% faq-item question="Does Margo automatically produce better-looking slides?" %}}
  No. Margo’s advantage is structural. It separates content from presentation systems and gives humans and agents clearer handles for maintaining a deck.
  {{% /faq-item %}}

  {{% faq-item question="What is the simplest way to decide?" %}}
  Use Marp when you need one Markdown file and a fast export. Use Margo when the presentation is becoming a maintained product with reusable structure, assets, notes, and build rules.
  {{% /faq-item %}}
{{< /faq >}}
