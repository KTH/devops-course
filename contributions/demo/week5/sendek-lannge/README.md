# Assignment Proposal

## Title

Automated Minecraft Server Deployment and Monitoring with Terraform

## Names and KTH ID

  - Lukas Lannge (lannge@kth.se)
  - Samuel Sendek (sendek@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

Terraform is an Infrastructure as Code (IaC) tool that we will use to automate the setup of a Minecraft server and later extend it with a monitoring platform. The Minecraft server, Prometheus, and Grafana will run in Docker containers locally.
We will first demonstrate provisioning the Minecraft server on its own. Then, by adding Prometheus and Grafana definitions to the same Terraform configuration, we show how IaC can provision both an application and its monitoring stack together. Prometheus will scrape metrics from the server and containers via manually configured endpoints, while Grafana connects to Prometheus to visualize these metrics in a dashboard. With a single Terraform command, the complete environment is created, configured, and started automatically, demonstrating IaC principles such as automation, reproducibility, and easy teardown.

**Relevance**

This demo highlights that observability itself can be managed as infrastructure. By defining both the application and its monitoring stack in Terraform, everything is provisioned consistently and with minimal manual effort. This illustrates the power of IaC: applications and their supporting services can be deployed, version-controlled, and reproduced as a single unit — aligning with DevOps principles of reliability, automation, and maintainability.
