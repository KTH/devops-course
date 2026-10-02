# Assignment Proposal

## Title
DevOps Pipeline for a Portfolio Website Builder

## Names and KTH ID

- Singvalliyappa Velayutham — (sinvel@kth.se)
- Robert Jenson — (robjen@kth.se)

## Deadline

- 11 October 2026

## Category

- Project

## Description

We will use a portfolio website builder that we built earlier (has no devops workflow -[https://github.com/Val0007/web-site-backend]( https://github.com/Val0007/web-site-backend)) and improve the DevOps workflow around it. Users log in with Google, edit their portfolio in an admin panel, and get a public site at their own subdomain. It is split into three repositories: a NestJS backend with MongoDB Atlas, a React admin panel, and a React public frontend. All three will have GitHub Actions CI (lint and build) and automated deployment (backend to Render, frontend and admin to Vercel). 

- **Dev platform:** GitHub
- **CI:** GitHub Actions runs lint, build and tests on every pull request. We will write unit tests for the backend services. The backend Docker image is also built in CI to verify it builds.
- **CD:** merges to main build the backend Docker image, push it to GitHub Container Registry tagged with the commit SHA, and deploy that image to Render. The two frontends deploy to Vercel. Everything deploys only after CI passes .
- **Feature flags:** new features are released behind flags stored in MongoDB. So a feature can be turned on and switched off without redeploying.
- **Infrastructure as code:** Terraform describes the Render service and the MongoDB Atlas cluster.
- **Quality and security automation:** CodeQL code scanning, Dependabot for dependency updates, and GitHub secret scanning. 
- **AI-assisted tools:** AI tool usage will be documented in the report.

**Relevance**

The project takes an existing multi-repository application and builds a complete DevOps pipeline around it. Changes are linted, built and tested in CI, deployed automatically in CD as a Docker image, and released with feature flags. The infrastructure is defined as code with Terraform, and code and dependencies are scanned automatically. These cover the necessary topics to adopt a devops workflow while building software.


