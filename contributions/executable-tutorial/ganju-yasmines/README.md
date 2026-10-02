# Assignment Proposal

## Title

Contract Testing: Pact and the Pact Broker

## Names and KTH ID

- Alexandru Gânju (ganju@kth.se)
- Yasmine Schüllerqvist (yasmines@kth.se)

## Deadline

- Task 1

## Category

- Executable tutorial

## Description

We will create an executable Killercoda tutorial on contract testing between microservices
with Pact. Everything runs in Docker (two Python services, the Pact Broker and its database),
with a Git hook standing in for CI, so no accounts are needed.

A user service renames a JSON field: its own tests pass, but the order service that depends
on it breaks. The learner writes a consumer contract with Pact (using type matchers so the
provider can still evolve), verifies the real provider against it using provider states, and
publishes the results to the Pact Broker. They then verify two consumer versions against three
provider versions and explore the resulting compatibility matrix. Starting from what is
recorded as deployed in production, they use `can-i-deploy` to discover that the rename can
only be released safely in three steps (expand, migrate, contract), with a Git pre-push hook
blocking unsafe deployments. Each step has an automated check, and the tutorial ends with a
reflection on when contract testing is worth it and its limits.

**Intended learning outcomes.** The learner can explain why separate test suites miss
breaking API changes, write and verify a Pact contract, read the compatibility matrix, and
use `can-i-deploy` to decide a safe deployment order.

**Relevance**
Contract testing lets teams deploy services independently: API
compatibility is checked in seconds in CI instead of in slow end-to-end environments, and
`can-i-deploy` acts as an automated deployment gate.

