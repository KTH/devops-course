# Assignment Proposal

## Title

Rule-based automated test execution through CI-pipeline

## Names and KTH ID

- Ahmad Al Khateeb (ahmadak@kth.se)
- Somaiya Abdulrahman (somaiya@kth.se)

## Deadline

- Week 2, Wednesday 2025-09-03

## Category

- Demo

## Description

The purpose with this demo is to demonstrate automated test prioritization in a CI-pipeline implemented in the pytest-based testing project.

We will build a simple pytest-based testing project with some test scripts for different purposes. After that, we will implement GitHub-builtin actions to handle the test prioritization - chooses which tests shall be executed based on what has been modified/added to the project. For instance, if a Python file is added, only run Python-quality checks. We will also take a look at tag-based rules and investigate the posibility of setting dependency-based rules.

The tools we're looking at to use are GitHub or GitLab built-in Continouse Integration tools (CI Actions).

The plan of what will be created:

1. Builing a very simple program (math functions) to simulate the System Under Test.
2. Setting up a GitHub/GitLab repository to be the Testing Project, containing all the Pytest-based test scripts.
3. Implement a pipeline that adapts GitHub/GitLab builtin functions to only execute selected amount of test case based on the type of change in the project.

**Relevance**

This idea matters to DevOps because in real life scenario, it's not realistic to execute all kinds of tests for every push/pull request (because it's time- and resources-demanding), and CI should be effective (be effective by being selective). At the same time, we need to make sure that not-verified code is not merged into production before verification. So, a decisive mechanism is needed to make sure only specific tests are executed for specific purpose.
