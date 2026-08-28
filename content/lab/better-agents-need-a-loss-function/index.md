---
title: "Better Agents Need a Loss Function"
date: 2026-08-28T09:03:12+08:00
summary: "A practical Lab memo on turning agent feedback into a measurable loss function, using a scheduling agent as the working example."
description: "A follow-up to Reliable Agents Need Contracts, Not Better Prompts: how to instrument outcomes, define a loss function, and use feedback loops to improve the judgment layer of workflow agents."
categories:
  - Technology
tags:
  - artificial-intelligence
  - software-engineering
  - systems-thinking
  - productivity
  - dev-ops
showReadingTime: true
showTableOfContents: true
draft: true
status: agent-pending
about:
  - name: "Intelligent agent"
    url: "https://en.wikipedia.org/wiki/Intelligent_agent"
mentions:
  - name: "Evaluation"
    url: "https://en.wikipedia.org/wiki/Evaluation"
  - name: "Contextual bandit"
    url: "https://en.wikipedia.org/wiki/Multi-armed_bandit#Contextual_bandit"
  - name: "Software testing"
    url: "https://en.wikipedia.org/wiki/Software_testing"
citations:
  - title: "Reliable Agents Need Contracts, Not Better Prompts"
    url: "https://januszczak.org/lab/developing-effective-agents/"
  - title: "Demystifying evals for AI agents"
    url: "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
  - title: "Building effective agents"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
  - title: "OpenAI Agents SDK"
    url: "https://openai.github.io/openai-agents-python/"
  - title: "OpenAI Agents SDK Guardrails"
    url: "https://openai.github.io/openai-agents-python/guardrails/"
  - title: "OpenAI Evals API Reference"
    url: "https://platform.openai.com/docs/api-reference/evals"
  - title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
    url: "https://arxiv.org/abs/2406.12045"
---

In [part one]({{< ref "lab/developing-effective-agents" >}}), I argued that reliable agents need contracts, not better prompts. That solves the first failure mode: the agent stops guessing about records, tools, permissions, and policy.

But a contract only tells the agent what it is allowed to do.

It does not tell the agent whether its judgment is improving.

A scheduling agent makes the gap obvious. The deterministic layer can prove that a proposed meeting time is valid, inside policy, correctly converted across time zones, and safe to send. That is necessary. It is not enough. The better question is whether the proposed time actually worked: did people accept it, counter it, move it, ignore it, or quietly resent it?

That outcome is the training signal.

{{< quick-answer >}}
Workflow agents improve when you separate hard constraints from learned judgment. Keep availability checks, policy gates, time-zone math, and external writes deterministic, then grade the judgment layer against real outcomes such as acceptance, counter-proposals, reschedules, delay, and explicit user feedback. The practical pattern is to instrument every attempt, compute a loss, and use that loss to tune retrieval, prompts, evals, ranking, or model training.
{{< /quick-answer >}}

## Why do agent contracts still need outcomes?

A contract can keep an agent inside the lines. It cannot prove the agent made the best call.

For a scheduler, the hard rules are clear:

1. Do not propose a slot that conflicts with a required participant.
2. Do not cross a protected sleep window.
3. Do not invent attendee emails or meeting links.
4. Do not book anything without authority.
5. Do not mutate an external calendar without a read-back check.

Those rules belong in code. The model should not simulate calendar math in prose.

The judgment problem sits one layer above that. Among all feasible slots, which one should the agent recommend first? Should it favor the organizer's usual preference, the client's local morning, the shortest confirmation path, or the least disruptive option across the week?

That is no longer a binary validation problem. It is a ranking problem with delayed feedback.

This is where many agent builds stall. They add more tools, longer prompts, and more elaborate reasoning instructions, but never define what "better" means after the agent acts. The result is a system that can pass deterministic tests and still make poor operational calls.

## What should the agent log?

Start with the trajectory, not the prompt.

Anthropic's 2026 eval guidance makes a useful distinction between a transcript or trajectory and the final outcome. The transcript records the agent's turns, tool calls, intermediate results, and reasoning context. The outcome is the actual end state in the environment. For a scheduling agent, the outcome is not "the agent said the meeting was proposed." The outcome is whether the meeting stuck.

For every scheduling attempt, log a compact event trail:

```text
scheduling_session_id
request_summary
participant_set
meeting_type
duration
urgency
explicit_constraints
derived_constraints
available_candidate_slots
ranked_proposed_slots
agent_scores
policy_checks
approval_state
proposal_sent_at
final_calendar_state
outcome_events
```

