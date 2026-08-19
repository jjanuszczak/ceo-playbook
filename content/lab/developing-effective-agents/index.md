---
title: "Reliable Agents Need Contracts, Not Better Prompts"
date: 2026-08-19
summary: "A practical Lab memo on turning a vague calendar assistant into a reliable agent with canonical records, deterministic tools, approval gates, and fixture-based evals."
description: "A scheduler-agent case study for operators and technical leaders: why effective AI agents need explicit contracts, deterministic components, approval boundaries, and regression tests before they touch real workflows."
categories:
  - Technology
tags:
  - artificial-intelligence
  - software-engineering
  - systems-thinking
  - dev-ops
  - productivity
showReadingTime: true
showTableOfContents: true
draft: false
status: published
about:
  - name: "Intelligent agent"
    url: "https://en.wikipedia.org/wiki/Intelligent_agent"
mentions:
  - name: "Software testing"
    url: "https://en.wikipedia.org/wiki/Software_testing"
  - name: "JSCalendar"
    url: "https://www.rfc-editor.org/rfc/rfc8984.html"
citations:
  - title: "Building effective agents"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
  - title: "Writing effective tools for agents"
    url: "https://www.anthropic.com/engineering/writing-tools-for-agents"
  - title: "OpenAI Agents SDK"
    url: "https://openai.github.io/openai-agents-python/"
  - title: "OpenAI Agents SDK Guardrails"
    url: "https://openai.github.io/openai-agents-python/guardrails/"
  - title: "Berkeley Function Calling Leaderboard"
    url: "https://gorilla.cs.berkeley.edu/leaderboard"
  - title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
    url: "https://arxiv.org/abs/2406.12045"
  - title: "RFC 8984: JSCalendar"
    url: "https://www.rfc-editor.org/rfc/rfc8984.html"
  - title: "Google Calendar Events API"
    url: "https://developers.google.com/workspace/calendar/api/v3/reference/events"
  - title: "Google Calendar FreeBusy API"
    url: "https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query"
  - title: "Python zoneinfo"
    url: "https://docs.python.org/3/library/zoneinfo.html"
---

Most teams do not fail at agents because the prompt is weak. They fail because the agent has no contract.

Consider the case of building a simple scheduling agent to help schedule meetings. The request usually starts cleanly enough: "Build me a calendar assistant." Then the edge cases arrive. Which calendar is authoritative? Is "next Thursday afternoon" the organizer's afternoon or the client's? Can the agent book, or only propose? What happens when a participant has no known time zone?

Those questions are the product. The model is only one component.

{{< quick-answer >}}
Reliable agents are built around explicit contracts: a canonical record, deterministic tools, policy rules, approval gates, and regression tests. A prompt can interpret intent, but code should handle time zones, API conversion, permissions, validation, and repeatable decisions. The practical pattern is to let the agent reason where judgment is needed and force everything else through inspectable software.
{{< /quick-answer >}}

## Why is a vague agent request dangerous?

**A vague request creates fake autonomy**. The agent sounds capable because it can describe the workflow, but it has no stable boundary between interpretation and execution.

Scheduling is a clean example because it looks simple but punishes sloppiness. A human can say, "Find time next week with two attendees, use Google Meet, and avoid late calls on my end." That sentence contains intent, constraints, tool choices, risk, and authority in one line.

If the agent treats that sentence as pure prose, it will improvise. It may infer a time zone, book an unapproved option, invent a video link, or ignore daylight saving time because the calendar math was never made explicit.

That is not an intelligence problem. It is an architecture problem.

Anthropic's practical agent guidance draws the right distinction: workflows follow predefined code paths, while agents dynamically direct their own process and tool use. It also recommends starting simple and adding agentic complexity only when simpler approaches fall short. OpenAI's Agents SDK takes the same engineering direction through a small set of primitives: agents, tools, handoffs, sessions, human review, tracing, and guardrails.

The operational lesson is blunt: **do not start by making the model smarter. Start by making the work less ambiguous.**

## What contract should every workflow agent have?

