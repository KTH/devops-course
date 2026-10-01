# Assignment Proposal

## Title

Progressive Delivery with Argo Rollouts: Canary Deployment and Rollback

## Names and KTH ID

- Ignacy Stepniewski (ignacys@kth.se)
- Moritz Constantin Schepp (mcschepp@kth.se)

## Deadline

Task 1

## Category

Executable tutorial

## Description

We propose an executable tutorial about progressive delivery using Argo Rollouts on Kubernetes.

The tutorial will be done in a browser-based Kubernetes environment using **Killercoda**. The learner will create an initial stable version of an app and then use Argo Rollouts to introduce a new version using canary deployment.

The tutorial will demonstrate how a rollout can gradually expose a new version to users, pause the deployment for verification, manually promote a successful release or (in case of failure) abort the unsuccessful rollout.

**Relevance**

Progressive delivery extends Continuous Delivery and Continuous Deployment (which relates it to Week 3 of the DevOps course) by reducing the risk associated with releasing new software versions, especially in big applications.

Instead of immediately replacing the currently running application, a canary deployment exposes the new version gradually. This limits the impact of failures and allows the new version to be evaluated before it becomes the stable verison of choice.

Argo Rollouts is a Kubernetes controller made specifically for deployment strategies such as canary and blue-green deployment.