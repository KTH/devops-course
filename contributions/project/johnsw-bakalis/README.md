# Assignment Proposal

## Title

Multi-environment CI/CD DevOps Infrastructure for Full-stack Typescript Webapp

## Names and KTH ID

  - John Swärd ([johnsw@kth.se](mailto:johnsw@kth.se))
  - Dimitrios Bakalis ([bakalis@kth.se](mailto:bakalis@kth.se))

## Deadline

- Task 3

## Category

- Project

## Description

We will build a dev → test → prod delivery pipeline for a True/Fake quiz game (web app) with a persistent leaderboard (React + Vite frontend, Express backend, PostgreSQL). Frontend and backend are written in TypeScript and each ships as its own Docker image.

- **Build and test (CI):** GitHub Actions runs path-filtered linting, type checking, unit tests and backend integration tests on every pull request, plus a check that new database migrations stay compatible with the previous release.
- **Deployment (CD):** on every push to the `dev`, `test` and `main` branches, images are built from that branch, tagged with the commit SHA and pushed to GHCR. Each branch is deployed to its own environment: dev and test automatically, prod after manual approval. Every deploy is followed by a smoke test, and a failed smoke test automatically rolls back to the last version that passed.
- **Infrastructure as code:** all three environments run locally in Docker and are defined in Terraform, with isolated per-environment state stored in a local MinIO bucket with state locking. A self-hosted runner, used only for deploy jobs, lets the pipeline reach the local Docker daemon.
- **Development platform:** GitHub, with protected `dev`, `test` and `main` branches, required status checks and GitHub Environments.
- **Quality and security automation:** Trivy image scanning, gitleaks and dependency review block merges on high-severity findings; Dependabot keeps dependencies up to date; Checkov scans the Terraform code.

Relevance

The project takes an ordinary web application and adds the practices the course covers: automated build, test and security checks on every change, infrastructure as code with isolated environments, and an immutable, commit-tagged image built for every environment branch. We also focus on failed deploys: rollback only works if the database schema stays compatible with the previous release, so migration safety is part of the pipeline. We will justify the key trade-offs in the report, such as running all environments on one host, building images separately per branch instead of promoting a single image, and using a self-hosted runner.
