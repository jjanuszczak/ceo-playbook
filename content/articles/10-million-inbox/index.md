---
title: "$10 Million Inbox"
date: 2026-09-13
summary: "Google’s bid for Spirit Airlines’ internal data puts a market price on the institutional memory companies once deleted to save storage costs."
description: "A strategic follow-up on why corporate email, chat, operational records, and decision trails should be treated as long-term knowledge assets rather than disposable IT overhead."
categories:
  - "Strategy"
tags:
  - "artificial-intelligence"
  - "knowledge-management"
  - "long-term-thinking"
  - "systems-thinking"
  - "capital-allocation"
  - "digital-transformation"
showReadingTime: true
showTableOfContents: true
draft: false
status: agent-pending
about:
  - name: "Knowledge management"
    url: "https://en.wikipedia.org/wiki/Knowledge_management"
  - name: "Artificial intelligence"
    url: "https://en.wikipedia.org/wiki/Artificial_intelligence"
mentions:
  - name: "Spirit Airlines"
    url: "https://en.wikipedia.org/wiki/Spirit_Airlines"
  - name: "Google"
    url: "https://en.wikipedia.org/wiki/Google"
  - name: "Microsoft Teams"
    url: "https://en.wikipedia.org/wiki/Microsoft_Teams"
citations:
  - title: "Notice of Auction Results and Successful Bidder for Spirit’s Deidentified Data"
    url: "https://document.epiq11.com/document/getdocumentbycode?docId=4606389&projectCode=SPJ&source=DM"
  - title: "Google wins bankruptcy auction for Spirit Airlines emails, chats, documents"
    url: "https://www.axios.com/2026/08/17/google-spirit-airlines-bankruptcy"
  - title: "US court delays hearing on Google’s purchase of Spirit Airlines data as union objects"
    url: "https://www.investing.com/news/stock-market-news/us-court-delays-hearing-on-googles-purchase-of-spirit-airlines-data-as-union-objects-4866249"
  - title: "Panic builds over bankrupt Spirit’s looming data sale to Google"
    url: "https://arstechnica.com/tech-policy/2026/09/panic-builds-over-bankrupt-spirits-looming-data-sale-to-google/"
---

*A follow-up to [The Emails We Deleted, The Value We Never Saw Coming]({{< relref "articles/deleted-emails" >}})*

In 2015, the rational move was to delete.

Storage was treated as a tax. Mailbox caps were a management tool. “Non-essential files” were a budget line. If the archive threatened the IT spend, the archive lost. That was not stupidity. It was the cost structure of the time.

Then a failed airline put a price on the opposite decision.

In August 2026, Google won a bankruptcy auction for Spirit Airlines’ de-identified corporate data, agreeing to pay $10 million for about 100 million emails, 80,000 email accounts, 500 million Teams items, tens of millions of OneDrive and SharePoint files, source code, operations records, and decades of workplace exhaust. Mercor was named the backup bidder at $7.5 million. A later $12.5 million bid from micro1 has put the proposed sale back before the bankruptcy court. The planes stopped flying in May. The inbox kept its value.

{{< quick-answer >}}
The Spirit Airlines data auction is a warning that corporate email, chat, code, and operational records can become strategic knowledge assets. The $10 million winning bid does not price email alone, and the sale is still contested, but the competitive bidding shows that AI companies value the record of how a real organization made decisions, handled exceptions, and operated over time.
{{< /quick-answer >}}

That is the punchline the 2015 cost-cutting memo never contemplated.

## What did we think we were saving?

A decade ago, corporate email was not an asset class. It was a storage problem with a legal hangover.

Use some conservative 2015 arithmetic as an illustration, not an audited estimate.

Corporate mail is small in the median and fat in the tail. A working average of 100 to 200 KB per stored message is plausible once you include attachments, HTML, and Exchange-style overhead. One hundred million messages is then roughly 10 to 20 TB of raw payload. Indexes, recovery databases, legal hold, replicas, and backup copies can multiply that three to five times. Call the provisioned estate 60 to 150 TB.

Even using a high-end fully burdened estimate, a decade of storage and operations would likely have cost hundreds of thousands of dollars, perhaps around $1 million in an extreme case. Painful on a 2015 cost-center dashboard. Trivial next to a multimillion-dollar auction for the retained enterprise corpus.

We deleted to save a number that would not have bought a spare engine.

## What did the market actually bid for?

Naive division is dangerous, because Google did not bid for “emails only.” It bid for how an airline priced, scheduled, crewed, maintained, argued, and failed, with mail as the narrative layer on top of systems of record.

Still, the auction gives us a useful set of reference points:

- $10,000,000 divided by 100,000,000 emails equals $0.10 per email.
- $10,000,000 divided by 80,000 accounts equals about $125 per mailbox over the life of the estate.
- Mercor’s $7.5 million bid means two sophisticated buyers saw substantial training and product value in the same broad data package.
- micro1’s later $12.5 million proposal shows that the market has not settled on a single price for this kind of asset.

