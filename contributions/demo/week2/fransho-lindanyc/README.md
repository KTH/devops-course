# Assignment Proposal

## Title

Blocking push by linting result and blocking commit by testing and todo-comment-checking results.

## Names and KTH ID

- Elin Fransholm (fransho@kth.se)
- Linda Nycander (lindanyc@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

This demonstration will demonstrate:

1. How linting is run automatically with a Git pre-push hook using Lefthook. If the linting fails the push is blocked and it gives a custom error message.
2. Also, it shows how tests and todo-comment-checks are automatically run with a Git pre-commit hook using Lefthook. If the tests or todo-comment-check fails the commit is blocked and it gives a custom error message. The pre-commit hook also ensures that the commit message follows a certain format.

This will be demonstrated on a basic react-website for checking which week it is. We will perform a failing commit and also a failing push.

**Relevance**

This demo is relevant to DevOps because it demonstrates how automated checks ensure code quality before merging into the main branch. By providing immediate feedback on commits and pushes, developers can identify and fix issues quickly, resulting in smoother and faster development. The ESLint pre-push hook ensures continuous code quality enforcement. This results in automation of repetitive tasks, quality checks and fast feedback. The testing pre-commit hook verifies that the code works correctly, helping to prevent bugs in the codebase. The todo-comment-checking pre-commit hook ensures that no unfinished tasks or reminders are left in the code, which could cause confusion later. The commit-message-checking pre-commit hook ensures consistency in commit messages, making it easier to follow the commit history and track issues and fixes. By combining these tools within a continuous integration workflow, developers can get code quality verifications and avoid bugs early in the workflow.
