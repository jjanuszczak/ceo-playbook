---
title: "Signals: Week 10, 2026"
date: 2026-03-08
type: signals
tags: [reading-list, artificial-intelligence, fintech, saas, venture-capital, software-engineering]
---

*Note: I took a couple weeks off to recover from some AI burnout! The **AI Productivity Paradox** seems real (well, real for me as I dig in). AI tools enable higher output, which paradoxically leads to higher expectations (even personally), increased workload (workload creep, because now you "can" do certain things that were difficult before), and longer hours, often resulting in less sleep! As the Hardvard Business Review aptly put it: [AI doesn’t reduce work—it intensifies it](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it).*

As we move deeper into 2026, the noise around AI is shifting from "what can it do?" to "what does it cost, and who actually pays?" This week's signals highlight a fascinating tension: while AI makes individual tasks cheaper, it's simultaneously driving an explosion in total complexity and demand. From the "Structural Jevons Paradox" in software engineering to the sobering unit economics of modern SaaS, the theme is clear: **efficiency isn't an endgame; it's a catalyst for higher-order complexity.**

## Highlights from Social

### The Structural Jevons Paradox in AI
{{< x user="rohanpaul_ai" id="2030164251369951545" >}}

*   **Summary:** Rohan Paul highlights an economic paper modeling the "Structural Jevons Paradox": as the unit cost of digital intelligence drops, total energy and computing demand are exploding.
*   **Why it Matters:** In finance and tech, we often assume efficiency leads to conservation. History (and this paper) proves the opposite. When you make a resource cheaper, we don't use less of it; we find infinite new ways to use more of it.
*   **My Take:** **Efficiency is a demand generator.** If AI makes coding 10x cheaper, we won't have 90% fewer engineers; we'll have 10x more complex systems.
---
### The Sobering Reality of SaaS Venture Math
{{< x user="deedydas" id="2030346710862713321" >}}

*   **Summary:** A breakdown of the math required for a $1M ARR company to reach the $250M exit threshold over 8 years, highlighting the aggressive growth expectations in today's market.
*   **Why it Matters:** It exposes the "Series A trap." Founders often raise on growth projections that are mathematically improbable without perfect execution and massive market tailwinds.
*   **My Take:** **Scale is a debt you owe the future.** Before you raise that Series A, make sure you actually want to run the $250M ARR marathon.
---
### Abstraction Must Be Earned
{{< x user="garrytan" id="2030286543684874590" >}}

*   **Summary:** Garry Tan argues that "good abstractions are never designed; they’re discovered." You have to do the manual work until the real bottleneck emerges.
*   **Why it Matters:** In venture building, we often over-engineer systems before we've validated the insight. 
*   **My Take:** **Insight is the prerequisite for automation.** If you automate a process you don't fully understand, you're just accelerating a mistake.

---

## Long Form Highlights

### Agents: Cards First, Stablecoins Later
**Source:** [Fintech Brainfood by Simon Taylor](https://www.linkedin.com/pulse/agents-use-cards-first-stablecoins-simon-taylor--8bnhe/)

{{< figure
    src="cards.png"
    alt="Agents using virtual cards"
    caption="Simon Taylor: Agents will use cards first. Then stablecoins."
    >}}

*   **Summary:** An analysis of how AI agents will likely utilize existing card rails (virtual cards) for payments before transitioning to native stablecoin protocols.
*   **Why it Matters:** It's a pragmatic bridge for the "Agentic Economy." We don't need to rebuild the entire financial stack for agents to start spending; we just need to give them better interfaces to the existing one.
*   **My Take:** **Legacy rails are the training wheels for decentralized finance.** The path to 402 (Payment Required) starts with a Visa API.
---
### The Plausibility Gap in LLM Code
**Source:** [Hōrōshi バガボンド](https://x.com/KatanaLarp/status/2029928471632224486)

{{< x-article user="KatanaLarp" id="2029928471632224486" title="Your LLM Doesn't Write Correct Code. It Writes Plausible Code." image="https://pbs.twimg.com/media/HCu3Su9WUAA1dzR?format=jpg&name=small" >}}

*   **Summary:** A deep dive into why LLM-generated code often passes tests but fails on performance, with a Rust/SQLite example showing a 20,000x slowdown.
*   **Why it Matters:** It distinguishes between "working" code and "engineered" code. For mission-critical infrastructure, "plausible" isn't good enough.
*   **My Take:** **LLMs are excellent at syntax, but poor at architecture.** The role of the Senior Engineer is shifting from "writer" to "editor and optimizer."

---

## From the Bookshelf

{{< figure
    src="farber.png"
    alt="Underwriters of the United States - Hannah Farber"
    caption="Hannah Farber: Underwriters of the United States"
    >}}

> "Investment is that which is beneficial to society, gambling is that which is immoral, and speculation lies in the legal and moral gray area in between."

**Source:** [Underwriters of the United States](https://www.amazon.com/Underwriters-United-States-Insurance-University-ebook/dp/B0915PS84Q/)

*   **Why it Matters:** This historical framing of insurance and finance shows that our modern debates about crypto or AI risk aren't new—they are part of a centuries-old struggle to categorize "productive" versus "extractive" capital.

{{< figure
    src="automate.png"
    alt="Three Strikes and You Automate"
    caption="Nicolai M. Josuttis: Three Strikes and You Automate"
    >}}

> "If you do the same thing at three different times, you automate it. This is known as the 'Three Strikes and You Automate' pattern. If you do the same thing in three different places, you refactor your code."

**Source:** [SOA in Practice](https://www.amazon.com/SOA-Practice-Distributed-System-Design-ebook/dp/B0026OR2R2/)

*   **Why it Matters:** A classic engineering rule of thumb applied to management. It prevents premature automation (which creates debt) and ensures that systems are built on patterns of actual behavior.

---

Looking for more? You can explore the archives of previous fast-twitch market observation and insights on the [Signals]({{< relref "signals" >}}) page.

If these market observations are relevant to the operations of, or innovation at, your organization and you want to discuss these further and more indepth, let's talk.

{{< button href="/contact/" target="_self" >}}Book a Call{{< /button >}}