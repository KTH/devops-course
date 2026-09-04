# Assignment Proposal

## Title

Neighborhood-Matching Housing Tool with a full DevOps Pipeline


## Names and KTH ID

  - Nalin Kundu (nvkundu@kth.se)
  - Hossein Ghadirzadeh (ghadirz@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We would like to create a tool that helps individuals new to Stockholm to find housing. Coming into a new city, it’s hard for outsiders to know where the best places are to live, something both of us have experienced. In terms of tech stack, we are flexible but were thinking React frontend with fastapi backend (open to anything simpler like node really though). 

Around this we'll build a full pipeline. Specifically, GitHub Actions for CI/CD, Terraform for infrastructure as code, GitHub as our development platform with branch protection and required reviews, and a security automation step (Dependabot for tracking outdated dependencies and CodeQL for vulnerable code) wired into the same pipeline. 
 
We’ll plan on using AI both for creating the app and for code reviews and will further detail our usage in our report. 

- **CI:** GitHub Actions running lint, type-checks, and tests on
  everfy push/PR
- **CD:** GitHub Actions with automated build and deploy on merge to main
- **IaC:** Terraform provisioning the server and database
- **Platform:** GitHub, with branch protection and required reviews
- **Security:** Dependabot + CodeQL
- **AI tools:** documenting both the AI-built origin of the concept
  and any AI coding assistants used during development


**Relevance**

We hope to create an actual tool that individuals new to Stockholm can use. Given that it's an actual tool, we need to utilize best practices for the project that we’ll learn throughout the DevOps course. Through integrating CI, CD, IaC, platform tooling, and security automation into one pipeline, we will both ensure we have a quality app and learn more about the DevOps process. 
