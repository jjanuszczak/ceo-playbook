---
title: "Deterministic Evals: Hardening AI Skills for Production"
date: 2026-05-18
summary: "Moving beyond 'vibe-checking' AI agents. This Lab entry explores the architecture of deterministic evaluation pipelines bundled directly with AI skills to ensure technical and governance compliance."
description: "A technical breakdown of implementing a modular evaluation framework for AI agents. Learn how to use a pipeline of deterministic Python scripts to validate LLM outputs against strict structural, governance, and build standards."
categories:
  - Technology
tags:
  - artificial-intelligence
  - software-engineering
  - dev-ops
  - systems-thinking
  - taxonomy
showReadingTime: true
showTableOfContents: true
draft: false
status: agent-pending
# Pillar 2: Advanced Schema
about:
  - name: "Software Testing"
    url: "https://en.wikipedia.org/wiki/Software_testing"
mentions:
  - name: "Large Language Model"
    url: "https://en.wikipedia.org/wiki/Large_language_model"
citations:
  - title: "Evaluation of LLM Applications"
    url: "https://www.promptengineering.org/evaluating-large-language-models-a-comprehensive-guide/"
---

The challenge with integrating Large Language Models (LLMs) into production workflows is not their intelligence; it is their variance. When an AI agent acts as a "Managing Editor" or "Content Creator", how do we ensure it doesn't just produce a great "vibe," but also follows every strict technical requirement of the platform?

{{< quick-answer >}}
Evaluation frameworks (Evals) are deterministic quality gates that verify AI outputs against specific rules. By bundling a modular pipeline of Python-based validators directly with an AI skill, we can autonomously enforce governance, formatting, and build standards, allowing agents to self-correct before human review.
{{< /quick-answer >}}

## The Problem: The "Vibe Check" vs. Production Standards

In the early stages of AI development, we rely on "vibe checks": reading an output and deciding if it looks correct. This doesn't scale. For example, on this platform, every post must meet eight specific criteria:
1. Correct directory structure (Leaf Bundles).
2. Category and Tag governance compliance.
3. Specific AEO/SEO frontmatter fields.
4. Presence of "Quick Answer" shortcodes.
5. Presence of FAQ blocks.
6. Semantic navigation (Related/Next) with valid parameters.
7. Executive style (speak in the first person).
8. A successful Hugo build.

Manually checking these is tedious and error-prone. We need a way to make the agent its own most rigorous critic.

## The Solution: Modular Deterministic Evals

I implemented a **Deterministic Evaluation Pipeline** bundled directly within the skill directory. This architecture treats an AI skill as a self-contained unit of work that includes both its instructions and its verification logic.

### 1. The Directory Structure
By co-locating the evals, we ensure the skill is portable and maintainable.
```text
./skills/managing-editor/
├── SKILL.md                 # The "Brain" (Instructions)
└── evals/                   # The "Nervous System" (Verification)
    ├── runner.py            # Orchestrator
    ├── config.yaml          # Pipeline Definition
    └── checks/              # Atomic Python Validators
        ├── structure.py
        ├── frontmatter.py
        ├── aeo.py
        └── build.py
```

### 2. The Evaluation Protocol
The `runner.py` acts as a central orchestrator. It reads a `config.yaml` file to determine which checks to run and in what order. Each check is a standalone Python script that follows a simple contract:
* **Input:** Receives the path to the file being validated.
* **Output:** Returns an exit code (0 for pass, 1 for fail) and a JSON string via STDOUT.

### 3. The Self-Correction Loop
The most powerful aspect of this framework is its integration into the agent's workflow. The `SKILL.md` defines a **Phase 5: Self-Evaluation** protocol:
1. **Act:** The agent creates the content.
2. **Eval:** The agent runs the `runner.py`.
3. **Analyze:** The agent parses the JSON results.
4. **Correction:** If a check fails (e.g., "Missing 'about' field"), the agent applies a surgical fix and re-runs the eval.

## Sample Implementation

You can see this pattern in action in the [GitHub Repository](https://github.com/jjanuszczak/ceo-playbook/tree/main/.gemini/skills/managing-editor/evals). 

For example, our `build.py` check doesn't just say the build failed; it captures Hugo's error output and passes it back to the LLM:
```python
# Extract relevant error context for the agent
error_lines = [line for line in result.stderr.split('\n') if "ERROR" in line]
print(json.dumps({"errors": ["Hugo build failed"], "hugo_output": error_lines}))
```

## Looking Ahead: The Future of Evals

While deterministic checks are perfect for structure and syntax, they struggle with "soft" metrics like tone or clarity. Our framework is designed to evolve:

* **LLM-as-Judge:** We could add a check script that passes a section of content to a separate LLM call to grade "readability" or "persuasiveness" against a rubric.
* **Human-in-the-Loop:** After the deterministic suite passes, the results could be posted as a comment on the PR for final human verification.
* **Hybrid Pipelines:** Combining regex-based structure checks with embedding-based similarity checks to ensure content remains on-topic.

By moving from "vibe-checking" to "automated verification," we transform AI agents from helpful assistants into reliable production-grade operators.

{{< faq >}}
  {{% faq-item question="What is a 'deterministic' eval?" %}}
  A deterministic evaluation is a test with a binary (pass/fail) outcome based on hard rules, such as the presence of a specific string, a valid file path, or a successful software build. Unlike "vibe checks," they are consistent and reproducible.
  {{% /faq-item %}}
  {{% faq-item question="Why bundle evals directly with the AI skill?" %}}
  Bundling evals with the skill ensures that the verification logic is always available wherever the skill is used, creating a self-contained, portable, and production-ready unit of automation.
  {{% /faq-item %}}
{{< /faq >}}

{{< related-posts title="Related Insights" paths="lab/chalk-circle, articles/git-design" >}}

{{< read-next title="Read Next" link="lab/chalk-circle" buttonText="View more Deep Dives" >}}
