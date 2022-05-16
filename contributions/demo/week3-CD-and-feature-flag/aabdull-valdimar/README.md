# Assignment Proposal

## Title

Microservices CI/CD pipeline on K8s Cluster in Digital Ocean (Cloud).

## Names and KTH ID

- Abdullah Abdullah (aabdull@kth.se)
- Valdimar Björnsson (valdimar@kth.se)

## Deadline

Deadline for task 1 (5th April)

## Category

Demo

## Description

DigitalOcean Kubernetes (DOKS) is a managed Kubernetes service that lets you deploy Kubernetes clusters without the complexities of handling the control plane and containerized infrastructure. In this demo we will show a CI/CD
pipeline with Github Actions for different microservices of a simple application where on each push to the master branch will trigger an action that will update the docker image for the microservice and deploy it on the digital ocean cluster.

***Task Submission***
During our demo we showed the CI/CD pipeline using Github Actions for one of our microservice and showed that a 
change in one microservice can trigger CI/CD for that particular microservice and hence the deployments are independent of
the environment and it does not affect the other deployed services in the kubernetes cluster. 

Repository for the Demo:
- [Microservices-CI/CD-Demo-For-Devops](https://github.com/Abdullah1428/microservices-ci-cd-demo)

Slides for the Demo:
- [Slides-For-Demo](https://docs.google.com/presentation/d/1aZPliPkqUnlL2rkJyi8gBB3codaFZPsUV-NkvZ_FI-E/edit?usp=sharing)
