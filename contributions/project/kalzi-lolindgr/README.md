# Assignment Proposal

## Title

Resubmission: Reproducible CI/CD for a task-tracking API

## Names and KTH ID

  - Hasan Kalzi (kalzi@kth.se)
  - Love Lingren (lolindgr@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

Revised project submission for the 27 October 2026 resubmission deadline, addressing the grading feedback on the report and missing failure-blocking evidence.

- [Accepted task proposal #3088](https://github.com/KTH/devops-course/pull/3088)
- [Previous submission #3248](https://github.com/KTH/devops-course/pull/3248)
- [Revised project report PDF](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/main/docs/report.pdf)
- [Implementation repository](https://github.com/Hasan-Kalzi/task-tracking-project-devops)
- [Rollback verification record](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/96c1a50e28834ec3163a87b23ec572d9440c811a/docs/verification/rollback-20261011.md)
- [Evidence commit 96c1a50](https://github.com/Hasan-Kalzi/task-tracking-project-devops/commit/96c1a50e28834ec3163a87b23ec572d9440c811a)
- [Failed-delivery verification record](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/96c1a50e28834ec3163a87b23ec572d9440c811a/docs/verification/failure-blocking-20261017.md)
- [Controlled failed delivery run](https://github.com/Hasan-Kalzi/task-tracking-project-devops/actions/runs/39058760546)
- [Successful release v0.1.1](https://github.com/Hasan-Kalzi/task-tracking-project-devops/releases/tag/v0.1.1)
- [Deployment and access instructions](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/main/docs/runbook.md)
- [AI assistance record](https://github.com/Hasan-Kalzi/task-tracking-project-devops/blob/main/docs/ai-use.md)

Changes responding to the feedback:

1. The three-page report removes the contradictory rollback statements and links to the dated verification record and evidence commit. The 11 October checks exercised v0.1.0 to v0.1.1 and back to v0.1.0 using the corrected deployment playbook; the original saved task remained unchanged.
2. The 17 October controlled experiment demonstrates that failing checks prevent delivery. Pytest recorded 25 passes and one intentional failure; packaging and publication were skipped, and no v0.1.2 release was created by that run. The deliberately failing test remains on an unmerged experiment branch.
3. The revised report explains the integrated architecture, design decisions, component interactions, limitations, trade-offs and AI assistance within the required page limit.

The FastAPI/SQLite implementation integrates GitHub Actions CI and tag-triggered delivery, Docker Compose persistence checks and Ansible infrastructure provisioning and archive deployment. Continuous delivery is automated; applying a release to the local Ubuntu VM is a separate Ansible operation, with HTTP access through SSH forwarding.

**Relevance**

The project demonstrates how tested source becomes a versioned deployable artefact. It combines CI, continuous delivery, Infrastructure as Code and quality automation, and records application version changes with persistent data. The revised report and linked evidence address the unmet criteria identified in the original grading.
