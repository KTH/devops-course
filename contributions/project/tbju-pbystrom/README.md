# Assignment Proposal

## Title

Building a DevOps Pipeline Around an Existing Web Application

## Names and KTH ID

  - Tobias Bjurström (tbju@kth.se)
  - Peter Byström  (pbystrom@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We take an existing web application built on Firebase and implement a complete DevOps Pipeline around it. The application will communicate with a database that contains user account information. The pipeline will then be tested against previous PRs.

 The CI/CD pipeline is built with Github Actions. The pipeline will consist of tests that define functionality and deploying a finished functional service. A/B testing with Firebase remote config will also be implemented.

IaC will be implemented with the firebase.json file that defines the relation between the web application and database. The project will be hosted on GitHub.

A DevSecOps tool will be used to scan for security flaws in the codebase, such as injection attacks, and check for dependency vulnerabilities with Dependabot.

**Relevance**

The project shows how to adopt the CI/CD pipeline in an existing project with added IaC, vulnerability scans, and dependency checks. This will result in the showcase of how DevOps principles help catch faulty code and vulnerabilities by using an agile workflow.
