# Assignment Proposal

## Title

Integrating doctests in your CI-pipeline

## Names and KTH ID

  - August Tengland (tengland@kth.se)
  - Daniel Hartler (dhartler@kth.se)

## Deadline

Week 2


## Category

Demo


## Description

We want to show how you can easily extend a Python CI-pipeline for testing (using Pytest) to automatically validate any doctests present in the project. We will: 
- Briefly discuss what doctests are and their relevance for DevOps.
- Introduce a small Python project with a CI-pipeline for Pytest.
- Demonstrate how a doctest can be easily created and run in the terminal.
- Demonstrate how Pytest can be configured to automatically find and run doctests anywhere in the project.
- Demonstrate how this change causes the CI-pipeline to also validate doctests on commits.   

**Relevance**

Doctests are a useful tool which promotes Test-Driven-Developement (TDD). Being able to test functions directly as their written makes it easier to continously intregate changes while still testing every alteration. This makes doctests a powerful extension to an existing Python testsuite and should therefore be considered when applying DevOps principles in a Python project. 

