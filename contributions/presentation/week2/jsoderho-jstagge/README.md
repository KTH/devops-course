# Assignment Proposal

## Title

Stop Rebuilding the Wheel: Accelerating Monorepos with Turborepo's Remote Cache

## Names and KTH ID

- John Söderholm (jsoderho@kth.se)
- Jonatan Stagge (jstagge@kth.se)

## Deadline

- Week 2

## Category

- Presentation

## Description

In this presentation we will explore Turborepo, a high-performance build system for JavaScript and TypeScript monorepos, focusing on how its Remote Caching feature accelerates both local development and CI workflows. By storing the outputs of tasks like builds, tests, and linting in a shared cache, Turborepo enables developers and CI pipelines to instantly reuse previous results instead of repeating identical work. For example, if only a single package is updated in a monorepo, Turborepo ensures that the CI server rebuilds only that package, as well as potential packages that are dependant on it, while reusing cached results for the rest.

**Relevance**

This is highly relevant to Continuous Integration, where the speed and reliability of feedback loops determine how effectively teams can integrate and deliver code. Long build times often discourage frequent commits and make CI feel like a bottleneck. Remote Caching directly addresses this by cutting down redundant computation, reducing pipeline costs, and providing near-instant feedback. Faster, more efficient builds not only save resources but also improve developer experience, making CI a smoother, more sustainable practice.
