# Assignment Proposal

## Title

Crypto & Stock Alerts Telegram Bot — A DevOps Pipeline for a Notification Service

## Names and KTH ID

  - Jafar (jafarm@kth.se)
  - Gabriel (gaag2@kth.se)

## Deadline

26 September

## Category

Project

## Description

We will build and operate a small Telegram notification service for cryptocurrency and stock price alerts. Users can subscribe to a symbol and define a target price or percentage-change threshold. The application periodically retrieves market prices from external APIs and sends a Telegram notification when an alert condition is reached. Alert subscriptions and state are stored persistently. The application will be written in Python and containerized with Docker.

The main focus of the project is the DevOps workflow around the application, rather than the complexity of the bot itself. The project will include:

- CI: on every pull request or push, GitHub Actions will run linting and automated tests and build the Docker image.
- CD: after a successful merge to the main branch, the Docker image will be published to GitHub Container Registry and automatically deployed to the runtime environment.
- Infrastructure as Code: Terraform will provision the deployment host and networking, and Docker Compose will define the application and its runtime configuration on that host, so the service can be recreated reproducibly.
- Development platform: GitHub will be used with issues, pull requests, branch protection, and required CI checks.
- Quality and security automation: static analysis and dependency/container security checks will be integrated into CI.
- Secrets management: the Telegram bot token and market-data API credentials will be provided through GitHub Actions secrets/environment variables and will not be stored in the repository.
- AI-assisted tools: any use of AI-assisted development tools will be documented, including what they were used for and how the generated output was reviewed.

The repository will contain the application code, tests, Docker configuration, CI/CD workflows, infrastructure/deployment configuration, and documentation required to reproduce the complete system, together with a short report describing the architecture, CI/CD workflow, infrastructure setup, security and quality automation, tooling choices, and limitations of the system.

**Relevance**

This project demonstrates a complete DevOps workflow for a long-running service. Each code change is automatically tested, analyzed, and packaged through CI, while accepted changes are automatically published and deployed through CD. The deployment environment is provisioned and defined as code, making it reproducible rather than manually configured. The application also introduces practical DevOps concerns such as external service dependencies, persistent state, secrets management, scheduled background work, containerization, automated security checks, and deployment reliability. This keeps the application itself relatively small while allowing us to focus on designing, implementing, testing, and explaining an end-to-end DevOps pipeline.
