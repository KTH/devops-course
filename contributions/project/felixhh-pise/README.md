# Assignment Proposal

## Title

Developing a DevOps Pipeline for a TypeScript Web Application

## Names and KTH ID

- Felix Castillo Huber (felixhh@kth.se)
- Pierre Segerström (pise@kth.se) 

## Deadline

- Task 3

## Category

- Project

## Description

Will utilize an existing web application – which currently lacks any DevOps components – and integrate a CI/CD DevOps pipeline on top of it.

**Development platform**:<br>GitHub

**CI Pipeline**
We will set up the CI pipeline using GitHub actions. This will:
- Run tests (conditionally, depending on file type).
- Verify that test coverage (e.g. statement coverage) is above certain threshold.

**CD Pipeline**
GitHub Actions will also be used to:
- Create a Docker image and push it to DockerHub.
- Every Docker image will be tagged with the hash of the commit that triggered the build.
- Will interact with a local GitHub Actions Runner, which receives the git hash, which is then passed to terraform, in order to re-run `terraform apply` to provision Docker containers using the new image.

**Infrastructure as Code techniques**
The app will be deployed locally, using Terraform to provision:
- At least 2 app containers
- A load balancer
- A database container

> *__Why using Terraform for this case, when Docker Compose achieves practically the same thing?__* <br> We are aware of this fact. However, by pursuing this setup, we can model how this scenario would interact with “real” cloud-based providers. Going for this “local approach” is purely for convenience and easier sharability of the repo.

**Quality or security automation**
- Enforce linting
- Static type checking
- Dependency vulnerability scanning

**Relevance**

The project will demonstrate how the core aspects of DevOps can be integrated into an existing web-based application. Nevertheless, the pipeline structure is highly applicable across any deployable application, since the same principles carry over.

**Performing this project will illustrate two things clearly:**
1. What value does a DevOps pipeline contribute to a project that is lacking it completely?
2. How an application can be deployed automatically, entirely on one local machine.