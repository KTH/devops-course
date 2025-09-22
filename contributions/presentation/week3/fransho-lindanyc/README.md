# Assignment Proposal

## Title

Implementing fan-in/fan-out pipelines in GoCD for continous deployment

## Names and KTH ID

- Elin Fransholm (fransho@kth.se)
- Linda Nycander (lindanyc@kth.se)

## Deadline

- Week 3

## Category

- Presentation

## Description

[GoCD](https://www.gocd.org/) is a free and open-source CI/CD server. This presentation will focus on its continuous deployment capabilities, specifically using fan-in/fan-out pipelines to manage large, complex workflows. In large, complex systems, multiple stages can run simultaneously to reduce build and test time, while other stages have dependencies and only occur when all dependencies succeed.

In addition to this, the presentation will also cover automatic material detection, where GoCD can automatically detect which pipelines need to run based on which files have changed. These pipelines allow code to be automatically deployed to stage/production as soon as all dependencies pass.

**Relevance**

Fan-in/fan-out pipelines are essential in modern DevOps since it allows scaling of continuous deployment across multiple services. They reduce pipeline runtime, they are reliable (because of dependencies) and scalable. Fan-in/fan-out in GoCD helps with automation, dependency management and parallel execution to achieve faster and safer continuous deployment.
