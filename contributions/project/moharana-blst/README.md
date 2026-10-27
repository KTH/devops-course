# Assignment Proposal

## Title
Project: Automation Pipeline for API Lifecycle using GitHub Actions

## Names and KTH ID

- Padmalaya Moharana (moharana@kth.se)
- Bogdan-Laurentiu Stefanescu (blst@kth.se)

## Deadline
11 October 2026

## Category
Project

## Description

**Project Overview**

The **Automation Pipeline for API Lifecycle DevOps Project** demonstrates an end-to-end DevOps workflow for designing, validating, testing, deploying, and managing a REST API using an API-first approach. The project uses an OpenAPI specification as the source of truth and integrates Continuous Integration (CI), Continuous Deployment (CD), Infrastructure as Code (IaC), quality automation, and cloud deployment practices within a single GitHub repository.

The API provides weather information for a requested city and is implemented using Node.js and Express. The API contract is defined using OpenAPI 3.0 and is automatically validated, tested, and deployed through GitHub Actions workflows to Azure API Management.

**Continuous Integration (CI)**

The CI pipeline is implemented using **GitHub Actions** and is automatically triggered on every push and pull request.

**Continuous Deployment (CD) to Azure API Management**

The CD pipeline automatically deploys the application package to App Service, imports the OpenAPI definition into **Azure API Management (APIM)**, and updates the APIM backend URL.

**CI/CD Workflow**
```text
Developer
    │
    ▼
GitHub Repository
    │
    ├── OpenAPI Specification
    ├── Node.js API
    ├── Terraform
    └── GitHub Actions
            │
            ▼
      CI Pipeline
      ├─ OpenAPI Validation
      ├─ Spectral Linting
      ├─ Unit Tests
      ├─ Build Verification
      └─ CodeQL Security Scan
            │
            ▼
      CD Pipeline
      ├─ Deploy Node.js Application
      └─ Deploy OpenAPI Definition
            │
            ▼
      Azure App Service
            │
            ▼
      Azure API Management
            │
            ▼
          Consumers
```

**Infrastructure as Code (IaC)**

Infrastructure provisioning is automated using **Terraform**.

**Infrastructure Components**

Terraform configuration is in [`terraform/`](terraform/). It defines:

- An Azure resource group.
- An Azure API Management service.
- A Linux App Service plan.
- A Linux Web App configured for Node.js 20.

The resource group name and Azure region are variables; outputs include the resource group name, APIM name and gateway URL, and Web App URL. Terraform is **not** run by the GitHub Actions workflows: provision or update the resources separately, and ensure they exist before deployment. The infrastructure definitions do not configure a remote Terraform state backend.


**Final Project submission**

**GitHub Repository**

**Repository:** https://github.com/Padmalaya26/api-lifecycle-devops

**Project report**

The report explains the architecture, demonstrated processes, design decisions, component interactions, and project limitations:

- [Download the report (PDF)](https://github.com/Padmalaya26/api-lifecycle-devops/blob/main/docs/report.pdf)


**GitHub Actions Pipeline**

**Workflow Location**

```text
.github/workflows/
│
├── ci.yml
├── codeql.yml
└── deploy-apim.yml
```

**GitHub workflow runs Example**

These links point to recorded GitHub workflow runs:

- [CodeQL security scan](https://github.com/Padmalaya26/api-lifecycle-devops/actions/runs/40029173843/job/120672832499)
- [CI pipeline](https://github.com/Padmalaya26/api-lifecycle-devops/actions/runs/40029107904/job/120672618644)
- [CD pipeline](https://github.com/Padmalaya26/api-lifecycle-devops/actions/runs/40029313371/job/120673306173)
    
**Previous Pull Request links**
- [Task proposal pull request](https://github.com/KTH/devops-course/pull/3127)
- [Previous project submission pull request](https://github.com/KTH/devops-course/pull/3199)

**Conclusion**

This project demonstrates the integration of **API-first development**, **Continuous Integration**, **Continuous Deployment**, **Infrastructure as Code**, **automated testing**, **security scanning**, and **cloud deployment** within a single DevOps workflow. The solution provides a practical implementation of modern DevOps practices using GitHub, GitHub Actions, Terraform, and Azure API Management.