Those figures do not establish a market price for every corporate inbox. The package includes code, workflow records, financial and operational data, and collaboration history. It also reinforces the distinction between [discovery and knowledge]({{< ref "articles/discovery-to-knowledge" >}}): a model can find patterns quickly, but the organization still has to preserve the context that makes those patterns useful. The arithmetic is a provocation, not a valuation model.

## Why is the sale still contested?

The word “de-identified” does not end the argument.

The proposed sale excludes customer profiles and other personally identifiable information, and the agreement requires a third-party de-identification process. But the value of the dataset depends partly on preserving relationships across records: the same workflow, exception, decision, and result need to remain connected. That creates a tension between usefulness and the risk that individuals or small groups could be inferred from context.

The Association of Flight Attendants-CWA objected to the sale and sought stronger restrictions around employee data. A late bid from micro1 has added another procedural and commercial question. As of this draft, the bankruptcy court has not completed the sale approval process.

That privacy dispute strengthens the article’s argument. Retention is not a license to ignore consent, privilege, labor obligations, or data governance. It is a reason to treat the archive as an asset with owners, access rules, and a documented purpose.

## What is the strategic error?

The original [article on deleted emails]({{< ref "articles/deleted-emails" >}}) argued that deletion was not just housekeeping. It erased institutional memory: negotiations, design debates, customer fights, the sequence of a bad decision, and the tone of a good one. Generative models need exactly that texture. Structured reservation systems tell you what happened. Mail and chat tell you how people thought while it was happening.

**Spirit is the first clean, public, comparable event that puts money around that claim.**

A going concern would not necessarily sell the same corpus for $10 million. Going concerns use the data. Distressed estates sell it. That is why the story is so sharp. The company died. The operational language it produced did not.

Two implications follow.

First, retention is now an investment decision, not just a hygiene policy. The question is no longer “what is the cheapest way to stay inside the mailbox cap?” It is “what is the option value of this corpus if models, buyers, or regulators want it in ten years?” Option value is not infinite. Privilege, privacy, and union objections show the other side of the ledger. But zero retention is no longer the default rational answer.

Second, cost-center IT systematically misprices tail assets. Storage looked expensive because it was measured against this year’s opex. The same terabytes look cheap when measured against a multimillion-dollar auction, or against the cost of reconstructing process knowledge from interviews after the people have left. The error was not the spreadsheet. It was the time horizon on the spreadsheet.

## What should companies keep now?

Not everything. Spam, newsletter sludge, and duplicated attachments were never the point. The original mandate failed because it was a volume cap, not a value filter.

The Spirit package offers a useful filter:

- Threaded work mail, not the all-hands blast
- Decision trails attached to deals, incidents, and product changes
- Cross-functional argument, especially the exchange that never made it into the SOP
- Code review, tickets, and the chat that explains why the ticket was wrong
- Operational exceptions: the irregular operation, the refund fight, and the vendor escalation

That is “non-essential” only if your model of the firm is last year’s org chart. It is essential if your model of the firm is a system that has to be learned by a machine.

Storage in 2026 is not the 2015 constraint. Object storage, cold tiers, and cheaper capacity have changed the cost curve. The scarce resource is no longer disk. It is judgment about what future models cannot reconstruct.

## What should the bill be?

In the first article, I wrote that we did not just reduce storage costs. We erased the raw material of future intelligence.

Spirit put a sticker on that raw material, even if the final buyer and final price remain unsettled.

Ten million dollars, offered by Google for the enterprise data of an airline that no longer exists, is enough to change the conversation. If your retention policy still reads like a 2015 storage-savings program, you are not controlling cost. You are writing down an asset you have not marked to market.

Keep with purpose. Delete with a reason that will still make sense when someone else is willing to pay millions for what you threw away.

{{< faq >}}
  {{% faq-item question="Did Google buy Spirit Airlines’ emails?" %}}
  Google won the bankruptcy auction and agreed to pay $10 million for Spirit’s de-identified enterprise data, but the sale remained subject to court approval and later attracted a competing $12.5 million bid from micro1.
  {{% /faq-item %}}
  {{% faq-item question="What makes corporate email valuable for AI?" %}}
  Email and chat capture decisions, exceptions, disagreements, and context that structured systems often omit. Combined with code, workflow, and operating data, they show how an organization actually worked over time.
  {{% /faq-item %}}
  {{% faq-item question="Should companies keep every email forever?" %}}
  No. Companies should retain high-value decision trails and operational context under clear privacy, privilege, access, and deletion rules. The goal is purposeful retention, not indiscriminate accumulation.
  {{% /faq-item %}}
{{< /faq >}}

*Featured image: [A view of the server room at The National Archives](https://commons.wikimedia.org/wiki/File:A_view_of_the_server_room_at_The_National_Archives.jpg), by The National Archives (UK), used under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).*
