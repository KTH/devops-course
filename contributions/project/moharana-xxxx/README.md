# Assignment Proposal

## Title

**Project: OpenWeather API Lifecycle Automation using OpenAPI, GitHub Actions and Azure API Management**

## Names and KTH ID

**Padamalaya Moharana** (moharana@kth.se)

## Deadline

**11 October 2026**

## Category

**Project**

## Description

This project demonstrates a complete DevOps workflow for designing, validating, testing, building, and deploying a REST API using an API-first approach based on the OpenAPI Specification.

The project will implement a simple REST API named **OpenWeather API**, which provides basic weather information for a requested city. The API design will be defined entirely through an OpenAPI 3.0 specification document before implementation. The repository will contain all source code, infrastructure definitions, CI/CD pipelines, quality automation rules, and deployment configurations necessary to manage the API lifecycle.

The project follows modern DevOps practices by integrating GitHub as the development platform and GitHub Actions as the Continuous Integration and Continuous Deployment (CI/CD) solution. Whenever code changes are pushed to the repository, automated workflows will validate the OpenAPI specification, perform linting checks, execute automated tests, generate API artifacts, and verify specification quality. Upon successful validation, a deployment pipeline will automatically publish the API definition to Azure API Management (APIM), making the API available through a managed API gateway.

Infrastructure resources required by the solution will be managed through Infrastructure as Code using Terraform. This enables reproducible, version-controlled infrastructure deployments and supports DevOps principles of automation and consistency.

The project will also incorporate quality and security automation through OpenAPI linting with Spectral, GitHub CodeQL security scanning, and Dependabot dependency management. Additionally, the project will document the use of AI-assisted development tools, such as GitHub Copilot and ChatGPT, including how they contributed to API design, pipeline creation, and documentation.

The final solution demonstrates how API-first development, automated testing, continuous integration, continuous deployment, infrastructure automation, and quality controls can be integrated into a single coherent DevOps workflow. The project is intentionally designed to remain simple enough for demonstration purposes while showcasing essential DevOps concepts and practices in a realistic cloud-native environment.