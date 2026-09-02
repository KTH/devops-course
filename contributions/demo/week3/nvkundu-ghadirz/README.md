# Assignment Proposal

## Title

Live CD Rollback on a To-Do List App, Comparing Manual vs. Automated Rollback

## Names and KTH ID

- Nalin Kundu (nvkundu@kth.se)
- Hossein Ghadirzadeh (ghadirz@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

We'll use a small, standalone to-do list app (static frontend + a lightweight API) built specifically for this demo to demonstrate automated rollback mechanics within CD.

Our CI/CD pipeline (GitHub Actions) deploys the app to [Render or a similar platform]. Right after each deployment, an automated health check runs against the live app. During the demo, we'll ship a deliberately broken change live (the health check detects the failure on its own), and the pipeline automatically rolls back to the last healthy release, with no manual intervention. We'll walk through the rollback strategy we chose and why we designed it to trigger automatically rather than being triggered by a developer.

**Relevance**

Rollback is a core DevOps practice: the ability to recover quickly and safely from a bad deployment is what makes frequent, automated releases viable. What we specifically want to highlight is the difference between a rollback a developer has to trigger manually and one the system performs on its own the moment it detects a problem. Running automatically is what actually makes continuous deployment safe to run unattended and at high frequency, which is the core promise of DevOps automation.