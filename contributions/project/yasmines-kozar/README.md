# Assignment Proposal

## Title
DevOps Pipeline for Native Android Mobile Application

## Names and KTH ID

- Yasmine Schüllerqvist (yasmines@kth.se)
- Matyas Kozar (kozar@kth.se)

## Deadline
11 October 2026

## Category
Project

## Description

Using an existing project developed in a previous course, we developed a complete DevOps pipeline based on the practices learned in this course. The pipeline includes:

- **CI:** GitHub Actions runs Gradle builds, automated unit tests, lint checks, and Docker image builds on every push and pull request to the `DD2482` branch.

- **CD:** GitHub Actions builds release-ready signed APK files and publishes them to the GitHub Releases page whenever a version tag is pushed.

- **IaC:** Terraform provisions and manages the Google Cloud infrastructure supporting the Firebase backend, including required APIs, Firestore, and Cloud Functions.

- **Platform:** GitHub is used for source-code hosting, version control, pull requests, releases, and GitHub Actions workflows.

- **Quality and Security Automation:** Static code analysis using Android Lint is integrated into the CI pipeline.

- **AI Tools:** The use of AI tools is documented in the report.

**Relevance:**
This project is relevant to DevOps because it demonstrates how CI/CD, infrastructure as code, containerisation, and automated quality checks can be integrated into a development workflow, enabling developers to automatically test, validate, and release changes in a consistent and repeatable manner.




