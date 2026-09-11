# Assignment Proposal

## Title

Designing a Coherent DevOps Pipeline for a Full-Stack Web Application: A TinyLink Case Study

## Names and KTH ID

- Sangeetha Murugesan — (sanmur@kth.se)
- Anna Remmare — (remmare@kth.se)

## Deadline

- 11 October 2026

## Category

- Project

## Description

We will build TinyLink, a small full-stack URL shortening service a Node.js/Express backend exposing a REST API to create and resolve short links, a React frontend providing a minimal UI over that API, and PostgreSQL for storage and wrap it in a complete, coherent DevOps pipeline. The frontend and backend are packaged into a single Docker image via a multi-stage build, so one container is the unit that moves through the entire pipeline. The pipeline will include:

**Build and test (CI)**: a GitHub Actions workflow that lints the code, runs the test suite against a real PostgreSQL service container, submits the code to a SonarCloud quality gate, and verifies the Docker image builds all gating the merge into main.
**Deployment (CD)**: a GitHub Actions workflow triggered on merge to main that builds the final Docker image, pushes it to GitHub Container Registry, applies the Terraform configuration for the application infrastructure, and runs a smoke test against the newly deployed endpoint.
**Infrastructure as code**: a Terraform stack provisioning the application infrastructure a Render web service, a Neon PostgreSQL database, and GitHub Container Registry re-applied on every deployment.**Quality and security automation**: SonarCloud paired with Renovate, with every Renovate PR routed back through the same CI gate as a human-authored change.
**AI-assisted tools**: documented in the final report 

**Relevance**

This project demonstrates a complete, working DevOps pipeline built around a single Docker image: the same artifact is linted, tested, scanned, and deployed, so what CI validates is exactly what runs live. Continuous integration and continuous deployment run as two GitHub Actions workflows, Terraform provisions the application infrastructure as code, and SonarCloud and Renovate together provide the project's quality and security automation. Every design decision, along with the project's limitations, is explained and justified in the final report.
