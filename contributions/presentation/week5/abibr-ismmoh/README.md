# Assignment Proposal

## Title

Coolify as Declarative Infrastructure as Code: Simplifying DevOps for Small Teams

## Names and KTH ID

  - Ahmedhadi Bashir (abibr@kth.se)
  - Ismail Mohammed (ismmoh@kth.se)

## Deadline

- Week 5

## Category

- Presentation

## Description

This presentation explores Coolify, an open-source, self-hosted Platform-as-a-Service (PaaS) that demonstrates how declarative Infrastructure as Code can be made accessible for small teams.

Coolify runs on Docker and automates important DevOps tasks such as Git-based deployments, SSL certificates, secrets management, and database provisioning. Instead of writing long step-by-step scripts like creating a virtual machine, installing dependencies, and configuring SSL, developers only need to declare the desired setup for example an application with a Postgres database and HTTPS. Coolify then provisions everything automatically

We will explain how Coolify applies IaC principles in a more user-friendly way, highlight its main features, and compare it with both managed platforms like Heroku and traditional IaC tools like Terraform. This allows us to discuss the trade-off between simplicity and control, and why Coolify is an interesting case for learning how IaC can be adapted beyond large-scale enterprise environments.


**Relevance**

Coolify is directly relevant to DevOps because it supports key principles like continuous deployment, infrastructure as code, and automation of everyday tasks. It shows how small teams can work with DevOps practices without needing complex Kubernetes setups or costly managed services. At the same time, it highlights the challenge of finding a balance between making operations simple and keeping enough control over the infrastructure, which is an ongoing issue in modern DevOps work.