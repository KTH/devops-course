# Assignment Proposal

## Title
DevSecOps with Checkov for Infrastructure Security Scanning

## Names and KTH ID
  - Alexandru Matcov (matcov@kth.se)
  - Phoebe Schwartz (phoebes@kth.se)

## Deadline
Task 3

## Category
Executable tutorial

## Description
This executable tutorial demonstrates how to implement Infrastructure as Code (IaC) security scanning using Checkov, creating a DevSecOps workflow that prevents misconfigured infrastructure from reaching production.

The tutorial will guide users through scanning and securing Terraform infrastructure code using Checkov, an open-source static analysis tool that identifies security misconfigurations and compliance violations.

The tutorial will include:
* Setting up Terraform code with intentional security misconfigurations (i.e. public S3 buckets, overpermissive security groups, unencrypted resources)
* Installing and configuring Checkov for IaC security scanning
* Interpreting security scan results and understanding vulnerability classifications
* Implementing step-by-step remediation of critical security findings
* Demonstrating the complete scan-fail-fix-pass cycle

Users will start with vulnerable AWS Terraform configurations, use Checkov to identify security issues, fix the vulnerabilities following security best practices, and finally show how to integrate automated security in CI/CD pipeline.

The tutorial will be delivered through KillerCoda platform in 4 steps: introduction to IaC security, Checkov scanning basics, vulnerability remediation, and CI/CD integration.

**Relevance**

This tutorial addresses a critical aspect of modern DevOps: infrastructure security integration throughout the development lifecycle. With 95% of cloud security breaches being preventable through proper configuration management, implementing IaC security scanning has become essential for DevOps teams. The approach demonstrates core DevOps principles of automation, continuous integration, and shift-left practices by catching security issues early in the infrastructure provisioning process rather than after deployment.
