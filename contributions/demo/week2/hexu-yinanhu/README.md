# Assignment Proposal

## Title

CircleCI Pipeline Improved with Cache and Parallel Workflow

## Names and KTH ID

  - Hexu Li (hexu@kth.se)
  - Yinan Hu (yinanhu@kth.se)

## Deadline

Week 2



## Category

Demo



## Description

We intend to demonstrate how to utilize CircleCI pipeline to automate the build and test process of a java application, and we will leverage the advanced features, such as cache and parallel workflow, to speed up the CI process. We will also showcase the difference between backend and frontend CI.

The CI pipeline is designed with the following functions/features:

- Build java project with backend and frontend via Apache Maven & Docker
- Run unit tests in parallel jobs, and run integration test
- Use Cache to reduce CI duration
- Send notice to Slack channel when all tests passed, so that other team members can get updated about it.

**Relevance**

CircleCI is a Continous Integration Platform which can work with Version Control System like Github. In this case, we integrate the CircleCI pipeline with Docker, Maven, Slack, which are common DevOps tools & platforms. And we explore how to utilize Cache and Parallel Workflow features to improve CI pipeline. 

