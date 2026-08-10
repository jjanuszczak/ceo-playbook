# Repurposed Social Drafts: AI Agents Do Not Feel Technical Debt

Source Article: `content/articles/human-pain-as-an-optimizer/index.md`

Status: Draft only. Do not post.

## X Candidates

### X Option 1

ai agents do not feel technical debt.

they can ship the feature.
they can pass the test.
they can still leave the next engineer with a mess.

the senior engineer's job is shifting:
protect the codebase from output that feels no pain.

### X Option 2

more code is not more progress.

ai makes code generation cheap.
it does not make architecture, review, rollback, or maintenance cheap.

use agents.
but make humans own the decisions that create future pain.

### X Option 3

the underrated skill in ai coding is not prompting.

it is knowing when the agent produced a technically correct answer to the wrong question.

that is taste.
that is scar tissue.
that is still human work.

## LinkedIn Candidates

### LinkedIn Option 1

AI coding agents do not feel technical debt.

That sounds like a soft statement, but it has hard operating consequences.

A senior engineer rejects bad architecture because they have lived with the cost:

- The brittle interface that slowed every later change
- The clever shortcut that made rollback painful
- The abstraction that looked elegant in March and became a tax by October
- The production incident that taught the team what not to do again

AI agents can draft, scaffold, test, migrate, and accelerate real work. But they do not carry the memory of maintenance pain.

So What?

Engineering leaders should not measure AI coding success by lines added or pull requests opened. Track survivability: churn, duplication, escaped defects, review time, rollback frequency, and refactoring capacity.

Use agents. But make humans own the architectural decisions that create future pain.

### LinkedIn Option 2

AI makes code generation cheaper.

That is the opportunity and the risk.

When generating a fresh implementation takes seconds, teams can drift toward the easy path:

- Add more code
- Reuse less
- Refactor later
- Push larger batches into review
- Let weak abstractions survive because they appear to work

The problem is not that every AI-generated line is bad. The problem is that the cost of producing code is falling faster than the cost of understanding the system.

So What?

Treat AI coding as an operating-model change, not a tool rollout.

The company needs stronger review gates, deterministic evals, refactoring capacity, and clear ownership of architecture boundaries. Otherwise AI does not remove technical debt. It accelerates the path to it.

### LinkedIn Option 3

The senior engineer is no longer just the person who can write the hardest code.

In an AI-assisted team, the senior engineer increasingly protects the system from cheap code.

That means knowing when:

- The abstraction is premature
- The dependency creates an upgrade burden
- The interface will hurt another team
- The generated code solves the prompt but misses the system
- The feature should be narrowed, not expanded

AI agents can help with the mechanical surface area. That is valuable.

But the scarce asset is judgment under pressure.

So What?

The future of software engineering is not humans versus agents. It is humans teaching the engineering system which kinds of pain are worth avoiding before the codebase has to learn the expensive way.
