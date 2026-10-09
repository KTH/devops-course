# Assignment Proposal

## Title

Reproducible CI/CD for a task-tracking API

## Names and KTH ID

  - Hasan Kalzi (kalzi@kth.se)
  - Love Lingren (lolindgr@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We will build a small task-tracking API using Python, FastAPI and SQLite. It will support creating, listing and completing tasks, with persistent storage and input validation. Our main focus will be an integrated DevOps workflow rather than extensive application features.

The project will include:

- Continuous integration: GitHub Actions will run pytest tests, Ruff static analysis, a Docker image build and a container smoke test. Tests will cover task operations, invalid input and persistence across application restarts.

- Continuous delivery: A version-tag-triggered workflow will publish a GitHub Release only after the required checks pass. Each release will contain the tested Docker image as an archive, deployment configuration and instructions.

- Infrastructure as Code: Ansible will configure a supported Linux host, including the container runtime and application directories. Docker Compose will define the service, persistent storage, port binding and health check. We will verify deployment on a clean Linux virtual machine.

- Collaboration: We will use GitHub issues and pull requests to organise and review our work.

- AI assistance: We will document how AI-assisted tools were used and how their output was reviewed and verified.

The implementation repository will contain all application code, tests, workflows, infrastructure configuration and instructions needed to run the system. We will demonstrate that failing checks prevent delivery and document rollback to a previous release, distinguishing application rollback from database recovery.

We will provide a 2–3 page report explaining the architecture, processes, component interactions, design decisions, limitations and trade-offs.

**Relevance**

The project demonstrates how source-code changes become tested, packaged and reproducibly deployable software. It combines CI, continuous delivery, Infrastructure as Code and automated quality checks into one coherent workflow.
