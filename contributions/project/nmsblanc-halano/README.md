# Assignment Proposal

## Title

End-to-End DevOps Pipeline for a messaging web application

## Names and KTH ID

  - Halan Ouensanga (halano@kth.se)
  - Nolan Blanc (nmsblanc@kth.se)

## Deadline

- Task 1

## Category

- Project

## Description

We want to build a complete DevOps pipeline around an existing small web app (React + Express + PostgreSQL, group messaging). The pipeline will include:

- Build and test (CI): GitHub Actions runs lint, unit tests and static analysis on every pull request.
- Deployment (CD): pull requests trigger integration tests against an ephemeral dev environment; merges to main deploy to a persistent staging environment and run E2E tests; releases promote the same validated Docker image to production.
- Infrastructure as code: all cloud resources (VMs, networking) are provisioned with Terraform, with a remote state backend and OIDC authentication to the cloud provider.
- Development platform: code and pull request flow live on GitHub, with branch protection and required reviews.
- Quality and security automation: SonarQube static analysis, dependency and secret scanning run on every pull request and block merges on findings.
- AI-assisted tools: documented continuously in AI_USAGE.md, covered in detail in the report.

**Relevance**

This project demonstrates a full promotion pipeline (dev → staging → production) built around a single immutable artifact rather than three independent deployments, so what gets tested is exactly what gets released. It combines CI, CD and IaC in one coherent workflow, and includes deliberate trade-offs (ephemeral vs. persistent environments, network exposure restricted per environment) that we justify explicitly in the report rather than leaving implicit.

