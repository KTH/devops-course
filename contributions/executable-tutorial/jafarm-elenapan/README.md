# Assignment Proposal

## Title

Diagnosing HTTP Service Errors with Prometheus and PromQL

## Names and KTH ID

  - Jafar (jafarm@kth.se)
  - Elena Pan (elenapan@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

This tutorial teaches how to investigate an operational failure in a running HTTP service using application metrics and PromQL. We observe healthy traffic, introduce a controlled failure, diagnose the affected endpoint, and verify recovery using Prometheus.

By the end of the tutorial, we will be able to: explain how an instrumented application exposes metrics and how Prometheus collects them; distinguish cumulative counters from request rates; write PromQL queries for request rate and error ratio grouped by endpoint; use metric labels to locate a failing endpoint and confirm recovery; and explain the limitations of metrics-based diagnosis.

The tutorial is a guided, ~20-30 minute Killercoda scenario. Automated setup starts a small instrumented Python application, a traffic generator, and Prometheus inside the browser. Only a free Killercoda account is needed: no local install, paid services, or external credentials. Each step includes executable commands, expected results, and an explanation of what it does and why.

Workflow:

1. Start the environment and verify Prometheus is scraping the application's metrics.
2. Generate continuous traffic against two endpoints and query request counters and rates.
3. Enable a failure mode that makes one endpoint return HTTP 500s while metrics stay available.
4. Compute the overall error ratio, then group by endpoint to find where failures occur, showing how aggregation can hide per-endpoint issues.
5. Disable the failure, keep generating traffic, and watch the error ratio recover as the query window moves past the incident.
6. Reflect on useful applications, design choices, and limitations of the approach.

**System architecture.** A traffic-generation script sends requests to a small HTTP application, which exposes a request counter via `/metrics`, labeled by endpoint and status code. Prometheus scrapes these metrics on an interval and serves them for querying and graphing. A diagram will show the application, traffic flow, and metrics collection path.

**Design decisions.** Prometheus combines metrics collection and querying in one tool, keeping the exercise focused. Counters support rate and error-ratio calculations, while endpoint/status labels support diagnosis; labels use a bounded set of values to avoid time-series growth. A provided container setup and scripted traffic/failure controls make the environment and the incident fully reproducible.

**Reflection on applicability.** This approach is useful for spotting service-wide or endpoint-specific spikes in errors, but aggregate metrics can hide individual failures, error ratios can mislead under low traffic, and scrape/query windows introduce observation delay. Metrics locate symptoms; logs or traces are often still needed to find the root cause. This makes the tutorial's relevance clearest for developers and operators responsible for keeping a running service healthy.

The tutorial will be validated end-to-end from a fresh Killercoda environment (setup, healthy traffic, failure injection, diagnosis, and recovery) within Killercoda's one-hour free session limit, before submission.

**Relevance**

This tutorial addresses monitoring and observability by showing how runtime measurements support incident investigation and recovery. It connects application instrumentation, automated metrics collection, and operational diagnosis in a single reproducible workflow, and is scoped narrowly around interpreting runtime metrics for service health rather than overlapping with other DevOps aspects such as testing/CI or deployment pipelines.
