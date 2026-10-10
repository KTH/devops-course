# Assignment Proposal

## Title

IaC with Ansible: Deploy, Test, and Repair a Basic Web Service

## Names and KTH ID

- Juozas Skarbalius (juozas@kth.se)
- Lorenzo Deflorian (ldef@kth.se)

## Deadline

- Task 1

## Category

- Executable tutorial

## Description

**Tutorial Submission:** The code and walkthrough is available at Google Colab [here](https://colab.research.google.com/drive/1b41FeQAy5chEU1k0rYReCbmy3Oc9we4j?usp=sharing)

**Proposal:** [#3051](https://github.com/KTH/devops-course/pull/3051)

This executable tutorial introduces Infrastructure as Code using Ansible in Google Colab. Learners deploy a small web-service stack with Flask, Gunicorn, and Nginx while working with inventories, variables, templates, desired state, and automated deployment verification.

The tutorial demonstrates idempotency, configuration drift, drift repair, and controlled updates. Learners intentionally modify the deployed configuration, detect the difference, restore the desired state with Ansible, and verify the repaired service automatically.

**Relevance**

The tutorial is relevant to DevOps and IaC because it demonstrates how infrastructure configuration can be automated, reproducible, testable, and recoverable. It connects configuration management with deployment, verification, and change management in a practical workflow.

