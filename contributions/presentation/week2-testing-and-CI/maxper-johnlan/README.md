# Assignment Proposal

## Title

Code coverage: how to improve performance

## Names and KTH ID

- Max Persson (maxper@kth.se)
- John Landeholt (johnlan@kth.se)

## Deadline

Task 1

## Category

Presentation

## Description

One of the most crucial aspects of the software development process is software verification. The most commonly used way of performing software verification is through the process of testing. Often a large part of the tests in a test suite are written at the start of a project and only partially extended as the code base grows. The effect of this is that the degree of code that is covered by the tests, the coverage, is reduced. A low degree of coverage could result in false negatives in the software verification process where code is thought to be safe when in reality it is not. 

The usage of coverage tools can add significant overhead in the form of increased execution time for tests in projects. Therefore we propose a presentation on the topic of speeding up the execution of the most popular coverage analysis tool in python using parallelization and the pytest-testmon plugin.
