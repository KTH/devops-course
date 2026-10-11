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

**Submission:**
- **Project repository:** https://github.com/JingzeGuo/docmost
- **Deployed application:** https://docmost.click
- **Final report:** https://docs.google.com/document/d/1bM0PvT3HvlQLIKrUHv9LMAOCP4dhmIWax1DQ_0lFY9E/edit?usp=sharing
- **Original proposal:** https://github.com/KTH/devops-course/pull/3037

We implemented an end-to-end DevOps pipeline for Docmost, an open-source collaborative wiki and documentation platform.

The completed project includes:

- **CI:** GitHub Actions runs automated frontend and backend tests, application and Docker image builds, and Trivy security scans on pull requests.
- **CD:** Changes merged into `main` trigger Docker image publishing to GHCR and automated deployment to AWS EC2 using GitHub Actions, OIDC authentication, and AWS Systems Manager.
- **IaC:** Terraform manages the AWS infrastructure, including EC2, networking, persistent storage, and load balancing. Docker Compose manages the application and its PostgreSQL and Redis services.
- **Development platform:** GitHub provides source control, pull request workflows, CI/CD automation, and container image hosting.
- **Security:** Trivy scans container images, while AWS IAM roles and Systems Manager Parameter Store are used for deployment permissions and secret management.
- **AI-assisted tools:** The use of AI-assisted tools during development is documented in the final report.

The project repository contains the source code, infrastructure configuration, deployment scripts, and setup instructions. The final report describes the architecture, implementation, design decisions, and limitations.

**Relevance**

The project demonstrates how CI, CD, Infrastructure as Code, containerization, and security automation can be integrated into a coherent DevOps workflow for a real-world application. The pipeline connects code changes, automated validation, infrastructure provisioning, and deployment into a reproducible delivery process.