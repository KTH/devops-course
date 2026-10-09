# Assignment Proposal

## Title

Finding the slow line in production with continuous profiling using Grafana Pyroscope

## Names and KTH ID

- Jēkabs Čudars (cudars@kth.se)
- Kristers Krīgers (krigers@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

In this demo we show continuous profiling as the fourth observability signal, next to metrics, logs and traces. Using Grafana Pyroscope on a Kubernetes cluster, we show how a team can go from "the service is slow" to "this function is the problem" directly in production, without guessing or reproducing the issue elsewhere. The demo follows these steps:

1. We introduce the problem. When a service gets slow, developers have to check dashboards, read logs and guess which part of the code is responsible. Often they then try to reproduce the issue locally or in another environment, where it behaves differently.

2. We introduce the architecture. Two small FastAPI services, api and its upstream pricing, run on a local K3s Kubernetes cluster with a small in-cluster traffic generator. Prometheus collects metrics, Tempo collects traces, and Grafana shows both. Grafana Pyroscope is installed in the cluster, but the services do not send profiles to it yet. Code and manifests live in one GitHub repository.

3. We show how Grafana looks initially: request rate, latency, CPU and traces. This tells us whether a service is healthy, but not what its code is doing.

4. Live, we uncomment the few Pyroscope lines in the pricing service and redeploy it.

5. We show Grafana again. Next to metrics and traces we now have a flame graph of pricing, showing where it spends its time while healthy.

6. We push a normal-looking commit that introduces a performance problem: pricing now parses a large rules file on every request. Latency and CPU go up, and the trace shows a long pricing span, but not why.

7. We open the flame graph and compare it with the profile from before the commit. It points directly to the slow function, without guessing and without reproducing the issue anywhere else.

**Relevance**

Monitoring usually tells a DevOps team that something is slow, but not which part of the code causes it. Continuous profiling closes that gap by bringing production performance data back to developers at the function level, shortening the feedback loop from operations to development.

We will also discuss the trade-offs: profiling overhead, sampling limits, and when traces are enough versus when profiles are needed.