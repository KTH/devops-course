# Assignment Proposal

## Title

Kubernetes Policy-as-Code tutorial with Kyverno in Killercoda

## Names and KTH ID

  - Hasan Kalzi (kalzi@kth.se)
  - Tobias Bjurström (tbju@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

**Completed tutorial:** [Run in Killercoda](https://killercoda.com/hasan-k/scenario/kubernetes-policy-as-code).

**Source repository:** [Hasan-Kalzi/kalzi-tbju-kyverno-killercoda](https://github.com/Hasan-Kalzi/kalzi-tbju-kyverno-killercoda).

**Accepted proposal:** [#3033](https://github.com/KTH/devops-course/pull/3033).

**Peer review:** [Feedback from Robert and Nalin](https://github.com/KTH/devops-course/pull/3033#issuecomment-6068960081). Following their review, we clarified policy-as-code, Kyverno and admission control, explained the exact hostPath violation, and described how the verification scripts check the expected outcomes.

We have created an executable Killercoda tutorial demonstrating how Kubernetes security policies can be tested before deployment and enforced inside a Kubernetes cluster using Kyverno.

Killercoda provides a browser-based terminal and a temporary single-node Kubernetes cluster. Automated setup scripts install pinned versions of Kyverno and the Kyverno CLI, wait until the required components are ready, and prepare the policy and workload manifests.
The tutorial explains the architecture and the interaction between the Kyverno CLI, the Kubernetes API server, the Kyverno admission controller, the policy, and the workload. It also discusses design decisions such as pre-deployment checking versus admission-time enforcement and strict enforcement versus gradual policy adoption.

**Relevance**

Security controls are often applied too late or inconsistently when they depend on manual review. Policy-as-Code makes security requirements declarative, versionable, testable, and reproducible.
This tutorial demonstrates a DevSecOps workflow in which developers receive fast feedback before deployment while the Kubernetes cluster independently enforces the same security requirements at admission time. The approach shifts security feedback earlier in the development process while maintaining a reliable enforcement boundary in the deployment environment.
