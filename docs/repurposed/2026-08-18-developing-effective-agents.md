# Repurposed Social Drafts: Reliable Agents Need Contracts, Not Better Prompts

Source Article: `content/lab/developing-effective-agents/index.md`
Source URL after publish: `https://januszczak.org/lab/developing-effective-agents/`
Status: draft-only, not posted

## X Candidates

### Option 1

better prompts will not save a weak agent.

define the contract first:
canonical record
deterministic tools
approval gates
read-back
eval fixtures

then let the model handle judgment.

### Option 2

the fastest way to break a calendar agent:

let prose handle time zones, approvals, meeting links, and API conversion.

that is not autonomy.
that is an untested side effect waiting to happen.

### Option 3

agents need a repair budget.

two implementation fixes? fine.
policy ambiguity? stop.
missing authority? stop.
external side effect? ask.

unbounded self-healing is just quiet production risk.

### Option 4

the reusable agent pattern:

intent -> missing facts -> deterministic policy -> canonical draft -> approval -> external action -> read-back -> evals

boring architecture.
better outcomes.

## LinkedIn Candidates

### Option 1

Most agent failures are not prompt failures. They are contract failures.

A scheduler agent is a useful example. "Find time next week and use Google Meet" sounds simple, but it hides several decisions:

- Which calendar is authoritative?
- Whose time zone anchors the request?
- Is this a proposal or a booked event?
- Is Google Meet being created natively, or is the agent inventing a link?
- What requires explicit approval?

The fix is not a longer prompt. It is a stronger operating contract:

- Canonical record
- Deterministic time-zone and API conversion logic
- Approval gates for side effects
- Read-back after execution
- Local fixtures for regression testing

So what? Treat agents like software that can reason, not prose that can act.

### Option 2

I do not want an agent to be clever about calendar math.

I want it to be boring.

Let the model interpret intent, identify missing facts, and explain tradeoffs. Let deterministic tools handle time zones, free/busy windows, event conversion, ranking, approval checks, and regression fixtures.

That split matters because reliable agents are built around contracts:

- Rules in policy
- Transformations in code
- Judgment in the agent
- Authority in approval gates
- Confidence in evals

So what? The more predictable the decision, the less it belongs in the model loop.

### Option 3

One clean demo tells you very little about whether an agent is ready for real workflow ownership.

The ninth run matters more.

That is why local evals are not optional. Public benchmarks keep showing that tool use, rule-following, and consistency remain hard. Your internal agent needs fixtures that reflect your actual operating risk:

- Missing attendee identity
- Unclear meeting method
- DST boundaries
- Approval before booking
- Third-party video links
- Read-back after insertion

So what? Do not approve "AI agents" as a category. Approve a specific agent with a specific contract, tools, permissions, logs, stopping conditions, and tests.
