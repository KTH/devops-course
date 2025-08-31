# Assignment Proposal

## Title

Deployment of a small test environment using Terraform, AWS and OPA

## Names and KTH ID

  - Leo Åkerberg (leo3@kth.se)
  - Ferran Solanes Serrat(solanes@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

This demo will show how Terraform can be used to deploy various cloud resources in AWS, using a script to deploy the basic setup of an environment; a server, a database and a bucket. This deployment will also be checked using different policies to ensure that the deployment is done securely and does not leak information. To do so we'll integrate the Terraform script with the deployment of a policy engine. The chosen policy agent is Open Policy Agent.

**Relevance**

During the DevOps lifecycle we need to test the features or bug fixes on a productive-like environment, with Terraform we can automate the deployment of a this needed environment, allowing developers to test their code before merging the changes to the main branch and applying the changes on the production environment.

