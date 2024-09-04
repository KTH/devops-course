# Assignment Proposal

## Title

Get started with Terraform : Continuous Deployment in AWS through Github Actions


## Names and KTH ID

- Zyad Haddad (zyad@kth.se)
- Kankanit Suppataratarn (kankanit@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

This demo is intended to walk the audience through the deployment of a web application setup on AWS using Terraform and Github Actions CI/CD pipelines. The demo will start with the setup of Terraform for AWS, with a detailed explanation of the how the HashiCorp Configuration Language works. Then we will continue with the CI/CD Pipeline Setup, which covers a quick walkthrough of the CI pipeline (which runs for every commit) and a detailed explanation of the CD pipeline (which only runs on a merge to main). Finally, we will show the case where CD pipeline fails, followed by troubleshooting and fixing the issue to complete the deployment.

**Relevance**

Computer Science students often avoid deployment because it typically involves paid services or complicated interfaces. In this demo, we aim to show how a developer new to DevOps can get started with Continuous Deployment using simple Terraform code, a widely-used Infrastructure as Code (IaC) tool. IaCs are crucial in modern development because they allow for automated, consistent, and scalable infrastructure management. The deployment will be done on AWS, the most widely used cloud provider, which offers a free plan, and will be continuously deployed using GitHub Actions, an accessible tool. This combination of tools provides an easy, quick, and intuitive starting point.