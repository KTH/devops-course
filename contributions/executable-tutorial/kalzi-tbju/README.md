# Assignment Proposal

## Title

Kubernetes Policy-as-Code tutorial with Kyverno in Killercoda

## Names and KTH ID

  - Hazan Kalzi (kalzi@kth.se)
  - Tobias Bjurström (tbju@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

We will create an executable Killercoda tutorial demonstrating how Kubernetes security policies can be tested before deployment and enforced inside a Kubernetes cluster using Kyverno. 

Killercoda will provide a browser-based terminal and a temporary single-node Kubernetes cluster. Automated setup scripts will install pinned versions of Kyverno and the Kyverno CLI, wait until the required components are ready, and prepare the policy and workload manifests. 
The tutorial will explain the architecture and the interaction between the Kyverno CLI, the Kubernetes API server, the Kyverno admission controller, the policy, and the workload. It will also discuss design decisions such as pre-deployment checking versus admission-time enforcement and strict enforcement versus gradual policy adoption.

**Relevance**

Security controls are often applied too late or inconsistently when they depend on manual review. Policy-as-Code makes security requirements declarative, versionable, testable, and reproducible.
This tutorial demonstrates a DevSecOps workflow in which developers receive fast feedback before deployment while the Kubernetes cluster independently enforces the same security requirements at admission time. The approach shifts security feedback earlier in the development process while maintaining a reliable enforcement boundary in the deployment environment.
