# Assignment Proposal

## Title

CI/CD and Infrastructure as Code for Conduit

## Names and KTH ID

- Oscar Walter (owalter@kth.se)
- Gabriel Räätäri Nyström (grn@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We will implement a DevOps pipeline around [Conduit](https://github.com/TonyMckes/conduit-realworld-example-app), an open-source application using React, Express, and PostgreSQL. The pipeline will include:

- **CI**: GitHub Actions for builds, linting, unit tests, and integration tests with a temporary PostgreSQL database on pull requests and pushes to main.
- **CD**: GitHub Actions for publishing commit-tagged Docker images to GitHub Container Registry after checks pass on main, then running the published image with PostgreSQL on a temporary GitHub-hosted runner for automated smoke tests.
- **IaC**: Docker Compose for reproducible application and database environments, used for deployment verification in CI and local deployment.
- **Platform**: GitHub with branch protection, required status checks, and pull-request reviews.
- **Security**: npm audit for dependency vulnerability checks and Dependabot for dependency updates.
- **AI tools**: Codex for assistance with configuration, debugging, and tests, with its use and our verification of suggestions documented.

**Relevance**

This project integrates testing, security checks, infrastructure configuration, and continuous delivery into a reproducible workflow for an existing web application.
