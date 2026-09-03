# Assignment Proposal

## Title

Automated Changelog and Release Management with a Custom GitCliff Docker Image

## Names and KTH ID

 - Jēkabs Čudars (cudars@kth.se)
 - Rami Khedair (khedair@kth.se)

## Deadline

- Task 1

## Category

- Executable tutorial

## Description

This executable tutorial will demonstrate how to build and use a customised GitCliff Docker image as part of a GitLab CI/CD release workflow.

The work will be split across **two separate repositories**:

1. **GitCliff Docker image repository**
   - Contains the Dockerfile for the customised GitCliff image.
   - The image will package GitCliff with the required configuration and tools.
   - Hadolint will be used to lint the Dockerfile.
   - Trivy will be used to scan the built image for vulnerabilities.
   - The resulting image will be published to a container registry.

2. **Example project repository**
   - Uses the published GitCliff Docker image in its GitLab CI/CD pipeline.
   - Contains two release jobs:
     - **Generate Changelog:** runs GitCliff to generate `CHANGELOG.md` and commits the result back to the repository.
     - **Create Tag:** runs `git cliff bump` to determine the next version and creates and pushes the corresponding Git tag.

The tutorial will show the complete workflow from a new commit to an automatically generated changelog and version tag.

**Relevance**

Release management is an important part of DevOps, but manually maintaining changelogs and release versions can introduce errors and inconsistent processes.

This tutorial demonstrates how CI/CD can automate these tasks and make the release process reproducible. Using a custom Docker image also ensures that the same GitCliff environment and configuration are used consistently across pipeline executions.

The integration of Hadolint and Trivy demonstrates how the tooling used in the CI/CD pipeline can itself be checked for Dockerfile quality and container vulnerabilities.

The tutorial therefore combines **CI/CD automation, containerisation, release automation, and DevSecOps practices** into one reproducible workflow.