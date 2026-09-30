---
title: "The Restatement Loop"
date: 2026-09-30T09:03:39+08:00
summary: "Algorithmic feeds turn one post into a thousand restatements. RSS and modern user-owned readers are not nostalgia. They are distribution infrastructure for people who want to follow ideas on purpose."
description: "A practical argument for treating RSS, open feeds, and modern personal readers as counterweights to algorithmic restatement loops, creator dependence on For You feeds, and AI-accelerated summary farming."
categories:
  - "Technology"
tags:
  - "artificial-intelligence"
  - "knowledge-management"
  - "platform-economics"
  - "systems-thinking"
  - "open-source"
showReadingTime: true
showTableOfContents: true
draft: true
status: "agent-review"
about:
  - name: "RSS"
    url: "https://en.wikipedia.org/wiki/RSS"
  - name: "Algorithmic curation"
    url: "https://en.wikipedia.org/wiki/Algorithmic_curation"
mentions:
  - name: "Jack Conte"
    url: "https://en.wikipedia.org/wiki/Jack_Conte"
  - name: "Google Reader"
    url: "https://en.wikipedia.org/wiki/Google_Reader"
  - name: "Pew Research Center"
    url: "https://www.pewresearch.org/"
citations:
  - title: "The Behaviors and Attitudes of U.S. Adults on Twitter"
    url: "https://www.pewresearch.org/internet/2021/11/15/the-behaviors-and-attitudes-of-u-s-adults-on-twitter/"
  - title: "Sizing Up Twitter Users"
    url: "https://www.pewresearch.org/internet/2019/04/24/sizing-up-twitter-users/"
  - title: "Death of the Follower & the Future of Creativity on the Web with Jack Conte | SXSW 2024 Keynote"
    url: "https://youtu.be/5zUndMfMInc"
  - title: "Announcing turndown of the Google Feed API"
    url: "https://developers.googleblog.com/announcing-turndown-of-the-google-feed-api/"
---

Most of what looks like a trend is often one post wearing a thousand costumes.

You have seen the pattern. One claim, clip, chart, screenshot, or complaint catches fire. Then the feed fills with quote posts, rewrites, replies, dunk threads, summaries, and summary-of-summary posts. By the afternoon, it feels like the internet has discovered a new subject. Often it has not. It has discovered a new object to restate.

{{< quick-answer >}}
Algorithmic feeds reward reaction, repetition, and commentary on whatever is already moving. RSS and its descendants are not a nostalgic retreat from the modern web. They are a practical way to rebuild user-owned followership: creators publish on property they control, readers choose the sources, and AI helps filter the stream without taking ownership of the relationship.
{{< /quick-answer >}}

This is not just an annoyance for writers. It is a distribution problem.

If the platform rewards reaction to the visible thing more than original work, creators adapt. They optimize for the machine. Readers adapt too. They stop following sources and start following whatever the ranking system decides is currently alive.

That is how a feed becomes a restatement loop.

## Why does one post become the whole conversation?

The social feed makes repetition look like consensus.

Pew Research Center has documented the concentration problem for years. In its 2019 analysis of U.S. adult Twitter users, the most active 10% produced 80% of all tweets from U.S. users. In its 2021 analysis, the most active quarter of U.S. adult Twitter users produced 97% of all tweets from the observed sample. Pew also found that original posts were only 14% of tweets from that highly active group. Most of the output was retweets or replies.

That does not mean every retweet or reply is low value. Conversation matters. Curation matters. A sharp response can be more useful than the original post.

But the structure matters more than the intention.

When a small group produces most of the visible output, and most of that output responds to other output, the feed naturally becomes recursive. A topic can feel culturally dominant because thousands of posts are orbiting one originating item. The volume is real. The independence is not.

X's trend and ranking systems do not need to surface a single tweet as the unit of attention. They can surface the topic, the argument, the phrase, the screenshot, or the argument about the screenshot. The result is the same for the reader: repetition becomes atmosphere.

That is why the feed feels so loud and so thin at the same time.

## Why did the follower stop being infrastructure?

Jack Conte's 2024 SXSW keynote, "Death of the Follower," is useful because it does not frame the problem as a simple fight between chronological feeds and ranking. His point is sharper: the follow used to be architecture.

The follow was a relationship. A reader, listener, or fan made a decision. The creator published. The follower had a reasonable expectation that the work would arrive.

Then ranking changed the bargain. Facebook ranked. TikTok made the For You feed the main interface. YouTube, Instagram, and X all moved deeper into algorithmic recommendation. The product goal shifted from "show me what I chose" toward "show me what keeps me here."

Conte's critique lands because it names the incentive conflict. A feed optimized for watch time and a feed optimized for creator-audience strength are different products. They can overlap, but they are not the same system.

This is the same underlying issue I wrote about in [Building an Audience Starts With a Reason to Belong]({{< ref "articles/building-an-audience" >}}). An audience compounds when people have a reason to return and a direct path back to the organizer. If a platform owns that path, the audience is partly rented, no matter how large the follower count looks.

The creator thinks they built distribution. The platform knows it owns allocation.

## Why is RSS suddenly relevant again?

RSS is boring in the best possible way.

A site publishes. A feed reader checks. New items appear. No ranking committee. No engagement auction. No forced pivot into short video because a competitor's format spiked last quarter.

That simplicity is easy to underrate because the consumer web taught people to confuse convenience with control. Google Reader made RSS easy enough for normal people, then Google shut it down in 2013. Google later turned down the Google Feed API in 2016 after years of deprecation. Platform APIs tightened. Social networks preferred traffic, identity, and monetization to stay inside their walls.

None of that made open feeds technically obsolete. It made them commercially inconvenient for companies that wanted to own the whole loop.

