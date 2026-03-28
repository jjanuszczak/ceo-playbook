---
title: "The Power of Decoupling"
date: 2022-10-28
# externalUrl: "https://medium.com/ubx-philippines/the-power-of-decoupling-491f3c4d2e40"
summary: "Explains why designing to interfaces and loosely coupling systems, teams, and processes lets organisations move faster, reduce risk, and test product‑market fit independently."
description: "Argues that the principle of coding to an interface extends beyond software: by decoupling sales from development and content from platform, teams can pre‑sell, iterate, and compose offerings without monolithic constraints. Provides practical examples and an actionable rule of thumb: look for false dependencies and introduce API‑like boundaries to unlock scalability, resilience, and faster learning."
categories:
   - "Strategy"
tags:
  - organizational-design
  - systems-thinking
  - long-term-thinking
showReadingTime: false
build:
  render: "false"
  list: "local"
---

*This article originally appeared on [Medium](https://medium.com/ubx-philippines/the-power-of-decoupling-491f3c4d2e40) on 2022-10-28*.

## And the Art of Removing Dependencies

In computer programming, one of the most powerful principles I ever learned is to **always code to an interface and never an implementation**. What does this mean? If the definition of the interface between two things that interact (e.g. like a client app and a back-end server) remains constant, the people building the client application and the people developing the back-end platform can work *independently* without worrying about breaking each other’s code when they make changes to their own code. Of course, there may always be some coordination required. Like when the meaning or intent (the *semantics*) of an interface changes even when the specification does not. But for the most part, it *removes dependencies* for development teams and allows for scalable and independent run-time *and design-time* performance. We say that components designed like this are *loosely coupled* versus intertwined or tightly coupled or monolithic. The whole rise of the API economy is largely based on exactly this principle: we can safely innovate on someone else’s services even if we do not know or have access to their underlying code because the API is an interface. API literally stands for **A**pplication **P**rogramming **I**nterface.

This is a very powerful concept that extends far beyond writing computer code! In any situation, always look for ways to decouple or loosely couple things that ultimately may need to work together. Let’s look at a couple real life examples beyond writing computer code.

## Decoupling Sales from Development

Building a working product is a dependency to people actually using it. However it is **not** a dependency to marketing and selling it! If you know what the product will do once built, then you have effectively defined an “interface” and you can market and sell to this specification *independently* of the actual product build. Why would we do this? So that we can test the product-market fit by triggering and measuring our potential customers’ interest in our product, get their first reaction and collect feedback. We can acquire customers before we invest significant resources into building something that may otherwise not resonate with the market even though we think it is a good idea! Proactive sales organizations often rally around this very principle articulated in a slightly different way: **always pre-sell your offer before building it**. You would be surprised how often this is done right under our noses without us even thinking about it: from pre-ordering books before they are published to buying tickets to a concert that will occur in 6 months time.

## Decoupling Content from Platform

A couple of years ago, my team looked at doing a government Public Private Partnership proposal. Given the size of the deal and the capital required to fund it, this required a joint venture entity for a consortium of companies to make the proposal viable. Crucially, while setting up the joint venture would have been a dependency to execution, it was not a dependency for writing the actual proposal! Since the nature and participants in the consortium were known, we had an “interface” around which we could write the proposal ahead of formally setting up the actual joint venture.

## An Actionable Principle

Often what seem like dependencies to our work are not. **Always look to decouple concerns in your work**. It can be subtle at times, but there are a lot of *false dependencies* that can quickly be cleared when we think of decoupling or loosely coupling the things that must be done.
