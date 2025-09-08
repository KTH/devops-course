# Assignment Proposal

## Title

How to Safely Perform Production Database Updates: Backward-Compatible Database Changes
## Names and KTH ID

- Reza Hosseini (rezahos@kth.se)
- Adam Fridén Rasmussen (ajfr2@kth.se)

## Deadline

Week 3

## Category

Presentation

## Description

We’ll show how to evolve a production database without downtime using backward-compatible schema changes and a safe deploy order (expand → migrate → contract). We will explain why coupling app and DB changes is risky and how small, staged changes reduce outages.

What we’ll cover :

* The core pattern: expand → migrate → contract
* Minimal, safe steps: add new schema → dual-write + backfill → switch reads → retire old schema
* Monitoring and reaching zero discrepancy
* An example of how this is done practically

**Relevance**

This topic has direct relevance to DevOps and Continuous Delivery. Database Migration is often the bottleneck when it comes to continuously deploy while ensuring nothing breaks in production. This topic shows a safe and fast practice on how to perform migration, so teams can ship faster without breaking production.
