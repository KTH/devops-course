# Assignment Proposal

## Title

State Reconciliation Defects in Infrastructure as Code

## Names and KTH ID

  - Halan Ouensanga (halano@kth.se)
  - Sangeetha Murugesan (sanmur@kth.se)

## Deadline

- Week 5

## Category

- Scientific paper

## Description

We want to present the FSE 2024 paper ["State Reconciliation Defects in Infrastructure as Code"](https://dl.acm.org/doi/10.1145/3660790), presenting state reconciliation: before applying any change, the orchestrator queries the current infrastructure state, compares it against the desired state defined in the script, and applies only the differences. This mechanism is what makes IaC different from simply re-running a script, but when reconciliation logic itself is buggy, the consequences can be severe and hard to detect. We plan to dive into the defect taxonomy derivation process (multi-phase open coding), the design of the heuristic-based LLM prompts used to generate defect-triggering playbooks, and the key empirical findings.


**Relevance**

State reconciliation is the core mechanism that distinguishes IaC from ordinary scripting, and it underpins how DevOps teams manage infrastructure at scale in CI/CD pipelines. This paper shows that defects in this reconciliation logic are both common and consequential, capable of causing configuration drift, silent misconfiguration, or security exposure across thousands of managed servers from a single bug. Understanding how these defects arise, and how they can be systematically detected using LLM-assisted testing, is directly relevant to anyone building or maintaining reliable, automated infrastructure pipelines in a DevOps context.