The important part is delayed outcomes:

1. Did all required attendees accept the proposed slot?
2. How many counter-proposals arrived?
3. How far was the final slot from the original recommendation?
4. How long did confirmation take?
5. Did the organizer later move the meeting?
6. Did the meeting produce a no-show, early end, or follow-up reschedule?
7. Did the user explicitly rate the suggestion?

Store those events immutably. Postgres plus JSONB is enough for most teams at the start. An event store is better if the agent is already part of a broader workflow platform. The technical choice matters less than the discipline: every recommendation needs an ID, every outcome needs to attach back to that ID, and missing outcomes need timeout rules.

## What does a useful loss function look like?

The loss function converts messy workflow reality into a signal the system can optimize.

For a scheduler, a simple first version can look like this:

```text
loss =
  4.0 * not_confirmed
+ 1.5 * counter_count
+ 3.0 * rescheduled
+ 1.0 * delay_hours_normalized
+ 2.0 * preference_violation
+ 1.0 * timezone_friction
+ 2.0 * fairness_penalty
```

Lower is better.

The weights are not sacred. They are the first management decision in the system. A CEO scheduling investor calls may care most about fast confirmation and avoiding late-night calls. A sales team may accept more counters if the proposed slot improves buyer attendance. A support team may prioritize SLA response windows.

This is why the loss breakdown matters. Do not only log the final score. Log the components.

```json
{
  "session_id": "sched_2026_08_28_0915",
  "not_confirmed": 0,
  "counter_count": 1,
  "rescheduled": 0,
  "delay_hours_normalized": 0.35,
  "preference_violation": 0,
  "timezone_friction": 0.4,
  "fairness_penalty": 0.2,
  "loss": 2.45
}
```

That breakdown tells you what is actually failing. If confirmation is high but delay is poor, the agent is proposing acceptable times too slowly. If counters are high, the ranking policy is misreading preferences. If fairness penalties climb, the system may be quietly favoring the organizer at the cost of external participants.

Without the breakdown, the team debates vibes.

## Which parts should stay deterministic?

The loss function should not weaken the contract from part one. It should sit on top of it.

Keep these as hard gates:

1. Calendar availability.
2. Time-zone conversion.
3. Sleep and reserved blocks.
4. Approval requirements.
5. Event schema conversion.
6. Attendee identity validation.
7. Read-back reconciliation.
8. Audit-log completeness.

OpenAI's guardrail model is useful here because it separates checks by workflow boundary: input guardrails, output guardrails, and tool guardrails. For workflow agents with side effects, tool guardrails are the critical layer because they can validate or block custom tool calls before and after execution.

The learned policy should only rank feasible options. It should not be allowed to discover that policy violations sometimes produce better short-term scores. That is how optimization turns into organizational damage.

The boundary is simple:

```text
deterministic layer: what is allowed?
judgment layer: what is best among allowed options?
outcome layer: did the judgment work?
```

## How do you close the learning loop?

There are three practical levels. Start with the cheapest one.

### Level 1: retrieval and prompt updates

Keep a retrieval index of prior scheduling attempts:

```text
state summary -> proposed slots -> outcome score -> notes
```

At runtime, retrieve similar high-performing cases and inject them as compact examples. When the agent sees a new cross-time-zone investor meeting, it can compare against past cases where similar stakeholders accepted quickly.

Batch the failures. Once a week, cluster low-scoring sessions and ask what rule or example would have prevented them. Some fixes become prompt edits. Some become deterministic checks. Some become new eval fixtures. This is the same operating logic behind [the prompt diet]({{< ref "lab/prompt-diet-agent-efficiency" >}}): keep judgment in the model, but move repeatable enforcement and reusable lessons into thinner, testable system components.

This already creates improvement without fine-tuning.

### Level 2: evals and regression suites

Use real failures to create test cases.

Anthropic's eval guidance recommends turning manual checks and user-reported failures into tasks with clear success criteria. That advice maps directly to workflow agents. If the agent repeatedly proposes late calls for Manila-based operators, write an eval. If it overweights the organizer's calendar against external participants, write an eval. If it books before approval, that is not an eval nuance. That is a hard failure.

OpenAI's Evals API supports structured eval definitions, data sources, graders, and repeated runs against model configurations. Whether you use a platform API or a local runner, the principle is the same: keep a stable bank of cases that protects the system from backsliding.

For this scheduler, I would track:

1. Confirmation rate.
2. Counter-proposals per session.
3. Time to confirmation.
4. Reschedule rate.
5. Policy violation rate.
6. User override rate.
7. Cost and latency per completed session.

