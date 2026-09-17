# Assignment Proposal

## Title

End-to-End DevOps Pipeline for Docmost

## Names and KTH ID

* Jingze Guo ([jingze@kth.se](mailto:jingze@kth.se))
* Shunkang Jia ([shunkang@kth.se](mailto:shunkang@kth.se))

## Deadline

* 11 October 2026

## Category

* Project

## Description

We plan to build a complete DevOps pipeline around [Docmost](https://github.com/docmost/docmost), an open-source collaborative wiki and documentation platform. Docmost is an existing full-stack application using React, NestJS/TypeScript, PostgreSQL, and Redis. It already supports containerized deployment and provides existing build, lint, unit test, and E2E test commands. This makes Docmost a suitable application for integrating and evaluating a complete DevOps workflow.

The project will include:

* **CI:** GitHub Actions will run linting, tests, builds, and security checks on pull requests.
* **CD:** merges to the main branch will build a Docker image, tag it with the commit SHA, push it to GitHub Container Registry, and automatically deploy it.
* **Infrastructure as Code:** Terraform will provision a VM-based deployment environment, including infrastructure such as networking, firewall rules, and a public IP. Docker Compose will run Docmost, PostgreSQL, Redis, and a reverse proxy on the provisioned host.
* **Development platform:** GitHub will be used for source control, pull requests, GitHub Actions, and container images.
* **Quality and security automation:** Trivy will be used for vulnerability scanning, together with relevant GitHub security features.
* **AI-assisted tools:** the use of AI tools during workflow development, Terraform configuration, debugging, and code review will be documented.

All configuration, code, and documentation required to reproduce the system will be kept in the project repository, together with the required final report.

## Relevance

The project demonstrates how CI, CD, Infrastructure as Code, containerization, and security automation can be integrated into a coherent DevOps workflow for a real-world application. The pipeline connects code changes, automated validation, infrastructure provisioning, and deployment into a reproducible delivery process.