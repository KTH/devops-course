
# Assignment Proposal

## Title

An Empirical Study on Kubernetes Operator Bugs

## Names and KTH ID

  - Adrian Grund (agrund@kth.se)
  - Alexander Runebou (alerun@kth.se)

## Deadline

Week 5

## Category

Scientific paper

## Description

We will present _"An Empirical Study on Kubernetes Operator Bugs"_ by Xu, Gao, and Wei (ISSTA '24, ACM SIGSOFT International Symposium on Software Testing and Analysis, https://dl.acm.org/doi/abs/10.1145/3650212.3680396), a study of operator bugs collected from open-source Kubernetes operators. 

Our presentation will first explain how Kubernetes operators extend declarative infrastructure management. We will then present the paper's four root-cause categories (access control misconfiguration, incorrect CRD, incorrect state observation and analysis, incorrect reconciliation), together with some selected examples from the paper.


We will frame these findings from an Infrastructure-as-Code perspective. Traditional IaC tools describe infrastructure through configuration files or scripts, but Kubernetes operators use more complex management logic. Bugs in custom resource definitions, state observation, and reconciliation can therefore cause the actual infrastructure to diverge from the desired state. 

We're contrasting the empirical study with two papers it doesn't cite itself: "Breaking the Bulkhead" (2025), which looks at Kubernetes operator misconfigurations as a security issue rather than a reliability one, and a 2025 paper on resilience in cloud-edge Kubernetes deployments that uses fault injection instead of mining historical bug reports. This gives us two points of comparison: how deep versus broad the bug coverage is, and testing prospectively versus analysing bugs after the fact.

**Relevance**

The paper is relevant to week 5 because Kubernetes operators implement declarative and automated infrastructure management, which is closely related to IaC. Instead of manually configuring infrastructure, developers specify a desired state and the operator continously reconciles the actual system with that specification. 

