# Assignment Proposal

## Title

DevOps for a webapp using TypeScript Frontend and Python Backend

## Names and KTH ID

  - Amin Nouiser (anouiser@kth.se)
  - Ivar Boqvist (ivarbo@kth.se)

## Deadline

- Task 1

## Category

- Project

## Description

We want to set up infrastructure for a simple webapp consisting of a Pomodoro timer with session logging. The application consists of a basic Svelte + Vite frontend in TypeScript, a basic FastAPI backend in Python, and a database set up on AWS using DynamoDB.

We'll use Terraform to define infrastructure as code that'll be deployed to AWS but can also be tested locally on LocalStack. We'll use Terraform's built-in tests feature to ensure proper network segmentation. 

We'll host the repository on GitHub and use GitHub Actions to set up our workflows.

For our CI pipeline, we'll set up:
- Linting, formatting, and type checking for the Python backend using ruff and pyrefly
- Linting and formatting for the TypeScript frontend using oxlint and oxfmt
- Dependency versioning and tracing using Dependabot
- Running unit tests on the Python backend using pytest
- Building the Docker image and pushing it to a container registry

As for our CD pipeline, we'll set up:
- Automated Terraform planning and applying using Terraform to deploy the app on AWS using resources such as EC2.


*AI disclosure:* The webapp was written with the help of Claude Opus 5.5. We believe this to be fine, seeing as the focus of the project is on the infrastructure. Nothing else has been written using or with the help of any LLM.

**Relevance**

This project is relevant to DecOps as it aims to set up a CI/CD pipeline for an plain WebApp CodeBase. It aims to follow the best-practices of DevOps.