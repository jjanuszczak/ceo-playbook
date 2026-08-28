# Editorial Notes

## Brief and intended reader

Issue #141 requested a follow-up to `Reliable Agents Need Contracts, Not Better Prompts`, focused on outcome tracking, loss functions, and optimization loops for agent judgment. Intended reader: technology and AI leaders responsible for agent performance.

## Content-type and taxonomy rationale

Content type: Lab. The piece is an architectural memo with a concrete scheduling-agent implementation model. Category: Technology. Tags reused from the approved taxonomy: `artificial-intelligence`, `software-engineering`, `systems-thinking`, `productivity`, `dev-ops`.

## Research basis and citations

Research authority came from the issue brief. Sources used: local part-one post, Anthropic's current agent-eval guidance, Anthropic's agent architecture guidance, OpenAI Agents SDK docs, OpenAI guardrail docs, OpenAI Evals API reference, and tau-bench for tool-agent-user benchmark context.

## Internal linking record

- `lab/developing-effective-agents`: required part-one link and the natural prerequisite for contracts, canonical records, and deterministic boundaries.
- `lab/deterministic-evals-for-ai-skills`: supports the point that repeated failures should become executable evals.
- `lab/prompt-diet-agent-efficiency`: supports the retrieval/prompt-update section by connecting feedback-loop improvements to thinner, testable system components.
- `lab/agent-vs-harness-explainer`: included in related posts because the piece depends on the distinction between agent behavior and harness/eval infrastructure.

## Featured image candidates and selected asset

Pixabay search query: `data dashboard feedback`.

1. https://pixabay.com/photos/computer-summary-chart-business-767776/ by Lalmch. Rights basis: Pixabay Content License, candidate returned by project adapter. Rejected because the laptop/chart composition felt generic.
2. https://pixabay.com/photos/data-digital-technology-analysis-7592568/ by u_syz4wcgykc. Rights basis: Pixabay Content License, candidate returned by project adapter. Selected because the data-analysis/dashboard subject fits outcome instrumentation and performance tracking.
3. https://pixabay.com/photos/speedometer-dashboard-car-speed-1249610/ by qimono. Rights basis: Pixabay Content License, candidate returned by project adapter. Rejected because the automotive dashboard metaphor was less precise.

Selected asset: `featured.jpg`, cropped from 1280x868 to 1280x720.

## Social draft archive

Saved to `docs/repurposed/2026-08-28-better-agents-need-a-loss-function.md`.

## Validation record

Content-creator provisioning eval reported a known issue-reuse false failure because it expected `feature/lab-better-agents-need-a-loss-function`; the workflow correctly used issue-linked branch `feature/141-lab-better-agents-need-a-loss-function`.

Managing Editor eval passed on 2026-08-28T09:08+08:00.

Full Editorial Agent eval passed on 2026-08-28T09:08+08:00, including local editorial package validation and Hugo build.

## Open questions and human decisions

None.
