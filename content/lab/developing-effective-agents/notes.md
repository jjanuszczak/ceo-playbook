# Editorial Notes

## Brief and intended reader

Issue #137 asked for a practical Lab post for operators, founders, and technical leaders building agents for real workflows. The draft uses the scheduler-agent build as an anonymized case study and avoids real calendar data, names, email addresses, event IDs, and meeting links.

## Content-type and taxonomy rationale

Content type: Lab. The brief requested the Lab section, a workflow diagram, pseudocode, and practical implementation guidance.

Taxonomy: Technology with existing tags `artificial-intelligence`, `software-engineering`, `systems-thinking`, `dev-ops`, and `productivity`. No new tag approval required.

## Research basis and citations

Research used the supplied draft, the anonymized scheduler-agent skill excerpt in issue #137, and public sources: Anthropic's agent workflow and tool-design guidance, OpenAI Agents SDK and guardrail docs, Berkeley Function Calling Leaderboard, tau-bench, RFC 8984 JSCalendar, Google Calendar Events and FreeBusy API docs, and Python `zoneinfo` documentation.

## Internal linking record

Selected contextual links:

- `lab/agents-vs-skills`: reinforces the boundary between the agent, deterministic scripts, and packaged skill procedure.
- `lab/deterministic-evals-for-ai-skills`: supports the argument that fixed rules belong in deterministic checks.
- `lab/prompt-diet-agent-efficiency`: supports the cost and reliability case for moving repeated enforcement out of prompts.
- `lab/agent-vs-harness-explainer`: added as nearby context for JSCalendar and agent architecture framing.

Related/read-next:

- Related posts: `lab/agents-vs-skills`, `lab/deterministic-evals-for-ai-skills`, `lab/prompt-diet-agent-efficiency`.
- Read next: `lab/javascript-object-gui`.

## Featured image candidates and selected asset

Source: Pixabay helper with `PIXABAY_API_KEY`, query `software team workflow calendar planning`, filtered for horizontal real photos and rejected AI-generated results.

Candidates:

1. `https://pixabay.com/photos/business-office-team-kanban-work-4051773/`, creator `geralt`, 5287x3505. Rights basis: Pixabay Content License, current terms to verify before publication. Rejected because it is more generic Kanban/workflow than scheduler-specific.
2. `https://pixabay.com/photos/meeting-business-architect-office-2284501/`, creator `mwitt1337`, 5400x3375. Rights basis: Pixabay Content License, current terms to verify before publication. Rejected because the blueprint table reads as project planning rather than calendar-agent workflow.
3. `https://pixabay.com/photos/calendar-meeting-planning-10045176/`, creator `Ralf1403`, 4800x3200. Rights basis: Pixabay Content License, current terms to verify before publication. Selected because the calendar/planning subject directly matches the scheduling-agent case study and crops cleanly to 16:9.

Selected asset: `featured.jpg`, cropped to 1280x720 from the selected Pixabay download.

## Social draft archive

Saved X and LinkedIn candidates to `docs/repurposed/2026-08-18-developing-effective-agents.md`.

## Validation record

Content-creator provisioning eval reported a known false failure because issue reuse created `feature/137-lab-developing-effective-agents` while the runner expected `feature/lab-developing-effective-agents`. The actual branch and bundle exist.

Managing-editor validation passed on 2026-08-18T09:09:44+08:00 after the final tightening pass.

Editorial-agent package validation and Hugo build passed on 2026-08-18T09:09:47+08:00 after the final tightening pass.

## Open questions and human decisions

None. Keep `draft: true` until human review approves a separate publishing workflow.
