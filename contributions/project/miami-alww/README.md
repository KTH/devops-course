# Assignment Submission

## Title

Security-Scanned Infrastructure as Code with Drift Detection for a FastAPI API

## Names and KTH ID

- Miami Alvelistin (miami@kth.se)
- Albin Wallenius Woxnerud (alww@kth.se)

## Deadline

- October 11 2026

## Category

- Project

## Description

Project repository: https://github.com/devops-mialww/project

We built a DevOps pipeline around a fork of [pytest-fastapi-crud-example](https://github.com/Pytest-with-Eric/pytest-fastapi-crud-example), a small FastAPI + SQLite user CRUD API with a pytest suite. The application is kept simple on purpose, so that the work goes into the pipeline. The focus is on checking the infrastructure code, not only the application code: the Terraform and Docker files are security-scanned, and the running container is checked against what Terraform declares.

- **CI** (`ci.yml`): on every push and pull request, GitHub Actions runs the pytest suite, builds the Docker image and runs Checkov.
- **Containerization** (`Dockerfile`): packages the FastAPI app as an image. The container runs as a non-root user with a read-only root filesystem, a memory limit, no Linux capabilities and `no-new-privileges`. The SQLite database lives in the Docker volume `fastapi-crud-data`.
- **IaC** (`terraform/`): Terraform with the Docker provider declares the container, the image and the data volume.
- **IaC security scanning** (`.checkov.yaml`, `.checkov/`): Checkov scans the Dockerfile and the Terraform files, with seven custom policies for `docker_container`, and fails the check on insecure settings such as running as root.
- **CD** (`cd.yml`): when CI succeeds on `main`, a self-hosted runner runs `terraform apply`, so the app keeps running after the workflow ends. The workflow then calls `/api/healthchecker` to verify the deployment.
- **Drift detection** (`drift.yml`): a scheduled workflow runs `terraform plan` every hour and fails if the running container no longer matches the Terraform code, for example after someone changes it by hand.
- **Dependency security** (`dependabot.yml`): Dependabot updates the Python packages, GitHub Actions, the base image and the Terraform provider.
- **Development platform:** GitHub, with pull requests for changes to `main`.
- **AI-assisted tools:** documented in [`AI_USAGE.md`](https://github.com/devops-mialww/project/blob/main/AI_USAGE.md).
- **Report:** [`REPORT.md`](https://github.com/devops-mialww/project/blob/main/REPORT.md) covers the architecture, our tool choices and the limitations.

**Relevance**

Infrastructure as Code only helps if the code is secure and still matches what is running. Checkov catches insecure configuration before it is deployed, and drift detection catches manual changes after deployment. Together with CI and CD, this shows how infrastructure can be tested and verified like application code.
