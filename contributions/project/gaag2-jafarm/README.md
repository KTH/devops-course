# Assignment Proposal

## Title

Crypto & Stock Alerts Telegram Bot — A DevOps Pipeline for a Notification Service

## Names and KTH ID

  - Jafar (jafarm@kth.se)
  - Gabriel (gaag2@kth.se)

## Deadline

26 September 2026

## Category

Project

## Description

We plan to build and operate a Telegram bot that lets users subscribe to price alerts for cryptocurrencies and stocks. The bot will be implemented in Python using python-telegram-bot, with APScheduler for periodic price polling against the CoinGecko API (crypto) and the Alpha Vantage or Yahoo Finance API (stocks). User subscriptions and alert state will be persisted in SQLite (or PostgreSQL), and the bot will be containerized with Docker. This makes the bot a suitable, self-contained application for integrating and evaluating a complete DevOps workflow.

The project will include:

CI: GitHub Actions will run linting, unit tests, and a Docker image build on every push and pull request.
CD: merges to the main branch will build a Docker image, push it to GitHub Container Registry, and automatically deploy it to the runtime host.
Infrastructure as Code: Terraform will provision the deployment environment (VM, networking, secrets wiring), and Docker Compose will configure the bot and its runtime dependencies on the provisioned host.
Development platform: GitHub will be used for source control, pull requests, GitHub Actions, and container images.
Quality and security automation: Dependabot for dependency updates, CodeQL for static analysis, and Trivy for container image vulnerability scanning.
AI-assisted tools: the use of AI tools during workflow development, CI/CD configuration, debugging, and code review will be documented; all design decisions and implementation are our own work.

All configuration, code, and documentation required to reproduce the system will be kept in the project repository, together with the required final report.

**Relevance**

This project demonstrates how CI, CD, Infrastructure as Code, containerization, and security automation can be integrated into a coherent DevOps workflow for a real-world application. Because the bot depends on external APIs, secrets, and a long-running scheduled process, the pipeline connects code changes, automated validation, infrastructure provisioning, and deployment into a reproducible delivery process.