Capability evals answer, "Can the agent improve this hard scenario?" Regression evals answer, "Did the agent break behavior that already worked?"

You need both.

### Level 3: preference data, ranking, and fine-tuning

Once you have enough labeled trajectories, build preference pairs:

```text
same input state
proposal A: lower loss
proposal B: higher loss
```

Those pairs can train a ranking model, tune the prompt examples, or support preference fine-tuning. If the system can safely propose multiple candidate slots and later observe which one the user chose or accepted, the problem starts to resemble a contextual bandit: choose an action under constraints, observe delayed reward, update the policy.

Do not start here. Most teams do not have enough clean data, and they usually have unresolved contract problems underneath.

Start by logging. Then score. Then retrieve. Then test. Only then train.

## What does the architecture look like?

The operating model is straightforward:

{{< mermaid >}}
flowchart TD
    A["User request"] --> B["Parse intent"]
    B --> C["Apply deterministic constraints"]
    C --> D["Generate feasible slots"]
    D --> E["Rank with judgment policy"]
    E --> F["Send proposal or request approval"]
    F --> G["Collect delayed outcomes"]
    G --> H["Compute loss components"]
    H --> I["Update retrieval, evals, and ranking policy"]
    I --> E
{{< /mermaid >}}

The dashboard should not be complicated. Track the loss components over time and drill into the sessions behind each spike. The agent is not "learning" because a slide says it has memory. It is learning when the organization can see a bad outcome, trace it to the decision that caused it, encode the lesson, and prove the next version performs better.

This also connects to [deterministic evals for AI skills]({{< ref "lab/deterministic-evals-for-ai-skills" >}}). Evals are not paperwork. They are how you turn operational pain into a reusable standard the agent cannot ignore on the next run.

## What should leaders approve?

Leaders should not approve "self-improving agents" as a vague category.

Approve a specific feedback contract:

1. What outcomes are logged?
2. Which outcomes count as success?
3. Which constraints are hard gates?
4. Which parts of the policy can update automatically?
5. Which updates require human review?
6. Which metrics prove the new version is better?
7. What is the rollback path?

That last question matters. A model, prompt, retrieval store, or ranking rule can get worse. If the system cannot compare versions and roll back, it is not an operating system. It is a moving target.

The best version is boring to manage. New outcomes arrive. Loss gets computed. Failed patterns become evals. High-performing patterns become examples. Risky changes wait for review. The system improves, but it does not get to rewrite its own authority.

## Where should a team start?

Start with a two-week implementation.

1. Add session IDs to every agent attempt.
2. Log inputs, feasible actions, selected actions, and policy checks.
3. Define five loss components.
4. Backfill outcomes for recent sessions.
5. Build a small dashboard.
6. Convert the five worst failures into eval fixtures.
7. Add retrieval examples from the five best sessions.

That is enough to change the management conversation. You stop asking whether the agent "seems better." You ask whether the loss moved, which component moved, and whether the change held across real sessions.

Part one was the contract. This is the scorecard.

An agent without a contract is unsafe. An agent without a loss function is unmanageable.

{{< faq >}}
  {{% faq-item question="What is a loss function for an AI agent?" %}}
  A loss function is a scoring formula that turns an agent's real outcome into a number the system can improve against. For a scheduling agent, the score can combine acceptance, counter-proposals, reschedules, confirmation delay, preference violations, and user feedback.
  {{% /faq-item %}}
  {{% faq-item question="Should an agent optimize directly against business outcomes?" %}}
  Yes, but only inside hard constraints. The agent can optimize among feasible, authorized actions. It should never learn that breaking policy, skipping approval, or hiding uncertainty is acceptable because it improves a short-term metric.
  {{% /faq-item %}}
  {{% faq-item question="Do I need fine-tuning to create a feedback loop?" %}}
  No. Most teams should start with structured logging, loss computation, retrieval examples, prompt updates, and eval fixtures. Fine-tuning becomes useful later, once the team has enough clean outcome data and a stable contract underneath.
  {{% /faq-item %}}
{{< /faq >}}

*Featured image source: <a href="https://pixabay.com/users/orko46-16495679/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7320893">orko46</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7320893">Pixabay</a>*

{{< related-posts title="Related Insights" paths="lab/developing-effective-agents, lab/deterministic-evals-for-ai-skills, lab/agent-vs-harness-explainer" >}}

{{< read-next title="Read Next" link="lab/developing-effective-agents" buttonText="View more Deep Dives" >}}
