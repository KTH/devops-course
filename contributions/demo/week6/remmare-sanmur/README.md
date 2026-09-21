# Assignment Proposal
 
## Title
Automated DevSecOps CI Pipeline for Vulnerability Detection and Remediation.
 
## Names and KTH ID
- Anna Remmare — (remmare@kth.se)
- Sangeetha Murugesan — (sanmur@kth.se)
  
## Deadline
Week 6
 
## Category
Demo
 
## Description
Our demo investigates how automated security testing and remediation can prevent vulnerable code from being merged into a shared codebase, using a small room-booking application (React frontend, Express API, a separate audit microservice, Supabase/Postgres) as the system under test. We use GitHub Actions together with CodeQL and Dependabot to detect vulnerabilities and automatically create fixes, without requiring a developer to manually triage every alert.

We introduce a controlled vulnerability and We demonstrate automatic detection and remediation for both, showing how tests, security checks, and a security gate validate a fix before a pull request is allowed to merge.

The core workflow is:

**Detect → Remediate → Validate → Security Gate → Merge/Block**

Critically, the two vulnerabilities are chosen to contrast a case where automation completes the fix end-to-end against a case where it structurally cannot. We showcase this limitation live either no automated fix is offered for that alert, or a suggested fix is generated but fails CI, correctly blocking the merge until a human completes the remaining step. This directly demonstrates incomplete automated remediation as an observed limitation, alongside the related risk of fix-induced regressions and the fact that passing security checks does not guarantee complete security. 

**Relevance**
The demo demonstrates DevSecOps by integrating security into the CI workflow. Automation provides fast feedback, reduces manual work, and ensures that vulnerable changes are blocked before reaching the main branch.



