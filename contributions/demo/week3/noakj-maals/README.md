# Assignment Proposal

## Title

An Interactive Demonstration of Automated Canary Deployment using AWS and GitHub Actions

## Names and KTH ID

  - Noak Jönsson (noakj@kth.se)
  - Marcus Alström (maals@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description
A live demonstration of how GitHub actions and AWS can be used to acheive Automated Canary Deployments.
Using an AWS load balancer a percentage of users can be given access to the latest deployed features, allowing developers to gather feedback as well as monitor for bugs, while not exposing the entire userbase to these changes, essentially allowing small scale testing in a production environment.
In case of drastic errors this deployment technique allows for easy rollbacks while still maintaining high availability of deployed (stable) applications.
This technique is definitely in the grayzone between CI and CD, however this demonstration will mostly focus on the infrastructure needed to automatically deploy/deliver code to a subset of an applications userbase.


**Relevance**

Canary Deployment, or any form of Progressive depolyment, is an effective Continuous Deployment technique which allows new code changes to be deployed to a subset of users, rather than the entire userbase, ensuring that any bugs which were not discoverd during testing are not deployed to all users.
Contnuous deployment allows for a more rapid feedback loop with users, leading to unwanted features or bad design choices being reported back to developers faster who can then make adaptations in their strategy.
However, as software bugs are innevitable, and no testing framework is guaranteed to discover all bugs or erroneous behavior, canary deployment adds an extra safety net where critical bugs are not deployed to an entire userbase.
AWS is a leading provider of cloud services and thus seems like a good candidate for showing a practical example of this type of deployment.
