# Assignment Proposal

## Title

Demo proposal - Dependency-Aware Blue/Green Continuous Deployment with GitHub Actions

## Names and KTH ID

  - John Swärd (johnsw@kth.se)
  - Dimitris Bakalis (bakalis@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

We want to demonstrate a Continuous Deployment pipeline for three dependent
Spring Boot microservices (`users`, `auth`, `orders`, where `auth` depends on
`users` and `orders` depends on `auth`), built on GitHub Actions with a
self-hosted runner. On every push, the pipeline detects which services
changed, resolves their declared dependency graph to find every impacted
downstream service, and deploys each one in order using blue/green
deployment: a new version is started in a second, idle slot alongside the
currently serving one, smoke-tested directly, and only switched into live
traffic via nginx once it passes. If a service's deployment fails, its
previous slot keeps serving traffic untouched, and every service depending on
it is automatically blocked and skipped rather than deployed on top of a
broken dependency. This is built with **GitHub Actions** for CI/CD orchestration, a **self-hosted
runner** so the pipeline can deploy to our own machine, **Maven** and
**Docker** to build each service, and **nginx** as the single component that
holds stable ports and performs the zero-downtime traffic switch between
blue/green slots.

**Relevance**

This demo reflects core DevOps principles by showing how a change to one
service in a dependency chain can be safely and automatically propagated
through its dependents, with each deployment gated by its own health check
via zero-downtime blue/green deployment rather than a single all-or-nothing
rollout. This approach lets teams reduce the blast radius of a faulty
deployment to just the services that actually depend on it, without manual
intervention.
