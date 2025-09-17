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

Terraform is an Infrastructure as Code (IaC) tool that we will use to automate the setup of a Minecraft server along with a monitoring platform. The Minecraft server, Prometheus, and Grafana will all run in Docker containers locally. Prometheus will scrape metrics from the server and containers, and Grafana will provide a dashboard to visualize these metrics. With a single Terraform command, the Minecraft server and monitoring stack are created, configured, and started automatically, demonstrating IaC principles such as automation, reproducibility, and easy teardown.

**Relevance**
Using Terraform, the Minecraft server and monitoring stack are provisioned with minimal manual effort, ensuring consistency and reproducibility. Prometheus and Grafana provide real-time insights into server performance and container health, highlighting the importance of observability in DevOps workflows.
