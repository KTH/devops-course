# Assignment Proposal

## Title

Demo proposal - SLO-Gated Canary Rollback in Kubernetes using ArgoCD

## Names and KTH ID

  - Ettore Mugisha Cirillo (emcir@kth.se)
  - Juozas Skarbalius (juozas@kth.se)

## Deadline

- Week 3

## Category

- Demo


## Description

We want to demonstrate how canary deployment can be used in Kubernetes cluster containing nodes of the 
same application using metrics provided by Prometheus to determine whether the new version of the application
should be rolled back or to become fully deployed. Our approach would involve deploying the new version to only 20% of the pods, while keeping current stable version in the rest of the nodes, and redirecting the same proportions of incoming traffic to those two clusters. Then, we plan to use Argo Rollouts to automatically detect whether the newly deployed version nodes adhere to the expected levels of service level objectives (SLOs) based on Prometheus metrics provided by each node. In case of incompliance of such SLOs, automatic rollback would be initiated. Otherwise, new version would be deployed to all available pods (or replace existing ones). We also plan to discuss drawbacks and benefits of such approach during our presentation.

**Relevance**

This demo reflects DevOPS principles by showing how observability data (i.e., in this case metrics) can be used to detect deviations from the expected metrics requirements and automatically issue rollbacks if needed. This approach provides the development teams with the ability to reduce the blast radius of possibly faulty deployments in production with the assumption that such faults were not detected before production.