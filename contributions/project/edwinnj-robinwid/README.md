`contributions/project/edwinnj-robinwid/README.md`

# Assignment Proposal

## Title

Implementing a CI/CD pipeline and IaC for an open source web app

## Names and KTH ID

  - Robin Widjeback (robinwid@kth.se)
  - Edwin Nordås Jogensjö (edwinnj@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

### Submission of project

We have a private repository available [here](https://github.com/edwinjogen/cv-devops-project). The repo is currently shared with algomaster99, carminecesarano and ericcornelissen. If there is a problem or anyone else needs to have access just contact us and we will fix it.

The link to the deployed rendering of a CV is [here](https://cv-devops-project.vercel.app/). The report can be found [here](https://github.com/edwinjogen/cv-devops-project/blob/main/report.pdf)

The project will consist of implementing a full CI/CD pipeline with IaC on [this](https://github.com/bartoszjarocki/cv) open source project that render CVs using TypeScript. The project doesn’t contain any DevOps tools to begin with so the full stack of CI, CD, IaC and dependency management will be handled by our project.

- CI: The CI will run tests, linting, formatting among other things on the code whenever a commit is pushed or merged to main
- CD: We will setup Vercel for the project which deploys the new version to a live website whenever a commit is pushed or merged to main and those changes passed the CI tests
- IaC: For IaC we will configure Terraform to manage the project’s infrastructure
- Security Automation: DependaBot will be used to maintain the projects dependencies, to ensure both security and quality when developing

**Relevance**

As mentioned above, we will implement several features that are automatically executed when changes are pushed to the main branch which demonstrates how different aspects of DevOps can be used. The tools we choose to use for integrating a CI pipeline, CD and IaC are well-known and commonly used for DevOps practices, showing how real-world projects work and integrate these.
