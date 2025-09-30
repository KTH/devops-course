# Assignment Proposal


## Title

Keeping track of third party and bloated dependencies using Dependabot

## Names and KTH ID


 - Tim Rundström (timru@kth.se)
 - Zhongmin Hu (zhongmin@kth.se)


## Deadline
- Week 6


## Category
- Presentation


## Description

In this presentation we will explain why having too many unchecked third party dependencies in a project poses a security risk (supply chain attack), especially for automated DevOps pipelines, and briefly go over the [SolarWinds Orion attack](https://www.encryptionconsulting.com/solarwinds-should-security-live-in-infosec-or-devops/) and MOVEIt supply chain attack as examples.

We will then present Dependabot, an automated tool from GItHub that can continuously scan dependencies for known vulnerabilities and/or new available updates, and automatically create alerts and pull requests in your repository to notify that an update is needed. We will explain how it can be configured, and why incorporating it into your workflow or pipeline can help mitigate the risk of supply chain attacks.

**Relevance**

Many times when a project grows in size and more dependencies are added to the stack, even a small vulnerability in a forgotten dependency can become catastrophic if left unchecked. This is especially important for DevOps where many steps of the pipeline are automated without human supervision, and Dependabot can help with detecting and remediating vulnerable dependencies before they can be exploited.
