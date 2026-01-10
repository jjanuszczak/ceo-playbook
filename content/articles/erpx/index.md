---
title: "Why Our \"Free ERP\" Failed (& Why AI Changes the Battlefield)"
date: 2025-12-20
summary: "We gave Philippine SMEs a free operating system, but they didn't use it. In this retrospective, I analyze the failure of ERPX through the lens of modern AI architecture and explain why solving the 'Cost' barrier wasn't enough without solving the 'Effort' barrier."
description: "A strategic look at why legacy database architectures fail in the SME market, contrasting UBX's ERPX experiment with the AI-native approach of Digits."
categories:
   - "Venture Building"
tags:
  - "Fintech"
  - "SME"
  - "ERP"
  - "AI"
  - "Venture Building"
  - "Transformation"
showTableOfContents: true
draft: false
---

In the trenches of building UBX, we operated with a clear mission: democratize financial access for the Philippine SME. We had the strategy, we had the capital (thanks to our investors), and we had the distribution channels. But even seasoned generals lose battles on the way to winning the war.

One of our boldest experiments was [**ERPX**](https://januszczak.org/portfolio/). The vision was textbook fintech strategy: build an "Operating System" for small businesses, give it away for free (or close to it), and monetize the financial rails: payments, lending, and insurance embedded directly into the workflow.

We did what any pragmatic execution team would do in 2019: we didn't reinvent the wheel. We forked a robust open-source ERP project to provide the scaffolding. We stripped it down, localized it, and pushed it out to the market.

**And it stalled.**

For years, I analyzed this through the lens of *product-market fit*. We hypothesized that we gave them a cockpit when they needed a bicycle. We tried to force-feed full-stack accounting when their bleeding-neck problem was just Point-of-Sale (POS) or Inventory Management. As a side benefit, this approach would also compliment our online store builder [Sentro](https://sentro.ph/).

But after watching the rise of [Digits](https://digits.com/) and hearing Jeff Seibert’s philosophy, I realized our mistake wasn't just about features. It was about **Data Architecture**.

## The "Legacy Debt" We Didn't Know We Had

At UBX, we built ERPX on a traditional SQL database structure. The same "forms and fields" architecture that has defined accounting since the 1990s. We were asking Filipino business owners, who run their empires on notebooks and intuition, to become data entry clerks.

Jeff Seibert at Digits pinpoints this perfectly: **Legacy software requires you to manually structure data before you can use it.** You have to define the vendor, pick the category, and reconcile the bank feed *before* the software gives you any value.

We tried to solve the **Cost** barrier (by making it free). But we failed to solve the **Effort** barrier.

## The Two Things We Got Right (That Digits Still Misses)

Ironically, our 2019 hypothesis about *what* the Philippine SME needs was spot on. We believed the "wedge" into the business wasn't the General Ledger (GL). It was the operational front-line: **POS and Inventory**.

To this day, Digits is purely a layer on top of the financial stack (QuickBooks/Xero). They don't do POS. They don't do Inventory. They are solving the "Review" phase of accounting, not the operational "Entry" phase.

In the Philippines, digitization for SMEs happens at the counter, not in the back office. Our instinct to build POS/Inventory first was correct. Where we failed was connecting that front-line data to the back-office ledger without requiring a human to be the middleware.

## The "Living Model" vs. The Static Ledger

If I could go back to the UBX war room in 2019 with today’s insights, here is how we would have pivoted ERPX:

1.  **Stop Building "Forms":** We spent months designing input screens. We should have spent that time building **ingestion engines**. The goal is zero data entry.
2.  **The Shift from "Entry" to "Review":** Digits uses AI to categorize transactions based on the *entire history* of the firm, not just rigid rules. In 2019, we didn't have GPT-4, but we had machine learning. We could have built a "Review First" interface where the software guessed the category (e.g., "This looks like a supplier payment to San Miguel Corp, correct?") rather than forcing the user to type it in.
3.  **The Ledger as a Graph, Not a List:** We treated the ledger as a static record of truth. It should have been a "Living Model", a dynamic vector that understands that *this* specific SME treats "Grab" as a delivery expense, while *that* SME treats it as a travel expense. _Given our investments in blockchain technology, we really should have known this._

## The Next Battlefield

To the fintech founders looking at the Philippines today: The opportunity to build the "ERPX" of the future is still wide open.

The winner won't just be the one who offers the cheapest software or the best lending rates (though embedded finance is still the endgame). The winner will be the one who realizes that **for an SME owner, every minute spent on data entry is a minute lost on sales.**

The next great Filipino ERP won't look like QuickBooks. It won't have a "Chart of Accounts" setup wizard. It will connect to the POS, watch the bank feed, and simply ask: *"I see you sold 50 units today and paid your supplier. Do you want me to update your inventory and cash flow forecast?"*

**That is the difference between a tool and a teammate. That is how we win.**

## Endnotes

### Jeff Seibert on Digits

Great video where Jeff shares the story of Digits:

{{< youtubeLite id="vdGpHoxkjqY" label="QuickBooks Is Getting Replaced. Meet the Founder Taking Them Down" >}}

### ERPX Launch

July 2019 and we are about to luanch ERPX!

{{< figure
    src="erpx-launch.png"
    alt="ERPX Launch"
    caption="Big launch at the UBX office!"
    >}}
