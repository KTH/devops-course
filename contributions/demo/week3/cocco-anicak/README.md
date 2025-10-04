# Assignment Proposal

## Title

Blue Green Deployment Demo

## Names and KTH ID

  - Riccardo Cocco (cocco@kth.se)
  - Anica Krüger (anicak@kth.se)

## Deadline
- Week 3

## Category
- Demo

## Description

We would demonstrate a Blue-Green Deployment pipeline implemented with two separate Docker Containers and an Envoy Proxy determining the traffic flow. We will have health checks before rerouting the traffic and implementing GitHub Actions.
The demo will show how an application is deployed to a Green env running in parallel to the Blue env (which serves users)
If health checks are passed, the traffic is shifted from Blue to Green with no downtime.

**Relevance**

The topic is connected to the Week 3 topic of Continuous Deployment / Delivery
Blue-Green is a commonly used deployment strategy, and the demo will demonstrate its application. 
It also highlights the importance of rollback strategies, safe releases, and zero-downtime switching.
