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

We propose an interactive tutorial demonstrating how to detect and fix container security misconfigurations using Checkov and Docker.

Participants will start with an insecure Dockerfile where the application runs as root, uses the `latest` image tag instead of a fixed version, and lacks a health check to detect application failures. They will scan the Dockerfile using Checkov, identify and fix these issues, and verify that the resulting container runs correctly and passes the security checks.

The tutorial will run in Killercoda without requiring local installation.

**Relevance**

Secure (code) infrastructure configuration is an important part of DevOps. This tutorial demonstrates how automated security scanning can identify misconfigurations and how security policies can be enforced before containers are deployed.