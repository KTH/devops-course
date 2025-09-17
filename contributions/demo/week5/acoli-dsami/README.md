# Assignment Proposal

## Title
_Spin It Up, Shut It Down On-Demand Staging with IaC_

## Names and KTH ID

  - Alessandro Coli (acoli@kth.se)
  - Dania Sami (dsami@kth.se)

## Deadline

Week 5

## Category
Demo

## Description
A demo showcasing how to provision and destroy a staging environment using Infrastructure as Code. The environment will run a simple containerized application, defined through either Terraform or Docker Compose.

In the demo, we will do the following:

- Showcase an IaC configuration (Terraform or Docker Compose).
- Deploy a simple containerized application (“Hello World” app).
- Demonstrate accessing the application in the browser.
- Update the configuration live (for example, change app text or infra config) and re-deploy.
- Tear down the entire staging environment with a single command.
- Conclude with why on-demand staging matters in DevOps.

**Relevance**

Staging environments are critical for testing new features before production, but permanent staging systems are costly and often underutilized. Using Infrastructure as Code, developers can spin up staging environments on demand, use them for testing, and tear them down when finished. This saves costs, increases agility, and ensures consistency across environments, all key DevOps goals.
