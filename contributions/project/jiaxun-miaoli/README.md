# Assignment Proposal

## Title

An end-to-end DevOps pipeline on Azure with Terraform

## Names and KTH ID

  - Jiaxun Wei (jiaxun@kth.se)
  - Miao Liu (miaoli@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We want to build a complete DevOps pipeline for a small web application of our own. The mandatory parts map to our stack as follows:

- **Build and test (CI)**: Azure Pipelines runs the build and the tests on every pull request.
- **Deployment (CD)**: the pipeline deploys to Azure once the checks pass, and it authenticates through workload identity federation.
- **Infrastructure as code**: the Azure resources are described in Terraform.
- **Development platform**: the code and the pull request flow live on KTH GitHub.
- **Quality and security automation**: Trivy scans the Terraform configuration and the dependencies, and a finding blocks the pipeline.
- **AI-assisted tools**: this will be covered in the report.

**Relevance**

The value of DevOps comes from the parts working together, not from any single tool. This project puts build, test, infrastructure and deployment into one repository and one pipeline, and demonstrates how a real-world application is delivered.
