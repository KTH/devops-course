# Assignment Proposal

## Title

Automatic Rollback in CI/CD pipelines using Kubernetes Flagger and Prometheus

## Names and KTH ID

- Eric Wernström (ericwer@kth.se)
- August Yvdal (yvdal@kth.se)

## Deadline

- Week 3

## Category

- Presentation

## Description

We wish to present the process of automated rollback in CD pipelines with canary releases. The process involves monitoring of the canary release which provides metrics for evaluation the performance and stability of a release using a tool like Prometheus. In Kubernetes projects, tools like Kubernetes Flagger can be used to either trigger a rollback or to mark the canary release as stable, making it the new stable version.

**Relevance**

Despite CI/CD pipelines often having extensive test suites, it is not guaranteed that said tests are up-to-date and able to catch everything which may go wrong when a change is deployed to production. Therefore it is important to implement safeguards like monitoring and rollback mechanisms. Looking at metrics like HTTP error rates and latency allows the system to detect shaky deployments and to revert back to a knwon stable version. The tools we mention are common choices in projects that are live today. These tools allign nicely with core principles of DevOps like automation.
