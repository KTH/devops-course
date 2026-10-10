# Assignment Proposal

## Title

SLO Error-Budget Alerting with Prometheus and Alertmanager

## Names and KTH ID

- Hasan Kalzi (kalzi@kth.se)
- Robert Jenson (robjen@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

We will demonstrate how a service-level objective can turn application metrics into an actionable reliability alert. A small FastAPI service, a load generator, Prometheus and Alertmanager will run locally as interacting Docker Compose services. The application will expose request and error counters that Prometheus scrapes.

We will define a 99% availability SLO and a corresponding 1% error budget. During the live demonstration, we will first generate healthy traffic and show that the service remains within its objective. We will then change the application's failure rate to approximately 20%, observe the error ratio and error-budget burn in Prometheus, and show the alert transition to firing in Alertmanager. Finally, we will restore healthy behaviour and verify recovery. We will explain that the short measurement window is chosen for a seven-minute demonstration and discuss how production systems use longer windows and multi-window burn-rate alerts.

**Relevance**

The demo connects application instrumentation, monitoring, SLOs and automated alerting in one observable DevOps workflow. It shows how teams can base operational decisions on user-facing reliability objectives instead of isolated infrastructure metrics. Unlike deployment-gating and rollback demonstrations, our focus is on detecting and communicating error-budget consumption during operation; the demo does not perform a canary deployment or automated rollback.
