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
 
This project demonstrates a Continuous Integration (CI) workflow for designing, validating, testing, and building a REST API using an API-first approach based on the OpenAPI Specification.
 
The project will implement a simple REST API named **OpenWeather API**, which provides basic weather information for a requested city. The API design will be defined through an OpenAPI 3.0 specification document before implementation. The repository will contain the API specification, source code, automated tests, quality automation configurations, and CI workflows required to manage and validate the API throughout its development lifecycle.
 
The project follows modern DevOps practices by integrating GitHub as the development platform and GitHub Actions as the Continuous Integration solution. Whenever code changes are pushed to the repository or submitted through a pull request, automated workflows will validate the OpenAPI specification, perform linting checks, execute unit tests, verify API quality, and build the application. This ensures that code quality is continuously assessed and that API changes meet established standards before being merged into the main branch.
 
To support API quality and maintainability, the project will use OpenAPI linting with Spectral, automated testing using Jest, and security analysis using GitHub CodeQL. Dependabot will be configured to monitor dependencies and suggest updates when vulnerabilities or outdated packages are detected. These practices help improve software reliability and encourage early detection of issues within the development workflow.
 
The project will also document the use of AI-assisted development tools such as GitHub Copilot and ChatGPT. The documentation will describe how these tools were used during API design, test generation, workflow creation, and documentation development, while emphasizing manual review and validation of all generated content.
 
The final solution demonstrates how API-first development, automated testing, quality assurance, security checks, and Continuous Integration can be combined within a single GitHub repository. The project is intentionally kept small and focused, enabling a clear demonstration of CI practices while showcasing essential DevOps concepts in a realistic software development environment.