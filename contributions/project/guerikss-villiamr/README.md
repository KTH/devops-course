# Assignment Proposal

## Title

DevOps pipeline for a todo web application with GitOps deployment

## Names and KTH ID

  - Harry Eriksson (guerikss@kth.se)
  - Villiam Riegler (villiamr@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We will build a small todo web application and set up a complete DevOps pipeline around it. The application
lets users create, complete and delete todo items, which are persisted in a PostgreSQL database running as a
sidecar container next to the application.

- **CI:** GitHub Actions runs tests on every pull request, and builds and pushes a container image to GitHub
  Container Registry on merge to main.
- **CD:** After the image is pushed, a CI job updates the image tag in the Kubernetes manifests in the
  repository. Argo CD watches these manifests and deploys the new release image to the cluster.
- **IaC:** Terraform creates a local Kubernetes cluster (kind) and installs Argo CD into it.
- **Development platform:** GitHub with branch protection.
- **Quality/security automation:** Dependabot for dependency updates.

**Relevance:** The project applies the core DevOps practices from the course, continuous integration, continuous
delivery, infrastructure as code and security automation, to a working application in one integrated workflow.
Using Argo CD gives us a pull-based CD model where the cluster state is defined in the repository, and Terraform
makes the whole environment reproducible with a single command.
