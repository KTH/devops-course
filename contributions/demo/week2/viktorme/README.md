# Assignment Proposal

## Title

Is 100% line coverage enough? The case for mutation testing with Rust.

## Names and KTH ID
- Viktor Meyer (viktorme@kth.se)

## Deadline
- Week 2

## Category
- Demo

## Description

Rust is a programming language that promises a rich type system and an emphasis on correctness. Along with this, it offers a built-in solution for unit testing. Most people are familiar with the concept of unit testing and 'code coverage', Mutation Testing is much less known/utilized. This demo will briefly explain the anatomy of a unit test, what makes a good test, and the concept of code-coverage. With a proper introduction to relevant background knowledge: we will move on to mutation testing, how we can utilize it, why it's attractive, and how the theory works behind the scenes. 

[Mutagen](https://github.com/llogiq/mutagen) and [cargo-mutants](https://mutants.rs/) are two relevant mutation testing tools.

**Relevance**

Automated testing is very important to ship software with quality and confidence. You could argue that a correctly tested piece of software (in combination with an automated pipeline) will always be in a 'deployable' state. For a DevOps workflow, running mutation tests in addition to unit tests can increase confidence in our software being correct - and therefore reduce uncertainty for a next deployment.
