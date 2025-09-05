# Assignment Proposal

## Title

Breaking and Fixing a React App with CI Guards

## Names and KTH ID

- Reza Hosseini (rezahos@kth.se)  
- Adam Johannes Fridén Rasmussen (ajfr2@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

This demo shows a basic CI workflow for a simple React application. The demonstration goes as follows: we first show the app running correctly, then intentionally break the code to trigger CI test failures, fix the code to pass tests, ask for code review and approval, and merge the PR after approval is received. The workflow uses GitHub Actions to run tests automatically on pull requests, it uses Cubic AI to do PR summarization as well as finding issues. The demo also includes:

- Automated PR comments when tests fail or pass.  
- Direct commit prohibition to main branch.  
- Branch protection to prevent merging broken code.  
- Live editing of code and workflow during the demo.  
- Automatic AI-generated PR summaries (Cubic AI) on every new/updated PR.  
- PR review and approval process where the PR author requests a review, the reviewer checks the AI summary and code, and approves the PR before merging.  

The demo shows how CI (using GitHub Actions) protects code quality and prevents broken code from reaching the main branch, while also demonstrating collaborative practices with AI assistance and mandatory reviews.

**Relevance**

This demo is relevant to DevOps because it illustrates the practical value of CI pipelines in a development workflow. It shows how automated testing, branch protection, AI-powered code summarization, and enforced reviews can prevent errors, reduce downtime, and maintain code quality—key principles in DevOps practices.  
