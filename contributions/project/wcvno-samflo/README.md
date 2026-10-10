# Assignment Proposal

## Title
Setting up DevOps for a flappy bird web app

## Names and KTH ID

- William Nordwall (wcvno@kth.se)
- Samuel Flodin (samflo@kth.se)

## Deadline
11 October 2026

## Category
Project

## Description
We will implement DevOps in a flappy bird game which runs as a web application. As part of this, we will set up a CI pipeline, a CD pipeline and infrastructure as code.
The project will be set up as a GitHub repository, and we will use GitHub Actions for CI/CD.
- The CI pipeline will run linting and tests on the code. This will run on every pull request and push to main.
- The CD pipeline will deploy our application to a Vercel project. This will run on every merge to the main branch.
- For IaC we will use Terraform to set up resources in Vercel.
- For quality and security checks we have linting/tests, and we will also set up Dependabot to monitor dependencies.


**Relevance:**
This is relevant to DevOps as we are utilizing main practices of CI, CD and IaC.
We are testing the code, automating deployments and setting up relevant infrastructure, which is central to DevOps.
