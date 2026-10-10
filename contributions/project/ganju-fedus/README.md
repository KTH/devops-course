# Assignment Proposal

## Title

PR-Driven Terraform Pipeline with Atlantis and Floci

## Names and KTH ID

- Alexandru Gânju (ganju@kth.se)
- Robert Fedus (fedus@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We will implement an automated DevOps pipeline for a small serverless API (AWS Lambda, API Gateway and DynamoDB), running locally on [Floci](https://github.com/floci-io/floci), an open-source AWS emulator, so no cloud subscription is needed. The pipeline will include:

- **CI**: GitHub Actions for linting, unit tests, and integration tests in an ephemeral Floci environment on every pull request.
- **CD**: [Atlantis](https://www.runatlantis.io/) for applying Terraform changes through pull requests, followed by an automated smoke test.
- **IaC**: Terraform for the AWS infrastructure, and Docker Compose for the local setup (Floci and Atlantis).
- **Platform**: GitHub with branch protection rules, required status checks and required reviews.
- **Security**: Checkov for Terraform scanning, pip-audit and Dependabot for dependencies, and GitHub secret scanning.
- **AI tools**: GitHub Copilot code review, whose usage will be documented and discussed in the report.

**Relevance**

This project demonstrates how CI, CD, Infrastructure as Code and security automation can be integrated into a pull-request-driven DevOps workflow, where infrastructure changes go through the same review and testing process as application code.
