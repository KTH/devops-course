# Assignment Proposal

## Title

Blocking push by linting result and automated testing on GitHub demo

## Names and KTH ID

- Elin Fransholm (fransho@kth.se)
- Linda Nycander (lindanyc@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

This demonstration will demonstrate:

1. How linting is run with a Git pre-push hook using Husky with every push. If the linting fails the push is stopped and gives a custom error message.
2. Also, it shows how tests are automatically run at GitHub, if linting and push was successful. The result of the tests is displayed on GitHub, and a PR cannot be merged with main unless the tests pass.

This will be demonstrated on a basic react-website for checking which week it is. We will perform a failing push and also a failing test.

**Relevance**

This demo is relevant to DevOps since GitHub actions automates testing, ensuring continuous integration. The ESLint pre-push hook ensures continuous quality enforcement. This results in automation of repetitive tasks, quality checks and fast feedback. By combining these two helpful methods, you can get a verification of the quality of the code and avoid bugs early in the workflow.
