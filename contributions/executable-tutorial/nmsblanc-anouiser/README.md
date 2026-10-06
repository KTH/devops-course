# Assignment Proposal

## Title

Executable tutorial: Create metrics on your backend and monitor them with prometheus and grafana
	
## Names and KTH ID

  - Nolan Blanc (nmsblanc@kth.se)
  - Amin Nouiser (anouiser@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

In this tutorial we will build a very simple backend API in Python or express.js. We want to show you how to add metrics for an endpoint with the prometheus client library. After that we will guide you to configure Prometheus and Grafana with Docker to scrape these metrics and display them in a dashboard. Finally, we will guide you to create a Grafana alert that fires when the volume of requests becomes/stay abnormally high.

Along the way, we explain what Prometheus and Grafana are used for. We also share tips and point out common traps that we met during our first experience with these tools, such as Docker networking and the limits of sampling.

**Relevance**

Monitoring is a core part of DevOps. A deployed application can fail or behave badly at any time. Without monitoring, you often learn about a problem from your users. With monitoring, you see it in your metrics and can react before it grows.

Metrics also help you:

- Detect anomalies, such as a sudden spike in traffic or a drop in successful requests.
- Understand how the application behaves over time, and plan capacity.
- Check the effect of a new release right after a deployment.
- Alert the team automatically, so nobody has to watch a screen.

Prometheus and Grafana are standard tools in the industry. Prometheus collects and stores metrics. Grafana displays them and raises alerts. Together they are a common base for monitoring containerized applications.

The tutorial will be relevant to DevOps because it will cover the full monitoring loop in one short exercise. You instrument an application, collect its metrics, visualize them and get alerted on abnormal behavior.
