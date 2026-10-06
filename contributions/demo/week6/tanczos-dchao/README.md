# Assignment Proposal

## Title

Automated DevSecOps CI Pipeline with Trivy

## Names and KTH ID
De Chi Hao (dchao@kth.se) 
Barnabas Tanczos (tanczos@kth.se)

## Deadline

Week 6

## Category

Demo

## Description

We will demonstrate a DevSecOps CI pipeline using Trivy on a basic [sample Spring Boot project](https://github.com/davidarchanjo/spring-boot-crud-rest). We will first introduce a known vulnerable dependency and an exposed secret token into the project. We will then show a GitHub Actions workflow that automatically builds the project and runs Trivy to scan for dependency vulnerabilities, leaked secrets, and other security issues.

The demo will show the pipeline failing when security issues are detected, followed by fixing the identified problems and rerunning the pipeline successfully. Finally, we will use Trivy to generate a Software Bill of Materials (SBOM) for the project.

We will explain the system architecture, detailing how GitHub Actions executes the scanner and how Trivy interacts with vulnerability databases to perform static analysis. We will also discuss the design decisions and limitations: while Trivy is lightweight and fast, adding comprehensive security scans increases pipeline execution time. Furthermore, static scanners only detect known CVEs and static secrets, meaning they cannot identify new vulnerabilities or logic flaws. 

**Relevance**

The demo demonstrates how security checks can be integrated directly into a DevOps CI pipeline, allowing security issues to be detected automatically during software development rather than manually after deployment. It covers several DevSecOps practices, including automated security scanning, secret detection, dependency vulnerability management, and SBOM generation.