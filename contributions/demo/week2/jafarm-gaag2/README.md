# Assignment Proposal

## Title

Automated Regression Testing with CI Quality Gates

## Names and KTH ID

- Jafar (jafarm@kth.se)
- Gabriel (gaag2@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

Our demo investigates how automated regression testing can help prevent faulty code from being merged into a shared codebase. We will construct a small application with a test suite containing unit tests and integration tests. The demo will begin by showing the expected behavior of the application and the tests passing locally.

We will then introduce a regression into the application code and rerun the automated tests. The failing tests will show how the regression is detected without manual verification. We will also demonstrate the same failure in a continuous integration workflow, where GitHub Actions runs the test suite automatically and blocks the pull request through a failing quality gate.

After identifying the issue, we will fix the regression and rerun the CI pipeline to show the quality gate passing again.

**System architecture.** The workflow has four interacting parts: (1) the application code, (2) the test suite (unit + integration), (3) a GitHub Actions workflow triggered on every pull request, and (4) GitHub branch protection with a required status check that connects the workflow result to the merge decision. We will show how a red check propagates from a single failing test up to a blocked merge button, and back to green after the fix.

**Beyond a plain test run.** To go past "CI runs the tests", the quality gate is composed of several checks that must all pass: the test suite, a line-coverage threshold enforced as a hard failure (not just a printed report), and a mutation-testing step on the changed module. The mutation step lets us show a case where the full suite is green but a seeded fault survives, making concrete the claim that passing tests do not prove correctness. We will also show the gate as a required status check in the GitHub UI so the merge is technically blocked, not blocked by convention.

**Design decisions.** We will justify the main choices during the demo: GitHub Actions (native to the platform hosting the code, no extra runner infrastructure, marketplace actions for coverage and annotations) versus a standalone CI server; splitting unit and integration tests so fast feedback is separated from slower, higher-confidence checks; enforcing coverage as a gate rather than a report to make the signal actionable; and branch protection with a required check as the actual enforcement point rather than developer discipline.

**Timing.** The demo is scripted for the 6:30-7:30 minute limit. Slow CI runs will be pre-triggered or pre-recorded so live time is spent on the regression, the blocked merge, the fix, and the trade-off discussion.

The demo will discuss trade-offs of regression testing in CI, such as flaky tests, incomplete test coverage, test maintenance cost, and the balance between fast feedback and deeper validation.

**Relevance**

This demo is directly relevant to testing automation and continuous integration. Automated tests are a central DevOps practice because they provide fast feedback, reduce manual testing effort, and make it safer for teams to integrate changes frequently.

By connecting regression tests to a CI quality gate, the demo shows how teams can automatically detect faulty changes before they reach the main branch. It also highlights that automated testing is useful but not perfect, since passing tests do not guarantee the absence of bugs and coverage alone does not prove correctness.
