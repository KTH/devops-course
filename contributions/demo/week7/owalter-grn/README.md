# Assignment Proposal

## Title

Chaos engineering and observability in Kubernetes

## Names and KTH ID

- Oscar Walter owalter@kth.se
- Gabriel Räätäri Nyström (grn@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

The system consists of producers sending jobs to a message queue and multiple worker pods processing them. Chaos is introduced by randomly terminating workers while load continues. The demo then observes queue growth, throughput, latency, pod recovery, and what happens when the recovered workers start draining the backlog.

Chaos will be introduced using Chaos Mesh, specifically `PodChaos`, to terminate random worker pods. A schedule will repeat this while producers continue sending jobs. The workers will run in a Kubernetes Deployment, so Kubernetes will automatically replace terminated pods. Prometheus and Grafana will be used to observe queue depth and recovery behavior as processing capacity is lost and restored.

The main focus is testing system resilience under failure and showing how observability helps explain the effects of the failure and recovery.

**Relevance**

This demo would cover both chaos engineering and observability. By terminating workers under a continuous load, we test how the system handles failures and recovers automatically. This connects to DevOps practices of testing resilience and using operational metrics to verify recovery.
