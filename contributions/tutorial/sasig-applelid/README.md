# Topic: GitOps with K8s & Flux CD

Sigrún Arna Sigurðardóttir sasig@kth.se @s1grun
Gunnar Applelid applelid@kth.se @gynther-k

# Introduction

GitOps is a way to do Kubernetes cluster management and application delivery.  It works by using Git as a single source of truth for declarative infrastructure and applications. With Git at the center of your delivery pipelines, developers can make pull requests to accelerate and simplify application deployments and operations tasks to Kubernetes(https://www.weave.works/technologies/gitops/). I will be using Flux to implement this methodology. 
Flux is the operator that makes GitOps happen in your cluster. It ensures that the cluster config matches the one in git and automates your deployments(https://www.weave.works/oss/flux/).
Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications (https://kubernetes.io/).

# Description

In this tutorial I will go over the following steps:
- Create a K8s cluster in Azure
- Setup Flux using Helm
- Deploy simple service using Flux
- Configure Continous Deployment 

Considerations:
- Can I assume or refrence other tutorials for:
  - Azure CLI already setup 
  - Sufficent privilidges in Azure
  - Docker for desktop already setup 
  - DockerHub access to be able to push images


Refrences: 
- https://fluxcd.io/