Let's consider the case of the scheduling agent. The contract starts with a canonical event record. In my case, I used [JSCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) as a stable representation because [RFC 8984](https://www.rfc-editor.org/info/rfc8984/) defines a JSON data model for calendar storage and exchange, with explicit attention to ambiguity, extensibility, and processing simplicity. The agent can interpret a request, but the durable draft has to become structured data.

That separation matters. I happen to mostly use Google Calendar. Google Calendar's Events API has its own event resource shape, conference creation rules, attendee fields, reminders, recurrence, and organizer semantics. Its FreeBusy API answers a narrower question: which calendars are unavailable across a time window. Python's `zoneinfo` [handles IANA time zones](https://docs.python.org/3/library/zoneinfo.html) and daylight saving transitions.

No prompt should carry all of that in its head.

The contract:

1. User intent enters as natural language.
2. Missing facts become questions, not guesses.
3. The agent drafts a canonical JSCalendar record.
4. Deterministic adapters convert that record to and from Google Calendar (or whatever client you are targetting).
5. Free/busy and time-zone calculations run through scripts.
6. Any insert, update, delete, or external side effect requires approval.
7. The final read-back is reconciled against the canonical record.

That design also strengthens [the agent-versus-skill boundary]({{< relref "lab/agents-vs-skills" >}}): the agent owns the scheduling objective, while scripts and skills own repeatable procedure.

## Where should deterministic code replace model judgment?

The more predictable a decision is, the less it belongs in the model loop.

In a scheduler build, code can handle:

1. Free/busy filtering.
2. Cross-time-zone overlap.
3. Sleep-window protection.
4. Date and duration normalization.
5. JSCalendar-to-Google conversion.
6. Google-to-JSCalendar read-back.
7. Fixture evaluation.
8. Repair-budget enforcement.

The model handles:

1. Interpreting the user's intent.
2. Identifying missing facts.
3. Explaining tradeoffs between candidate slots.
4. Deciding when the request needs approval or escalation.

This is the same lesson behind [deterministic evals for AI skills]({{< relref "lab/deterministic-evals-for-ai-skills" >}}): fixed rules should become checks. If the rule is "never create an event before approval," make that a policy gate. If the rule is "never cross the user's 10:00 PM to 6:00 AM Manila sleep window," make that a time-window constraint. If the rule is "do not invent meeting URLs," make the converter reject missing virtual-location data unless the user explicitly requested platform-native creation.

Anthropic's tool-design guidance makes a related point: tools form a contract between deterministic systems and non-deterministic agents. The best tools are shaped around the tasks agents need to perform, with names, arguments, examples, and returned context that make misuse harder.

A scheduler agent should expose higher-level, validated operations: find candidate slots, draft canonical event, convert event, insert approved event, read back event, reconcile result.

## What does a reliable scheduling loop look like?

Here is the pattern I would reuse for agents such as CRM agents, inbox agents, research agents, document agents, and reporting agents:

{{< mermaid >}}
flowchart TD
    A["User intent"] --> B["Resolve missing facts"]
    B --> C["Apply deterministic policy"]
    C --> D["Draft canonical record"]
    D --> E["Run tool adapters and validators"]
    E --> F{"External side effect?"}
    F -->|No| G["Return proposal or draft"]
    F -->|Yes| H["Request explicit approval"]
    H --> I["Execute approved action"]
    I --> J["Read back external state"]
    J --> K["Reconcile against canonical record"]
    K --> L["Run fixture-based evals"]
{{< /mermaid >}}

The loop is intentionally boring. Agents should be exciting because they handle useful work, not because the runtime is mysterious.

A scheduler's core decision path can be reduced to a small pseudocode block:

```text
intent = parse_request(user_message)
facts = resolve_required_facts(intent)

if facts.missing:
    ask_user(facts.missing)
    stop

availability = freebusy_query(facts.calendars, facts.window)
slots = rank_slots(availability, facts.time_zones, policy)

event = build_jscalendar(intent, slots.best, policy)
google_event = convert_to_google(event)

if google_event.has_side_effect:
    request_approval(google_event.summary)
    stop

return proposal(event, slots.alternatives, assumptions)
```

Notice what is absent: no live write before approval, no invented attendee email, no placeholder meeting link, no hidden calendar mutation, and no time-zone math through prose.

## What do the benchmarks tell us?

Public agent benchmarks are imperfect, but they make one point clear: tool use and rule-following remain bottlenecks.

The [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) tracks tool-use accuracy across single-turn, multi-turn, live, and agentic scenarios. Its current leaderboard still leaves meaningful headroom even for top models, which is why production systems should verify tool selection and parameters.

The [tau-bench paper](https://sierra.ai/resources/research/tau-bench) is even closer to real workflow risk. It evaluates agents through conversations with simulated users, domain-specific API tools, and policy guidelines. The paper reports that state-of-the-art function-calling agents succeeded on less than half of tasks in its tested domains and behaved inconsistently across repeated trials.

Benchmarks do not tell you whether your calendar agent is ready for your use, your customers, or your regulated workflow. They tell you why your local evals matter.

For a scheduler, local evals should cover:

1. Ambiguous attendee identity.
2. Missing meeting method.
3. Organizer inside working hours, attendee outside working hours.
4. DST boundary and back-to-back slots.
5. Attempted event insertion without approval.

Each fixture should pair the prompt, assumptions, canonical record, expected tool calls, expected approval behavior, and expected final response.

## How much self-healing should you allow?

Self-healing sounds powerful until it becomes an unbounded loop making quiet policy changes.

My rule is two repair attempts. Let the agent fix implementation mistakes: malformed JSON, a broken adapter, a missing required field, or a failing test fixture. Stop when the failure is policy ambiguity, missing authority, changed expected behavior, or real-world judgment.

OpenAI's guardrail model separates checks by boundary: input guardrails, output guardrails, and tool guardrails. For workflow agents, tool guardrails matter most when side effects are possible because they validate or block a tool call before and after execution.

This protects the transaction boundary. An agent that drafts a proposal can be wrong cheaply. An agent that mutates a calendar, sends an email, edits a CRM record, or changes production data needs explicit authority.

## What is the operator checklist?

Before approving an agent, ask:

1. **What is the canonical record?** If the workflow crosses systems, the agent needs one stable representation.
2. **Which steps are deterministic?** Time, money, IDs, permissions, ranking, conversion, and validation should not depend on prose.
3. **Where are the approval gates?** External side effects need explicit user approval unless the policy says otherwise.
4. **What can the agent ask about?** Missing facts should produce questions, not fabricated certainty.
5. **What does the read-back prove?** After any external action, inspect the resulting state.
6. **What fixtures prevent regression?** Each edge case needs a local test.
7. **What is the repair budget?** Give the agent room to fix implementation errors, then force escalation.

The tradeoff is real. More structure costs setup time. It also cuts hallucination risk, reduces runtime reasoning cost, and gives you an audit trail when something breaks.

That is the reusable pattern: judgment in the agent, rules in policy, transformations in code, authority in approval gates, and confidence in evals.

{{< faq >}}
  {{% faq-item question="What is the first thing to define when building a workflow agent?" %}}
  Define the canonical record. For a scheduler, that can be JSCalendar. For a CRM agent, it may be an account or interaction schema. For a research agent, it may be a source-backed evidence table. Without a stable record, each tool call becomes a separate interpretation.
  {{% /faq-item %}}
  {{% faq-item question="When should an agent ask the user instead of acting?" %}}
  It should ask when a required fact, authority boundary, external side effect, or policy decision is missing. Missing attendee email, unclear meeting method, unclear calendar ownership, and approval to book are all stop-and-ask moments.
  {{% /faq-item %}}
  {{% faq-item question="Do stronger models remove the need for deterministic tools?" %}}
  No. Stronger models improve interpretation and planning, but calendar math, API conversion, authorization, side-effect control, and regression testing still belong in deterministic components. Better reasoning does not replace contracts.
  {{% /faq-item %}}
{{< /faq >}}

Featured image source: <a href="https://pixabay.com/users/Ralf1403-21380246/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=10045176">Ralf1403</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=10045176">Pixabay</a>

{{< related-posts title="Related Insights" paths="lab/agents-vs-skills, lab/deterministic-evals-for-ai-skills, lab/prompt-diet-agent-efficiency" >}}

{{< read-next title="Read Next" link="lab/javascript-object-gui" buttonText="View more Deep Dives" >}}
