# Assignment Proposal

## Title

Crypto & Stock Alerts Telegram Bot — A DevOps Pipeline for a Notification Service

## Names and KTH ID

  - Jafar (jafarm@kth.se)
  - Gabriel (gaag2@kth.se)

## Deadline

Task 1

Target completion: around Week 5 (23-26/09/2026), ahead of the Oct 11 23:59 Stockholm hard deadline for async tasks.

## Category

Project

## Description

We will build and operate a Telegram bot that lets users subscribe to price alerts for cryptocurrencies (via a public exchange/market-data API such as CoinGecko or Binance) and stocks (via a market-data API such as Alpha Vantage or Yahoo Finance). Users interact with the bot to set a symbol and a target price/percentage-change threshold; a background scheduler periodically polls prices and pushes a Telegram notification when a threshold is crossed. Subscriptions and alert state are persisted in a database.

The core of this proposal is not the bot itself but the DevOps pipeline wrapped around it, covering all mandatory project criteria:

- **Application stack**: the bot is implemented in Python with `python-telegram-bot`, using APScheduler for periodic price polling against the CoinGecko API (crypto) and Alpha Vantage or Yahoo Finance API (stocks); subscriptions and alert state are persisted in SQLite (or PostgreSQL); the bot is containerized with Docker.
- **Automated build and testing (CI)**: GitHub Actions workflow that lints, runs unit tests (pytest) and builds the Docker image on every push/PR.
- **Automated deployment/delivery (CD)**: a GitHub Actions workflow that, on merge to the main branch, publishes the Docker image to GitHub Container Registry (GHCR) and triggers a deployment to the runtime host.
- **Infrastructure as Code**: the deployment target (a small VM or container host) and its configuration (Docker runtime, environment/secrets wiring, networking) will be defined declaratively (Terraform for provisioning, Ansible or a Docker Compose file for configuration), so the environment can be recreated from code.
- **Modern development platform**: GitHub, using issues/PRs, branch protection and required status checks for the CI pipeline.
- **Quality/security automation**: Dependabot for dependency updates, CodeQL static analysis, and a container image scan (e.g., Trivy) in the CI pipeline; secrets (bot token, API keys) are managed via GitHub Actions encrypted secrets and never committed.
- **Documented use of AI-assisted tools**: any AI-assisted coding tool used during development (e.g., an AI coding assistant for boilerplate, CI config drafting or code review suggestions) will be explicitly documented in the final report, including what it was used for and what was authored/reviewed by us. All design decisions, implementation and testing are our own work.
- **Project repository**: a fully functional repository with all code, configuration (CI/CD workflows, Dockerfile, IaC scripts) and documentation needed to build, test and run the bot end to end.
- **Short report (2-3 pages)**: architecture diagram and explanation, justification of tooling/design choices, description of how CI, CD, IaC and quality/security automation interact, and a reflection on limitations and trade-offs.

**Relevance**

This project is a direct, hands-on demonstration of an integrated DevOps workflow: every code change is automatically built, tested and security/quality-checked (CI, static analysis, dependency and container scanning), and every merge is automatically packaged and deployed to infrastructure that is itself defined and provisioned as code (CD + IaC). Because the bot depends on external APIs, secrets and a long-running scheduled process, it forces us to make real decisions about configuration management, secret handling and deployment strategy — the same concerns that arise in production DevOps pipelines — while staying small enough to fully understand, operate and explain within the scope of the course.
