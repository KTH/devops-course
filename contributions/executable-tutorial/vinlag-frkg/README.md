# Assignment Proposal

## Title

Vulnerability scanning in Pythons using Pip-Audit

## Names and KTH ID

  - Vincent Lagerros (vinlag@kth.se)
  - Francis Gniady (frkg@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

We will create an executable tutorian on how one can do vulnerability scanning in their python environment using pip-audit.
Futhermore we will demonstrate this by setting up a project, initially without vulnerabilities. Then we will then add a vulnerable dependency, show how pip-audit can warn us about that, and how we can automatically fix broken versions using pip-audit.

Moreover, we intend to also show an example on how this can be integrated into a CI/CD pipeline step. The plan is to use killercoda.com to 
showcase this executable tutorial.

**Relevance**

pip-audit is a tool that scans your packages for known vulnerabilities and can also propose version changes to upgrade vulnerable packages to newer versions. Security scanning is very relevant to devops, as we have seen in recent weeks, with the multiple attacks and subsequent vulnerabilities on npm. This acts as an early vulnerability detection in the DevSecOps cycle.
