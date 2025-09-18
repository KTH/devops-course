# Assignment Proposal

## Title

Policy-as-Code for IaC: Enforcing Security, Compliance and Cost Control with Open Agent Policy (OPA)

## Names and KTH ID

  - Leo Åkerberg (leo3@kth.se)
  - Ferran Solanes Serrat(solanes@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

This demo will show how Open Agent Policy can ensure security, compliance and cost-efficiency when deploying Infrastructure as Code. We will use Terraform to deploy a basic environment setup composed by a server, a database, and a bucket, and showcase how OPA automatically validates Terraform configurations and blocks insecure or non-compliant deployments. Examples of insecure or non-compliant deployments are publicly accessible buckets, unknown images, or unsecure firewall configurations. The goal of the demo is to show how to prevent misconfigurations from scaling across environments.

**Relevance**

The relevance of the Demo lies in showing how Policy-as-Code can be used to ensure seurity, compliance and even cost control at the deployment stage. This automation avoids misconfigurations and non-compliant infrastructure to be deployed at large-scale, shifting from the simple, unchecked infrastructure deployment to controlled, secure and compliant infrastructure deployment.