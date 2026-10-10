# Assignment Proposal

## Title

End-to-End DevOps Pipeline and Infrastructure Automation for an Open-Source Git Web Viewer

---

## Names and KTH ID

Erik Söderlund – eriso@kth.se

Anders Mouanga – mouanga@kth.se

---

## Deadline

Deadline: 11 October 2026

## Category
Project

---

## Description

We will adopt [klaus](https://github.com/jonashaag/klaus), a 1,500-LOC Python/Flask web-based Git repository viewer. While the core application logic is functional, it lacks automated CI/CD, containerization, Infrastructure as Code (IaC), and security gates.

We will build a production-ready DevOps pipeline managing the complete lifecycle from commit to host deployment:

* **Platform & Governance:** GitHub using PR workflows, branch protection rules, and required status checks on `main`.
* **Continuous Integration (CI):** GitHub Actions running **Ruff** (linting), **mypy** (type checking), and **pytest** (unit testing). Ephemeral Git repos will be initialized in CI to run integration tests against real diffs and tree views.
* **Continuous Delivery (CD):** Merges to `main` trigger a multi-stage Docker build, publishing images to **GHCR** (tagged with commit SHA and `latest`) and deploying to the live host.
* **Infrastructure as Code (IaC):** **Terraform** provisions cloud VMs, network interfaces, and firewalls. **Docker Compose** orchestrates the host environment, managing reverse proxy routing and persistent volume mounts.
* **Quality & Security Gates:** Automated scanning via **Bandit** (SAST), **Trivy** (containers), **Dependabot** (dependencies), and **Gitleaks** (secret detection). Findings above set thresholds will block pipeline releases.
* **Secrets Management:** Injected at runtime via GitHub Actions Secrets—no sensitive values or private keys in source control or Terraform state.
* **AI Assistance Tracking:** Any AI tools used for scripts, test fixtures, or IaC manifests will be logged, reviewed, and documented in the final report.

The repository will deliver source code, tests, Dockerfiles, GitHub Actions workflows, Terraform/Compose manifests, and a **2–3 page report** covering architecture, security, and trade-offs.

---

Relevance

This project applies real-world DevOps practices to an existing web application. It demonstrates automated integration testing against file-system state, persistent storage management via IaC, multi-stage Docker security, automated security gates, and automated host deployment.