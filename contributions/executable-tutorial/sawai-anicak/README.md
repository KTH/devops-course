# Assignment Proposal
## Title
Automated Security Scanning in CI/CD Pipelines: Building a DevSecOps Tutorial

## Names and KTH ID
  - Anica Krüger (anicak@kth.se)
  - Shreyas Sawai (sawai@kth.se)
  
## Deadline
  - Task 2
  
## Category
  - Executable tutorial
  
## Description
This executable tutorial demonstrates how to implement automated security vulnerability scanning in CI/CD pipelines, creating a complete DevSecOps workflow that prevents vulnerable code from reaching production environments.
The tutorial will guide users through building a CI/CD pipeline that automatically scans code for security vulnerabilities using industry-standard open-source tools: Semgrep (Static Application Security Testing), OWASP Dependency Check (dependency vulnerability scanning), and Grype (container image scanning). Users will learn to configure security gates that fail builds when critical vulnerabilities are detected, implement vulnerability thresholds, and create automated security reporting.
The hands-on tutorial will include:
- Setting up a sample application with intentional security vulnerabilities
- Configuring GitHub Actions workflow with integrated security scanning
- Implementing multiple security scanning tools (Semgrep for SAST, OWASP Dependency Check for dependency scanning, and Grype for container scanning)
- Configuring failure thresholds and security policies
- Demonstrating the complete scan-fail-fix-pass cycle
- Creating security reports and vulnerability management workflows

The tutorial will be delivered through KillerKoda platform.
You can find our tutorial under this link: [https://killercoda.com/devsecops-tutorial/scenario/killerkoda-tutorial](https://killercoda.com/devsecops-tutorial/scenario/killerkoda-tutorial) <br>

We have also implemented this in GitHub, and have a 7 Step Actions configured using GitHub Actions, which you can find here: https://github.com/anica279p/devsecops-pipeline-tutorial/actions/runs/17978006810

**Relevance**
This tutorial addresses a critical need in modern DevOps practices where security integration (DevSecOps) has become essential for organisational resilience. 

The security approach demonstrated in this tutorial is fundamental to DevOps methodology, where security checks are integrated early in the development lifecycle rather than being an afterthought. This aligns with core DevOps principles of automation, continuous integration, and early feedback loops.

Modern software supply chain attacks and the increasing complexity of dependencies make automated security scanning not just a best practice, but a necessity for any production system.
