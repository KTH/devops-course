# Assignment Proposal

## Title

Observability for Containerized Apps with cAdvisor, Prometheus & Grafana

## Names and KTH ID

  - Adam Fridén Rasmussen (ajfr2@kth.se)
  - John Söderholm (jsoderho@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

This executable tutorial will cover container observability, where we will set up a monitoring stack including Prometheus for collecting and storing metrics, Grafana visualize and understanding our data, and cAdvisor for gathering detailed resource metrics directly from the running containers, a layer Prometheus alone does not cover.

This stack will monitor a simple Flask application. We will put the app under different kinds of load, like using a /cpu-stress endpoint, and then observe these performance changes using cAdvisor's metrics. KillerKoda will handle setting up services, monitoring, and testing, all in one place.

**General structure**
1. Explain container observability in DevOps. Define Prometheus, Grafana, and cAdvisor.
1. Create all necessary config files. Build and start the monitoring stack.
1. Verify cAdvisor data collection. Set up Grafana to visualize cAdvisor's container performance metrics.
1. Trigger different load on the Flask app's container. See changes in cAdvisor data highlighted on their Grafana dashboards

**Relevance**

Container observability is essential in DevOps for understanding service performance. This tutorial uses cAdvisor to provide low-level data about container resource use, which is important for using resources smartly, identifying problems, and ensuring apps run optimally.
