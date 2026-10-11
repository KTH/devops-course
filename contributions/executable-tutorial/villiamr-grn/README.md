# Assignment Proposal

## Title

Chaos Engineering: Testing How Your Service Behaves When a Dependency Fails

## Names and KTH ID

  - Villiam Riegler (villiamr@kth.se)
  - Gabriel Räätäri Nyström (grn@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

We will create an executable tutorial on chaos engineering with [Chaos Mesh](https://chaos-mesh.org/), running on
Killercoda's Kubernetes playground.

The setup deploys a `frontend` that serves a list fetched from a `backend`, and `vegeta` sends constant traffic so
that failed requests and latency are visible during each experiment.

1. Apply a `PodChaos` pod-kill experiment on the backend. Requests fail until the new pod is up. Fix the backend
   Deployment (replicas, readiness probe) and run the experiment again.
2. Apply a `NetworkChaos` partition between frontend and backend. The frontend's HTTP call has no timeout, so
   requests hang and the frontend stops responding entirely. Fix the frontend and run the experiment again.
3. Turn the experiment into a test: a Chaos Mesh `Workflow` that runs the partition while a `StatusCheck` polls the
   frontend and fails the workflow if it stops responding, and set it up to run automatically after deployment.

The tutorial ends with examples of where this test fits in a delivery pipeline: as a gate in a blue-green
deployment, where the new version has to pass it before receiving traffic, or against a staging environment after
each deployment.

**Relevance**

Pods die and networks fail in every system; the question is whether the system survives it. That is hard to test:
unit and integration tests mock dependencies as healthy, so the failure path is usually first exercised in
production. Chaos engineering injects these failures deliberately and checks that the system
still behaves. Set up as part of the delivery pipeline, it catches a change that removes a timeout or a replica
before users do.
