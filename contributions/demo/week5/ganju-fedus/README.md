
# Assignment Proposal

## Title

Solving configuration drifts using ArgoCD's automated self-healing feature 

## Names and KTH ID

  - Alexandru Gânju (ganju@kth.se)
  - Robert Fedus (fedus@kth.se)

## Deadline

Week 5

## Category

Demo

## Description

We're going to present a simple scalable microservice deployed on a live Kubernetes cluster.
In a ConfigMap we'll have a feature flag for our app and showcase how drifts happen by manually making changes to some resources in the live cluster.
Then, we'll show how to use the auto-sync and self-healing features and how ArgoCD solves the drift by syncing from our git repository.
In the end, in the case of using a Horizontal Pod Autoscaler (HPA), ArgoCD will fight against it when the above features are enabled. We'll explain how and when you might want to ignore some drifts.

**Relevance**

From a DevOps perspective it is really important to have a maintainable and auditable infrastructure.
We chose ArgoCD because of its core features that enables DevOps Engineers to achive that by using GitOps principles (have the git repository act as the source of truth).
