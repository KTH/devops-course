# Assignment Proposal

## Title

Efficient Continuous Delivery: Resource Usage and Optimization in GitHub Actions Workflows

## Names and KTH ID

  - Einar Harri (eharri@kth.se)
  - Elena Pan (elenapan@kth.se)

## Deadline

Week 3

## Category

Scientific paper

## Description

We propose to present the paper “Resource Usage and Optimization Opportunities in Workflows of GitHub Actions” by Islem Bouzenia and Michael Pradel, published in the research track of the 46th IEEE/ACM International Conference on Software Engineering (ICSE 2024).

Paper: https://conf.researchr.org/details/icse-2024/icse-2024-research-track/15/Resource-Usage-and-Optimization-Opportunities-in-Workflows-of-GitHub-Actions

The paper presents an empirical study of resource usage in GitHub Actions workflows. It analyzes a large dataset of workflow executions to determine which activities consume the most computational resources and to identify opportunities for improving workflow efficiency. The paper finds that building and testing account for most of the observed resource usage and that optimizations such as caching remain underused.

Our presentation will explain the study’s motivation, dataset, methodology, principal findings, and implications for continuous delivery. As the key technical component, we will examine how the authors collect and classify GitHub Actions executions, estimate resource consumption and costs, and identify optimization opportunities.

We will critically discuss the generalizability of the dataset, the assumptions used when estimating costs, and the distinction between optimizing computational resource usage and improving software delivery performance. In particular, the paper does not directly measure deployment frequency, lead time for changes, change failure rate, or recovery time. We will therefore discuss to what extent its conclusions can be applied to continuous delivery systems.

We will also compare the paper with at least two related scientific papers that are not included in its bibliography.

**Relevance**

Continuous delivery depends on automated pipelines that can build, test, and prepare software for deployment quickly and reliably. Inefficient CI/CD workflows increase feedback time, infrastructure costs, and the time required to deliver changes. Optimization techniques such as dependency caching, avoiding redundant executions, and selectively running workflow jobs can consequently improve the practical ability of a team to deliver software frequently.

The paper is relevant to DevOps because it studies the interaction between development workflows, automation, computational infrastructure, and delivery performance. It also illustrates an important DevOps trade-off: reducing pipeline cost and execution time without removing quality or security checks that are necessary for dependable delivery.
