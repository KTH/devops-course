# Assignment Proposal

## Title

Container Vulnerability Scanning and Remediation with Trivy and GitHub Actions

## Names and KTH ID

- Hanzhi Zhang (hanzhizh@kth.se)  
- Bingjie Zhao (bingjiez@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

Ensuring container security is a critical part of DevSecOps practices. In this tutorial, we want to use [Trivy](https://aquasecurity.github.io/trivy) and GitHub Actions to demonstrate the following scenario:

1. **Build a vulnerable Docker container** with outdated dependencies (e.g., `lodash@4.17.15`), scan it with Trivy, and observe vulnerabilities being reported.
   
2. **Remediate the vulnerabilities** by updating dependencies (e.g., upgrading `lodash` and `cross-spawn`) and rebuilding the container. Then, scan again with Trivy to confirm that vulnerabilities are fixed or reduced.

3. **Handle unfixable vulnerabilities** (e.g., `zlib1g` with `CVE-2023-45853`) by using Trivy flags such as `--ignore-unfixed` or `.trivyignore`. This highlights the reality that not all vulnerabilities have patches and shows how to configure scanning policies.

4. **Integrate vulnerability scanning into CI/CD** using GitHub Actions. We configure a workflow that automatically builds images and runs Trivy scans, failing the pipeline if `HIGH` or `CRITICAL` vulnerabilities are found.

With this tutorial, we want to highlight the **before (vulnerable)** vs **after (remediated)** condition, and demonstrate how vulnerability scanning becomes part of an automated DevSecOps workflow. We plan to deliver our tutorial on [KillerCoda](https://killercoda.com).

Trivy is chosen in the tutorial as an open-source, lightweight, and widely used vulnerability scanner for containers, file systems, and Infrastructure-as-Code (IaC).

**Relevance**

Vulnerability management is central to DevSecOps because it ensures that insecure dependencies are detected early, developers can remediate issues quickly, and CI/CD pipelines enforce security gates. This aligns security scanning with continuous delivery workflows and raises awareness about both remediable and unfixable vulnerabilities in containerized applications.
