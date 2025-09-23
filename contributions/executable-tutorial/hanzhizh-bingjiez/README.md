# Assignment Proposal

## Title

Chaos Engineering with Pumba: Building Fault-Tolerant Containerized Applications

## Names and KTH ID

- Hanzhi Zhang (hanzhizh@kth.se)  
- Bingjie Zhao (bingjiez@kth.se)

## Deadline

- Task 3  

## Category

- Executable tutorial  

## Description

This executable tutorial demonstrates how to apply **Chaos Engineering** in containerized environments to improve system **fault tolerance** and **resilience**. Using [Pumba](https://github.com/alexei-led/pumba), a chaos testing tool for Docker, learners will inject controlled failures (random restarts, network delays, resource stress) into a containerized web application, and then gradually enhance the system to withstand these disruptions.  

The tutorial will guide users through the following scenario:

1. **Baseline setup**: Run a single-container Flask web application. Inject chaos (kill/restart, latency) with Pumba and observe how the service becomes unavailable.  

2. **Redundancy with multiple replicas**: Deploy multiple web containers behind an NGINX load balancer. Repeat the chaos experiments and see how the system remains available despite single-container failures.  

3. **Self-healing with restart policies**: Enable Docker restart policies so containers automatically recover after being killed by Pumba. Demonstrate improved resilience.  

4. **Application-level resilience**: Modify the Flask app to handle timeouts and provide fallback responses when backend services are delayed by chaos injections.  

5. **Iterative improvement**: Compare “before vs after” conditions, highlighting how redundancy, self-healing, and graceful degradation improve system reliability.  

This tutorial will be delivered through [KillerKoda](https://killercoda.com), using Docker Playground to safely run chaos experiments.  

## Relevance

Chaos Engineering is a key practice in **Site Reliability Engineering (SRE)**. By deliberately introducing controlled failures, teams can identify weaknesses early and build systems that remain reliable under stress. This tutorial highlights the transition from a fragile single-container system to a resilient multi-container setup, aligning with real-world practices for designing reliable, fault-tolerant cloud-native applications.  
