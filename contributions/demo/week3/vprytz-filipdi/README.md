# Assignment Proposal

## Title

GitOps-Driven Ephemeral Preview Environments on Kubernetes with DNSControl

## Names and KTH ID

  - Vilhelm Prytz (vprytz@kth.se)
  - Filip Dimitrijevic (filipdi@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

The idea is to have preview deployments for pull requests, so someone reviewing a pull request can look at the live result and not just the diff. The live result would be a real URL with HTTPS. So the main branch would, using GitHub actions, automatically deploy to a "production" environment. For each Pull Request created towards the main branch, GitHub Actions would setup a temporary deployment environment (review environment), which would run the version of the code as it exists in that specific branch. To do this, we would use a small lightweight Kubernetes setup using [K3s](https://docs.k3s.io) (as well as Helm and ingress) and an automated DNS setup using [DNSControl](https://dnscontrol.org/) (to create DNS records used for the review deployments).

**Relevance**

Review environments are used to separate a deployment from release. Since all changes are built and running in a real environment, that turns code review into using the change. This relates strongly to the principles of CD, Continuous Deployment, since all code is continuously deployed. As soon as someone opens a PR, this has been deployed into a separate environment, continuously. This relates to the DevOps principles in the sense that it keeps code deployable at any time, meaning it is still a human decision to deploy it.

