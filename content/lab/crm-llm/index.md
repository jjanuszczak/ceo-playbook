---
title: "From CRM App to LLM Knowledge Base: A Markdown-Native CRM for the Agent Era"
date: 2026-04-10
summary: "Exploring the shift from traditional CRM software to LLM-maintained knowledge bases, where structured markdown files serve as the system of record for the agent era."
description: "A domain-specific look at building a markdown-native CRM as an LLM knowledge base, emphasizing durability, auditability, and human-agent collaboration."
draft: false
categories: ["Technology"]
tags: ["artificial-intelligence", "knowledge-management", "software-engineering", "systems-thinking", "git", "open-source", "second-brain"]
---

Andrej Karpathy’s recent LLM Knowledge Bases idea is best understood as a shift in software architecture. Instead of treating the model as a stateless chatbot sitting on top of a pile of documents, the model incrementally compiles raw inputs into a persistent, structured, human-readable knowledge base. The durable artifact is not embeddings, not a hidden vector store, and not a proprietary SaaS backend. It is files.

{{< x user="karpathy" id="2039805659525644595" >}}

This CRM project is a domain-specific implementation of that same pattern:

{{< github repo="jjanuszczak/crm-logic" showThumbnail=true >}}

The core idea of the project is simple: the source of truth is a markdown vault, not an app. Companies, people, tasks, meetings, leads, opportunities, and fundraising deals are all stored as explicit records in structured markdown. Agents do not “own” the CRM. They operate on it. They ingest email and calendar data, propose updates, create or enrich records, refresh derived views, and surface next actions. But the durable system is the data itself.

That is exactly where this project overlaps with @karpathy’s LLM Knowledge Base framing. In both cases, the model is not just answering questions from a retrieval layer. It is maintaining a living corpus. The knowledge base is local-first, inspectable, diffable, and versioned with Git. It is designed to survive model changes, tool changes, and session resets. It is meant to compound.

## Similarities

There are several important similarities.

First, both systems reject the idea that useful AI memory has to begin with a vector database. Instead, they rely on structured files that can be read directly, rewritten incrementally, and curated over time.

Second, both assume that the most valuable artifact is not the prompt or the chat transcript, but the compiled knowledge object that remains after the interaction. In Karpathy’s framing, that is a personal wiki. In this project, it is a CRM memory system made of `Organizations`, `Accounts`, `Contacts`, `Deals`, `Opportunities`, `Activities`, `Notes`, `Tasks`, and generated views like `DASHBOARD.md`, `INTELLIGENCE.md`, and `RELATIONSHIP_MEMORY.md`.

Third, both are fundamentally **agent-compatible**. A human can read the files directly. An agent can read the same files, update them, synthesize them, and use them as working memory. That shared substrate matters. It reduces hidden state and makes AI work auditable.

## Differences

But this CRM project also differs from Karpathy’s more general idea in important ways.

Karpathy’s concept is broad. It is a general LLM-maintained knowledge base for research, projects, documents, and personal work. This CRM is narrower and more operational. It is not just a knowledge repository. It is a workflow system. It has explicit entity models, explicit state transitions, explicit task semantics, and explicit operational loops.

That changes the design.

A generic knowledge base can tolerate ambiguity. A CRM cannot. A person can be a `Contact`, a `Lead`, or both across time. A company can exist as an `Organization`, an `Account`, a `Deal`, and an `Opportunity`, but those records mean different things. A `waiting` task is not the same as a `todo` task. A note is not the same as an activity. A startup can be fundraising inventory without being a paid mandate. Those distinctions are not UI details. They are **business logic**.

That is why this project adds “skills” and scripts on top of the markdown base. The markdown vault is the memory layer, but the **skills are the mutation layer**. They encode workflows like workspace ingestion, lead conversion, dashboard refresh, opportunity management, intelligence scoring, and match generation. In Karpathy’s framing, the LLM knowledge base is the main story. Here, the more precise statement is: a CRM becomes an LLM knowledge base **plus domain schema plus workflows plus human judgment**.

That last part matters most: human judgment.

## New Philosophy for CRM

