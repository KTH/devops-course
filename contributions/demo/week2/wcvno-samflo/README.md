# Assignment Proposal

## Title

Setup automated linting and code checks with SonarCloud

## Names and KTH ID

  - William Nordwall (wcvno@kth.se)
  - Samuel Flodin (samflo@kth.se)

## Deadline

- Week 2

## Category

- Demo

## Description

We want to set up a GitHub Actions CI which runs linting on each PR to check for correct formatting.
The CI will also use SonarCloud to scan the code for code quality issues as well as security risks.
These can be issues such as unused variables or functions with high complexity.

In the demo we will first show a functioning application. We will then demonstrate what happens if we push code that is poorly formatted or has other issues that SonarCloud will find.

**Relevance**

Ensuring high code quality is an important part of DevOps.
Linting code to check for correct formatting helps with clarity, and using SonarCloud to check for other code issues such as unused functions also improves the quality of the code.
SonarCloud can also detect security issues which helps prevent leaking sensitive information.
