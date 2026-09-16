# Assignment Proposal

## Title

Preventing Version Skew Between Independently Deployed Services

## Names and KTH ID

- Miami Alvelistin (miami@kth.se)
- Albin Wallenius Woxnerud (alww@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

Two services in separate repositories can both pass CI and still break when deployed together. Each pipeline tests only its own service, so the exact production combination may never be tested.

We demonstrate this with a provider and consumer over HTTP. Both have independent GitHub Actions pipelines that test, build, push and deploy.

First, both services receive matching API changes. Both pipelines pass, but deployment order briefly creates an incompatible pair and the app breaks.

Then we fix it by pinning both image digests in one release manifest, testing that exact pair and deploying them together. Only tested combinations reach production.

**Relevance**

Continuous Deployment is often described one service at a time, but real systems depend on services staying compatible. A green pipeline proves one service works, not that the deployed combination does.

We also cover the limits of coordinated releases. Rollouts can still create brief version mismatches, so breaking contract changes should remain backward compatible. Coupling releases also reduces service independence, and our local deployment uses a trusted self-hosted runner.
