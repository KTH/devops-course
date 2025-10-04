# Assignment Proposal  

## Title  

Gitleaks: Detecting secrets in Git repositories

## Names and KTH ID  

- Guillaume Roboam (roboam@kth.se)  
- Jonatan Stagge (jstagge@kth.se)

## Deadline  

- Task 3  

## Category  

- Executable tutorial  

## Description  

We aim to illustrate how to use **Gitleaks** to automatically detect and prevent secrets (API keys, passwords, tokens, certificates) from being committed to Git repositories. The tutorial will cover:  

- Installing and configuring Gitleaks locally and in CI pipelines  
- Running scans on existing repositories and interpreting the results  
- Writing and customizing Gitleaks configuration files (regex patterns, allowlists)  
- Demonstrating integration into Git hooks to block commits containing secrets  

The tutorial will use practical examples with repositories containing simulated secrets, showing how Gitleaks can detect them and how developers can remediate the issues.  

**Relevance**  

Secret sprawl is one of the most common security risks in DevSecOps. Tools like Gitleaks helps to prevent credentials from ever reaching version control. This knowledge is highly relevant for DevOps engineers, since mismanaged secrets can lead to major security breaches and compliance issues, even on private repositories.