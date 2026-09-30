# Assignment Proposal

## Title

Cost-Aware Infrastructure Changes with Infracost

## Names and KTH ID

* Erik Söderlund eriso

  * Anders Mouanga mouanga

## Deadline

Week 5

## Category

Demo

## Description

Infrastructure is about more than whether an application runs or not. A developer could submit a completely valid Terraform configuration that passes all technical checks, but accidentally increases the monthly infrastructure cost by much more than what the company is comfortable with. This is a property that should be checked before the change reaches production, even though it is not always easy to evaluate during a normal infrastructure review.

We will create a small web application deployed on a cloud service provider using Terraform. The infrastructure consists of an application server and its supporting resources. Terraform describes the desired infrastructure, while Infracost calculates an estimated cost from the Terraform configuration and plan. GitHub Actions runs these checks automatically when infrastructure changes are submitted.

We will define a maximum acceptable cost increase for infrastructure changes. If a proposed Terraform change exceeds this threshold, the CI pipeline will block the pull request before the change can be deployed.

**What we will show:**

* The application running with a basic infrastructure configuration and a low estimated cost. We show the Terraform configuration and the estimated monthly cost.
* An infrastructure change is made in an open pull request. GitHub Actions runs `terraform plan` and Infracost calculates the expected cost of the new infrastructure.
* We make a deliberately excessive change that makes the infrastructure significantly larger. The Terraform configuration is still valid and the application would still work, but the estimated cost increases beyond our defined threshold.
* The cost gate detects the increase and blocks the pull request. We can see both the current cost and the expected cost after the proposed change.
* We change the infrastructure to a more reasonable configuration and push the update, after which the pipeline passes.
* We discuss potential failure conditions and how the same approach could be extended to a real production environment.

We will also discuss limitations. Cloud prices change over time, and cost estimates will not necessarily be identical to the final bill. Some resources have usage-based pricing that cannot be accurately predicted from Terraform alone. Additionally, a large increase in cost can sometimes be intentional, so a simple threshold can produce false positives and block legitimate infrastructure changes.

** Relevance **

Infrastructure as Code makes infrastructure changes reproducible, reviewable, and automatable, but it also provides an opportunity to evaluate properties of infrastructure beyond whether it can be deployed. Cost estimation can be incorporated into the same CI/CD workflow as `terraform plan`, allowing infrastructure costs to become part of the infrastructure review process. The demo shows how a DevOps pipeline can automatically detect an otherwise invisible consequence of an infrastructure change before it reaches production.

