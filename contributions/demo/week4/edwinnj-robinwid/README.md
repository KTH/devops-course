# Assignment Proposal

## Title

_Automating investigating and resolving database errors using HolmesGPT_

## Names and KTH ID

  - Edwin Nordås Jogensjö (edwinnj@kth.se)
  - Robin Widjeback (robinwid@kth.se)

## Deadline

- Week 4

## Category

- Demo

## Description

We will demo investigating a database failure and automatically suggesting a PR to fix the failure with HolmesGPT. The Holmes environment, the database and the demo api will be kept inside a Kubernetes cluster.

The storyline of the demo will follow these points:
  1. App is healthy
  2. We manually introduce a MongoDB problem
  3. App starts slowing down or displays an error
  4. We manually alert Holmes about the incident
  5. Holmes investigates
  6. Holmes identifies MongoDB-related code problem
  7. Holmes modifies repository
  8. Github PR is created by Holmes

**Relevance**

We will show relevance to DevOps by partly automating the feedback loop. That is, when something goes wrong, we only have to alert Holmes which starts the development process and submits a PR. Since the development will be automated by using AI, the demo will be related to AIOps where operations will be carried out by HolmesGPT.