The original appeal still matters. RSS is a pre-social version of the follow. A creator can publish from their own site. A reader can subscribe without asking a platform to mediate the relationship. The reader's list can move. The source can be inspected. The feed does not need to pretend that every reading decision is a growth-hacking opportunity.

This is not nostalgia. It is ownership.

## What does AI make worse?

AI makes the restatement loop cheaper.

It can summarize one post into ten versions. It can convert a video into a thread. It can rewrite a hot take in the tone of whatever account is currently performing well. It can generate synthetic replies that make a topic feel bigger than it is. It can produce plausible commentary before anyone has read the underlying source.

That does not make AI the villain. It makes AI an accelerant.

The real risk is not that machines write. The risk is that the economics of the feed reward writing that behaves like a machine: fast, derivative, frictionless, and optimized for visible motion.

That is close to the issue in [AI Is Not Killing Reading. It Is Testing Whether We Still Think]({{< ref "articles/is-ai-killing-book-reading" >}}). The problem is not access to summaries. The problem is losing the habit of forming a view before the summary arrives.

It is also the old gap between [discovery and knowledge]({{< ref "articles/discovery-to-knowledge" >}}). AI can reveal the shape of a conversation quickly. It cannot decide which source deserves trust, which incentive is distorting the discussion, or whether the visible conversation is only a copy of a copy.

In a restatement loop, the source becomes almost incidental. What matters is being adjacent to momentum.

AI makes adjacency abundant.

## What can AI make better?

The same technology can also make user-owned reading more useful.

The old feed reader had one big weakness: it treated every source update as roughly equal. That was clean, but it created work for the reader. Once you subscribed to enough sites, newsletters, podcasts, GitHub releases, and channels, the reader became another inbox.

A modern reader should not copy the old model exactly.

It should combine three layers:

1. **Chronological source control.** Show me what the sources I chose published, in an order I can understand.
2. **Personal briefing.** Let AI group, summarize, translate, de-duplicate, and flag what changed since I last checked.
3. **Creator-owned publishing.** Preserve the direct path back to the original site, feed, newsletter, repo, or media file.

That is the useful split: let AI help the reader manage abundance, but do not let it own the relationship.

This is where [Architecture of Attention]({{< ref "articles/architecture-of-attention" >}}) becomes practical rather than abstract. The strategic issue is not whether you consume more information. It is whether your information architecture helps you separate signal from repeated noise.

A reader that can say "five people are reacting to the same original source" is already more valuable than a feed that shows all five reactions as independent events.

## How should builders and creators respond?

Do not abandon platforms. That is too clean and usually unrealistic.

Platforms still provide discovery. They still create serendipity. They still let a new creator reach someone who did not know they existed yesterday. The answer is not to become a digital hermit with an RSS icon and a moral superiority complex.

The answer is to stop treating platform distribution as the whole asset.

Creators should publish somewhere they control, expose a feed, build an email list, and make the canonical version of the work easy to find. Builders should make readers that respect source ownership, keep subscriptions portable, and use AI as a reader-side tool rather than another black-box allocation system.

Readers should rebuild the habit of choosing sources on purpose.

That last point is the hardest because algorithmic feeds train passivity. They create the feeling that you are informed because you have seen what the feed made loud. But "what is loud" and "what is worth understanding" are not the same category.

The open web used to be clumsy, but it had one virtue worth recovering: the user had to decide what to follow.

That decision is infrastructure.

## What would a modern feed reader actually look like?

It would be boring at the base and intelligent at the edge.

At the base: RSS, Atom, email ingestion, podcast feeds, YouTube channels, public newsletters, GitHub releases, and website updates. Open inputs. Portable subscriptions. Clear source attribution.

At the edge: AI summaries, topic clustering, semantic search, translation, personal briefings, and duplicate detection. The AI should help the reader ask better questions: What is original here? What is a reaction? What source is everyone responding to? What did my chosen experts say that I would have missed?

The important design principle is structural separation. The creator owns the publishing endpoint. The reader owns the subscription list. The tool helps with comprehension, but it does not become the new platform gatekeeper.

That is the practical counterweight to the restatement loop.

Not nostalgia. Not a product tour. Not a purity test.

Just a better allocation of control.

The feed is broken because we outsourced too much of the follow to systems that profit from keeping us inside the reaction machine. Bringing back the reader means bringing back a simple discipline: choose your sources, read closer to the origin, and let technology reduce noise without replacing judgment.

The future of the web does not need fewer algorithms.

It needs more user-owned intent.

{{< faq >}}
  {{% faq-item question="Is RSS still useful in 2026?" %}}
  Yes. RSS remains useful because it gives readers a portable way to follow sources directly. The modern version should pair open feeds with AI-assisted briefing, de-duplication, and search rather than copying the old Google Reader experience exactly.
  {{% /faq-item %}}
  {{% faq-item question="What is the restatement loop?" %}}
  The restatement loop is the pattern where one original post, claim, clip, or screenshot becomes a wave of reactions, summaries, quote posts, replies, and rewrites. The feed then makes that repetition feel like broad independent activity.
  {{% /faq-item %}}
  {{% faq-item question="Does AI make algorithmic feeds worse?" %}}
  AI can make the loop worse by making derivative commentary cheaper to produce. It can also help readers if it runs on the reader's side: grouping duplicates, summarizing chosen sources, and pointing back to originals instead of replacing them.
  {{% /faq-item %}}
{{< /faq >}}

*Featured image by <a href="https://unsplash.com/@anyutakejbalo">Anna Keibalo</a> from <a href="https://unsplash.com/photos/a-person-reading-a-newspaper-next-to-a-laptop-1RVduxIDdY4">Unsplash</a>.*
