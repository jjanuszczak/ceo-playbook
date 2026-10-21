---
title: "Your AI Just Picked 47. Again."
date: 2026-10-21
summary: "A biased random-number prompt exposes a practical rule for enterprise AI: use language models to help build reliable systems, not to impersonate them at runtime."
description: "Why a language model cannot stand in for a random number generator, and how technical leaders should separate design-time AI leverage from runtime system guarantees."
categories:
  - "Technology"
tags:
  - "artificial-intelligence"
  - "software-engineering"
  - "systems-thinking"
  - "programming"
  - "data-science"
showReadingTime: true
showTableOfContents: true
draft: true
status: "user-review"
about:
  - name: "Large language model"
    url: "https://en.wikipedia.org/wiki/Large_language_model"
  - name: "Random number generation"
    url: "https://en.wikipedia.org/wiki/Random_number_generation"
mentions:
  - name: "Randy Olson"
    url: "https://x.com/randal_olson"
  - name: "National Institute of Standards and Technology"
    url: "https://www.nist.gov/"
citations:
  - title: "Randy Olson's random-number experiment"
    url: "https://x.com/randal_olson/status/2112210551137010100"
  - title: "NIST Random Bit Generation"
    url: "https://csrc.nist.gov/projects/random-bit-generation"
  - title: "Python secrets module"
    url: "https://docs.python.org/3/library/secrets.html"
---

Ask an AI to pick a random number from 1 to 100. Do it again in a fresh chat. Then repeat it hundreds of times.

You will not get anything close to a random distribution.

In an [informal experiment shared by Randy Olson](https://x.com/randal_olson/status/2112210551137010100), Claude Sonnet 5.5 chose 47 in 92% of fresh chats. Opus 5.5 favored 42 in 61%. Haiku 4.5 returned only two distinct numbers in the reported trials. The point is not that those figures establish a universal law for every model or prompt. They do not. The point is that a plausible-looking answer can fail the property your system actually needs.

{{< quick-answer >}}
Language models produce likely tokens, not a uniform distribution or a correctness guarantee. Use them at design time to help write, explain, and review an implementation; at runtime, execute a tested generator, validator, or rules engine that provides the property your workflow requires.
{{< /quick-answer >}}

{{< figure src="featured.jpg" alt="Dice on a tabletop, representing the difference between an apparent random choice and a verified random process" caption="A random-looking outcome is not the same thing as a system with tested randomness properties." >}}

## Why is a good answer not the same as a random answer?

An LLM predicts a continuation from learned patterns. When it sees “pick a random number,” it does not call a random-number generator. It produces a number that fits the prompt and its learned distribution. Cultural references, familiar number patterns, and the wording of the request can all affect the answer.

Sampling settings can make outputs less repetitive. They do not turn a text model into an audited source of uniform or cryptographically secure randomness.

That distinction matters because “looks random” is not a requirement. A system may need a uniform sample, an unpredictable token, a stable identifier, or a reproducible test fixture. Each has a different implementation and test method. NIST’s [random-bit-generation guidance](https://csrc.nist.gov/projects/random-bit-generation) separates generator construction, entropy, and validation for a reason.

## Where does runtime prompting create enterprise risk?

The failure begins when a conversational interface becomes a production dependency for a property it cannot guarantee.

Asking a model at runtime to create identifiers, select test samples, set routing thresholds, or invent reference numbers creates a quiet control gap. The output may appear sensible in a demo. It may even work for weeks. But no one has established its distribution, collision rate, reproducibility, or security properties.

That can degrade experiments, narrow test coverage, and push biased samples into downstream reporting. In a higher-stakes workflow, it can turn into an audit problem. The issue is not that the model made an obvious mistake. The issue is that the system treated fluent output as a verified result.

This is one of the operational reasons so many firms remain in [AI pilot purgatory]({{< ref "articles/pilot-purgatory" >}}). A useful demonstration is not yet a production control.

## What should run at design time instead?

Use the model where it adds leverage: specification, code generation, test scaffolding, documentation, edge-case review, and implementation alternatives.

Then move the critical operation into ordinary software. A developer can ask the model to propose a Python implementation, review it, and write tests. The deployed system should still use an appropriate standard-library or platform primitive. For security-sensitive tokens, Python’s [`secrets` module](https://docs.python.org/3/library/secrets.html), for example, draws on the operating system’s strongest available randomness source.

That gives the team something it can inspect, test, version, monitor, and replace. It also keeps the model in the role where it is strongest: speeding up the work of building a system, not becoming an unexamined component inside the system.

The same split applies well beyond randomness:

- Generate a database migration with an LLM, then run the reviewed migration.
- Draft a validation rule with an LLM, then enforce the reviewed rule in code.
- Design a sampling approach with an LLM, then execute the tested sampler.
- Explain an incident with an LLM, then use monitored telemetry and explicit controls to prevent recurrence.

This is the practical version of the shift described in [The Next Compiler]({{< ref "articles/the-next-compiler" >}}). AI can raise the abstraction layer for builders, but it does not remove the need to verify what reaches production.

## What should technical leaders ask before deploying an AI workflow?

Start with the property that must hold. Do not start with the prompt.

1. Is the output required to be correct, random, private, unique, deterministic, or explainable?
2. Which component provides that property today?
3. Can the team test and monitor it independently of the model?
4. What happens when the model changes, the prompt changes, or a provider changes its sampling behavior?
5. Is the LLM producing a draft for review, or is it making the production decision itself?

If the answer to the last question is “the model makes the decision,” the burden of proof goes up sharply. You need explicit evaluation, constraints, and a recovery path. Otherwise, move the decision into a deterministic or statistically validated component and use the model to improve the surrounding work.

## The real lesson is about system boundaries

The 47 experiment is memorable because the failure is easy to see. A chart with one bar towering over the rest makes the point fast.

Production failures are rarely that visible. They arrive as a biased sample, a reused identifier, a routing exception, or an audit question no one expected. The discipline is simple: let AI help build the tool, then rely on the tool for the property it was designed to provide.

That is how technical leaders get the speed without pretending that a fluent model is a random-number generator, a control system, or a source of truth.

{{< faq >}}
  {{% faq-item question="Can an LLM generate random numbers?" %}}
  An LLM can produce varied numbers, but it is not a substitute for a verified random-number generator. Its output depends on learned patterns, prompt wording, and sampling settings. Use a standard library or platform generator when a workflow needs a defined randomness property.
  {{% /faq-item %}}
  {{% faq-item question="When should a team use AI at runtime?" %}}
  Use AI at runtime when probabilistic language or judgment is the intended product behavior and the workflow has appropriate evaluation, constraints, and recovery. Do not use it as an untested substitute for a function that must be deterministic, unique, secure, or statistically valid.
  {{% /faq-item %}}
  {{% faq-item question="What is the design-time pattern for enterprise AI?" %}}
  Use the model to help specify, write, test, document, and review an implementation. Put the reviewed implementation in version control, run it with normal observability, and keep the system property in a component that can be independently tested.
  {{% /faq-item %}}
{{< /faq >}}

## Further Reading

- [The Next Compiler: AI and the Evolution of Abstraction]({{< ref "articles/the-next-compiler" >}}): Why AI-generated code still needs human review and engineering controls.
- [Are We Stuck in AI Pilot Purgatory?]({{< ref "articles/pilot-purgatory" >}}): Why organizations must turn useful demonstrations into durable operating systems.

*Featured image: [Exploration (game) Dice](https://commons.wikimedia.org/wiki/File:Exploration_(game)_Dice.jpg) by Smartiperson, released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), cropped to 16:9.*
