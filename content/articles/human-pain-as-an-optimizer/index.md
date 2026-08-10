---
title: "AI Agents Do Not Feel Pain"
date: 2026-08-10T09:01:57+08:00
summary: "AI coding agents can write code quickly, but they do not feel the future maintenance pain that teaches human engineers to avoid brittle architecture."
description: "A practical argument for why human judgment still matters in agentic coding: senior engineers optimize against future maintenance pain, while AI agents optimize for the immediate stated goal."
categories:
  - "Technology"
tags:
  - "artificial-intelligence"
  - "software-engineering"
  - "programming"
  - "systems-thinking"
  - "productivity"
showReadingTime: true
showTableOfContents: true
draft: true
status: "user-review"
about:
  - name: "AI-assisted programming"
    url: "https://en.wikipedia.org/wiki/Artificial_intelligence_in_software_engineering"
  - name: "Technical debt"
    url: "https://en.wikipedia.org/wiki/Technical_debt"
mentions:
  - name: "Pi"
    url: "https://pi.dev/"
  - name: "The Pragmatic Engineer"
    url: "https://newsletter.pragmaticengineer.com/"
  - name: "DORA"
    url: "https://dora.dev/"
citations:
  - title: "Building Pi, and what makes self-modifying software so fascinating"
    url: "https://newsletter.pragmaticengineer.com/p/building-pi-and-what-makes-self-modifying"
  - title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
    url: "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
  - title: "Impact of Generative AI in Software Development"
    url: "https://dora.dev/ai/gen-ai-report/report/"
  - title: "AI Copilot Code Quality: 2025 Look Back at 12 Months of Data"
    url: "https://www.gitclear.com/ai_assistant_code_quality_2025_research"
  - title: "Technical Debt: From Metaphor to Theory and Practice"
    url: "https://www.sei.cmu.edu/library/technical-debt-from-metaphor-to-theory-and-practice/"
  - title: "Technical debt in AI-enabled systems"
    url: "https://doi.org/10.1016/j.jss.2024.112151"
---

The most useful warning I have heard about AI coding agents is not about hallucinations, security, or prompt tricks.

It is simpler than that: **agents do not feel pain**.

A human engineer feels bad architecture in their body. They remember the weekend production fire. They remember the interface that looked clever in March and became impossible to change in October. They remember the pull request that took three days to review because every decision was buried behind a layer of unnecessary abstraction.

That pain is not sentimental. **It is an optimizer**.

{{< quick-answer >}}
AI coding agents can produce useful code, but they do not feel the future maintenance pain that teaches human engineers to avoid complexity, duplication, and weak abstractions. The executive lesson is not to stop using agents. It is to redesign the engineering system so human judgment, review friction, automated checks, and refactoring capacity protect the codebase from output that looks productive today and becomes expensive later.
{{< /quick-answer >}}

## Why does human pain matter in software engineering?

Pain is information.

Not emotional drama. Operating data.

When a senior engineer rejects an abstraction, they are often compressing years of damage into one short sentence: "No, this will hurt us later." That judgment comes from carrying the future cost of bad decisions. It comes from maintaining the system after the demo, after the sprint, after the person who wrote the original code has moved on.

