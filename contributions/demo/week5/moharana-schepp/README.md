# Assignment Proposal

## Title

Policy as Code: Blast-Radius Protection for Terraform Changes

## Names and KTH ID

* Moritz Schepp mcschepp@kth.se
* Padmalaya Moharana moharana@kth.se

## Deadline

Week 5

## Category

Demo

## Description

Terraform makes infrastructure changes reproducible, but a plan can be syntactically valid but dangerous still: a change that looks small can mean destroying and recreating a large share of the existing fleet, e.g. if many resources share a common attribute, changing one attribute value can force all of them to be replaced at once. Regex-based linters can't catch this because they have no notion of the terraform plan as a whole.

We will create a policy written in Rego using Conftest to ensure that no more than x percent of a given resource type is destroyed and replaced at once. Without the policy in place, a proposed plan could replace 90% of running containers, which would likely get the system to crash. Our policy is in place to avoid that.

We will provision a set of containers locally using Terraform's Docker provider, standing in for a larger production fleet (which is infeasable and not required for our demo purpose). Before every `terraform apply`, we generate the machine-readable plan (`terraform show -json`) and evaluate it against our policy: no plan may destroy or replace more than a defined percentage of a given resource type at once. The policy computes this ratio directly from the plan output, which lists every managed resource including the unaffected ones (`action: no-op`).

Tools: Terraform (Docker provider), Conftest (using Rego policies).

**Relevance**

This directly follows up on the IaC lecture: it targets the policy as code as a pipeline gate applied before infrastructure changes take effect. It demonstrates that Infrastructure as Code brings not only reproducibility but, by applying policy as code, also the possibility of encoding organizational safety constraints as versioned, testable, and automatically enforced code rather than as common knowledge or some manual review step.

