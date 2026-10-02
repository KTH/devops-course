# Assignment Proposal

## Title

DevOps Pipeline for Spring Boot CRUD Application

## Names and KTH ID
- De Chi Hao (dchao@kth.se) 
- Barnabas Tanczos (tanczos@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We will implement a complete, automated DevOps pipeline for a sample [Spring Boot CRUD REST API application](https://github.com/davidarchanjo/spring-boot-crud-rest). The pipeline will include:
- **CI**: GitHub Actions runs Maven builds, automated unit tests, and code quality checks on every push and pull request.
- **CD**: GitHub Actions handles the automated building of Docker images and deployment to local VMs.
- **IaC**: Terraform provisions the necessary VMs and configures the environment for the Spring Boot application.
- **Platform**: GitHub will be used for source control, configured with branch protection rules and required reviews.
- **Security**: Trivy is integrated into the CI/CD pipeline to automatically scan Docker images and dependencies for vulnerabilities before deployment.
- **AI tools**: AI usage will be documented in the report.

**Relevance**

This project demonstrates how CI, CD, Infrastructure as Code, containerization, and security automation can be integrated into a cohesive DevOps workflow, allowing changes to be automatically tested, validated, and deployed. This provides a practical understanding of how DevOps practices can be applied to a real-world application.
