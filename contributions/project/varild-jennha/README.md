# Assignment Proposal

## Title

Automated CI/CD Pipeline with Preview Environments

## Names and KTH ID

  - Jonathan Värild (varild@kth.se)
  - Jennifer Ha (jennha@kth.se)

## Deadline

11 October 2026

## Category

- Project

## Description

We have taken one of my [previous projects](https://github.com/JonathanVarild/IV1201-group7-recruitment-application) from another course and will build a complete DevOps workflow surrounding this project, including automated testing, deployment, infrastructure, and security. We have planned an extensive CI/CD pipeline as explained below which mostly will be implemented using GitHub Actions to deploy the application on a Virtual Private Server (VPS) with preview and production environments. Relevant checks are automatically made to ensure that everything works and that all changes to the codebase live up to the desired quality of the project.

On every commit, we run a quick Continuous Integration (CI) workflow that installs dependencies, performs code linting, checks formatting, builds the project, checks for security issues, etc. When the developer is done implementing something, a pull request must be made to the main branch. Once a new pull request is made, we verify that all CI workflows still pass, perform more in-depth testing and security scanning, build the application into a Docker image, upload the Docker image to GitHub Container Registry, and deploy it to a temporary preview environment available on the deployment server. Once a pull request is closed, the preview environment shall be destroyed.

The source code is [hosted on GitHub](https://github.com/JonathanVarild/DD2482-Automated-Software-Testing-and-DevOps) and the application will be containerized with Docker. We will use Terraform for managing preview and production environments, and Nginx as a reverse proxy running on the server.

* **On Every Commit/Push (CI)**
  * Install dependencies
  * Lint
  * Formatting check
  * Type checking
  * Build the project
  * Perform unit tests
  * Perform code security scanning
* **On Every Pull Request (CI/CD)**
  * Run CI
  * Perform integration tests
  * Perform E2E tests
  * Build Docker image
  * Perform vulnerability scan on Docker image
  * Upload built Docker image to GHCR
  * Deploy to a temporary preview environment
  * Perform smoke tests on deployed preview environment
* **On Merge to Main (CD)**
  * Deploy the tested Docker image to production environment
  * Perform smoke tests on deployed production environment
* **On Closing of Pull Request (CD)**
  * Destroy the preview environment
* **Infrastructure**
  * Source code hosted on GitHub
  * Application running in Docker
  * IaC with Terraform
  * Deployment on VPS
  * Nginx as reverse proxy
* **Repository Security**
  * GitHub Dependabot alerts
  * GitHub Dependabot security update PRs
  * GitHub Code scanning alerts
  * GitHub Secret Scanning alerts
  * Branch protections requiring pull request to main and successful checks

**Relevance**

This implementation shows an extensive DevOps workflow which greatly reduces the work needed to be performed every time a new application version is released. Extensive testing and preview environments ensure that the application works in the way that it is intended to before it is exposed to live users. Automated security scanning and Dependabot security updates make it possible to detect critical problems early and to quickly test and roll out updates of dependencies which may be affected by newly discovered vulnerabilities. Infrastructure as Code (IaC) with Terraform helps ensure that our environments are consistent and reproducible, and greatly reduces the work needed to test and ship each new application version.
