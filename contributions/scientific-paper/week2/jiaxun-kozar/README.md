# Assignment Proposal

## Title

FlakyGuard: Automatically Fixing Flaky Tests at Industry Scale (ASE 2025)

## Names and KTH ID

  - Jiaxun Wei (jiaxun@kth.se)
  - Matyas Kozar (kozar@kth.se)

## Deadline

- Week 2

## Category

- Scientific paper

## Description

We want to present the ASE 2025 paper ["FlakyGuard: Automatically Fixing Flaky Tests at Industry Scale"](https://doi.org/10.1109/ASE63991.2025.00179) by Li, Behrang, Shi, and Liu. The authors propose a tool called FlakyGuard that automatically repairs flaky tests, and they evaluate it in production at Uber. We plan to focus on how FlakyGuard traverses a call graph to collect just enough context to resolve flakiness, discuss the reported success rate together with how many fixes actually land in production, and contrast the approach with previous work in this field.

**Relevance**

Flaky tests break the assumption that a failing build means the code is broken. When working with flaky tests, developers prefer to rerun jobs rather than investigate the failure, and over time the test suite loses its value. Therefore, fixing them automatically is directly relevant to the subject of test automation and CI.
