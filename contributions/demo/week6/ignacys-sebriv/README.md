# Assignment Proposal

## Title

Automated Supply Chain Security and Vulnerability Quality Gate with Syft and Grype

## Names and KTH ID

- Ignacy Stępniewski (ignacys@kth.se)
- Sébastien Rivière (sebriv@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

Container images often bundle operating system packages and language dependencies containing known security vulnerabilities (CVEs), exposing the software supply chain to critical risks. This demo presents an automated DevSecOps quality gate using **Syft** (for Software Bill of Materials generation) and **Grype** (for vulnerability scanning) integrated into GitHub Actions. We demonstrate how to automatically detect critical CVEs on Pull Requests, fail the build to prevent vulnerable code from merging, and perform a live fix by updating container base images. Finally, we reflect on practical challenges in DevSecOps such as managing false positives and unpatched upstream vulnerabilities.

**Relevance**

This demo directly aligns with Week 6 topics (Dependency Management, DevSecOps & Supply Chain Integrity). It illustrates how to shift security left by automatically generating an SBOM and enforcing automated vulnerability quality gates on every Pull Request before code reaches production.
