
# Assignment Proposal

## Title

An Empirical Study on Kubernetes Operator Bugs

## Names and KTH ID

  - Adrian Grund (agrund@kth.se)
  - Alexander Runebou (alerun@kth.se)

## Deadline

Week 3

## Category

Scientific paper

## Description

We will present _"An Empirical Study on Kubernetes Operator Bugs"_ by Xu, Gao, and Wei (ISSTA '24, ACM SIGSOFT International Symposium on Software Testing and Analysis, https://dl.acm.org/doi/abs/10.1145/3650212.3680396), a study of operator bugs collected from open-source Kubernetes operators. Our presentation will cover the operator control loop and the paper's four root-cause categories (access control misconfiguration, incorrect CRD, incorrect state observation and analysis, incorrect reconciliation). Then we will give some specific examples taken directly from the paper's worked examples. We will frame this component explicitly through the CD lens: an operator's reconcile loop is itself a form of continuous deployment, since it observes a declared desired state and drives the live cluster towards it without human intervention. Thus, the bug patterns the paper identifies are effectively CD-pipeline failure modes rather than generic application bugs.

We're contrasting the empirical study with two papers it doesn't cite itself: "Breaking the Bulkhead" (2025), which looks at Kubernetes operator misconfigurations as a security issue rather than a reliability one, and a 2025 paper on resilience in cloud-edge Kubernetes deployments that uses fault injection instead of mining historical bug reports. This gives us two points of comparison: how deep versus broad the bug coverage is, and testing prospectively versus analysing bugs after the fact.

**Relevance**

The paper's subject, the reconciliation loop of Kubernetes operators, is a declarative continuous deployment mechanism that automatically drives a cluster's actual state towards a desired state, making it a direct fit for week 3's CD theme. The reconciliation bugs (synchronization failures, reconciliation loops, incorrect ordering of resource operations) are directly relevant to anyone using Kubernetes-based CD pipelines. Its findings on silent failures and detection gaps in existing testing tools point to open problems in verifying automated deployment correctness.
