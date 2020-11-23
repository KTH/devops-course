# Demo

## Members

Robin Bråtfors (bratfors@kth.se)

Kasper Liu (kasperli@kth.se)

## Topic

Demo of using Calico policies in Kubernetes, utilizing the Google Kubernetes Engine.

## Details
Containers are becoming more popular and so does the demand for security around containers. Calico is used for network security and source networking for containers and virtual machines. According to a study performed by StackRox (2020), security is the top concern when it comes to container strategies. Furthermore, 94% of respondents had experienced a security incident in the past year, the majority of it due to misconfiguration. We want to demonstrate how Calico policies can be used in Kubernetes to increase the security in an easy way. We will do this using the Google Kubernetes Engine (GKE) provided on the Google Cloud Platform.

### Reference
StackRox. (2020). *Kubernetes and Container Security and Adoption Trends*.
https://www.stackrox.com/kubernetes-adoption-and-security-trends-and-market-share-for-containers/ 

## Prior setup
We set up a single cluster on GKE and enabled network policies on it.

We created the namespace stars.

We created 4 pods: a client pod on its own client namespace, backend and frontend on the stars namespace, and a management-ui pod on its own management-ui namespace.

## Easter egg
<details><summary>Spoiler warning!!</summary>There's a COVID PSA visible the first time we enter the web browser @0:35</details>

## Screencast
https://youtu.be/Nz0DZyXkcu4

## Demo repository
https://github.com/rbratfors/calico-demo
