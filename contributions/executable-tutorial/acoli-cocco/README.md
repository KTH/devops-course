# Assignment Proposal

## Title

_Zero-Trust Data Pipelines: A Practical DevOps Security Tutorial_

## Names and KTH ID

  - Coli Alessandro (acoli@kth.se)
  - Cocco Riccardo (cocco@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

The tutorial can be found at https://colab.research.google.com/drive/1Qak_zpwuk8imhXdM1hchimNOjuk5eGtC?usp=sharing 

This interactive tutorial will provide students with some training and explanation on securing pipelines against threats. It will guide people in transforming a vulnerable deployment workflow into a secure, automated pipeline by implementing security controls that run automatically during build and deployment processes.

Specifically, it will have students add good practices inside their code:

- **Pre-commit security states**: automated integrity verification, blocking deployments when data integrity checks fail.
- **Build time srotection**: cryptographic hashing and secret scanning to prevent credential exposure in pipeline artifacts.
- **Deployment controls**: automated security validation and rollback mechanism, enforcing security standards before deployment
- **Pipeline incident response**: continuous security validation throughout lifecycle.

The **intended learning outcomes** of our tutorial are:

- Implement automated security gates in CI/CD workflows
- Configure integrity verification in pipelines
- Build deployment security controls that maintain DevOps velocity
- Automate security incident response within pipeline operations

All exercises run directly in Colab using GitHub Actions examples and pipeline configuration patterns that participants can immediately apply to their workflows.

**Relevance**

One of the most expensive and common reasons for DevOps pipeline failures is data integrity issues. The ability to have automated security controls in place becomes crucial as DevOps teams handle sensitive data across distributed systems more frequently. This tutorial bridges the gap between security theory and real-world application, giving DevOps students useful skills.
