---
title: "Signals: Week 36, 2026"
date: 2026-09-06T06:30:00+08:00
type: signals
tags: ["reading-list", "artificial-intelligence", "systems-thinking", "organizational-design", "tokenization", "software-engineering", "venture-building"]
description: "Weekly curation of high-signal observations on enterprise AI process re-engineering, six-layer agent harness architecture, tokenizing capital markets, and why legacy software abstractions fail modern systems."
summary: "This week's signals cover why enterprise AI fails without process redesign, the six layers of agent harness engineering, the London Stock Exchange tokenizing the FTSE 100, and the gap between legacy abstractions and modern architecture."
draft: false
showCopyPage: true
---

This week’s signals reveal a unifying truth across enterprise technology, software engineering, and global financial markets: raw capability is useless without the right architecture and process design. In the enterprise, deploying frontier models onto broken, legacy workflows merely accelerates organizational waste. Real leverage requires gutting the process and wrapping probabilistic models in rigorous, deterministic harnesses. 

Simultaneously, in capital markets, tokenization is moving from speculative side-projects to sovereign market plumbing, exposing the brittle monopolies that govern traditional ownership. Across every layer of the stack, the winners are not those who blindly automate the past, but those who redesign the underlying system for execution.

## Market Observations & Insights

### Enterprise AI and the Re-Engineering Trap
{{< x-article user="vasuman" id="2095999742031675738" title="Applied AI Doesn't Work" image="https://pbs.twimg.com/media/HRZ5qYabkAADtzK?format=jpg&name=small" >}}
*   **Summary:** Vas from Varick argues that enterprise AI spend is failing to produce measurable ROI because companies are applying models directly onto broken legacy processes, echoing Michael Hammer’s 1990 warning against "paving cow paths" instead of fundamentally re-engineering the workflow into deterministic software, agentic judgment, and human-in-the-loop checkpoints.
*   **Why it Matters:** The bottleneck in business throughput is almost never individual task execution time; it is the friction of handoffs, queues, and cross-departmental coordination. Speeding up a 17-minute task within a 22-day cycle delivers zero economic leverage.
*   **My Take:** **Automating a broken process only produces faster dysfunction.** True enterprise transformation requires leaders who possess the organizational authority to eliminate legacy handoffs and the technical depth to separate deterministic rules from probabilistic judgment.

### The Six Layers of Harness Engineering
{{< x-article user="iiiichigo_chan" id="2093765205276713218" title="Harness Engineering: Build a Reliable AI Agent in 6 Layers" image="https://pbs.twimg.com/media/HQ5Z1ZMWcAEIdIP?format=jpg&name=small" >}}
*   **Summary:** Ichigo outlines a practical six-layer agent harness spanning task contracts, context compilers, permissioned tool gateways, durable state, evidence gates, and trace recovery loops. It demonstrates that agent reliability is an environment design problem rather than a prompting challenge.
*   **Why it Matters:** As teams build autonomous coding and operational agents, prompt engineering reaches diminishing returns. Systems succeed when models are bounded by explicit schemas, progressive context retrieval, and deterministic verification gates. In short, [reliable agents need better contracts, not better prompts]({{< relref "lab/developing-effective-agents" >}}).
*   **My Take:** **The prompt is an input; the harness is the operating system.** Capable models become reliable enterprise agents only when we externalize state, constrain tool actions with policy gateways, and turn execution failures into permanent infrastructural regression tests.

### The Centralized Custody Illusion in Public Equities
{{< x user="malekanoms" id="2095867602958500233" >}}
*   **Summary:** Omid Malekan points out that critics who claim crypto token holders lack shareholder rights fail to understand that public equity markets operate on the exact same synthetic basis: the central securities depository (a subsidiary of the DTCC) is the sole legal shareholder, leaving investors with custodial derivatives.
*   **Why it Matters:** Modern capital markets are structured around centralized government-protected monopolies that introduce systemic counterparty risks, reduce direct property rights, and entrench legacy clearing inefficiencies.
*   **My Take:** **TradFi equity ownership is already a derivative.** Acknowledging that paper share certificates were replaced decades ago by centralized ledger entries clarifies the debate: public blockchain tokenization is not a dilution of property rights, but an upgrade to transparent, cryptographically enforceable direct ownership.

PS. I will have something to say about all this at greater length tomorrow. Stay tuned!

### Tokenizing Sovereign Market Plumbing
{{< x user="sytaylor" id="2094747983665381493" >}}
*   **Summary:** Simon Taylor analyzes the London Stock Exchange’s initiative with Kraken parent Payward to bring the FTSE 100 onchain via 1:1 backed xStocks, contrasting London’s self-custody and native issuance exploration with the US DTCC’s closed-vault tokenization approach.
*   **Why it Matters:** After years of losing premier listings to New York, exchanges are shifting the battleground from prestige to market structure plumbing, opening 24/7 global liquidity and programmability across decentralized finance rails.
*   **My Take:** **Liquidity follows the path of least administrative friction.** While legacy financial centers attempt to wall off tokenization within permissioned, bank-controlled vaults, real liquidity will aggregate on open, global rails where equities can settle instantly and compose directly with autonomous economic agents.

---

## Deep Reads from the Library

### [The Incumbents Are Coming](https://a16z.com/the-incumbents-are-coming/)
**Author:** Seema Amble
*   **Summary:** Seema Amble examines the battle between SaaS systems of record and AI-native startups, outlining an agent hierarchy from retrieval and process automation to policy and principal judgment, and showing how vertical startups win by manufacturing specialized training curricula and owning the full cross-system job rather than just the underlying database record.
*   **Why it Matters:** Incumbent platforms like Salesforce and Docusign own proprietary corporate data, but the customer's actual workflow crosses numerous departments and systems. The ultimate value accrues to the layer that orchestrates the entire job to completion.
*   **My Take:** **The job to be done is always bigger than the system of record.** Incumbents will capture the low-hanging fruit of basic query retrieval and localized task completion within their own silos. The breakthrough venture opportunity lies in building vertical harnesses that coordinate multi-stakeholder workflows and take legal and financial responsibility for the final outcome.

