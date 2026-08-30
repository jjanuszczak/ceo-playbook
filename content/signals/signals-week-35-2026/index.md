---
title: "Signals: Week 35, 2026"
date: 2026-08-30
type: signals
tags: ["reading-list", "artificial-intelligence", "venture-building", "organizational-design", "productivity", "saas", "platform-economics", "defi"]
description: "Weekly curation of high-signal observations on DeFi-native agents, the transition from SaaS to outcome-based service models, the modular WikiSkill architecture, and the infinite abstraction stack of technological progress."
summary: "This week's signals cover DeFi-native agents, outcome-based service models replacing SaaS, Google's WikiSkill architecture, and why the AI jobs apocalypse is a historical misunderstanding."
draft: false
showCopyPage: true
---

This week's signals trace a fundamental shift in the architecture of both technology and business models. We are moving from static tools to dynamic, persistent agents that learn, operate on-chain, and own end-to-end outcomes. At the same time, the transition from traditional SaaS to outcome-based service models is accelerating, driven by the collapse of coordination costs. As we build more complex AI agents, the hard part isn't just getting them to act, it's giving them shared memory and continuous feedback loops so they can scale safely. Far from an economic apocalypse, this represents the next major layer of our "infinite stack".

## Market Observations & Insights

### DeFi-Native AI Agents
{{< x user="emilylai" id="2093449036401705349" >}}
*   **Summary:** Emily Lai has compiled a DeFi-native skill library for AI agents, drawing on over 6,000 pages of banking history and protocol transcripts to enable agents to evaluate yield sources and manage risk across 90+ protocols.
*   **Why it Matters:** As finance migrates to on-chain rails, agents must evolve beyond simple data querying. They need deep domain expertise to transact and allocate capital autonomously.
*   **My Take:** **On-chain is the ultimate execution environment for agents.** In the next era of finance, AI agents will not just advise on capital allocation; execution moves to the agent. They will analyze risk parameters in real-time, and route yields without the friction of legacy banking intermediaries.

### Wiki-Skill Agent Architectures
{{< x user="dair_ai" id="2093324233158045788" >}}
*   **Summary:** A new Google research paper introduces "WikiSkill," a framework that decouples raw execution traces, persistent wikis of accumulated knowledge, and executable skills, allowing smaller models with evolved skills to outperform static, larger models.
*   **Why it Matters:** Retraining large models to capture new operational behaviors is inefficient. Decoupling memory and execution allows organizational knowledge to compound dynamically.
*   **My Take:** **Modular memory beats raw parameter scale.** The winning enterprise AI architectures will prioritize structured, persistent databases of operational history that can be dynamically loaded as skills, turning every execution loop into a permanent capability improvement.

### The Post-SaaS Services Paradigm
{{< x-article user="lukesophinos" id="2092731959848116429" title="The 5 New Models That Replace SaaS" image="https://pbs.twimg.com/media/HQrWq_fWkAAYRhg?format=jpg&name=small" >}}
*   **Summary:** Highlighting insights from Slow Ventures' Yoni Rechtman, this piece details the collapse of SaaS gross margins and switching costs, outlining five new models where AI companies sell outcomes and labor rather than software tools.
*   **Why it Matters:** Standard software represents just 1–3% of corporate revenue, whereas labor and services represent the remaining 97%. AI enables builders to target this massive budget by selling outcomes.
*   **My Take:** **Sell the hammered nail, not the hammer.** The subscription software era is giving way to outcome-oriented neo-firms. Builders who take responsibility for quality and delivery, rather than just offering a clean interface, will capture the bulk of the market's value.

### Continuous Eval Engineering
{{< x-article user="Vtrivedy10" id="2092266609838604368" title="How we Build Agent Environments & Tasks" image="https://pbs.twimg.com/media/HQixxfUXYAAvBfv?format=png&name=small" >}}
*   **Summary:** LangChain shares a practical guide on engineering agent environments, emphasizing a two-step pipeline that separates natural language "task specs" from automated task creation to build robust, reproducible benchmarks.
*   **Why it Matters:** Standard static evaluations fail to capture the dynamic trajectories of agentic systems. To deploy AI with confidence, engineering teams need automated, continuous testing frameworks.
*   **My Take:** **You cannot scale what you cannot reliably test.** Eval engineering is the core discipline that bridges the gap between a compelling demo and a production-grade enterprise system. Organizations must treat evaluation design as a first-class engineering priority.

---

## Deep Reads from the Library

