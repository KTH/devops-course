# Assignment Proposal

## Title

Race-Safe Continuous Deployment on Kubernetes

## Names and KTH ID

- Miami Alvelistin (miami@kth.se)
- Albin Wallenius Woxnerud (alww@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

We will demonstrate a continuous deployment pipeline that prevents older GitHub Actions runs from overwriting newer releases. Each push tests the application, publishes a commit-tagged Docker image to GitHub Container Registry, and deploys it through a self-hosted runner to a local k3d Kubernetes cluster. Stale commits are rejected before deployment.

During the demo, we will deploy a new version, attempt to deploy an older version, and delete a running pod. Kubernetes will recreate the pod while another replica continues serving traffic.

**Relevance**

CI/CD pipelines can finish out of order, causing an older release to replace a newer one. This demo combines release-order protection with Kubernetes reconciliation to show automated, reproducible deployment and recovery. We will also discuss the limitations of a local cluster and trusted self-hosted runner.
