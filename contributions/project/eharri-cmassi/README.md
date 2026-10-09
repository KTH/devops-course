# Assignment Proposal

## Title

Matjakt: A Reproducible DevOps Pipeline with Terraform

## Names and KTH ID

- Einar Harri (eharri@kth.se)
- Christopher Massi (cmassi@kth.se)

## Deadline

Task 3

## Category

Project

## Description

We will build an integrated DevOps workflow for [Matjakt](https://github.com/einhar1/matjakt), an existing grocery price comparison application using React, TypeScript, Vite and Supabase. Originally developed as a thesis project by one team member, the application will be deployed to a separate course environment on Google Cloud Run.

The project will include:

- **CI:** GitHub Actions will run ESLint, TypeScript checks, Vitest, database tests, Playwright end-to-end tests and a production build. Integration tests will use real local Supabase; external routing and map requests will be mocked.
- **Infrastructure as Code:** Terraform will manage Cloud Run, Artifact Registry, APIs, IAM and OIDC identities within a separate Google Cloud project. HCP Terraform will store state, provide speculative PR plans and automatically plan/apply infrastructure changes pushed to main.
- **CD:** After successful main checks, Actions will apply course migrations, package the verified build into a container and deploy a tagged revision without live traffic. Smoke tests will precede promotion of that same revision. Releases will record their commit and support frontend rollback.
- **Reproducibility:** Versioned Supabase configuration, migrations, synthetic fixtures, pinned dependencies and Docker-based local development will support starting from a clean clone. Creating the hosted Supabase project will be a documented bootstrap step.
- **Quality and collaboration:** GitHub pull requests and required checks, ESLint, Dependabot and dependency auditing will support change control. Google authentication will use short-lived OIDC credentials.

The course database will use a catalog-only production snapshot, excluding accounts and profiles. Local development and CI will use deterministic synthetic data. Price collection will remain outside scope.

We will document AI assistance and provide a 2–3-page report explaining architecture, verification, decisions and limitations, alongside repository instructions and pipeline evidence.

**Relevance**

The project will connect testing, infrastructure provisioning and deployment into one reproducible workflow. It will demonstrate CI/CD, Infrastructure as Code and recovery, including the trade-offs of managed services and a shared preview/live database.
