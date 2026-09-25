# Assignment Proposal

## Title

Catching non-idempotent infrastructure code with Terraform, Ansible and CI

## Names and KTH ID

  - Georgi Tsonchev Hristov (georgith@kth.se)
  - Cesar Aceves Hernández (cesarah@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

In a CD pipeline the infrastructure code runs on every deploy, so if running it twice doesn't give the same result, each run can break something on the servers.

In the demo we use Terraform to create a couple of servers as Docker containers and Ansible to configure them. First we run the playbook twice to show that when it's written correctly the second run doesn't change anything. Then we add a task that isn't idempotent, a shell command that appends a line to a file, run it again and show how the line gets duplicated. We push that change and the GitHub Actions pipeline with ansible-lint fails, then we fix it using the proper Ansible module and the pipeline passes.

We also want to explain why we use one tool to create the infrastructure and another one to configure it. We'll talk about what ansible-lint doesn't catch too, and about immutable infrastructure as another way to avoid this problem.

**Relevance**

If infrastructure code isn't idempotent you can't really run it automatically on every deploy, and continuous delivery needs that. The demo shows how to catch this kind of bug in CI, same as we already do with tests for normal code.
