# Assignment Proposal

## Title
Project: group scheduling app with IaC multi-deployment

## Names and KTH ID

<Adrian Grund> (agrund@kth.se)
<Alexander Runebou> (alerun@kth.se)

## Deadline
11 October 2026

## Category
Project

## Description
We are building Schedular, a crab.fit-style group scheduling app, from scratch: a React
and TypeScript frontend, a Python backend (likely FastAPI), a database (TBD), KTH schedule
import, group creation, availability voting, calendar export and email reminders. The
codebase itself is largely AI-generated from an architecture plan we write up-front
(including API contracts).

CI on GitHub Actions runs the test suite, linting and static checks, and at least one
dependency/vulnerability scanner on every push. Infrastructure is defined as code: a
docker-compose setup for a dev deployment to our KTH VM, and Kubernetes manifests for a
production deployment on Google Cloud or comparable, both provisioned and updated via GitHub Actions
pipelines. CD automatically pushes to the KTH VM on relevant branches and to the GCP
cluster on merges to main. GitHub is used as the development platform throughout (repo,
issues, Actions). Time permitting, we might extend this with a monitoring dashboard with
heartbeat/circuit-breaker checks between containers, and look into an MLOps component,
scoped after the relevant lectures.

**Relevance:** The project integrates the core DevOps practices required by the course in
one coherent system: automated CI (tests, lint, dependency/vulnerability scanning),
automated CD to both a dev and a production environment, infrastructure as code for both
deployment targets.