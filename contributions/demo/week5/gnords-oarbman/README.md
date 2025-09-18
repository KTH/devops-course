# Assignment Proposal

## Title
Preventing Misconfigurations in IaC with Policies

## Names and KTH ID
- Gustav Nordström (gnords@kth.se)  
- Oscar Arbman (oarbman@kth.se)  

## Deadline
- Week 5

## Category
- Demo

## Description
The demo will showcase Infrastructure as Code using Pulumi on AWS. With the help of a template, we will create a static website with an S3 bucket entirely in code. We will pretend this website contains sensitive information, but it could in theory be any other resource. To showcase potential risks, the initial deployment will intentionally make the bucket publicly accessible. Next, we will introduce policy as code using Pulumi CrossGuard to enforce security rules, such as requiring private buckets and blocking public access. This highlights how policies can prevent unsafe infrastructure from being deployed.

**Relevance**
The demo illustrates important DevOps principles by automating infrastructure deployment, enforcing security through policies, and enabling repeatable, version-controlled workflows.
