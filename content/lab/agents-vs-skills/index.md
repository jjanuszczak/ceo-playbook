---
title: "Agents vs. Skills: Ownership, Scope, and the Blurring Line"
date: 2026-07-25
draft: false
summary: "Agents own outcomes across an open-ended loop. Skills package reusable procedures for bounded work, even when those procedures contain scripts, retries, and evaluations."
description: "A practical architecture guide to separating agents from skills: who owns the goal, where orchestration belongs, why sophisticated skills can look agentic, and how modular skills make AI systems easier to test and improve."
categories:
  - Technology
tags:
  - artificial-intelligence
  - systems-thinking
  - software-engineering
  - knowledge-management
  - taxonomy
showReadingTime: true
showTableOfContents: true
status: agent-pending
about:
  - name: "Intelligent agent"
    url: "https://en.wikipedia.org/wiki/Intelligent_agent"
mentions:
  - name: "Agent Skills"
    url: "https://agentskills.io/specification"
  - name: "Software architecture"
    url: "https://en.wikipedia.org/wiki/Software_architecture"
citations:
  - title: "Agent Skills Specification"
    url: "https://agentskills.io/specification"
---

In the current generation of LLM systems, people often use "agent" and "skill" as if they mean the same thing. They do not. The distinction matters when the objective is a reliable, maintainable operating system rather than a convincing demo.

An agent owns a goal. A skill packages the repeatable procedure for one bounded part of achieving it. The words can blur in practice, but keeping the ownership boundary clear makes systems easier to test, reuse, and improve.

{{< quick-answer >}}
An agent owns the outer loop: it decides what outcome to pursue, which capabilities to use, what to do after each result, and when the objective is complete. A skill is a modular, reusable playbook for a defined class of work. It can contain scripts, retries, and evaluations without taking ownership of the broader goal.
{{< /quick-answer >}}

## What is the core difference between an agent and a skill?

An agent is the system that owns the outcome. It runs the outer loop: perceive, reason, decide, act, observe, then decide whether to continue. It maintains or accesses state across steps, selects capabilities, and stays accountable for progress when the work crosses domains.

