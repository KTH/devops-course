# Assignment Proposal

## Title

Blue-Green Deployment with Automated CI/CD for a Node.js Demo App

## Names and KTH ID

  - Miami Alvelistin (miami@kth.se)
  - Ludwig Laukka (ludw@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

Our demo shows how to turn a manually run web app into a self-updating local deployment that pushes new code automatically with no downtime.

We fork the open-source nodejs-demoapp (a small Express app) and build a GitHub Actions pipeline around it. On every push, the pipeline lints the code, runs integration tests, and builds a Docker image. When a change lands on main, a self-hosted runner on our local machine triggers a blue-green deployment. It builds a new container and health-checks it against a readiness endpoint. Traffic switches over only once the container is confirmed healthy. The old container is then removed. If the health check fails, the previous version keeps serving traffic, and the deployment aborts automatically.

During the live demo, we will push a code change to the repository and show the full chain reacting in real time: the pipeline running its checks, the new image being built, and the running application being hot-swapped for the new version without any observable downtime or manual intervention. We will also intentionally push a broken change to demonstrate that the pipeline blocks a bad deployment before it ever reaches the running container.

**Relevance**

This demo covers several core DevOps practices: continuous integration (automated linting and testing on every commit), continuous deployment (an automated, hands-off path from commit to running software), and zero-downtime release strategies (blue-green deployment). Automated quality gates act as a safety net, while health checks and gradual traffic cutover make deployments safe and reversible. It also covers a common constraint: deploying to infrastructure a cloud-hosted CI runner can't reach. A self-hosted runner bridges that gap, a pattern used for on-premises deployments.