A normal CRM app assumes that the software is the authority and the user fills in fields. This project assumes the opposite. The authority is the human operator, the files are the durable record, and agents are assistants that propose, enrich, classify, and execute with review. Gmail and Calendar ingestion, for example, do not directly rewrite the CRM blindly. They stage activity updates, contact discoveries, lead decisions, opportunity suggestions, and task suggestions. The agent can automate parts of that flow, but the human remains in the loop where judgment is required.

{{< mermaid >}}
flowchart TD
    A["Google Workspace Inputs<br/>Gmail + Calendar"] --> B["Ingestion Layer<br/>crm-ingest-gws"]
    C["Human Inputs<br/>Calls, WhatsApp, in-person, judgment"] --> D["Agent Review Loop"]
    B --> E["Staging Files<br/>activity_updates, lead_decisions,<br/>task_suggestions, interactions"]
    E --> D
    D --> F["Canonical CRM Records<br/>Organizations, Accounts, Contacts,<br/>Leads, Opportunities, Deals,<br/>Activities, Notes, Tasks"]
    F --> G["Derived Views<br/>DASHBOARD.md<br/>INTELLIGENCE.md<br/>RELATIONSHIP_MEMORY.md"]
    F --> H["Git History<br/>Diffs, auditability, rollback"]
    G --> D
{{< /mermaid >}}

That is a very different philosophy from traditional CRM software.

Most CRMs are database-plus-UI products. Their strength is standardization, permissions, reporting, and multi-user process control. Their weakness is that they are rigid, shallow, and optimized for the fields the vendor imagined. They are good at pipeline hygiene and poor at real memory. They do not naturally store nuanced context, evolving relationship interpretation, investment theses, meeting notes, or partial convictions. They also tend to trap the system of record inside the application.

An LLM-native CRM flips that model.

The future version of a CRM may not be “an app” in the traditional sense at all. It may be:
* structured data files as the system of record
* domain schemas to keep the data coherent
* skills and scripts as reusable workflows
* agents as operators over the data
* human review at key decision points
* lightweight generated interfaces, not heavyweight primary UIs

In that world, the CRM is less like Salesforce and more like a living operational memory substrate.

{{< mermaid >}}
flowchart TD
    A["Unstructured Signals"] --> B["Normalization"]
    B --> C["Structured Records"]
    C --> D["Derived Intelligence"]
    D --> E["Operator Decisions"]
    E --> C
{{< /mermaid >}}

## Consequences

That has several consequences.

The first is **durability**. If the UI changes, the data remains. If the model changes, the data remains. If the agent changes, the data remains. If a workflow is wrong, it can be patched without migrating off a vendor.

The second is **transparency**. A markdown record, a Git diff, and a workflow log are easier to inspect than opaque AI behavior inside a SaaS platform.

The third is **composability**. Once the CRM is just a structured knowledge base, different agents can operate on it: ingestion agents, enrichment agents, task-review agents, opportunity agents, matchmaking agents, reporting agents.

The fourth is **personalization**. Traditional CRMs flatten all users toward the same ontology. A markdown-native CRM can encode the operating model of a specific person or firm: advisory work, founder support, investor mapping, relationship warmth, strategic notes, and nuanced task states that generic software rarely handles well.

The fifth is **epistemic discipline**. Because the record is explicit and reviewable, the system can distinguish between observed facts, inferred judgments, staged suggestions, and durable truth. That is critical for any serious AI-assisted operating system.

## Big Picture

The larger insight is that “knowledge base” is not a niche note-taking concept. It is a **new application architecture**.

Karpathy’s framing points to a world where LLMs are not mainly chat endpoints. They are compilers and maintainers of structured memory. This CRM project applies that idea to one of the most important but poorly served categories in software: **relationships**.

A relationship is not a ticket. It is not a row in a pipeline table. It is a compounding memory object made of people, interactions, obligations, opportunities, context, and timing. That is exactly the kind of thing LLM-maintained knowledge bases are good at, provided the system is grounded in durable files, explicit schemas, auditable workflows, and human supervision.

That is the real promise here: not “AI CRM” as a layer of automation on top of an old app, but **CRM rethought** as a maintained knowledge base with agents.

The long-term destination is not a smarter form. It is a better memory system.