# Assignment Proposal

## Title

CD in GitLab

## Names and KTH ID

- Somaiya Abdulrahman (somaiya@kth.se)
- Ahmad Al Khateeb (ahmadak@kth.se)

## Deadline

- Task 3

## Category

- Executable Tutorial

## Description

This tutorial introduces users to the fundamentals of Continuous Integration and Continuous Delivery (CI/CD) using GitLab through a progressive scenario; starting with a simple pipeline, then extending it to more advanced real-world workflows.
1. Step 1 - Basic CI/CD
   * Introduce a minimal `.gitlab-ci.yml` file.
   * Configure jobs to build and test a simple Dockerized application.
   * Show how every commit triggers a pipeline automatically.
2. Step 2 - Branch and Environment Rules
   * Add rules for staging vs. production deployments.
   * Demonstrate conditional jobs (e.g., `only: main` for production)
3. Step 3 - Multi-Stage Delivery with Approvals
   * Introduce sequential environments: build -> test -> staging -> production.
   * Use manual approvals or protected branches for production releases.
4. Step 4 - Security & Quality Gates
   * Add jobs for litning, unit tests, and a container vulnerability scan.
   * Fail the pipeline if vulnerabilities or test errors are found.
5. Step 5 - Visualization and Reflection
   * Show pipeline flow using GitLab's pipeline graph.
   * Discuss trade-offs: speed vs. safety, automation vs. manual control.



Following our tutorial, users will:
* Understand how to set up `.gitlab-ci.yml` with multiple stages.
* Learn how to deploy to different environments securely.
* Gain hands-on practice with DevOps concepts: automation, quality gates, and safe releases.


**Relevance**

CI/CD is a key part of modern DevOps. It helps teams get quick feedback, lower the risk of failed releases, and deliver updates faster. GitLab's built-in CI/CD is popular across many industries because it makes development workflows easier to manage. In this tutorial, participants will learn how to set up and run GitLab pipelines and think about how automation affects both speed and reliability. Users will also see how CI/CD practices can be adapted to different teams and projects. 
