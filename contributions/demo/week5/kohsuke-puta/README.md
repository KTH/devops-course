# Assignment Proposal

## Title

Compliant Ephemeral Environments with IaC

## Names and KTH ID

  - Kohsuke Sonoda (kohsuke@kth.se)
  - Štěpán Půta (puta@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description
With the evolution of DevOps, many companies deploy test environments, staging environments, and production environments. However, if only one test environment is always launched, other developers must wait until someone's test is complete, and infrastructure testing is also difficult. Furthermore, keeping a test environment running constantly incurs costs. In demo we demonstrate how to build Ephemeral Environments using Infrastructure as Code (IaC), allowing environments to be deployed and destroyed as needed. However, the freedom to create environments also carries risks of increased costs and security vulnerabilities due to misconfigurations. To prevent this, we combine Policy as Code (PaC) to manage infrastructure policy.

We will build our Compliant Ephemeral Environments as follows.
First, when a PR is opened, we will use GitHub Actions to have PaC check the infrastructure code. If the infrastructure is confirmed to comply with the policy, a virtual environment will be deployed on AWS, enabling testing and other activities. Subsequently, when the PR is closed, the virtual environment will be discarded.

**Relevance**
Ephemeral Environments are an idea made possible by leveraging IaC, and they are closely connected to DevOps practices. Demonstrating how combining them with Policy as Code (PaC) can reduce the risks and costs associated with creating ephemeral environments in real-world scenarios represents an original contribution. We plan to use a simple tech stack: AWS, Terraform, GitHub Actions, and Checkov. However, the key point isn't the tech stack itself. By controlling ephemeral environments with PaC and demonstrating it, people will understand the benefits and gain practical ideas for real-world scenarios.