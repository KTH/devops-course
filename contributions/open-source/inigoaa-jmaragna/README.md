# Assignment Proposal

## Title

_--enable-feature: Consider removing no-default-scrape-port_

## Names and KTH ID

  - Jacopo Maragna (jmaragna@kth.se)
  - Íñigo Aréjula Aísa (inigoaa@kth.se)

## Deadline

- Task 3 

## Category

- open-source

## Description

Prometheus has different features available. However, some of them are not immediately available by default, but they can be enabled using flags. What the community is requesting is to enable some of these features by default. What we are proposing to do is to take this [issue](https://github.com/prometheus/prometheus/issues/13959) and resolve the problem.

Now, an outline of the various tasks we aim to solve:
1. Understand the project architecture and source code.
2. Set up the environment and run the project/tests.
3. Tackle the problem itself:
    - By default, we want the `no-default-scrape-port` feature to be enabled.
    - Add the possibility to disable it on demand.
    - Update the documentation.

**Relevance**

Prometheus is crucial in DevOps for its ability to monitor (Week 7) and analyze system performance in real-time. It helps teams collect metrics, set alerts, and automate responses, ensuring system reliability and quick incident resolution. This enhances the core DevOps practices of continuous integration, deployment, and collaboration.

Link: https://github.com/prometheus/prometheus/pull/14958
