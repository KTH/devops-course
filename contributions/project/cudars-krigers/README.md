# Assignment Proposal

## Title

End-to-end DevOps pipeline on GKE with Terraform and Helm

## Names and KTH ID

- Jēkabs Čudars (cudars@kth.se)
- Kristers Krīgers (krigers@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We take a small three-tier app (frontend, REST API, PostgreSQL) and build the whole DevOps pipeline around it, with configuration for deployment on a GKE cluster. Everything lives in one GitHub repository.

1. On pull requests GitHub Actions runs lint, type checks and unit tests, E2E tests with Playwright, dependency checks, container scanning, Helm lint, and Terraform validate + TFLint + Trivy configuration scanning. Terraform plans can be posted on the PR when cloud access is configured.
2. Terraform defines the GKE Autopilot cluster, VPC, Workload Identity Federation for GitHub Actions, a budget alert and database backup storage. GCS provides remote state. Separate Helm configuration installs kube-prometheus-stack, Loki and Alloy.
3. We write the application Helm chart ourselves: Deployments, Services, Ingress, HPA, a StatefulSet with persistent storage for PostgreSQL, a migration Job, RBAC and NetworkPolicies.
4. After successful CI on main, CD builds images tagged with the commit SHA and pushes them to GitHub Container Registry alongside a versioned OCI chart. Deployment uses helm upgrade --install with rollback on failure. Authentication to GCP is keyless through Workload Identity Federation.
5. The app lets visitors suggest beer prices and authorised admins approve, reject or reverse changes. PostgreSQL stores suggestions, published changes and audit history. Clerk Development handles administrator authentication and MFA. Grafana dashboards and Prometheus alert rules cover workload health, while Loki collects logs.
6. The repository includes Docker startup, infrastructure configuration, deployment workflows and setup documentation. Local startup has been verified; a complete deployment from a fresh GCP project still needs end-to-end verification.

**Relevance**

The project puts CI, CD, infrastructure as code, a modern development platform and quality/security automation into one repository. We chose hands-on options to learn them: our own Helm chart, an in-cluster database over Cloud SQL, and Kubernetes over the Docker Swarm one of us already knows. GKE Autopilot reduces node-management work, and the report explains the limitations and what we would do differently in production. Links: Hosted project: https://alus.chudars.lv/ Link to proposal:https://github.com/KTH/devops-course/pull/3027