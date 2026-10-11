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

Project repository: https://github.com/a-runebou/dd2482_project

We built Schedular, a crab.fit-style group scheduling app, from scratch: a React
and TypeScript frontend, a Python FastAPI backend, a PostgreSQL database, KTH schedule
import, group creation, availability voting, calendar export, and email reminders. The
codebase was developed with AI assistance based on an architecture plan and API contracts
defined up-front. 

CI on GitHub Actions runs automated tests, linting, static checks, and security scanning. 
Infrastructure is defined as code: Docker Compose for development deployment to a Raspberry Pi 
and Kubernetes manifests for production deployment on Azure. CD automatically deploys to the
development environment on pushes to `develop` while production releases are managed through a 
controlled GitHub Actions workflow. Both environments use containerized services, health checks, 
and rollback mechanisms. 

**Relevance:** The project integrates the core DevOps practices required by the course in
one coherent system: automated CI (tests, linting, dependency/vulnerability scanning),
automated CD to both a dev and a production environment, infrastructure as code for both
deployment targets, and monitoring and recovery mechanisms.
