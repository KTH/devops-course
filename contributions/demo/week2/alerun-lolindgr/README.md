
# Assignment Proposal

## Title

Improving Test Quality with Mutation Testing in a CI Workflow

## Names and KTH ID

  - Alexander Runebou (alerun@kth.se)
  - Love Lindgren (lolindgr@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

Our demo investigates why conventional code coverage is not always sufficient for evaluating the quality of a test suite. We will construct a small application with tests that achieve high or complete statement coverage while still failing to detect meaningful faults.

We will introduce mutation testing in a CI workflow, where small artificial faults are introduced into the program and the existing test suite is evaluated based on whether it detects them. Surviving mutations will expose weaknesses that are not visible from code coverage alone.

We will then improve the test suite using techniques such as boundary-value testing and property-based testing, and rerun the mutation tests to demonstrate how the test suite can improve without necessarily increasing code coverage.

The CI pipeline will use the results as automated validation mechanisms and enforce a quality gate based on the code coverage, test results, and mutation score. During the live demo, we will change the tests and CI workflow to showcase how these changes affect the validation results.

The demo will also discuss some trade-offs of mutation testing, such as computational cost, when mutation testing is appropriate in a CI pipeline, and how it can be balanced against execution time.

**Relevance**

This demo is directly relevant to the topics of software testing, verification, and continuous integration. Automated tests are a central validation mechanism in CI pipelines, but commonly used metrics such as code coverage only indicate whether the code has been executed, but not necessarily whether the tests can detect incorrect behaviour.

Mutation testing provides a way to evaluate the effectiveness of a test suite by checking whether deliberately introduced changes are detected by the tests. Combining mutation testing wih boundary-value and property-based testing demonstrates how different testing techniques can complement one another.
