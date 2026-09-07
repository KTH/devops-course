# Assignment Proposal

## Title

Automatic network failure resilience testing

## Names and KTH ID

  - Alexander Forslund (alforslu@kth.se)
  - Jonatan Bölenius (boleni@kth.se)

## Deadline

- Week 2

## Category

- Demo

## Description

We will implement and demo network failure testing within a CI pipeline.

First we will create a basic app for blogging, which will be connected to an external database (PostgreSQL). The CI pipeline (automated tests using Github actions set to run tests on PUSH/PR) has two targets: One without resilience testing, and one with. The first target/job would pass PRs under normal conditions, since there is nothing inherently wrong with the code (and no latency etc., causing issues). Then, in the second target, we deliberately introduce latency and timeouts of variyng degree using Toxiproxy (https://github.com/shopify/toxiproxy). The point is to see that our integration tests catch lacking network error handling, and therefore denies the PR (marks it as having failed tests). After that we add some resilience to the application, i.e. timeout and retry handling and show that the tests then pass. 

**Relevance**

When working with real world networking applications, problems will inevitabily occur with connection or external services. It is then crucial to test for these scenarios, and that the software can handle the issues that occur without breaking the rest of the program to ensure that it is resilient. This is relevant to DevOps since we test the resilience during CI, instead of discovering the issues after deploying to a real world scenario. 


