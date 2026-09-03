# Assignment Proposal

## Title

_Testing Infrastructure is Provisioned Correctly in Terraform_

## Names and KTH IDs

- Felix Castillo Huber (felixhh@kth.se)
- Pierre Segerström (pise@kth.se) 

## Deadline

Week 5

## Category

Demo

## Description

Prevents incorrect changes to Infrastructure as Code (IaC) from provisioning resources by allowing infrastructure configurations to be automatically tested before or during the provisioning process.

Have a small Terraform configuration prepared with a few assertions, run ```terraform test``` (https://developer.hashicorp.com/terraform/language/tests) unsuccessfully, having intentionally introduced a configuration error and show the test failing, fix it, and show the test passing. Then briefly discuss how it can be utilized as a CI/CD gate.

Tests cannot guarantee that infrastructure is completely correct, and tests that provision real resources can be slow, costly, and potentially destructive. Alternatives include ```terraform validate```, ```terraform plan```, policy-as-code tools, static analysis, and integration testing, which catch different classes of problems. We intend to discuss the differences between these approaches, and what each achieves in terms of validation of IaC configurations.

**Relevance**

This demo is relevant to infrastructure as code as it shows how we can provision infrastructure with higher confidence. We apply common software engineering practices of automating testing to infrastructure itself. This generates fast feedback and prevents reliability challenges. Furthermore, faulty IaC configurations naturally affect the entire DevOps pipeline, as a consequence from being the underlying infrastructure and the foundation to the entire service/product itself.