A skill is a reusable package of procedural knowledge for a specific class of task. In the emerging open format, that usually means a directory anchored by a `SKILL.md`, with optional scripts, templates, references, and evaluation criteria. The format is deliberately modular: instructions are loaded when relevant, while supporting resources are pulled in only when needed. [The Agent Skills specification](https://agentskills.io/specification) documents that structure.

The useful shorthand is simple: the agent is the director; the skill is a specialized playbook the director can use.

## Why do the lines blur in production systems?

The line starts to blur once a skill gains real operational depth. A skill may contain:

1. Executable scripts and tool calls.
2. Multi-step workflows with conditional branches.
3. Retry and recovery logic.
4. Internal evaluation loops and termination checks.

At that point, the skill can orchestrate a substantial amount of work inside a narrow boundary. It may recover from intermediate failures and produce consistent output without forcing the calling agent to manage every detail.

That is not a design problem. It is the point of a well-built skill. It externalizes the how, so the agent does not need to rediscover a reliable procedure every time it meets a familiar task.

The distinction is clearer if we separate judgment from enforcement. In [a practical prompt-design experiment]({{< relref "lab/prompt-diet-agent-efficiency" >}}), I argued that deterministic requirements belong in code whenever possible. Skills are a natural home for that code, validation, and local control flow. The agent should keep its attention on the wider decision: whether this is the right workflow, whether its output changes the plan, and what comes next.

## Who owns the goal when a skill has its own loop?

The owner of the outer loop is still the agent.

Even a sophisticated skill does not decide whether the wider objective remains worthwhile, whether another capability should run next, or whether the system must change course across an arbitrary horizon. It executes because the agent invoked it for a scoped purpose.

Three questions keep the boundary sharp:

1. **How wide is the scope?** A skill handles a defined class of work. An agent can compose skills, tools, and human decisions across domains.
2. **Who decides when to start and stop?** A skill can terminate its internal workflow. The agent decides whether the overall objective has been met.
3. **Can the procedure stand alone?** Skills should be versioned, evaluated, shared, and improved independently. The agent is the coordinator that assembles them for a specific outcome.

The difference resembles a microservice and the application that calls it. A service can have retries, a state machine, and monitoring. It remains a component. The application owns the business objective and coordination across components.

> [!NOTE]+ Codex and Claude are Agents
> If you are using Codex on a repo and ask it to generate some code using a skill (in the repo or gloablly defined), **Codex is the owner of the outer loop** and is therefore the agent!

## What does the distinction look like in practice?

Consider three levels of complexity.

### A narrow skill

"Generate a compliant promotional video script under our brand rules."

The skill contains the required structure, tone, length constraints, and a small validation script. The agent recognizes the task, activates the playbook, evaluates the result, and moves on.

### A richer skill that looks agent-like

"Analyze customer churn and produce an executive summary."

This skill may load data, handle data-quality failures, choose among analytical branches, retry an API call, run a checklist, and format the final report. It orchestrates internally, but it remains a skill because a higher-level retention agent decides that churn analysis is needed, combines the conclusion with pricing or outreach work, and evaluates the wider retention goal.

### An agent

"Improve next-quarter retention for segment X."

The agent decomposes the objective, selects churn analysis, pricing experiments, and outreach sequencing as needed, retains state across each step, and adapts when results conflict with the plan. It may decide a missing workflow deserves a new or revised skill. That broad ownership is the defining feature.

## Why does the boundary matter for system design?

Calling every component an agent creates monolithic systems that are difficult to test, share, and maintain. Calling reusable procedures skills creates a library of operational knowledge with clear interfaces and local success criteria.

The agent layer can then focus on the work that actually needs broad judgment: goal decomposition, sequencing, cross-skill coordination, tradeoffs, and accountability. The skill layer can focus on repeatable execution. [Deterministic evaluations]({{< relref "lab/deterministic-evals-for-ai-skills" >}}) make that separation stronger by turning fixed requirements into measurable quality gates.

This also makes system ownership explicit. A skill can be upgraded without changing the agent's mandate. An agent can choose a different skill without rebuilding the entire system. Teams can inspect where a failure occurred: in the goal, the orchestration, the procedure, or the tool.

The practical design question is not, "Is this agentic?" Ask instead: who owns the goal, how wide is the scope, and can this knowledge be reused and improved independently? That separation of concerns is what turns a collection of clever prompts into software engineering.

## Summary

A skill can possess agent-like internals. The key remaining difference is usually one of *scope, ownership, and composition*, not raw technical capability:

| Aspect                  | Skill (even a sophisticated one)                  | Agent                                      |
|-------------------------|---------------------------------------------------|--------------------------------------------|
| **Scope**               | Narrow, task-class specific, bounded              | Open-ended, goal-oriented                  |
| **Ownership**           | Invoked and supervised by something else          | Owns the top-level goal and decision to continue |
| **State & memory**      | Usually local / ephemeral to the skill run        | Persistent across skills and sessions      |
| **Composition**         | Designed to be loaded, composed, or swapped       | Decides *which* skills to load and in what order |
| **Initiation**          | Reactive (triggered when relevant)                | Proactive (pursues a goal autonomously)    |
| **Reusability**         | Highly modular and shareable across agents        | The system that uses the modules           |

{{< faq >}}
  {{% faq-item question="Can a skill use tools, retries, and evaluations without becoming an agent?" %}}
  Yes. Those features make a skill more capable within its defined scope. The agent remains responsible for choosing when to invoke it, interpreting its result in the wider plan, and deciding when the overall objective is complete.
  {{% /faq-item %}}
  {{% faq-item question="Should every agent capability become a separate skill?" %}}
  No. Extract a skill when the procedure is bounded, repeatable, and worth reusing or evaluating independently. One-off reasoning and cross-domain prioritization belong with the agent that owns the outcome.
  {{% /faq-item %}}
  {{% faq-item question="What is the simplest test for the boundary?" %}}
  Ask who can change the objective. If a component only executes a defined procedure and reports its result, it is a skill. If it can redefine the plan, select other capabilities, and continue toward an open-ended outcome, it is acting as the agent.
  {{% /faq-item %}}
{{< /faq >}}

Featured image source: <a href="https://pixabay.com/users/mrhà-49741683/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=10258355">Mr Hà</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=10258355">Pixabay</a>

{{< related-posts title="Related Insights" paths="articles/architecture-of-attention, lab/deterministic-evals-for-ai-skills" >}}

{{< read-next title="Read Next" link="lab/ai-glossary" buttonText="View more Deep Dives" >}}
