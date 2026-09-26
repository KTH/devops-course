# Assignment Proposal

## Title

Container Security: Detecting and Fixing Misconfigurations with Checkov

## Names and KTH ID

- Filip Dimitrijevic (filipdi@kth.se)
- Jonatan Bölenius (boleni@kth.se)

## Deadline

Task 2

## Category

Executable tutorial

## Description

We propose an interactive tutorial demonstrating how to detect, understand, and fix container security misconfigurations using Checkov and Docker.

Participants will start with an insecure Dockerfile where the application runs as root, uses the `latest` image tag instead of a pinned version, and lacks a health check. They will use Checkov to identify these misconfigurations and investigate their practical consequences:

- **Root privileges:** Participants will inspect the permissions of a container running as root, then create a non-root user and verify the difference.
- **Missing health check:** Participants will simulate an application failure and observe that the container remains running without any health status being reported. They will then add a health check and verify that Docker detects the unhealthy application.
- **Unpinned base image:** Participants will examine how using `latest` affects build reproducibility and learn how pinning an image version improves predictability.

After fixing the issues, participants will rebuild the image, rescan the Dockerfile with Checkov, run the container, and verify its runtime behavior and security checks.

The tutorial will run in Killercoda without requiring local installation or a paid account.

**Relevance**

Secure (code) infrastructure configuration is an important part of DevOps. This tutorial combines automated security scanning with runtime verification to demonstrate how misconfigurations affect container security, reliability, and reproducibility. It also shows how automated policy checks help identify insecure configurations before deployment.