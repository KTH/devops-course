# Assignment Proposal

## Title

Disaster Recovery using [Terraform](https://developer.hashicorp.com/terraform/intro) and the [Pilot Light Strategy](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/) in a Multi-Cloud Environment

## Names and KTH ID

  - Adrian Thees (thees@kth.se)
  - Alexandru Matcov (matcov@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

This demo will show how to create a disaster recovery plan for an application in a multi-cloud environment using Terraform and how it works in a demonstration. 
The main goal is to use infrastructure as code to automatically fail over the application from a primary cloud (e.g. [AWS](https://aws.amazon.com/)) to a secondary, standby cloud (e.g. [GCP](https://cloud.google.com/?hl=en)). 
The secondary cloud runs a minimal, scaled-down version of the infrastructure. This is called a "pilot light" and is just enough to maintain connectivity and replicate important data. 
In the case of a disaster on the primary cloud the standby server will automatically be scaled up and the traffic is routed to the secondary server.

**Relevance**

Disaster Control has always been a prevelant topic in any system that requires robustness. While disaster control is already pretty well documented we want to take it a step further and implement a multi cloud environment which would cover more failures, e.g. AWS having a serious outage (which is very unlikely but possible).

We decided to use Terraform because it is well established in the field and includes API's for the most common cloud providers, which helps to prevent vendor lock-in.

