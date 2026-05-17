---
title: "The Art of Strategic Forgetting: World Models and the Future of AI"
date: 2026-05-04
summary: "AI pioneer Yann LeCun argues that intelligence is the art of strategic forgetting. Discover why 'world models' and hierarchical abstraction are the keys to human-level AI."
description: "Yann LeCun, the Godfather of AI, recently shared his vision for the future of artificial intelligence. He argues that true intelligence requires finding the right level of abstraction—ignoring infinite subatomic detail to make long-term predictions about the world."
categories:
  - "Technology"
tags:
  - "artificial-intelligence"
  - "mental-models"
  - "systems-thinking"
  - "long-term-thinking"
  - "simulation"
showReadingTime: true
showTableOfContents: true
draft: false
status: "user-review"
# Pillar 2: Advanced Schema
about:
  - name: "Artificial General Intelligence"
    url: "https://en.wikipedia.org/wiki/Artificial_general_intelligence"
  - name: "World model (AI)"
    url: "https://en.wikipedia.org/wiki/World_model"
mentions:
  - name: "Yann LeCun"
    url: "https://en.wikipedia.org/wiki/Yann_LeCun"
  - name: "Meta Platforms"
    url: "https://en.wikipedia.org/wiki/Meta_Platforms"
citations:
  - title: "A path towards autonomous machine intelligence"
    url: "https://openreview.net/forum?id=BZ5a1r-kVsf"
---
[Yann LeCun](http://yann.lecun.com/) is a pioneering French-American computer scientist, currently serving as the Chief AI Scientist at Meta and a Silver Professor at New York University. Often hailed as one of the "Godfathers of AI," he was co-awarded the 2018 Turing Award for his foundational breakthroughs in deep learning and the development of Convolutional Neural Networks (CNNs), which revolutionized computer vision. Today, LeCun is a leading advocate for moving beyond current Large Language Models toward "World Models": autonomous systems capable of hierarchical abstraction, common sense, and human-level reasoning.

{{< quick-answer >}}
**World Models** are a proposed architecture for AI that moves beyond predicting the "next token" to understanding hierarchical abstractions of the real world. By practicing "strategic forgetting"—ignoring irrelevant, low-level data—an AI can create a conceptual map that allows for long-term reasoning and human-level planning.
{{< /quick-answer >}}

He recently shared the following perspective on intelligence:

> In principle, I could explain everything that is taking place in this room here, in terms of, let's say, Quantum field theory...I can reduce everything to physics. But, in fact, we don't because it would be completely impractical to simulate our brain processes in sufficient detail to predict our reactions to this talk by doing quantum field simulation.
>
> So, we invent abstractions, particles, atoms, molecules, in the living world, proteins, organelles, cells, organisms, individuals, societies, ecosystems. Every level of description in this hierarchy allows us to make longer-term predictions than the level below and ignores a lot of details about the level below. That's the essence of being able to understand the world.
> 
> There's a wonderful quote from Albert Einstein, which is the most incomprehensible thing about the world is that the world is comprehensible. And it could be because there are all those abstractions that we can derive that allow us to predict or explain certain behaviors of the world that would otherwise would be way too complicated for us to understand.
>
> So, the basic idea of understanding the world and modeling it and being able to make predictions is finding good, abstract representations that ignore the details that we cannot predict.

Intelligence is essentially the art of *strategic forgetting*. A "world model" (and the future of AI according to his argument) needs to **think in concepts rather than just data points**.

## Why is there a trap of "infinite detail"?

There is a trap of "infinite detail". In theory, Quantum Field Theory (QFT) is the "source code" of the universe. If you had a powerful enough computer, you could simulate every subatomic particle in your brain to predict exactly when you’ll blink.

But that is impractical. The "noise" of trillions of particles would drown out the signal of what’s actually happening. If you want to predict if someone will like a speech, you don't look at their electrons; you look at their facial expressions and their culture.

## How does the hierarchy of abstraction work?

To make sense of the world, we build a "ladder" of abstractions or descriptions. Each step up the ladder ignores the messy details of the step below it to find a new, useful pattern.

* Subatomic Particles &rarr; Atoms (Ignores quarks)
* Molecules &rarr; Cells (Ignores individual chemical bonds)
* Organisms &rarr; Societies (Ignores individual biology)

By moving up to "organisms," you can predict that a hungry cat will move toward a bowl of food. If you tried to predict that same movement using only particle physics, the math would be so complex it would be effectively impossible.

## Why is prediction the goal?

Keeping the end in mind: prediction is the goal! *"Every level...allows us to make longer-term predictions than the level below."*

Low level physics can predict what a particle does in a nanosecond. High level psychology can predict what a person will do next week (e.g., "They will go to work on Monday").

Intelligence, in LeCun's view, is the ability to find the **right level of abstraction for the task at hand**. If an AI is trying to drive a car, it shouldn't care about the molecular structure of the asphalt; it should care about the "abstract representation" of a "pothole."

## How do World Models impact AI?

LeCun is currently critical of Large Language Models because he believes they mostly predict the "next token" (the low-level detail) without truly understanding the "world model" (the high-level abstraction). He’s arguing that for AI to reach human-level intelligence, it must learn to perceive the world in these hierarchical layers, allowing it to plan long-term actions instead of just reacting to immediate data.

**The Takeaway**: You don't understand a forest by looking at the atoms in a leaf. You understand it by seeing the "Forest" as its own thing. Understanding is the process of ignoring what doesn't matter so you can see what does.

{{< faq >}}
  {{% faq-item question="What does Yann LeCun mean by 'strategic forgetting'?" %}}
  Strategic forgetting is the process of filtering out infinite, granular detail to focus on higher-level concepts. Just as humans ignore subatomic physics to understand that a hungry cat moves toward food, AI must ignore non-predictive noise to model the world effectively.
  {{% /faq-item %}}
  {{% faq-item question="Why are World Models considered superior to Large Language Models (LLMs)?" %}}
  Current LLMs excel at predicting the 'next token' (immediate data), but they lack a conceptual 'world model' (long-term reasoning). LeCun argues that human-level intelligence requires perceiving the world in hierarchical layers, which enables complex planning rather than mere reaction.
  {{% /faq-item %}}
  {{% faq-item question="How does hierarchical abstraction help AI improve its predictions?" %}}
  Each level of abstraction ignores the messy, low-level details of the layer below it, focusing instead on consistent patterns. This allows the AI to make predictions across larger time horizons, making it more efficient and capable of reasoning in real-world scenarios.
  {{% /faq-item %}}
{{< /faq >}}

## Watch the Lecture

If you have an hour, watch the whole lecture for yourself:

{{< youtubeLite id="ZbrfvMLZZK4" label="2026 Lemley Lecture Featuring AI Pioneer Yann LeCun" >}}

{{< related-posts title="Related Insights" paths="articles/beos,lab/chalk-circle" >}}
{{< read-next title="Read Next" link="articles/burke-lecture" buttonText="View more Insights" buttonLink="/articles/" >}}
