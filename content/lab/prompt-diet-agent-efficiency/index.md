---
title: "The Prompt Diet: How We Chopped 57% of Our Agent's Mind and Made It Smarter"
date: 2026-06-22
summary: "A Lab entry on reducing agent prompt overhead by moving 57 percent of instruction logic into deterministic scripts, cutting token waste while improving reliability."
description: "This technical deep dive explains why autonomous coding agents become expensive when they re-read large markdown playbooks on every loop, and how I reduced that overhead by translating repeatable instructions into deterministic code."
categories:
  - Technology
tags:
  - artificial-intelligence
  - software-engineering
  - systems-thinking
  - productivity
  - programming
showReadingTime: true
showTableOfContents: true
draft: false
status: agent-pending
about:
  - name: "Prompt engineering"
    url: "https://en.wikipedia.org/wiki/Prompt_engineering"
mentions:
  - name: "Context window"
    url: "https://en.wikipedia.org/wiki/Context_window"
  - name: "ReAct"
    url: "https://arxiv.org/abs/2210.03629"
citations:
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    url: "https://arxiv.org/abs/2210.03629"
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    url: "https://arxiv.org/abs/2307.03172"
---

Every time an autonomous coding agent loops to inspect a bug, write a test, or run a linter, it has to reacquire its working context. If too much of that context lives in long markdown playbooks, the agent ends up spending real money re-reading its own operating manual before it does any useful work.

I hit that wall in one of my own agent setups and took a different path: I moved 57 percent of the instruction load out of prompt text and into deterministic scripts. The result was not just lower token cost. It was a cleaner architecture, faster loops, and a more disciplined boundary between reasoning and enforcement.

{{< quick-answer >}}
If an AI agent repeats a multi-step loop, every instruction token you leave in markdown gets paid for again and again. I reduced that recurring tax by translating repeatable prompt logic into deterministic scripts, which cut prompt overhead by 57 percent and improved both reliability and focus.
{{< /quick-answer >}}

## Why does prompt bloat become expensive in agent loops?

AI agents rarely operate in a single pass. In practice, they run a repeated cycle: reason, act, observe, repeat. For a normal coding task, that can mean 15 to 20 iterations before the work is actually done.

That loop structure changes the economics of prompt design. A 3,000-token instruction block is not paid once. It is paid every time the model re-enters the loop. If the agent needs 15 steps to finish a task, that static instruction payload alone consumes 45,000 input tokens before the model has even accounted for the repo state, tool outputs, or the actual problem.

This is the hidden tax in many early agent systems. We optimize for cognitive flexibility and forget that repeated context is infrastructure cost.

## What did I actually move out of the prompt?

I did not remove the model's ability to reason. I removed the parts of the workflow that never should have relied on probabilistic interpretation in the first place.

The pattern was simple: if a task could be enforced with code, I stopped describing it in prose and started encoding it directly in scripts.

That included things like:

1. Syntax and structure validators.
2. Regex-based formatting checks.
3. Git workflow steps with predictable branching logic.
4. Content and file-path compliance checks.
5. [Reusable evaluation runners]({{< relref "lab/deterministic-evals-for-ai-skills" >}}) that return binary pass or fail outcomes.

Once those responsibilities moved into deterministic tools, the markdown prompt stopped acting like an overgrown policy binder. It became a thinner strategic layer that tells the model how to think, not how to imitate a shell script.

## How does the math of the 57% reduction work?

The savings look modest if you view them at the level of a single prompt. They look meaningful once you model them across repeated iterations and production volume.

The formula is straightforward:

```text
tokens saved = (total instruction tokens x 0.57) x number of loop iterations
```

Using the workload from this experiment:

1. Original instruction block: 3,000 tokens.
2. Reduction moved into code: 57 percent.
3. Tokens saved per loop: 1,710.
4. Example task length: 15 iterations.

That means a single 15-step task avoids:

```text
1,710 x 15 = 25,650 input tokens
```

The remaining instruction load drops to 1,290 tokens per call, or 19,350 tokens across the same 15-step task.

