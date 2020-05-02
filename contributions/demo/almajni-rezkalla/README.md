# Demo Proposal: End-to-End CI/CD (Continuous Deployment) pipeline with Jenkins, ansible, and Kubernetes `Minikube`

## Contributors
* Nour Alhuda Almajni - almajni@kth.se - @nour95
* George Rezkalla - rezkalla@kth.se - @georgewbar

## Description
We will create an End-to-End CI/CD pipeline with Continuous Deployment (Zero-Downtime Deployment) using Jenkins, Ansible and Kubernetes `Minikube`. The deployed application will be a Java (or Javascript; we are already done with Javascript application to be honest) application that shows the current Date and Time together with the current version of the application to show that a new version of the application was deployed with Zero-Down time.

To be more concrete, we will create a **local** cluster consisting of one node in a virtual machine on a macOS laptop using `Minikube`. Moreover, we  will use `Kubectl` to show debugging information. Then, we will create a pipeline (i.e `Declarative` Pipeline that has some blocks of `Scripted` pipeline) in `Jenkins` that is triggered when new code is pushed to Github. This Pipeline will create a `Docker` image, and build the app and test it, and if it passes all the tests, it will continue to deploy it on the Kubernetes cluster using Ansible playbook that defines a `Deployment` and a `NodePort` service to be deployed on the `Minikube` cluster.

As beginners in Kubernetes, this Demo was difficult because we needed to understand `Kubernetes` at first, and it took some time to decide which environment to choose to install `Kubernetes` and then install `Kubernetes` locally. Then, it took some time to know how to integrate `Ansible` with `Jenkins` and `Kubernetes`.

## Criteria that we want to fulfill
* The demonstration screencast is clearly motivated (why it matters for Devops?).
* The demonstration screencast is difficult to do.
* The demonstration screencast is original. -> (Every demo or tutorial does things in other ways, and there is no one way to do things. We mixed things from different references).
* The demonstration screencast is sublime (eg visually appealing).
* The demonstration screencast contains an easter egg -> (there will be a surprise).
* An accompanying Github repository has been made (optional).
