# Assignment Proposal

## Title

Declarative Continuous Deployment on K8s Using ArgoCD

## Names and KTH ID

- Ayushman Khazanchi (ayushman@kth.se) 

## Deadline

Task 1: Apr 5th

## Category

Demo

## Description

In imperative deployment there is often someone "pushing a button" to start a deployment. The final environment is the result of a number of steps as defined by the deployment scripts. With Declarative deployment this concept is shifted to defining the environment as a "state". As soon as this state is modified, declarative tools attempt to do deployment by "syncing" towards the new state. ArgoCD is a declarative GitOps tool that is used for continuous deployment to Kubernetes. ArgoCD considers a git repository as its source of truth and attempts to do automatic deployments on K8s whenever it observes a change in the git repo. 

For my demo, I will attempt to deploy a small example application on minikube using ArgoCD. I will then make a small change to the application and push it to the repo and demo the automatic sync capability of ArgoCD (declarative deployment). On seeing the change in the repo, ArgoCD should automatically update the application.

Final Submission

- Demo scheduled for Thursday, Apr 7, 920 am
- Git repo and documentation: https://github.com/aykhazanchi/argocd-demo
