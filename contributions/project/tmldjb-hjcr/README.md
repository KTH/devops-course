# Assignment Proposal

## Title

House Split: GitOps Delivery to a Local Kubernetes Cluster with Terraform and Argo CD

## Names and KTH ID

- Tomás Brito (tmldjb@kth.se)
- Henrique Cavaco (hjcr@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We are housemates, so the application is a small web app we made for this project to split shared house expenses: housemates add who paid what, and the app computes each balance and a short list of payments that settles everything. It is a Python (Flask) app with SQLite storage, a simple HTML page, a JSON endpoint and unit tests for the settling logic. The code is in https://github.com/tomasmbrito/house-split.

Around it we will build a DevOps pipeline that anyone can reproduce on a laptop, with no cloud account. A laptop has no public address, so a pipeline running on GitHub cannot push a deployment to it. We therefore use pull-based delivery (GitOps): Argo CD runs inside the cluster, watches the repository, and applies every new version by itself. The pipeline only needs to publish an image and change one line in Git, and it never gets credentials to the cluster.

How each criterion is covered:

- **Automated build and testing (CI)**: a GitHub Actions workflow runs on every push and pull request. It lints the code (ruff), runs the tests (pytest) and builds the Docker image.
- **Automated deployment (CD)**: on every merge to main, a workflow pushes the image to the GitHub Container Registry, tagged with the commit, and updates the image tag in the Kubernetes manifests. Argo CD sees the change and rolls out the new version automatically. Rolling back means reverting that commit.
- **Infrastructure as Code**: Terraform creates the Kubernetes cluster (kind), installs Argo CD with Helm and registers the application. The application itself is described declaratively in Kubernetes manifests (Deployment, Service and a volume for the SQLite database), so the whole system can be rebuilt with one command.
- **Development platform**: GitHub for the code, pull requests, Actions, the container registry and branch protection that requires the CI checks to pass before a merge.
- **Quality and security automation**: Trivy scans the Docker image in CI and fails the build on critical vulnerabilities that have a fix, and Dependabot opens pull requests to update the Python packages, the base image and the Actions.
- **Documented use of AI-assisted tools**: we will describe in the README and in the report what we used AI tools for and what we did ourselves.
- **Repository and report**: the repository will contain all code, configuration and instructions to run the system, and the 2-3 page report will explain the architecture, our design decisions and their limitations (for example, a single-node local cluster is not production, and Argo CD only checks the repository every few minutes).

**Relevance**

Most deployment pipelines push changes into an environment and need credentials for it. GitOps reverses this: the environment pulls its desired state from Git, so Git becomes the single source of truth and every deployment and rollback is a commit. This project shows that model end to end, connected to CI, Infrastructure as Code and automated security checks, in a setup small enough that we can explain every part of it.
