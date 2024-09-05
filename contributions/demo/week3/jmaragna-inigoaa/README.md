# Assignment Proposal

## Title

Github Actions workflow for deploying to an AWS Lambda function.

## Names and KTH ID

  - Jacopo Maragna (jmaragna@kth.se)
  - Íñigo Aréjula Aísa (inigoaa@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

In this assignment, we are going to create a Github Actions workflow that will deploy a AWS Lambda function. The workflow will be triggered when a new commit is pushed to the repository. We are going to adopt a modular approach, so we will have different files that can be used in different projects. We are going to set up different workflows that will be conditionally triggered  based on the success of the previous one.

What we aim to demonstrate the possibility to vary the deployment setup with a few slight changes in the configuration files.

**Relevance**

Github actions is one of the most common services for CI/CD. In this case, we will use it to deploy a AWS Lambda function. This is a very interesting use case, as AWS Lambda is a very popular service for serverless computing. We are going to automate all the precess since the code is changed until the final deployment is done.
