# Assignment Proposal

## Title

Demo Proposal - Using Terraform to Detect and Recover from Infrastructure Drift

## Names and KTH ID

  - Jonathan Värild (varild@kth.se)
  - Jennifer Ha (jennha@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

We are going to use Terraform to visualize how Infrastructure as Code can be used to deploy a simple infrastructure. We are then going to create a configuration drift by making a manual change directly to the environment outside of Terraform, effectively meaning that the deployed environment no longer is 1-to-1 with the Terraform configuration. We should then be able to run the command `terraform plan` to show that Terraform detects this anomaly between the desired and actual state. If Terraform detects it, we should be able to run `terraform apply` to restore the infrastructure to the desired state.

**Relevance**

Infrastructure as Code is very relevant to keep infrastructure reproducible, automated, version-controlled, and to detect configuration drift and keep infrastructure consistent. If you instead were to manually configure all of your systems, it would often be way harder to keep track of the state of your systems. This can in turn can cause security problems, inconsistent parallel environments, and make restoration harder in the case of a catastrophic event. This task is thus very relevant to understand how a system like this can be used in practice.
