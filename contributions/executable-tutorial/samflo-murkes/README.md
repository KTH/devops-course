# Assignment Proposal

## Title

Infrastructure as Code with Terraform and Docker tutorial in killercoda

## Names and KTH ID

  - Samuel Flodin (samflo@kth.se)
  - Felicia Murkes (murkes@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

**Tutorial:** [Killecoda](https://killercoda.com/fmurkes/scenario/iac-terraform-docker)

We will create an executable tutorial in killercoda where tutorial users will follow along to learn how to set up a simple application with two containers connected with Docker. By using Terraform, the user will create a file that instead of running docker manually will describe what the setup should be like, which Terraform will execute.

This setup will contain two containers with nginx and a simple backend.

The tutorial will then simulate what happens when someone breaks the container by hand. To simulate a real incident (e.g an engineer accidentally removes the wrong container during cleanup), the user will manually delete the backend container, causing nginx to fail since it depends on the backend to handle requests. The user will then use terraform plan and apply to detect this drift and automatically restore the setup. The user will then learn how to use Terraform in order to identify and automatically fix the problem.

**Relevance**

This tutorial will reflect core DevOps goals such as reproducibility and environment consistency. Manual infrastructure changes are a common cause of outages and inconsistent environments in real systems. IaC addresses this by making changes visible in the code, repeatable, and self correcting.

