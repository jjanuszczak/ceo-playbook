---
title: "Flatpeak: The Missing Layer of the Energy Transition"
date: 2026-01-26
summary: "Why your EV is flying blind, and how Flatpeak—founded by the architect of M-PESA—is building the 'Stripe for Energy' to fix it."
description: "At 1882 Energy Ventures, we look for the infrastructure that unlocks decentralized energy. Flatpeak is building the API layer that allows smart devices to trade energy like a currency, bypassing legacy grid bottlenecks."
categories:
  - "Energy Transition"
tags:
  - "energy-markets"
  - "api-economy"
  - "electric-vehicles"
  - "platform-economics"
draft: false
---

At [1882 Energy Ventures](https://www.1882energyventures.com/), we talk about decentralized energy: electric vehicles (EVs), batteries, solar panels, and the sheer physics of moving electrons. But if you look closely at the Energy Transition, you realize something that is a bit crazy: **The hardware is flying blind.**

If you buy a state-of-the-art electric vehicle today, or a smart air conditioner, that device has almost no idea how much electricity costs *right now*. It doesn't know if the grid is dirty or clean. It doesn't know if you're paying 10 cents or 50 cents per kilowatt-hour.

It is like trying to run an algorithmic trading firm, but you only get the stock prices once a month via a paper statement in the mail.

Enter **Flatpeak**.

I believe this might be the most important piece of infrastructure you’ve never heard of. They are building the "Stripe for Energy," and their story involves the legendary M-PESA payment network, the central nervous system of the UK power grid, and a counter-intuitive secret about how utility companies actually make money.

## The Origin: From Kenya to the Grid

To understand Flatpeak, you have to understand its founders.

**Matthew Roderick** is an engineer’s engineer. Before energy, he was the Chief Architect and CTO of **M-PESA**, the mobile money service that banked the unbanked population of Kenya. Matt’s superpower is taking complex, regulated, messy systems and turning them into something simple enough to work on a Nokia brick phone.

After M-PESA, Matt shifted his focus to the UK grid, specifically the Smart DCC (Data Communications Company). It was here that he aligned with **Alex Alenberg**, an MIT grad with a deep background in defense and connectivity. Together, they tackled the government’s massive project to connect 50+ million smart meters to the grid.

They built the plumbing and saw the "Matrix" of energy data. But they also saw the problem: The data was locked up.

If you were a multinational device provider like Samsung, or a startup building EV chargers, you couldn't just "ping" the grid to ask for the price of power. You had to be a licensed energy supplier, which takes years and millions of dollars—only to access a tiny subset of customers.

In 2022, Matt and Alex officially teamed up to solve this, realizing that **energy tariffs are the new payments code**.

## The Tech Deep Dive: Inside the "Stripe for Energy"

We often hear companies call themselves the "Stripe for X," but looking at Flatpeak, the analogy is shockingly accurate. Just as Stripe wraps the complex banking system in a few lines of code, Flatpeak wraps the chaotic global energy grid in a clean API.

Consider the following examples:

### 1. The "Checkout" Experience
Flatpeak has a product called **Flatpeak Connect**. It is literally a UI widget, identical in concept to "Stripe Checkout" or "Plaid Link."
*   **The User Flow:** A user opens their EV charging app. They click "Connect Utility." Flatpeak handles the authentication with the utility company (whether it's PG&E in California or British Gas in the UK).
*   **The Result:** The app suddenly knows everything about that user's energy contract.

### 2. The "Intelligence" endpoint
This is where the magic happens. Users don't want to look at graphs; they want their car to just work.
Flatpeak exposes an API to handle exactly this. A hardware device (like a Tesla) sends a request: *"I need 40kWh of energy by 7:00 AM. Here is my max charging speed."*

Flatpeak’s API calculates the optimal 15-minute windows during the night when energy is cheapest (and usually greenest) and sends that schedule back to the car. This enables **Automated Load Shifting** without the user lifting a finger.

### 3. The Big Unlock: Smart Tariffs Without Smart Meters
This is the most critical update to our understanding of the grid. Historically, we believed you couldn't have dynamic pricing without a utility-installed Smart Meter on the side of your house.

Flatpeak proves this wrong.

Modern assets—EV chargers, inverters, heat pumps—have their *own* internal, revenue-grade meters. Flatpeak allows utilities to treat the **device as the meter**.
*   **The Scenario:** You live in a jurisdiction (like Germany or the Philippines) with low smart meter penetration.
*   **The Fix:** Flatpeak can isolate the EV charging load using the charger's internal data. The utility can bill the *car* at a cheap, dynamic rate, while billing the rest of the *house* at the standard flat rate.

This allows developing markets to "leapfrog" the expensive infrastructure phase and go straight to dynamic pricing.

## The Playbook: The Counter-Intuitive Margin

Why would utilities let Flatpeak do this? Why would they share their data?

**The Secret: Utilities make more margin when energy is cheap.**

It sounds backwards. But when energy prices are high (peak demand), utilities are often turning on expensive, dirty thermal plants (peaker plants) or upgrading low-voltage wires to prevent transformers from blowing up. Their margins are razor-thin or negative.

But when energy is cheap (wind is blowing, sun is shining), the marginal cost of that energy is near zero. If Flatpeak can shift consumption to those cheap times, the utility makes a fatter margin. It’s the rare "Win-Win-Win":
1.  **Consumer:** Saves money.
2.  **Utility:** Makes higher margin and defers CapEx.
3.  **Planet:** Uses green electrons instead of brown ones.

## The Grading: High Potential

Flatpeak is currently a Seed-stage company, but the macro tailwinds are undeniable. They are essentially building the "global roaming" layer for energy hardware.

Major OEMs (Chinese battery makers, European EV manufacturers) face a fragmented world. They want to sell one device that works in 50 countries. They can't integrate with 50 different national grids. Flatpeak offers them one API to rule them all.

The future of energy isn't just about building more power plants. **It's about building the digital layer that tells the electrons where to go**.
