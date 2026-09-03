# Assignment Proposal

## Title

Automated Regression Testing with CI Quality Gates

## Names and KTH ID

- jafarm (jafarm@kth.se)
- gaag2 (gaag2@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

Our demo investigates how automated regression testing can help prevent faulty code from being merged into a shared codebase. We will construct a small application with a test suite containing unit tests and integration tests. The demo will begin by showing the expected behavior of the application and the tests passing locally.

We will then introduce a regression into the application code and rerun the automated tests. The failing tests will show how the regression is detected without manual verification. We will also demonstrate the same failure in a continuous integration workflow, where GitHub Actions runs the test suite automatically and blocks the pull request through a failing quality gate.

After identifying the issue, we will fix the regression and rerun the CI pipeline to show the quality gate passing again. The demo will also include a coverage report and explain how coverage can support automated testing while still having limitations.

The demo will discuss trade-offs of regression testing in CI, such as flaky tests, incomplete test coverage, test maintenance cost, and the balance between fast feedback and deeper validation.

**Relevance**

This demo is directly relevant to testing automation and continuous integration. Automated tests are a central DevOps practice because they provide fast feedback, reduce manual testing effort, and make it safer for teams to integrate changes frequently.

By connecting regression tests to a CI quality gate, the demo shows how teams can automatically detect faulty changes before they reach the main branch. It also highlights that automated testing is useful but not perfect, since passing tests do not guarantee the absence of bugs and coverage alone does not prove correctness.
