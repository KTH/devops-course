# Assignment Proposal

## Title

AI assisted incident investigation with HolmesGPT and improved observability

## Names and KTH ID

- Jēkabs Čudars (cudars@kth.se)
- Kristers Krīgers (krigers@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

We present a workflow where AI investigates a service failure on a local Kubernetes cluster and a gated step remediates it. The system is two small FastAPI services, api and its upstream pricing, under constant Locust load, monitored with Prometheus, Loki and Grafana. Code and manifests live in one GitHub repository.

We introduce the fault as a commit that changes pricing configuration, making it slow; api starts timing out. A Grafana alert rule fires when the error rate stays above a threshold and triggers HolmesGPT, which investigates using metrics, logs and recent GitHub changes through MCP. With only default request metrics and plain logs, its diagnosis is plausible but unverified.

Live, we add observability: a per-upstream latency metric and a structured log field in api, plus a Grafana panel for them. We re-trigger the alert and Holmes now pinpoints pricing and the commit with evidence. A separate remediation step, allowed to run one predefined action, rolls back the pricing deployment. We verify in Grafana that the error rate returns to normal.

**Relevance**

From a DevOps perspective, monitoring helps us detect failures, but investigation and recovery still take time. This demo connects monitoring, AI-assisted diagnosis, and automated remediation in one workflow.

We'll show how AI agents can support service recovery, while highlighting the need to check their findings, limit their permissions, and verify that a fix actually resolves the issue.