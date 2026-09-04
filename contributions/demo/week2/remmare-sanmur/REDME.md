# Assignment Proposal
 
## Title
Secure CI Pipeline for Automated Vulnerability Detection and Remediation
 
## Names and KTH ID
- Anna Remmare — (remmare@kth.se)
- Sangeetha Murugesan — (sanmur@kth.se)
## Deadline
Week 2
 
## Category
Demo
 
## Description
Our demo investigates how automated security testing and remediation can prevent vulnerable code from being merged into a shared codebase. We will use GitHub Actions together with CodeQL and Dependabot to detect vulnerabilities and automatically create fixes.

We will introduce a controlled vulnerability, demonstrate its automatic detection and remediation, and show how tests, security checks, and a security gate validate the fix before allowing the pull request to merge.

The core workflow is:

**Detect → Remediate → Validate → Security Gate → Merge/Block**

We will also discuss limitations such as incomplete automated remediation, regressions caused by fixes, and the fact that passing security checks does not guarantee complete security.

## Relevance

The demo demonstrates DevSecOps by integrating security into the CI workflow. Automation provides fast feedback, reduces manual work, and ensures that vulnerable changes are blocked before reaching the main branch.



