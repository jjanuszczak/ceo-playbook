---
title: "Agent vs. Harness: The Executive Explanation"
date: 2026-07-27T09:03:16+08:00
summary: "An executive-friendly explanation of why an AI agent is the running goal-seeking process, while the harness is the runtime that hosts the loop, tools, memory, permissions, and state."
description: "A practical Lab explainer for executives and board members: what an AI agent is, what a harness does, why Codex, Claude Code, Pi, and LangGraph sit at different layers, and how to avoid misreading infrastructure as autonomy."
categories:
  - Technology
tags:
  - artificial-intelligence
  - software-engineering
  - systems-thinking
  - dev-ops
  - open-source
showReadingTime: true
showTableOfContents: true
draft: true
status: agent-pending
about:
  - name: "Intelligent agent"
    url: "https://en.wikipedia.org/wiki/Intelligent_agent"
mentions:
  - name: "Software framework"
    url: "https://en.wikipedia.org/wiki/Software_framework"
  - name: "Model Context Protocol"
    url: "https://modelcontextprotocol.io/docs/learn/architecture"
citations:
  - title: "A practical guide to building agents"
    url: "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/"
  - title: "Agents, OpenAI Agents SDK"
    url: "https://openai.github.io/openai-agents-python/agents/"
  - title: "Building effective agents"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
  - title: "Architecture overview, Model Context Protocol"
    url: "https://modelcontextprotocol.io/docs/learn/architecture"
  - title: "LangGraph overview"
    url: "https://docs.langchain.com/oss/python/langgraph/overview"
  - title: "pi-team-harness"
    url: "https://pi.dev/packages/pi-team-harness"
---

Executives do not need another fuzzy AI term. They need a clean operating distinction.

An agent is the running process that owns a goal. A harness is the runtime that gives that process a place to live, a loop to run, tools to use, state to keep, permissions to respect, and logs to leave behind.

{{< quick-answer >}}
An AI agent is the goal-seeking process: it reasons, chooses tools, observes results, and continues until it finishes or stops. The harness is the surrounding runtime that hosts that process, manages tool execution, memory, state, permissions, context, and recovery. A harness can run agents, but it is not automatically an agent itself.
{{< /quick-answer >}}

## Why does this distinction matter?

The agent-versus-harness boundary matters because it changes how you assign accountability.

If the system fails, did the model make a bad decision? Did the tool return bad data? Did the permissions layer block a necessary action? Did the context management fail? Or did the workflow have no proper stopping condition?

Those are not academic questions. They are board-level questions once an AI system starts touching code, customers, contracts, financial operations, or regulated workflows.