### [The Infinite Stack](https://danieljeffries.substack.com/p/the-infinite-stack)
**Author:** Daniel Jeffries
*   **Summary:** Jeffries argues that fear of an AI-driven jobs apocalypse is a historical misunderstanding of technological progress. Technology is an infinite stack of abstraction layers: every solved problem abstracts a task but simultaneously creates a larger, more complex layer of new challenges.
*   **Why it Matters:** This perspective shifts the debate from a zero-sum battle for scarce work to an abundance-driven framework where complexity continuously breeds new industries.
*   **My Take:** **The complexity ratchet only turns one way.** Just as the steam engine and personal computer destroyed specific jobs but spawned entirely new economic sectors, AI will automate basic tasks to free us for the next, highly specialized layers of the stack that we cannot even name from our current viewpoint.

### [The Death of the Company](https://x.com/PeterDiamandis/article/2092667837529694400)
**Author:** Peter H. Diamandis, MD
*   **Summary:** Diamandis introduces the concept of the "Organizational Singularity," detailing how AI-native companies using a five-layer intelligence stack can operate at 100x the throughput of legacy firms with a fraction of the headcount.
*   **Why it Matters:** Traditional corporate structures are optimized for predictability and will actively reject radical disruption from within. To survive, organizations must build autonomous digital twins at their edge.
*   **My Take:** **Corporate immune systems are fatal to innovation.** Attempting to slowly refactor a legacy organization is a recipe for failure. The winning strategy is to stand up a parallel, AI-native twin at the edge and gradually deprecate the old core as the twin demonstrates superior execution.

### [What if everything goes right for AI? Learnings from the Aluminium trade.](https://x.com/p_bonnet/status/2091928684621860889/?s=12&t=R57JcIMupAjU7vMgFWH2fA&rw_tt_thread=True)
**Author:** Paul
*   **Summary:** This essay draws parallels between the 99% price collapse of aluminium in the 19th century and the current cost trajectory of AI tokens, illustrating how drastic cost reductions unlock massive application-layer industries that were previously economically impossible.
*   **Why it Matters:** It shows that hardware commoditization is not a failure of the technology, but the necessary precursor to building entirely new markets (like the aviation industry in the case of aluminium).
*   **My Take:** **Commoditization is the ultimate catalyst for application-layer value.** While chip providers and hardware builders compete in a race to the bottom, the permanent, compounding value will accrue to the application layers that package these ultra-cheap tokens into outcomes that users are willing to pay for.

---

## Highlights from the Stacks

### [The Seven Figure Agency Roadmap](https://www.amazon.com/dp/B07YVL4XDJ)
{{< figure src="nelson.png" alt="The Seven Figure Agency Roadmap by Josh Nelson" >}}
> One thing I found that will make them leave quicker than anything else is perceived indifference and the sense that you have taken them as far as they’re going to go. So, you must constantly be helping them see what’s next.
*   **Summary:** Nelson highlights the primary driver of customer churn in professional services: the perception that a provider has ceased to innovate or deliver incremental value.
*   **Why it Matters:** In both SaaS and services, retention is driven by momentum. If a customer believes they have outgrown your product or framework, they will immediately seek alternatives.
*   **My Take:** **Stagnation is churn.** To build long-term enterprise value, your product roadmap and client relationships must continuously paint a picture of the future. The moment you stop showing clients "what is next," they start looking elsewhere.

### [The Industries of the Future](https://www.amazon.com/dp/B00UDCNJYO)
{{< figure src="ross.png" alt="The Industries of the Future by Alec Ross" >}}
> In effect, these algorithms can hide bias behind a curtain of code.
*   **Summary:** Ross cautions that automated systems and algorithms can easily institutionalize and obscure bias under the guise of objective, mathematical execution.
*   **Why it Matters:** As decisions in finance, hiring, and governance are delegated to machine learning systems, maintaining auditable and transparent governance frameworks is essential.
*   **My Take:** **Code is policy, and policy must be auditable.** We cannot treat algorithms as objective black boxes. As agentic networks scale, building robust observability and governance guardrails is critical to ensuring algorithmic accountability.

### [The Airbnb Story](https://www.amazon.com/dp/B01NCJRMQV)
{{< figure src="gallagher.png" alt="The Airbnb Story by Leigh Gallagher" >}}
> “Success almost always results in legitimacy,” says Airbnb board member Jeff Jordan.
*   **Summary:** Reflecting on Airbnb’s regulatory battles, Jordan notes that achieving massive scale and market success is often what forces regulators and incumbents to accept a disruptive business model.
*   **Why it Matters:** Disrupters in highly regulated fields (like Fintech or Energy) cannot wait for permission. Scale creates the economic gravitational pull that rewrites the rules.
*   **My Take:** **Scale is its own regulatory strategy.** Do not ask for permission to build a better future. Focus entirely on customer obsession and growth; once you become indispensable to the market, legitimacy and regulatory frameworks will adapt to you.

{{< related-posts title="Related Insights" paths="portfolio/intelletto,lab/chalk-circle" >}}

---

{{< read-next title="Read Next" link="signals/signals-week-34-2026" buttonText="View more Signals" >}}
