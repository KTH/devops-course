# Assignment Proposal

## Title

Breaking and Fixing a React App with CI Guards

## Names and KTH ID

  - Reza Hosseini (rezahos@kth.se)
  - TBD (TBD@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

This demo shows a basic CI workflow for a simple React application. The demonstration goes as following: we first show the app running correctly, then intentionally break the code to trigger CI test failures, and finally fix the code to pass tests and merge the PR. The workflow uses GitHub Actions to run tests automatically on pull requests. The demo also includes:

- Automated PR comments when tests fail or pass.
- Direct commit prohibition to main branch
- Branch protection to prevent merging broken code.
- Live editing of code and workflow during the demo.


The demo shows how CI (using GitHub Actions) protects code quality and prevents broken code from reaching the main branch.

**Relevance**

This demo is relevant to DevOps because it illustrates the practical value of CI pipelines in a development workflow. It shows how automated testing and branch protection can prevent errors, reduce downtime, and maintain code quality, which are key principles in DevOps practices.