OpenAI's agent guide frames agents as systems that accomplish tasks on a user's behalf with a high degree of independence, using an LLM to manage workflow execution and tools to act on external systems. [Anthropic draws a useful distinction](https://www.anthropic.com/engineering/building-effective-agents) between workflows, where code follows predefined paths, and agents, where the LLM dynamically directs its own process and tool use.

That gives us the executive version:

1. **The agent owns the loop.**
2. **The harness hosts the loop.**
3. **The tools and protocols extend what the loop can touch.**

Confuse those layers and you end up buying demos. Separate them and you can ask practical diligence questions.

## What is an agent?

An agent is a running process, or a logical process, that carries a goal across multiple steps.

It typically does five things:

1. Holds an objective.
2. Maintains or retrieves state.
3. Reasons about the next move.
4. Acts through tools, APIs, files, browsers, shells, or other systems.
5. Observes the result and decides whether to continue, stop, retry, or ask for help.

The key feature is not that an LLM produced text. The key feature is control over execution.

OpenAI's Agents SDK makes this boundary concrete: an agent is an LLM configured with instructions, tools, handoffs, guardrails, and structured outputs, while the SDK runner manages turns, tools, guardrails, handoffs, and sessions. In other words, the agent is the configured decision-maker. The runner and surrounding SDK machinery are the harness layer.

The old ReAct pattern captured the same operating rhythm: reasoning and acting interleave, actions produce observations, and those observations shape the next step. Modern agents add stronger tooling, persistence, guardrails, sandboxing, and recovery, but the basic loop is still there.

## What is a harness?

A harness is the runtime infrastructure around the agent.

It may provide:

1. The agent loop.
2. Tool dispatch.
3. Context-window management.
4. Memory and session persistence.
5. Sandboxing and permissions.
6. Human approval gates.
7. Logging, tracing, and evaluations.
8. Extension, skill, and prompt-loading systems.

The harness is not the same thing as the model. It is not the same thing as a tool. It is the operating environment that makes the model useful as a process rather than a single answer generator.

The [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture) is a good example of a supporting infrastructure layer. MCP defines a host-client-server architecture where an AI application can connect to servers that expose tools, resources, and prompts. MCP does not decide the business goal by itself. It gives the host application a structured way to add context and actions.

LangGraph gives another clean example. Its documentation describes LangGraph as an orchestration runtime for durable execution, streaming, human-in-the-loop control, and persistence. LangGraph can support agents, but the runtime capabilities are not the same as the agent's goal ownership.

## Is the harness an outer agent?

Usually, no.

Calling the harness an "outer agent" sounds intuitive because the harness sits around the agent. But that framing creates confusion. The harness may launch the loop, load skills, enforce tool permissions, save state, and resume sessions. Those are infrastructure responsibilities.

An outer agent exists only when another goal-seeking process is actually making decisions above the first one.

For example:

1. A manager agent can delegate work to specialist agents.
2. A triage agent can hand off a customer case to a refund agent.
3. A lead coding agent can ask reviewer and test agents to inspect separate parts of a change.

In those cases, the outer layer is an agent because it owns a goal and makes decisions. The harness underneath still hosts the runtime.

Pi makes the distinction visible. The `pi-team-harness` package turns a Pi session into a team lead over specialist agents on a shared message bus. That package is harness infrastructure: commands, extensions, guards, message transport, worktrees, and finalization flow. The team lead behavior running inside it is the agentic process.

## How should executives think about Codex, Claude Code, Pi, and LangGraph?

The clean framing is this:

| System | Practical role |
| --- | --- |
| Codex, Claude Code, Cursor agent mode, Pi | Product harnesses that host coding-agent processes |
| LangGraph | Orchestration runtime for durable, stateful agent workflows |
| MCP | Protocol layer for tools, resources, prompts, and context exchange |
| Skills and extensions | Packaged capabilities loaded into a harness |
| The model | Reasoning engine used by the agent |
| The agent | The running goal owner using the model, harness, and tools |

This is why "Agent = Model + Harness" works as a boardroom shorthand, even though engineers will quickly add more detail. The model alone is not enough. The harness alone is not enough. The agent appears when a model operates inside a runtime that lets it pursue a goal across steps.

That distinction also clarifies [the difference between agents and skills]({{< relref "lab/agents-vs-skills" >}}). A skill can contain scripts, references, and validations. It can look sophisticated. But unless it owns the outer goal and decides what to do next across an open horizon, it is still a capability loaded into the agent's environment.

## What questions should leaders ask before approving an agent system?

The question is not, "Do we have an agent?"

That is too easy to answer with marketing language. Ask these instead:

1. **What goal does the agent own?** If the answer is vague, the system is not ready for autonomy.
2. **What does the harness control?** Look for tools, state, permissions, context, logs, and recovery.
3. **Where are the stopping conditions?** A useful agent knows when to finish, escalate, or halt.
4. **Which actions require human approval?** High-risk actions should not hide behind vague automation language.
5. **How do we test the harness?** Tool calls, permission checks, and output gates should have deterministic tests where possible.
6. **How do we inspect failures?** Logs should show what the agent tried, what the environment returned, and why the loop continued.

That last point matters. [Deterministic evaluations]({{< relref "lab/deterministic-evals-for-ai-skills" >}}) are not bureaucracy. They are the operating discipline that keeps the harness honest. My own [prompt-diet experiment]({{< relref "lab/prompt-diet-agent-efficiency" >}}) reached the same conclusion from the cost side: put fixed rules in code, leave judgment to the agent, and stop paying the model to simulate enforcement.

## What is the clean mental model?

Think in layers:

1. **Model:** the reasoning engine.
2. **Agent:** the goal-seeking process that uses the model.
3. **Harness:** the runtime that hosts the process.
4. **Tools and protocols:** the external capabilities the process can use.
5. **Policies and evaluations:** the boundaries that keep the system accountable.

The harness is not a decorative wrapper. It is where most of the operational risk lives. A weak harness turns a capable model into an unsafe operator. A strong harness turns model capability into inspectable software.

That is the real point for executives and boards. Do not approve "AI agents" as a category. Approve a specific agent, running inside a specific harness, with specific tools, specific permissions, specific logs, and specific stopping conditions.

{{< faq >}}
  {{% faq-item question="Is an agent just an LLM with tools?" %}}
  Not quite. Tools are necessary for many agents, but the defining feature is goal-directed control across steps. A chatbot can call a tool once without becoming a meaningful agent. An agent uses tools inside a loop and decides what to do after each observation.
  {{% /faq-item %}}
  {{% faq-item question="Can a harness create and run agents?" %}}
  Yes. A harness such as Pi, Codex, Claude Code, or a LangGraph-based runtime can define, configure, host, and run agent processes. The harness supplies the operating environment. The agent is the goal-seeking process running inside it.
  {{% /faq-item %}}
  {{% faq-item question="When is a harness also an agent?" %}}
  Only when the outer layer is itself making goal-directed decisions. A manager that delegates to specialist agents is an agent. A runtime that loads tools, enforces permissions, and stores state is infrastructure, even if it is sophisticated.
  {{% /faq-item %}}
{{< /faq >}}

Featured image source: <a href="https://pixabay.com/users/Pexels-2286921/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1853330">Pexels</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1853330">Pixabay</a>

{{< related-posts title="Related Insights" paths="lab/agents-vs-skills, lab/deterministic-evals-for-ai-skills" >}}

{{< read-next title="Read Next" link="lab/agents-vs-skills" buttonText="View more Deep Dives" >}}
