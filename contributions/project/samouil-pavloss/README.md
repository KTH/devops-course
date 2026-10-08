# Assignment Proposal

## Title

Self-hosted PaaS Cluster with Dokploy

## Names and KTH ID

  - Samouil Mosios (samouil@kth.se)
  - Pavlos Spanoudakis (pavloss@kth.se)

## Deadline

Oct 11th

## Category

Project

## Description

**Project submission.** The project is complete. Proposal: [#2997](https://github.com/KTH/devops-course/pull/2997).

- Source repo: https://github.com/sammosios/dd2482-project
- Report: https://github.com/sammosios/dd2482-project/blob/main/REPORT.md
- Walkthrough guide: https://github.com/sammosios/dd2482-project/blob/main/WALKTHROUGH.md

We built a self-hosted PaaS: a 3-node Docker Swarm cluster on Google Cloud (1 manager, 2 workers), managed by [Dokploy](https://dokploy.com/). The whole cluster is created from the repository with `./up.sh` and torn down with `./down.sh`, using staged Terraform (VMs, network, DNS, registry, OpenBao, CI runners, apps) and no manual steps. On top of the cluster we run:

- self-hosted GitHub Actions runners inside the cluster
- an example app (Roster, Go + htmx) with 2 replicas, PostgreSQL and Redis, deployed through a CD pipeline: tests, Trivy secret scan, image build, Trivy vulnerability gate, push to the in-cluster registry, then a Dokploy deploy
- OpenBao as the secrets vault, which Dokploy queries at deploy time so apps never hold vault credentials

The cluster is currently running on GCP and burning through credits, so please let us know once it has been reviewed so we can take it down. To see the systems in action instead of only reading the report, follow the walkthrough guide.

Our services (Dokploy, OpenBao, Roster) are public on the internet and require authentication. Credentials are not in the documents or the repo, so please contact us privately if you want to browse the tools.
