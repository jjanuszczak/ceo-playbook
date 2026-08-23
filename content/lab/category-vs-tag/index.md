---
title: "You’re Using Categories and Tags Wrong (Here’s How to Fix It)"
date: 2026-01-10
draft: true
summary: "Categories define the durable role of a post. Tags connect the ideas that recur across the site. Treat both as governed systems, not decorative labels."
description: "A practical operating model for using Hugo categories and tags to create a durable content architecture, strengthen discovery, and avoid a pile of one-off labels."
categories:
  - Technology
tags:
  - systems-thinking
  - taxonomy
  - hugo
  - knowledge-management
  - digital-transformation
showReadingTime: true
showTableOfContents: true
about:
  - name: "Taxonomy"
    url: "https://en.wikipedia.org/wiki/Taxonomy_(general)"
  - name: "Knowledge organization"
    url: "https://www.w3.org/TR/skos-primer/"
mentions:
  - name: "Hugo"
    url: "https://gohugo.io/"
citations:
  - title: "Hugo Taxonomies"
    url: "https://gohugo.io/content-management/taxonomies/"
  - title: "SKOS Simple Knowledge Organization System Primer"
    url: "https://www.w3.org/TR/skos-primer/"
---

Most sites treat categories and tags as a filing exercise. That is how they end up with 30 categories, hundreds of one-off tags, and no useful path from one idea to the next.

I use them differently, and so should you! Categories state the durable role of a post on this site. Tags connect the recurring ideas that cut across that structure. Together, they turn a growing archive into an intelligible body of work.

{{< quick-answer >}}
Use one category to answer, "What kind of work is this?" Use a small set of reused tags to answer, "Which ideas does this work extend?" Categories should change rarely. Tags should create useful connections across the archive, not merely describe every noun on the page.
{{< /quick-answer >}}

## What are categories and tags actually for?

Both are taxonomies, which are classification systems for expressing relationships between content. [Hugo](https://gohugo.io/) (the site generator I use) makes that explicit: a taxonomy groups content under terms and automatically creates pages for those terms. 

The mechanics are straightforward. The editorial decision is harder. A taxonomy only helps when its terms remain stable enough to mean something, and specific enough to guide a reader to the next useful piece of work.

For this site, the division is deliberate:

* Categories describe my role and the durable pillars of the work.
* Tags describe the concepts, domains, practices, and sources that recur across those pillars.

That distinction keeps the navigation legible while giving the archive a real *semantic graph* (which is a fancy way of saying a web of connected ideas based on what they mean).

## Why should categories stay broad and stable?

Categories are the macro-structure. A reader should be able to see them in a navigation bar and immediately understand the kind of work I do.

This site uses a single approved category per post. `Strategy`, `Technology`, `Fintech`, and `Venture Building` are useful because they can hold years of writing without becoming vague. `AI`, `Innovation`, and `Blog` are not categories. They are topics, claims, or empty labels.

If I need a new category every month, I have not discovered a new pillar. I have avoided making a classification decision.

```yaml
categories:
  - Technology
```

## How should tags build a useful knowledge graph?

Tags do the connective work. They should cross category boundaries and reflect concepts I expect to return to, such as `systems-thinking`, `knowledge-management`, `platform-economics`, or `board-governance`.

The test is practical: would I want a landing page for this tag, and can I credibly use it across at least ten posts? If not, it is probably a detail, not a tag.

For example, `hugo` is useful when a post is materially about the platform. `taxonomy` is useful when a post examines how knowledge is organized. A tag such as `publishing-thoughts-2026` is not useful. It creates an archive page with no future.

```yaml
tags:
  - systems-thinking
  - taxonomy
  - hugo
  - knowledge-management
  - digital-transformation
```

This is also why I avoid treating every keyword as a tag. A tag is an editorial commitment to an intellectual thread, not a search index.

## What does the decision look like on a real post?

Take a post about a new Hugo capability that lets readers carry clean Markdown into their own working context. Its category is `Technology` because that states the role of the work. Its tags could include `hugo`, `knowledge-management`, and `software-engineering` because those threads recur elsewhere on the site.

[The Copy Page feature]({{< ref "lab/ai-built-copy-page-hugo" >}}) is a concrete example. The implementation is small, but the editorial point is larger: structured source material becomes more useful when readers and their agents can work with it directly.

{{< figure
    src="category-vs-tag.png"
    alt="Decision model showing categories as durable site pillars and tags as reusable cross-cutting concepts"
    caption="Use categories to define a post’s durable role. Use tags to connect its recurring ideas."
    >}}

## When should I create a new taxonomy instead?

Do not create a new taxonomy because the existing ones feel inconvenient. Create one only when the site needs a genuinely different browsing lens with its own rules and landing pages.

For example, a `series` taxonomy can make sense for a deliberate multi-part body of work. A `role` taxonomy could make sense if executives, operators, and investors need distinct paths through the archive. A redundant `topics` taxonomy usually does not. It often duplicates tags without solving a reader problem.

Many content management systems (like Hugo) support custom taxonomies, but the framework does not supply the governance. That is the editorial work. The same principle applies to the wider platform: [the architecture of attention]({{< ref "articles/architecture-of-attention" >}}) matters because structure determines what readers can discover, connect, and act on.

## What are the common mistakes?

* Creating categories that describe a passing topic rather than a durable role.
* Adding tags that appear once and never build a reader path.
* Using categories and tags interchangeably because the CMS permits both.
* Creating a custom taxonomy before proving that categories and tags cannot do the job.
* Letting front matter drift away from the site’s published governance.

The last mistake is the most expensive. Weak labels do not fail loudly. They quietly turn an archive into a pile of isolated pages.

## How do I keep the system useful as the site grows?

Review the taxonomy periodically. Retire labels that never gained a body of work. Do not invent replacements merely to make a dashboard look complete. Keep the categories narrow and durable; use tags only where there is a real recurring thread.

That discipline is the difference between discovery and knowledge. [From Discovery to Knowledge]({{< ref "articles/discovery-to-knowledge" >}}) makes the same point in a different context: more information does not create understanding until someone imposes judgment, context, and accountability.

{{< faq >}}
  {{% faq-item question="Can a post have more than one category?" %}}
  It can technically, but I use one category per post. A single durable role keeps the primary structure clear. If a post spans several themes, tags should capture the cross-cutting ideas.
  {{% /faq-item %}}
  {{% faq-item question="How many tags should a post have?" %}}
  Use enough to create meaningful connections, usually five to eight. Every tag should be reusable, lower-case and hyphenated, and strong enough to deserve its own archive page.
  {{% /faq-item %}}
  {{% faq-item question="When is a new tag justified?" %}}
  Add one only when it names a core idea that I expect to reuse repeatedly, not a one-off detail. If an existing tag can carry the meaning, use the existing tag.
  {{% /faq-item %}}
{{< /faq >}}

## Is there a video associated with this article?

If you enjoy watching more than reading, check this out:

{{< youtubeLite id="ISzNJ_FTMhQ" label="Categories vs Tags: You’re Doing It WRONG!" >}}

Featured image by [StockSnap](https://pixabay.com/users/stocksnap-894430/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=923188) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=923188).

{{< related-posts title="Related Insights" paths="lab/deterministic-evals-for-ai-skills, lab/agents-vs-skills" >}}

{{< read-next title="Read Next" link="lab/pyenv" buttonText="View more Deep Dives" >}}
