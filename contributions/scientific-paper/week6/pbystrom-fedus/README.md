# Assignment Proposal

## Title

Propagation-Based Vulnerability Impact Assessment for Software Supply Chains: Vulnerability Propagation Analysis

## Names and KTH ID

- Robert Fedus (fedus@kth.se)
- Peter Byström (pbystrom@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

This proposal is based on "Propagation-Based Vulnerability Impact Assessment for Software Supply Chains" by Bonan Ruan, Zhiwei Lin, Jiahao Liu, Chuqi Zhang, Kaihang Ji, and Zhenkai Liang (https://arxiv.org/abs/2506.01342).

For the presentation, we will focus on Section III-D, "Vulnerability Propagation Analysis", rather than covering the entire paper. This section explains how to check whether a vulnerability in one software dependency actually affects the projects that depend on it. The analysis follows the dependency chain and checks whether a downstream project uses a vulnerable version, includes code from the dependency, and can reach the vulnerable function.

We picked this focus because dependency alerts are common in modern software development, but not every reported vulnerability necessarily affects an application in practice. The paper’s approach gives us a simple way to explain how teams can investigate alerts and prioritise which dependencies to update. We can illustrate the main idea with a small dependency graph and some checks, without going into the paper’s more complex algorithm or scoring formulas.

**Relevance**

This paper is relevant to the Week 6 topics because it addresses DevSecOps with software dependency management security concepts. Dev teams can use dependency and vulnerability analysis during CI to understang whether a reported issue reachers their own software and decide what to fix first.