At scale, the effect compounds:

1. 10,000 tasks x 25,650 saved tokens each = 256,500,000 input tokens avoided.
2. At $3.00 per million input tokens, that is roughly $769.50 in direct savings.

The dollar amount matters, but the more important point is architectural: repeated prompt waste behaves like operational drag. Once you can see it, you stop treating prompt length as free.

## Why did deterministic scripts make the agent more reliable?

Because code enforces rules more cleanly than natural language.

When I ask a model to "make sure the file path follows the correct structure" or "format the output exactly like this," I am still asking a stochastic system to simulate compliance. It may do that well, but it is still simulation.

A script changes the contract.

1. The rule becomes executable.
2. The output becomes measurable.
3. Failure becomes explicit.
4. The model gets concrete feedback instead of vague instruction.

This is especially important in multi-tool agents. The model should spend its reasoning budget on diagnosis, prioritization, tradeoffs, and synthesis. It should not waste attention pretending to be a linter, a path validator, or a git policy engine.

In practice, this also reduced context drift. Smaller prompts meant less irrelevant instruction mass competing with the actual task. That aligns with the broader long-context problem documented in research such as [Lost in the Middle](https://arxiv.org/abs/2307.03172), where relevant information becomes harder for models to use consistently as context grows and attention gets diluted.

## What changed beyond cost?

The biggest gain was not financial. It was conceptual clarity.

Once I moved repeatable enforcement into code, the agent architecture started to separate into cleaner layers:

1. The prompt handled judgment, prioritization, and tone.
2. The tools handled deterministic enforcement.
3. The evals handled quality gates.
4. The loop became easier to inspect and improve.

That is a healthier design pattern than asking the model to carry the whole system in-language.

It also changes how I think about scaling autonomous agent fleets. If every agent must repeatedly ingest a bloated rulebook, scale multiplies waste. If the rulebook becomes a compact reasoning layer sitting on top of hardened utilities, scale starts to look much more like software engineering and much less like prompt theater.

## What is the practical design rule I took away from this?

I now use a simple standard when designing agent systems:

> Never use a non-deterministic LLM prompt to solve a problem that can be handled by a few lines of deterministic code.

This does not mean prompts stop mattering. It means prompt design matures when it becomes more selective. The goal is not to make the model responsible for everything. The goal is to reserve the model for the parts of the system that genuinely benefit from abstraction, synthesis, and judgment.

Longer prompts can make an agent feel sophisticated. Better system boundaries make it actually useful.

## Where does this lead next?

I think this is where a lot of agent engineering is heading: away from giant instruction monoliths and toward thinner cognitive layers wrapped around hardened execution primitives.

The next frontier is not just better prompting. It is better decomposition:

1. Which instructions belong in the model?
2. Which belong in evaluators?
3. Which belong in tooling?
4. Which should be deleted altogether?

That is the shift from building demos to building operating systems.

{{< faq >}}
  {{% faq-item question="Why does reducing prompt size matter if models already support long context?" %}}
  Long context does not mean free context. Bigger prompts still increase cost, latency, and the risk that important instructions get diluted by less important text. In looping agents, those costs recur every time the model re-enters the workflow.
  {{% /faq-item %}}
  {{% faq-item question="What kinds of instructions should move into deterministic scripts first?" %}}
  I start with anything that has a binary outcome: syntax checks, path rules, output formatting, workflow gates, and validation logic. If a script can verify it reliably, I prefer code over prose.
  {{% /faq-item %}}
  {{% faq-item question="Does the prompt diet make the agent less flexible?" %}}
  It reduces unnecessary flexibility, which is usually a benefit. The model still handles reasoning and adaptation, but it no longer has to simulate precision for tasks that software can enforce directly.
  {{% /faq-item %}}
{{< /faq >}}

{{< related-posts title="Related Insights" paths="lab/chalk-circle, lab/pyenv" >}}

{{< read-next title="Read Next" link="lab/margo" buttonText="View more Deep Dives" >}}
