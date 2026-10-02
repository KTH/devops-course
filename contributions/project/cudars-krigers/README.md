# Assignment Proposal

## Title

End-to-end DevOps pipeline on GKE with Terraform, Helm and AI-assisted remediation

## Names and KTH ID

- Jēkabs Čudars (cudars@kth.se)
- Kristers Krīgers (krigers@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We take a small three-tier app (frontend, REST API, PostgreSQL) and build the whole
DevOps pipeline around it, deployed on a GKE cluster. Everything lives in one GitHub
repository.

1. On every pull request GitHub Actions runs lint, type checks and unit tests, E2E tests with playwright, SonarQube with a quality gate, dependency and secret scanning, helm lint, and terraform validate + tflint + Trivy config scan with the terraform plan posted on the PR.
2. Terraform will create the GKE Standard cluster, VPC, Artifact Registry,
Workload Identity Federation for GitHub Actions, a budget alert and GCS remote state,
split into modules. It also installs the third-party charts (kube-prometheus-stack,
Loki, Tempo, HolmesGPT) through the Helm provider.
3. We will write the application Helm chart ourselves: Deployments, Services, Ingress, HPA, a StatefulSet with persistent volumes for PostgreSQL, a pre-upgrade migration Job, RBAC and NetworkPolicies.
4. On release a CD will be triggered, images are tagged with the commit SHA and pushed to Artifact Registry with a versioned OCI chart, then deployed with helm upgrade --install --atomic. Auth to GCP is keyless via Workload Identity Federation.
5. The app is instrumented with OpenTelemetry and monitored in Grafana. An alert triggers HolmesGPT, which investigates with Prometheus and Loki data and proposes a helm rollback that runs only after human approval.
6. As a result we will deliver a repo runnable from a fresh GCP project.

**Relevance**

The project puts CI, CD, infrastructure as code, a modern development platform and
quality/security automation into one repository, and closes the loop from delivery to
operation with observability-driven remediation. We chose the more hands-on options on
purpose to learn them - GKE Standard over Autopilot, our own Helm chart, an in-cluster
database over Cloud SQL, and Kubernetes over the Docker Swarm one of us already knows -
and the report explains what we would do differently in production.
