# Assignment Proposal

## Title
_Spin It Up, Shut It Down On-Demand Staging with IaC_

## Names and KTH ID

  - Alessandro Coli (acoli@kth.se)
  - Dania Sami (dsami@kth.se)

## Deadline

Week 5

## Category
Demo

## Description
Our demo will focus on on-demand staging as a DevOps workflow. We will demonstrate the full lifecycle of an ephemeral staging environment:

- Provision: Spin up a staging environment using IaC.
- Deploy: Run a simple containerized application and access it in the browser.
- Update live: Make a small change (e.g., update the app’s message or add an easter egg) and re-deploy, showing how environments can be iterated quickly.
- Tear down: Destroy the staging environment with a single command, leaving no leftovers.

The demo narrative ties directly to DevOps concerns:

- Cost savings – environments exist only when needed.
- Agility – fast iteration without long setup times.
- Compliance – consistency and reproducibility reduce drift and errors.


**Relevance**

Staging environments are critical for testing new features before production, but permanent staging systems are costly and often underutilized. Using Infrastructure as Code, developers can spin up staging environments on demand, use them for testing, and tear them down when finished. This saves costs, increases agility, and ensures consistency across environments, all key DevOps goals.

