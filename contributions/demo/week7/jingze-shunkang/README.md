# Assignment Proposal

## Title

Keeping Failures Visible with OpenTelemetry Tail Sampling

## Names and KTH ID

- Jingze Guo (jingze@kth.se)
- Shunkang Jia (shunkang@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

We will demonstrate how a DevOps engineer can reduce the volume of stored traces without losing the evidence needed to investigate rare failures. Our local Docker Compose setup will contain two small HTTP services that call each other, an OpenTelemetry Collector, Jaeger, and a repeatable traffic generator. The generator will send normal requests, requests that fail, and requests that are deliberately slow. Both services will contribute spans to the same distributed trace.

Initially, the Collector will retain a random 10% of traces. We will run the traffic generator and compare its request counts with the traces available in Jaeger, showing that uniform sampling can discard failures and slow requests.

During the live demo, we will edit the Collector configuration and restart only the Collector. The new tail-sampling policies will retain every trace containing an error or exceeding a latency threshold, while retaining approximately 10% of the remaining traces. We will repeat the same traffic, inspect the retained cross-service traces in Jaeger, and compare the results with the initial policy.

We will explain why the Collector needs to receive the complete traces before making these decisions. We will also discuss the costs and limitations: tail sampling buffers traces in memory and delays decisions; a scaled deployment must route all spans of a trace to the same Collector instance. The policy reduces trace ingestion into Jaeger, but does not reduce the traffic sent from the services to the Collector.

**Relevance**

Choosing which operational evidence to retain is a DevOps decision. This demo shows an engineer changing and validating an observability configuration against repeatable workload data, balancing diagnostic value against storage volume. It demonstrates a live configuration change across interacting services rather than only displaying a monitoring dashboard.