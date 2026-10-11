# Assignment Proposal

## Title

SLO Error-Budget Alerting with Prometheus and Alertmanager

## Names and KTH ID

- Hasan Kalzi (kalzi@kth.se)
- Robert Jensen (robjen@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

We will demonstrate how a service-level objective can turn application metrics into an actionable reliability alert. A small FastAPI service, a load generator, Prometheus and Alertmanager will run locally as interacting Docker Compose services. The application will expose request and error counters that Prometheus scrapes.

We will define a 99% availability SLO and a corresponding 1% error budget. During the live demonstration, we will first generate healthy traffic and show that the service remains within its objective. We will then change the application's failure rate to approximately 20%, observe the error ratio and error-budget burn in Prometheus, and show the alert transition to firing in Alertmanager. Finally, we will restore healthy behaviour and verify recovery. We will explain that the short measurement window is chosen for a seven-minute demonstration and discuss how production systems use longer windows and multi-window burn-rate alerts.

**Relevance**

The demo connects application instrumentation, monitoring, SLOs and automated alerting in one observable DevOps workflow. It shows how teams can base operational decisions on user-facing reliability objectives instead of isolated infrastructure metrics. Unlike deployment-gating and rollback demonstrations, our focus is on detecting and communicating error-budget consumption during operation; the demo does not perform a canary deployment or automated rollback.

**Implementation and related material**

- [Public implementation repository](https://github.com/Hasan-Kalzi/slo-error-budget-demo)
- [Setup, SLO calculations, validation and live demo instructions](https://github.com/Hasan-Kalzi/slo-error-budget-demo/blob/main/README.md)
- [Accepted proposal](https://github.com/KTH/devops-course/pull/3096)
- [Peer feedback from Yasmine and Alexandru](https://github.com/KTH/devops-course/pull/3096#issuecomment-6098051296)

The implementation is available on the main branch. It includes the application, load generator, Compose configuration, recording and alert rules, Alertmanager configuration, demo controls and seven API integration tests. Failure injection and recovery change the application's configuration through its HTTP API without restarting it.

**System behaviour**

The error budget is the allowed fraction of failed work requests: 1%. Prometheus divides the observed error ratio over 30 seconds by 0.01 to calculate recent burn. A 20% error ratio gives a burn rate of 20. This calculation does not measure a remaining budget over an entire reporting period.

Healthy, Incident and Recovery are the presenter-controlled demo stages. Inactive, Pending and Firing are Prometheus alert states. The alert fires after the burn rate remains above 1 for 10 seconds. Recovery is delayed while earlier errors remain in the rolling window.

**Design choices and reflection**

FastAPI provides a small instrumented API. Compose makes the interacting services reproducible on one host. Prometheus evaluates metrics and rules, while Alertmanager handles grouping and routing. Recording rules keep the graph and alert based on the same calculation.

A shared SLO supports agreement between development and operations about when reliability work should take priority over new features. The short measurement window makes behaviour visible during the demo but can produce noisy readings. Production systems need appropriate reporting periods and alert windows. This demo measures handled requests only, uses manual recovery and displays alerts in web interfaces. It does not provision cloud infrastructure or send external notifications.

**Validation and peer feedback**

Seven API tests and configuration validation passed during preparation, as recorded in [implementation PR #1](https://github.com/Hasan-Kalzi/slo-error-budget-demo/pull/1). The failure-injection, alerting and recovery sequence was exercised during the peer-feedback rehearsal.

Yasmine and Alexandru reviewed the rehearsal on 9 October and posted their feedback on 10 October 2026. They supported the technical depth, live interaction, architecture explanation and DevOps relevance, while identifying timing and explanation improvements. The final timed rehearsal and the Week 7 in-person presentation remain.