[Carnegie Mellon University's Software Engineering Institute](https://www.sei.cmu.edu/library/technical-debt-from-metaphor-to-theory-and-practice/) frames technical debt as more than a rhetorical metaphor. It is a way to make explicit decisions about short-term development choices, future change, and the work needed to manage debt through a backlog.

That is the point executives often miss.

Technical debt is not only bad code. It is deferred pain. The code may compile. The feature may ship. The demo may impress the room. But the repayment schedule starts later, usually when the team is under pressure and least able to afford it.

Human engineers learn from that repayment schedule. Agents do not.

This connects directly to [The Next Compiler]({{< ref "articles/the-next-compiler" >}}). Natural language is becoming a higher-level instruction layer for software work, but abstraction does not remove engineering judgment. It changes where judgment has to sit.

## What did the Pi discussion get right?

The clearest version of this argument came from the Pi discussion on [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/building-pi-and-what-makes-self-modifying). Mario Zechner, creator of Pi, and Armin Ronacher, creator of Flask, made a practical point: junior engineers learn because maintenance hurts. Agents keep extending bad structures because they do not carry that experience forward in the same way.

That observation cuts through a lot of AI coding hype.

An agent can follow instructions. It can inspect files. It can write tests. It can create a plausible refactor plan. In the right harness, it can be genuinely useful.

But it does not look at a tangled module and remember the last time a similar module burned a release cycle. It does not feel the social cost of asking three teams to coordinate around a bad interface. It does not get embarrassed when a supposedly elegant pattern becomes a maintenance tax.

That matters because many of the best engineering decisions are acts of avoidance:

1. Avoiding an abstraction until the shape of the problem is clearer.
2. Avoiding a dependency that creates a long-term upgrade burden.
3. Avoiding a clever shortcut that the next maintainer will have to decode.
4. Avoiding a broad rewrite when a narrow repair would protect the system.
5. Avoiding a feature design that makes rollback nearly impossible.

Agents can be instructed to consider those risks. They can even list them. But listing risk is not the same as feeling accountable for it.

That is why [From Discovery to Knowledge]({{< ref "articles/discovery-to-knowledge" >}}) is the more useful frame than "which model is smartest?" Agents are excellent at revealing terrain. The human task is still turning that terrain into judgment, context, and accountable decisions.

## Why does AI-generated code feel productive while adding risk?

AI makes code generation cheap. That changes behavior.

When a developer can generate a fresh implementation in seconds, the cost of adding code drops. The cost of understanding, consolidating, and deleting code does not drop at the same rate. That is the trap.

[GitClear's 2025 AI Copilot Code Quality research](https://www.gitclear.com/ai_assistant_code_quality_2025_research) analyzed 211 million changed lines from 2020 through 2024 and found a measurable shift toward more copied code and less moved or refactored code. The headline is not that every AI-generated line is bad. The better reading is that teams are being pulled toward the path of least resistance: add more, reuse less, clean up later.

Later is where the bill arrives.

The [DORA 2026 generative AI report](https://dora.dev/ai/gen-ai-report/report/) makes a related point at the software delivery level. It reports that a 25% increase in AI adoption is associated with lower delivery throughput and lower delivery stability, with larger batch sizes as one explanation. Faster code creation can create slower review, higher instability, and more operational drag if the delivery system does not adapt.

That should sound familiar to any executive who has watched a transformation program confuse activity with progress.

More code is not the same thing as more system value. More pull requests are not the same thing as more customer value. More automation is not the same thing as more organizational capacity.

It can be the opposite.

## What does the productivity research actually say?

The evidence is mixed, which is exactly why leaders need discipline.

[METR's 2025 field study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) found that experienced open-source developers working on familiar repositories took 19% longer when AI tools were allowed, despite believing the tools had sped them up. METR later warned that those historical results no longer reflect current model impact, and its 2026 update suggests the productivity picture is changing as tools improve and adoption behavior shifts.

That nuance matters.

The wrong lesson is "AI coding tools do not work." They clearly do work in many contexts: scaffolding, test generation, small repairs, unfamiliar syntax, documentation, migration assistance, and repetitive implementation.

The other wrong lesson is "AI makes the team faster, therefore the codebase is healthier." That does not follow.

DORA's [2025 State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/) describes AI as an amplifier of the underlying organizational system. Strong teams can turn it into leverage. Weak systems can use it to produce more defects, bigger batches, and faster accumulation of unreviewed decisions.

That is the executive read.

AI does not replace engineering management. It makes engineering management more visible. If the team already has weak review discipline, poor test coverage, loose architecture ownership, and no refactoring budget, agents will not fix that. They will give the weakness more throughput.

## Where should humans stay in the loop?

Keep humans where pain, accountability, and tradeoff judgment matter.

That does not mean humans must review every generated line with equal intensity. That would waste the tool. It means leaders need to separate low-risk code production from high-risk system decisions.

Humans should own:

1. Architecture boundaries.
2. Interface design.
3. Data model changes.
4. Security and permission models.
5. Migration plans.
6. Dependency choices.
7. Rollback strategy.
8. Refactoring priorities.
9. Definition of done.

Agents can support all of those. They should not silently decide them.

The research on [technical debt in AI-enabled systems](https://doi.org/10.1016/j.jss.2024.112151) points in the same direction. Practitioners dealing with AI technical debt still rely heavily on manual review and ad hoc refactoring, especially where architecture, understandability, and security are affected. That is a signal: the harder the maintenance burden, the more human judgment remains central.

This is also why the [deterministic evals work]({{< ref "lab/deterministic-evals-for-ai-skills" >}}) matters. Teams should not ask humans to remember every rule by force of will. Move repeatable enforcement into tests, lint rules, evals, CI gates, review checklists, and release checks. Then reserve human attention for decisions the system cannot yet judge.

## What should executives change?

The answer is not "ban AI coding."

That would be lazy.

The answer is to treat AI coding as an operating-model change, not a tooling rollout. If agents lower the cost of producing code, the company must raise its standards for accepting code.

Use five rules.

1. **Measure survivability, not just output.** Track code that survives without rewrite, two-week churn, duplicated blocks, escaped defects, review cycle time, and rollback frequency. Lines added is a weak metric.

2. **Spend some of the speed on refactoring.** If agents save implementation time, allocate part of that capacity to consolidation, deletion, and simplification. Otherwise the team converts productivity into debt.

3. **Make friction deliberate.** Critical services need stronger gates: multiple reviewers, migration checklists, SLO checks, threat modeling, and rollback plans. Friction is not waste when it protects the system.

4. **Separate drafts from decisions.** Treat agent output as a draft until a responsible human approves the architecture, interface, test strategy, and operational impact.

5. **Codify pain.** When a production incident or maintenance failure teaches the team something, turn it into a rule, eval, checklist, test, or design constraint. Do not leave the lesson trapped in one engineer's memory.

That last point is the whole game.

Human pain becomes organizational advantage only when the company captures it. Otherwise the same lesson gets relearned every quarter by a different team at a higher cost.

## What is the real role of the senior engineer now?

The senior engineer is no longer just the person who can write the hardest code.

The senior engineer is the person who can protect the system from cheap code.

That role becomes more important, not less, as agents improve. Better agents will produce more plausible work at higher speed. They will make it easier for weak ideas to look finished. They will also make strong engineers far more effective when the surrounding system is disciplined.

This is the same point behind [Moats in the Era of Vibe Coding]({{< ref "articles/moats-vibe-coding" >}}). When software creation gets cheaper, durable advantage moves to the constraints around the code: judgment, workflow depth, proprietary context, distribution, trust, and operating discipline.

For engineering teams, that means the scarce asset is not typing speed. It is taste under pressure.

A strong engineer knows when the code is too clever. They know when the abstraction is premature. They know when a shortcut will turn into a support burden. They know when the agent gave a technically correct answer to the wrong question.

They know because they have felt the pain before.

Agents do not.

So use them. Let them draft, scaffold, test, search, migrate, and accelerate the work.

But do not mistake output for judgment.

The future of software engineering is not humans versus agents. It is humans teaching the system which kinds of pain are worth avoiding before the codebase has to learn it the expensive way.

{{< faq >}}
  {{% faq-item question="Do AI coding agents create technical debt?" %}}
  AI coding agents can create technical debt when teams accept generated code without enough review, refactoring, testing, and architectural discipline. The risk is not that every generated line is poor. The risk is that code generation gets cheaper than understanding and consolidating the system.
  {{% /faq-item %}}
  {{% faq-item question="Why is human judgment still important in agentic coding?" %}}
  Human judgment matters because software quality depends on future tradeoffs: maintainability, operational risk, interface clarity, migration safety, security, and organizational accountability. Agents can assist with those decisions, but humans carry the consequences when the system breaks.
  {{% /faq-item %}}
  {{% faq-item question="How should engineering leaders manage AI-generated code?" %}}
  Engineering leaders should treat AI output as a draft, not a final answer. They should track churn and duplication, require stronger gates for high-risk changes, preserve refactoring capacity, and codify lessons from incidents into tests, evals, and review rules.
  {{% /faq-item %}}
{{< /faq >}}

*Featured image source: <a href="https://pixabay.com/users/51581-51581/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1627703">51581</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1627703">Pixabay</a>.*

{{< related-posts title="Related Insights" paths="articles/the-next-compiler, articles/discovery-to-knowledge" >}}

{{< read-next title="Read Next" link="articles/moats-vibe-coding" buttonText="View More Insights" buttonLink="/articles/" >}}
