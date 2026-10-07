# Assignment Proposal

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

We will build a DevOps pipeline around a fork of [pytest-fastapi-crud-example](https://github.com/Pytest-with-Eric/pytest-fastapi-crud-example), a small FastAPI CRUD API that already has a pytest test suite. We keep the application simple on purpose, so that the work goes into the pipeline. Our focus is checking the infrastructure code, not only the application code: the Terraform and Docker files are security-scanned, and the running container is checked against what Terraform declares.

- **CI:** a GitHub Actions workflow runs the pytest suite on every push and pull request.
- **Containerization:** a Dockerfile packages the FastAPI app as an image.
- **IaC:** Terraform with the Docker provider defines the app container as infrastructure.
- **CD:** when the checks pass on `main`, a workflow builds the image and runs `terraform apply` on a self-hosted runner, so the app keeps running after the workflow ends.
- **IaC security scanning:** Checkov scans the Terraform files and the Dockerfile on every pull request and fails the check on insecure settings, such as a container running as root.
- **Drift detection:** a scheduled workflow runs `terraform plan` and fails if the running container no longer matches the Terraform code, for example after someone changes it by hand.
- **Development platform:** GitHub, with pull requests for every change to `main`.
- **Dependency security:** Dependabot keeps the dependencies up to date.
- **AI-assisted tools:** we will document how we used AI assistants.
- **Report:** a 2-3 page report on the architecture, our tool choices and the limitations.

**Relevance**

Infrastructure as Code only helps if the code is secure and still matches what is running. Checkov catches insecure configuration before it is deployed, and drift detection catches manual changes after deployment. Together with CI and CD, this shows how infrastructure can be tested and verified like application code.
