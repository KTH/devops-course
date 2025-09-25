# Assignment Proposal

## Title

Executable Tutorial: Using Tsunami to discover vulnerable applications

## Names and KTH ID

  - Emil Kanerva (ekanerva@kth.se)
  - Samuel Sendek (sendek@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

This tutorial will introduce Google’s Tsunami security scanner through a KillerCoda tutorial, show  how it can be set up and used to scan an endpoint for advanced vulnerabilities.

The flow of the tutorial will be to first set up Tsunami and a vulnerable server. Then Tsunami will be used to scan the vulnerable server for its vulnerabilities, inspecting the output. Subsequently the server will be updated to a non-vulnerable version, to show that Tsunami will no longer detect the vulnerability, as it has been removed. Then finally demonstrate how Tsunami could be integrated into a CI/CD pipeline, so scans are automatically triggered during builds or deployment.

**Relevance**

This is relevant for DevOps and DevSecOps as integrating with a CI pipeline would allow for checking the system for possible vulnerabilities before it ever reaches deployment. This means vulnerabilities that could make their way to the deployment systems are caught as early as possible, which is a core component of DevSecOps.
