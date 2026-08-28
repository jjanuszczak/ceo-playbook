# Repurposed Social Drafts

Source Article: Better Agents Need a Loss Function
Source Path: `content/lab/better-agents-need-a-loss-function/index.md`
Canonical URL: https://januszczak.org/lab/better-agents-need-a-loss-function/
Status: Draft only. Do not post.

## X Candidates

### X Option 1

your agent does not improve because it has memory.

it improves when you can trace a bad outcome to a decision, encode the lesson, and prove the next version performs better.

contracts make agents safe.
loss functions make them manageable.

### X Option 2

most agent evals stop too early.

"did the tool call work?" matters.

but for a scheduling agent, the real question is:

did the meeting stick?
did people counter?
did they reschedule?
did the user override it?

that is the scorecard.

### X Option 3

do not let an agent optimize its way around policy.

hard constraints first:
availability
time zones
approval gates
read-back checks
audit logs

then let the judgment layer rank what remains.

allowed first.
best second.

### X Option 4

the fastest useful agent feedback loop:

1. log every attempt
2. score the outcome
3. cluster the failures
4. turn failures into evals
5. turn wins into retrieval examples

no fine-tuning required.

## LinkedIn Candidates

### LinkedIn Option 1

Most agent programs confuse memory with learning.

Memory is just stored context.

Learning starts when the organization can answer a harder question: did the agent's decision produce a better real-world outcome?

For a scheduling agent, that means tracking:

- acceptance rate
- counter-proposals
- reschedules
- delay to confirmation
- user overrides
- policy violations

The deterministic layer should still enforce the hard rules: availability, time zones, approvals, and read-back checks.

But the judgment layer needs a loss function.

So what?

If you cannot define the scorecard, you cannot manage the agent. You are just reading transcripts and debating vibes.

### LinkedIn Option 2

Part one of building better agents is the contract.

What records are canonical?
Which tools can run?
Where are the approval gates?
What is never allowed?

Part two is the loss function.

Among all valid actions, which one worked best?

That second question is where most workflow agents become interesting. A scheduling agent may propose a technically valid meeting slot, but the real outcome is whether people accepted it, countered it, rescheduled it, or ignored it.

So what?

Contracts make agents safer. Loss functions make them improvable. You need both before autonomy deserves trust.

### LinkedIn Option 3

The practical path to agent improvement does not start with fine-tuning.

Start smaller:

- Add session IDs to every attempt
- Log feasible actions and selected actions
- Track delayed outcomes
- Compute a simple loss score
- Convert failures into eval fixtures
- Convert wins into retrieval examples

That loop gives leaders something concrete to manage.

Did the loss move?
Which component moved?
Did the change hold across real sessions?

So what?

If the agent cannot be measured, it cannot be managed. If it cannot be managed, it should not be trusted with real workflow authority.
