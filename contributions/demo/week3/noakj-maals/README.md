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
A live demonstration of how GitHub actions and AWS can be used to achieve Automated Canary Deployments.
We will start off by inviting the audience to visit an application we have deployed using ECS on AWS. 
We will then show how newly commited code on github can be automatically deployed to our ECS which will be accesible by a specified percentage of users through the use of a load balancer.
After explaining our use of the Canary deployment strategy, and how this can be achieved in AWS, we will then ask the audience to again view the application, where some will see the newest deployed version (... and some might even see a bug), while the rest will see the stable version.
Lastly we will show how to rollback a deployed verion in case of a bug being reported.

**Relevance**

Canary Deployment, or any form of Progressive deployment, is an effective Continuous Deployment technique which allows new code changes to be deployed to a subset of users, rather than the entire user base, ensuring that any bugs which were not discovered during testing are not deployed to all users.
Continuous deployment allows for a more rapid feedback loop with users, leading to unwanted features or bad design choices being reported back to developers faster who can then make adaptations in their strategy.
However, as software bugs are inevitable, and no testing framework is guaranteed to discover all bugs or erroneous behavior, canary deployment adds an extra safety net where critical bugs are not deployed to an entire user base.
AWS is a leading provider of cloud services and thus seems like a good candidate for showing a practical example of this type of deployment.
