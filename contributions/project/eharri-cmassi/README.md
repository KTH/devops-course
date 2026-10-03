# Assignment Proposal

## Title

Matjakt: A Reproducible DevOps Pipeline with Terraform

## Names and KTH ID

- Einar Harri (eharri@kth.se)
- Christopher Massi (cmassi@kth.se)

## Deadline

Task 3 — 11 October 2026

## Category

Project

## Description

We will implement an integrated DevOps pipeline for Matjakt, an existing grocery price comparison application built with React, TypeScript and Vite, using Firebase Hosting and Supabase. Matjakt was originally built as one of the group member's thesis project. The project will make development, testing and deployment reproducible while preserving the existing application stack.

We will use separate Firebase/Google Cloud and Supabase projects for the course environment, with deterministic synthetic grocery data. The existing production environment will remain operational. Price collection is outside the scope of this project.

Our implementation will include:

- **Reproducible development:** Version-controlled Supabase configuration, database migrations and seed data, pinned tool versions, an environment variable template and instructions for running the application from a clean clone with local Supabase through Docker.
- **Continuous integration:** GitHub Actions will run ESLint, TypeScript checks, Vitest unit tests, database integration tests, Playwright end-to-end tests and a production build on pull requests. Tests will cover search, product details, shopping cart calculations, authentication and profile access controls. External routing and map requests will be mocked for deterministic tests.
- **Infrastructure as Code:** Terraform will provision the course Google Cloud project, required APIs, Firebase configuration, Hosting site and deployment identity with GitHub OIDC through Workload Identity Federation. Terraform state will be stored in a private GCS bucket. CI will check formatting and configuration validity; infrastructure plans and applies will be performed locally after review. Creating the Supabase project will be a documented bootstrap step, followed by version-controlled database migrations.
- **Continuous deployment:** After merging to main, GitHub Actions will verify the merge commit, apply database migrations and deploy the frontend to a Firebase preview channel. Passing smoke tests will trigger promotion of the same Hosting version to the course environment's live channel. Releases will be serialized and linked to their source commit.
- **Development workflow and quality automation:** GitHub pull requests, required checks and peer review will control changes. ESLint and Dependabot will provide quality and dependency automation. Deployment credentials will be restricted to the release workflow.
- **Documentation and verification:** The repository will contain application code, infrastructure configuration, workflows, migrations, test data and setup instructions. We will document AI-assisted planning and implementation, including how generated suggestions were reviewed and tested. A 2–3-page report will explain the architecture, component interactions, design decisions, verified results and limitations.

We will demonstrate that a clean clone can run with test data, a failing test blocks merging and deployment, and an approved change reaches the live course environment automatically. We will also verify a Terraform plan with no unexpected changes after provisioning and test frontend rollback.

Preview and live deployments will share the course database, so subsequent migrations must remain backward-compatible. Database failures will be addressed through corrective migrations. Kubernetes, self-hosted Supabase, price collection and a separate monitoring system are outside the project scope.

**Relevance**

The project connects core DevOps practices in a single workflow: reviewed changes, automated builds and tests, reproducible infrastructure and automated deployment. Applying these practices to an existing application lets us demonstrate their practical value and explain how application code, database changes and infrastructure evolve together.

We will evaluate the trade-offs of managed services, shared database environments and separate infrastructure and application release processes, supported by recorded pipeline runs and deployment evidence.