### [C Is Not a Low-level Language: Your computer is not a fast PDP-11](https://queue.acm.org/detail.cfm?id=3212479)
**Author:** David Chisnall
*   **Summary:** Computer scientist David Chisnall argues in ACM Queue that C no longer maps cleanly to modern hardware; instead, processors and compilers have spent decades contorting themselves with speculative execution, out-of-order execution, and complex cache hierarchies to maintain the illusion of a sequential, flat-memory machine, creating massive vulnerabilities (like Meltdown and Spectre at the time of the writing the article) in the process. 
*   **Why it Matters:** When software abstractions fundamentally diverge from physical reality, performance optimizations become increasingly fragile and dangerous. True scalability requires computing abstractions that embrace hardware concurrency rather than masking it. Something to keep in mind as we embrace AI coding agents, [the next evolution of abstraction]({{< relref "articles/the-next-compiler" >}}).
*   **My Take:** **Leaky abstractions eventually compound into catastrophic debt.** Just as CPU architects endangered hardware security to preserve a 1970s serial programming model, enterprise architects frequently butcher modern autonomous systems trying to force them into obsolete organizational charts. When the underlying primitives change, the abstract model must be rebuilt from first principles.

### [Procurement’s Bullying Stands in the Way of Madison Avenue’s Renewal](https://michaelfarmer.substack.com/p/procurements-bullying-stands-in-the)
**Author:** Michael Farmer
*   **Summary:** Former Bain director Michael Farmer charts the decline of corporate agency relationships from collaborative, Japanese-style supply chain partnerships in the 1980s to adversarial, fee-bashing procurement regimes today, advocating for a shift toward output-based remuneration tied to outcome-based pricing.
*   **Why it Matters:** Relentlessly grinding vendors on hourly rates destroys strategic alignment and starves service providers of the margin required to innovate, resulting in low-quality commoditized execution that damages top-line enterprise growth.
*   **My Take:** **Cost-plus contracting is a mutual suicide pact.** When you pay partners for billable hours rather than business outcomes, you incentivize bureaucracy over velocity. High-performing enterprises must treat critical external partners as integrated supply-chain collaborators, sharing the upside of measurable value creation.

---

## Highlights from the Stacks

### [The House of Morgan](https://www.amazon.com/dp/B003CIQ57E)
{{< figure src="chernow.png" alt="The House of Morgan by Ron Chernow" >}}
> Untermyer: Is not commercial credit based primarily upon money or property?
> Morgan: No, sir, the first thing is character.
> Untermyer: Before money or property?
> Morgan: Before money or anything else. Money cannot buy it. . . . Because a man I do not trust could not get money from me on all the bonds in Christendom.
*   **Summary:** In his famous 1912 Congressional testimony before the Pujo Committee, J. Pierpont Morgan asserts that character and trustworthiness, rather than collateral or balance sheet assets, constitute the true bedrock of commercial credit.
*   **Why it Matters:** Financial systems can construct infinite layers of legal documentation, automated covenants, and collateral pledges, but counterparty trust remains the irreducible requirement for systemic stability.
*   **My Take:** **Reputation is the ultimate collateral.** In an era of anonymous liquidity, synthetic tokens, and automated credit scoring, the most valuable and scarce asset in capital allocation remains uncompromised institutional integrity.

### [Turing's Cathedral](https://www.amazon.com/dp/B005IEGK5C)
{{< figure src="dyson.png" alt="Turing's Cathedral by George Dyson" >}}
> The paradox of artificial intelligence is that any system simple enough to be understandable is not complicated enough to behave intelligently, and any system complicated enough to behave intelligently is not simple enough to understand. The path to artificial intelligence, suggested Turing, is to construct a machine with the curiosity of a child, and let intelligence evolve.
*   **Summary:** George Dyson reflects on Alan Turing’s insight into the fundamental paradox of machine intelligence: comprehension and sophisticated behavior exist in perpetual tension, requiring builders to prioritize evolutionary architectures over rigid, deterministic programming.
*   **Why it Matters:** Attempting to hand-code every rule and anticipate every edge case in complex systems is a mathematical dead end. Builders must construct robust exploratory environments where intelligence can adapt dynamically.
*   **My Take:** **Build systems that learn, not systems that know.** The winning engineering posture in the agentic era is not to micromanage every intermediate response, but to build an unshakeable harness that provides rich feedback loops and allows capability to compound through trial and error.

### [My Life and Work](https://www.amazon.com/dp/B0084AMXOY)
{{< figure src="ford.png" alt="My Life and Work by Henry Ford" >}}
> Everything can always be done better than it is being done.
*   **Summary:** Henry Ford encapsulates the operational philosophy that drove the modern assembly line: no process, regardless of historical precedent or current profitability, is exempt from radical continuous improvement.
*   **Why it Matters:** Organizations naturally calcify around their existing operating models, mistaking temporary profitability for operational perfection. Complacency invites disruptive displacement.
*   **My Take:** **The status quo is a depreciating asset.** The moment a leadership team convinces itself that an operational workflow has reached its optimal state is the moment a leaner competitor begins re-engineering the economics from the ground up.

{{< subscribe >}}

{{< related-posts title="Related Insights" paths="articles/acqui-hiring-as-a-people-strategy,lab/chalk-circle" >}}

---

{{< read-next title="Read Next" link="signals/signals-week-35-2026" buttonText="View more Signals" >}}
