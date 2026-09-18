---
title: "The Presentation Is Not the Product. The System Is."
date: 2026-09-17
draft: false
summary: "Margo turns presentations from disposable AI-generated decks into versioned, portable company assets that improve with use."
description: "Why the defensible value in AI-era presentations is not generating the first deck, but preserving the evidence, narrative, visual rules, and institutional memory that make every subsequent deck better."
categories: ["Technology"]
tags:
  - artificial-intelligence
  - knowledge-management
  - design-systems
  - systems-thinking
  - software-engineering
  - open-source
showReadingTime: true
showTableOfContents: true
featuredImage: "featured.jpg"
about:
  - name: "Margo"
    url: "https://github.com/jjanuszczak/margo"
mentions:
  - name: "Version control"
    url: "https://en.wikipedia.org/wiki/Version_control"
citations:
  - title: "Brand as software"
    url: "https://pauljun.substack.com/p/brand-as-software"
  - title: "Cowork is now Claude"
    url: "https://claude.com/blog/cowork-is-now-claude"
---

Most AI slide generators solve the visible problem.

You give them a prompt, a document, or a pile of notes. They give you a deck. Sometimes it is surprisingly good. Increasingly, it will be excellent.

But the slide deck was never the real problem.

The hard part is turning a company's accumulated judgment into work that can be produced repeatedly without losing the plot: approved language, evidence behind the claims, financial logic, visual hierarchy, and the difference between a board update, investor memo, client proposal, and public point of view. Those choices make the work recognizably yours.

{{< quick-answer >}}
AI can create a presentation quickly, but it cannot by itself preserve the source material, review history, evidence, and design decisions that make later presentations stronger. [Margo](https://github.com/jjanuszczak/margo) is built to make those decisions durable, so a deck becomes a company asset rather than a disposable export.
{{< /quick-answer >}}

That is the position Margo fills.

Margo is not an AI slide generator. It is a system for making presentations into durable company assets.

A deck built in Margo has a source of truth. Its content, notes, assets, structure, and visual rules live in an explicit project. It can be versioned, reviewed, rebuilt, published, and handed to the next person without asking them to reconstruct the logic from a chat history, a folder of exports, and a brand PDF nobody has opened in months.

That matters because serious presentations are not disposable.

A market-entry briefing changes as local evidence comes in. An investor narrative evolves as the numbers move. A board pack gets tighter after every meeting. A sales deck absorbs the objections that actually matter in the field. The best version of that work should not disappear into the project where it was first made.

It should compound.

## Why should a presentation become institutional memory?

Most presentation tools treat each deck as a separate object. That makes sense when the work is primarily visual assembly.

But companies do not need more isolated files. They need a system that retains their decisions.

Margo treats a deck as structured source material plus a reusable rendering system. Markdown holds the narrative. Themes hold the visual language. Notes preserve speaker context and research. Assets remain attached to the work. Version control records what changed. Build and publishing workflows create consistent outputs.

The underlying engine is deliberately markdown-native, as I set out in [Margo: The Presentation Engine for the AI Era]({{< relref "lab/margo" >}}). This article extends that technical premise into an operating one: the deck is not only a compiled artifact, but a durable record of company judgment.

This does not make the work less creative. It moves the repetitive part into infrastructure.

The person making the deck no longer needs to remember every logo rule, reconstruct the layout logic, or search old folders for the last approved wording. They can focus on the argument: What is true? What matters to this audience? What decision must this presentation drive?

The result is not a rigid template factory.

A strong system gives the organization coherence without forcing sameness. A board pack should not feel like a product launch. A market analysis should not look like a recruiting deck. But they should still feel as if they came from the same company, with the same standards of evidence, editorial judgment, and visual discipline.

Paul Jun described this idea well in ["Brand as software."](https://pauljun.substack.com/p/brand-as-software) Brand guidelines describe rules. Brand software carries those decisions into the work itself.

Margo applies that idea to presentations.

## Where does AI fit in a durable presentation workflow?

AI makes Margo more valuable, not less.

An AI assistant can research, structure a narrative, draft slide content, propose alternatives, and make revisions at a speed no traditional workflow can match. Claude Slides is a strong example of where this is going. It makes the path from conversation to editable presentation dramatically shorter, as [Claude's announcement](https://claude.com/blog/cowork-is-now-claude) illustrates.

That is good for everyone.

But the company still needs somewhere for its approved work to live after the conversation ends. It needs a stable source of truth that is not tied to one model, one workspace, or one export format. It needs to know what changed, what was approved, what evidence supports the claims, and how to rebuild the deliverable next quarter.

The same architecture matters outside presentations. In [a markdown-native CRM experiment]({{< relref "lab/crm-llm" >}}), I made the case for structured, inspectable files as the durable record while agents operate on top of them. Margo applies that model to presentation work.

Margo is that layer.

Claude, Codex, Gemini, or an internal agent can write into a Margo deck. The output remains portable. The theme remains reusable. The build remains deterministic. The presentation can be published as a web artifact, exported as a PDF, or handed over in the format a client requires.

The AI helps create the work. Margo preserves the system that makes the work better over time.

## What is Margo building toward?

The ambition is not to make it easier to produce more slides.

It is to let a company encode its best presentation decisions once, then improve them through use.

A good Margo project should eventually know:

- which claims require sources
- which layouts fit which kinds of arguments
- how a brand behaves across different audiences and moments
- which content is approved, current, or due for review
- how to build the same deck reliably for web, PDF, and handoff
- how corrections from one presentation improve the next one

That is a very different product from a generator that produces plausible pages on demand.

The generator is useful. The system is defensible.

The real value appears after the first deck, when the company has to make the tenth, fiftieth, or five-hundredth artifact without losing its voice, standards, or institutional memory.

That is where Margo belongs.

> AI can draft the deck. Margo turns it into an asset the organization can own.

{{< faq >}}
  {{% faq-item question="Is Margo an AI slide generator?" %}}
  No. AI tools can author or revise a Margo deck, but Margo is the structured system of record for the presentation's source, themes, assets, notes, and build process.
  {{% /faq-item %}}
  {{% faq-item question="Why does version control matter for presentations?" %}}
  It makes the evolution of an argument inspectable. Teams can see what changed, review approved language and evidence, rebuild an earlier version, and carry the working logic into the next presentation.
  {{% /faq-item %}}
  {{% faq-item question="Does a presentation system force every deck to look the same?" %}}
  No. A system should preserve shared standards while allowing different structures and visual treatment for board packs, investor narratives, client proposals, and public points of view.
  {{% /faq-item %}}
{{< /faq >}}
