# Assignment Proposal

## Title

Bringing OptiFarm to the Cloud: A DevOps pipeline for a farm-management application

## Names and KTH ID

  - Elena Pan (elenapan@kth.se)
  - Moritz Constantin Schepp (mcschepp@kth.se)

## Deadline

- Task 3

## Category

Project


## Description

We are going to bring OptiFarm, a farm-management application implemented as a student project from another course, into the cloud.
We will implement a DevOps pipeline that allows for continuous integration and continuous deployment. The pipeline will be implemented with GitHub Actions workflows.
We're planning on deploying the application to a VM hosted in Google Cloud. The VM will be managed using Terraform to implement a widely used Infrastructure as Code approach. The application will be containerized and deployed to the VM with Docker.

The pipeline will be fully automated, running tests on every PR and deploying to the VM on every merge to the main branch.
Dependabot will be used to keep dependencies up to date, and GitHub's secret scanning will detect committed secrets.

**Relevance**

This proposal demonstrates the implementation of a complete DevOps pipeline for a non-trivial application. Everything is automated and version-controlled, so a changes goes from commit to running system without manual steps, and the infrastructure can be recreated from the repo.
