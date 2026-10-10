# Assignment Proposal

## Title

DevOps pipeline for a course review web app

## Names and KTH ID

  - Georgi Tsonchev Hristov (georgith@kth.se)
  - Cesar Aceves Hernández (cesarah@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We'll make a small web app with Flask and SQLite where students can leave anonymous reviews of KTH courses. We're keeping the app simple so most of the work goes into the pipeline.

- Development platform: GitHub for the repo, Actions and the container registry. Main is protected, so every change goes through a pull request.
- CI: every pull request runs ruff, the pytest tests and a Docker build, and it can't be merged until they pass.
- CD: when something is merged to main, the pipeline builds a Docker image tagged with the commit, pushes it to GitHub Container Registry and deploys it. The deploy runs on a self-hosted runner on our own machine.
- Infrastructure as Code: Terraform with the Docker provider defines the app container, the network and the volume for the database. The pipeline changes the image tag and runs terraform apply, and anyone with Docker can bring up the same setup locally.
- Quality and security automation: Dependabot for dependency updates and CodeQL for static analysis.

In the report we'll explain the architecture and why we chose these tools. We'll also cover the limits, like running everything on one machine and having a self-hosted runner on a public repo.

**Relevance**

A change goes from a pull request to the running app without any manual steps, and the infrastructure it runs on is written as code.
