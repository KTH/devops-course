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

Blue-green deployment is a release strategy that uses two identical production environments: one active environment serving users and one inactive environment. A new application version is deployed to the inactive environment and tested before production traffic is redirected to it. If the checks fail, the active environment continues serving traffic. If problems appear after the switch, traffic can quickly be redirected to the previous environment.

During the demo, deployed in [Killercoda](https://killercoda.com/) we will show a simple Continuous Deployment pipeline that:

1. Starts with the current application version running in the active environment.
2. Deploys a new version to the inactive environment.
3. Runs automated health checks against the new version.
4. Switches traffic to the new environment when the checks pass.
5. Demonstrates a failed deployment where health checks prevent a faulty version from receiving traffic.
6. Demonstrates a rollback by redirecting traffic to the previous working environment.

This will allow us to compare successful and unsuccessful deployments and show how blue-green deployment can reduce downtime and deployment risk.

**Relevance**

Continuous Deployment is an important DevOps practice for releasing changes quickly and safely. This demo illustrates how automated validation, failure handling, traffic switching, and rollback can reduce production downtime and prevent faulty releases from reaching users.
