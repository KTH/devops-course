# Assignment Proposal

## Title

Arcmutate: Improving code with mutation testing for Java

## Names and KTH ID

Tobias Mattsson (tmatts@kth.se)
Georgios Akkogiounoglou (gakk@kth.se)

## Deadline

Week 2

## Category

Presentation

## Description

Traditional code coverage, such as line coverage, is often not enough. This is because it is only capable of checking which code is executed, but it is not able to detect faults. For this reason, things like mutation testing have become relevant. Mutation testing is a software testing technique that involves small changes to a program's source code to evaluate the effectiveness of the testing state in detecting those changes. One modern tool which is focused on providing mutation testing for code bases is *Arcmutate*, which builds and improves upon the open-source project Pitest. Arcmutate introduces a series of mutations or small changes to the original code, and then runs the test state against the mutated code. If the test state detects the mutation, then it is considered "killed" and the test suite is considered effective. If the mutation goes undetected, then it is considered "lived" and the test state is considered not enough. Arcmutate offers integration for a number of things, such as Azure DevOps, Bitbucket, GitHub and GitLabs. 

**Relevance**

Since Java is an undeniably popular language in the industry, it goes without saying that a tool meant for Java mutation testing would be relevant. Arcmutate works for both Gradle and Maven, which are two of the most popular build tools for Java. All in all, the tool offers fast and effective mutation testing for code bases of any size, making it a good tool for Java projects.

