# Assignment Proposal

## Title

GitOps Deployment of a URL Shortener on Azure Kubernetes Service with Argo CD

## Names and KTH ID

  - Lorenzo Deflorian (ldef@kth.se)
  - Riccardo Fragale (fragale@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We will build an integrated DevOps pipeline for **Snip**, a URL-shortening service with a FastAPI backend, a browser frontend, and PostgreSQL storage, deployed on Microsoft Azure.

- **CI:** GitHub Actions will build the Docker image and run Pytest tests, Ruff formatting and lint checks, and ty type checks on pull requests.
- **CD:** GitHub Actions will publish commit SHA-tagged images to Azure Container Registry and update the deployment configuration in Git. Argo CD will deploy changes to Azure Kubernetes Service, with automated database migrations and smoke tests.
- **IaC:** Terraform will configure the Azure infrastructure, networking, and access permissions. Kustomize will define the Kubernetes workload and production settings.
- **Security:** Gitleaks will scan for exposed secrets, Trivy will scan dependencies, container images, and infrastructure configuration, and Dependabot will propose dependency updates.
- **Development platform:** GitHub will support version control, pull requests, code reviews, and required automated checks.

**Relevance**

The project demonstrates core DevOps practices through a unified workflow connecting development, testing, security, infrastructure management, and deployment. GitHub Actions provides continuous integration and artifact delivery, Terraform makes infrastructure reproducible, and Argo CD keeps the deployed application aligned with the desired state in Git. By integrating these practices around a small but complete application, we can demonstrate and explain how an application change moves from source code to a running service.
We believe it is very important to be able to show a complete pipeline that covers all aspect of DevOps we talked about during the course.