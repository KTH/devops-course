
# Assignment Proposal

## Title

Self-hosted PaaS Cluster with Dokploy

## Names and KTH ID

  - Samouil Mosios (samouil@kth.se)
  - Pavlos Spanoudakis (pavloss@@kth.se)

## Deadline

Oct 11th

## Category

Project

## Description

We will bootstrap a small cluster of VMs (using Multipass) and set up [Dokploy](https://dokploy.com/) in cluster mode as a self-hosted PaaS. One node acts as the Dokploy leader/control-plane, and we will configure automatic registration of worker nodes so that new VMs can join the cluster and scale it horizontally without manual setup.

Our Infrastructure as Code will mostly take the form of scripts driving the Dokploy CLI (VM provisioning, cluster bootstrap, worker registration, and service deployment), and we will use ephemeral testing environments to validate that the provisioning scripts are reproducible from a clean state.

On top of the cluster we will stand up a set of core services: self-hosted CI runners, example web applications, databases, a secrets vault for credential management, and static analysis via Trivy for scanning images and dependencies for vulnerabilities. Time permitting, we would also like to add object storage, message queues, and observability (metrics/logs/tracing) as nice-to-have extensions.

**Relevance**

This project is directly relevant to infrastructure as code, cloud-native tooling, and CI/CD. It demonstrates how a self-hosted PaaS can be provisioned and scaled from scratch through scripted automation rather than a managed cloud provider, and it touches on horizontal scaling, secrets management, vulnerability scanning, and CI infrastructure — core building blocks of a real DevOps platform. It also highlights the tradeoffs of a CLI-scripting-based approach to IaC compared to fully declarative tools.
