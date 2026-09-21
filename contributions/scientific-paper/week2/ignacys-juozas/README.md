# Assignment Proposal

## Title

Is this Build Failure Related to my Patch? An Empirical Study of Unrelated Build Failures in Continuous Integration

## Names and KTH ID

* Ignacy Stepniewski (ignacys@kth.se)
* Juozas Skarbalius (juozas@kth.se)

## Deadline

* Week 2

## Category

* Scientific paper

## Description

This paper was published in Empirical Software Engineering in May 2026.

Continuous Integration systems often execute many builds concurrently, which means that a build failure is not always caused by the code change that triggered the build. Such unrelated build failures can waste developers' time, as they first need to find out whether the problem was actually introduced by their own change.

The paper studies over 70 thousand CI build failures from seven open-source projects. The authors find that developers spend a median of four hours determining whether a failure is related to their code change. They then use issue reports, comments, and commits to build semi-supervised Positive and Unlabeled (PU) learning models for predicting unrelated build failures.

During our presentation, we aim to explain the problem of unrelated CI failures, describe the proposed prediction approach, discuss the main empirical results, and evaluate how such a system could improve the developer feedback loop in CI environments.

**Relevance**


This paper is highly relevant to DevOps and Week 2 because it focuses directly on Continuous Integration and automated build pipelines. Fast and reliable feedback from CI is a central DevOps practice. Unrelated build failures can slow down development by causing developers to investigate problems that were not introduced by their own changes.

Automatically identifying such failures could reduce unnecessary debugging effort, improve time-to-feedback, and help developers decide what to do.
