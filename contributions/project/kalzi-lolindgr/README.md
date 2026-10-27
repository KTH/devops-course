# Assignment Proposal

## Title

Final submission: Reproducible CI/CD for a task-tracking API

## Names and KTH ID

  - Hasan Kalzi (kalzi@kth.se)
  - Love Lingren (lolindgr@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

Final submission of the completed project from the accepted proposal [#3088](https://github.com/KTH/devops-course/pull/3088).

- [Implementation repository](https://github.com/Hasan-Kalzi/task-tracking-project-devops)
- [Project report (PDF)](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/main/docs/report.pdf)
- [Release v0.1.1 and deployment assets](https://github.com/Hasan-Kalzi/task-tracking-project-devops/releases/tag/v0.1.1)
- [Successful CI run](https://github.com/Hasan-Kalzi/task-tracking-project-devops/actions/runs/38172535137)
- [Successful delivery run](https://github.com/Hasan-Kalzi/task-tracking-project-devops/actions/runs/38172535183)
- [Deployment and access instructions](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/main/docs/runbook.md)
- [AI assistance record](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/main/docs/ai-use.md)

The FastAPI/SQLite application supports creating, listing and completing tasks with input validation and persistent storage. GitHub Actions runs 25 tests, Ruff checks, Ansible and Compose validation, a Docker build and container persistence checks. Version tags trigger delivery of the tested Linux/amd64 image archive, deployment bundle, release manifest and SHA256 checksums. Ansible provisions an Ubuntu 24.04 x86_64 VM and applies the delivered image without rebuilding.

We confirmed provisioning and deployment, unchanged repeats, task persistence after container recreation, an upgrade from v0.1.0 to v0.1.1 and manual rollback to v0.1.0. The original saved task remained unchanged across the upgrade and rollback.

The application runs on a local Ubuntu VM. Its loopback HTTP endpoint is accessed through an SSH tunnel as described in the runbook. Continuous delivery is automated; applying a release to the VM is a separate Ansible operation.

Codex generated the implementation baseline and report draft. The students integrated contributions and ran the checks. AI assistance, corrections, responsibilities and verification limits are documented in the report and AI assistance record.

**Relevance**

The project integrates CI, versioned software delivery, Infrastructure as Code and automated quality checks in one repository. It demonstrates how tested source becomes a deployable artefact and how application versions can be changed while retaining persistent data. The report explains the architecture, design decisions, component interactions, limitations and trade-offs.
