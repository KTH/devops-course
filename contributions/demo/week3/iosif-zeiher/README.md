# Assignment Proposal

## Title

_How to deploy on AWS EC2 using ECS and GitHub Actions_

## Names and KTH ID

  - Iosif Koen (iosif@kth.se)
  - Fabian Zeiher (zeiher@kth.se)

## Deadline


- Week 3

## Category

- Demo

## Description

In our Demo we present how to setup a deployment in the AWS cloud service. We use ECS (Elastic Container Service) to deploy our application
from a docker image. As infrastructure we choose EC2 instances (instead of a serverless approach). ECS is a managed Kubernetes service from AWS.
We show how to automate the deployment using github actions and docker, but the focus of our demo is on ECS. In parallel we are going to
run a live deployment of a flask server and webpage. The audiance can easily follow the live deployment using their phone.

**Relevance**

AWS is the most relevant cloud platform right now with over 30% market share. We us a docker based deploment because it gives us
more flexibility to run on different architectures. We choose ECS on EC2 hardware to keep more control over our infrastructure.
Github actions is the most user friendly way to orchestrate a deployment pipeline. Our Webpage runs on python flask because it
one of two most state-of-the-art web framework for python.
