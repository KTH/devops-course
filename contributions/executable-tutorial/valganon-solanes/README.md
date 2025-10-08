# Assignment Proposal

## Title

Building a secure CI/CD for Containers with Chainguard

## Names and KTH ID

  - Miguel Valgañon (valganon@kth.se)
  - Ferran Solanes (solanes@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

In this tutorial, we will use Killercoda to build a small application, containerize it with Docker, and then integrate Chainguard in the CI/CD to scan the resulting image. If Chainguard deems the image insecure, the pipeline will fail, and therefore the insecure container will not be deployed. This ensures that only secure, and signed images are deployed in a Kubernetes cluster.

At the end of the tutorial, the user should be able to deploy a CI/CD pipeline, which takes security into account using Chainguard, as well as be familiar with the Kubernetes environment.

Steps of the tutorial:
1- Set up environment; Docker, Chainguard, Kubernetes
2- Create the CI/CD (With Jenkins)
3- Develop a Simple application
4- Containerize the application with Docker
5- Run Pipeline to check the container for vulnerabilities. The container will be deployed if Chainguard deems it secure.

**Relevance**

This tutorial is relevant to this course, since it is a crucial part of the DevOps lifecycle, and more specifically to the DevSecOps practices. It is a mix of the topics studied on Weeks 2, 3 and 6. By incorporating Chainguard into CI/CD workflows, teams ensure that only verified, vulnerability-free images reach deployment, reducing risk and improving reliablility.

The link to the Killercoda tutorial is: https://killercoda.com/killercoda-testing/scenario/devops_tutorial
The link to the Github repository is: https://github.com/mivalgan/killercoda-testing