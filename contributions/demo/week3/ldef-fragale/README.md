# Assignment Proposal

## Title

Safe Continuous Deployment with Blue-Green Deployment

## Names and KTH ID

  - Lorenzo Deflorian (ldef@kth.se)
  - Riccardo Fragale (fragale@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

This demo aims to show a simple Continuous Deployment pipeline using blue-green deployment. A new version is deployed to an inactive environment, health checked automatically and only then it is switched to receive oncoming traffic. If the checks fails, the new version is rejected and the current version stays live.

**Relevance**

Continuous Deployment is an important DevOps practice for releasing changes quickly and safely. This demo shows how important it is the process of failure handling and traffic switching to reduce as much as possible the downtime of production systems.
