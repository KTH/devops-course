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

**CI Workflow**

```text
Developer Commit
       ↓
GitHub Push
       ↓
GitHub Actions
       ↓
OpenAPI Validation
       ↓
Spectral Linting
       ↓
Unit Testing
       ↓
Build Verification
```

**Continuous Deployment (CD) to Azure API Management**

The CD pipeline automatically deploys the OpenAPI specification to **Azure API Management (APIM)** after successful validation.

**CD Workflow**

```text
GitHub Push
      ↓
GitHub Actions
      ↓
Azure Authentication
      ↓
Import OpenAPI Specification
      ↓
Azure API Management
```

**Infrastructure as Code (IaC)**

Infrastructure provisioning is automated using **Terraform**.

**Infrastructure Components**

Terraform resource provisions:

```text
Azure Resource Group
Azure API Management Service
```

**Final Project submission**

**GitHub Repository**

**Repository:**

```text
https://github.com/Padmalaya26/api-lifecycle-devops
```
**GitHub Actions Pipeline**

**Workflow Location**

```text
.github/workflows/
│
├── ci.yml
├── codeql.yml
└── deploy-apim.yml
```
**GitHub Actions Pipeline Run**
The Actions tab provides visibility into all CI/CD piepline executions, validation results, test reports, security scans, and deployment status. Links are below.

- **CodeQl Security Scan run Report:**
    ```Text
    https://github.com/Padmalaya26/api-lifecycle-devops/actions/runs/37990068923
    ```
- **CI Pipeline Run Report:**
    ```Text
    https://github.com/Padmalaya26/api-lifecycle-devops/actions/runs/37990068792
    ```
- **CD Pipeline Run Report:**
    ```Text
    https://github.com/Padmalaya26/api-lifecycle-devops/actions/runs/37990068662
    ```

**Conclusion**

This project demonstrates the integration of **API-first development**, **Continuous Integration**, **Continuous Deployment**, **Infrastructure as Code**, **automated testing**, **security scanning**, and **cloud deployment** within a single DevOps workflow. The solution provides a practical implementation of modern DevOps practices using GitHub, GitHub Actions, Terraform, and Azure API Management.
