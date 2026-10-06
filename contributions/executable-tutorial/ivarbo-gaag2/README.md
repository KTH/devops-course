# Assignment Proposal


## Title

Event-driven autoscaling in Kubernetes with KEDA and RabbitMQ

## Names and KTH ID

- Gabriel Arias (gaag2@kth.se)
- Ivar Boqvist (ivarbo@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

This tutorial goes into how you can use KEDA, a Kubernetes Event-driven Autoscaler, to better scale Kubernetes workloads. To introduce the problem at hand, the built-in autoscaler in Kubernetes, HorizontalPodAutoscaler, only scales on CPU utilization by default. For workloads that are largely I/O dependent, such as receiving and processing thousands of emails, this autoscaling doesn't quite cut it. This is where KEDA comes in. With KEDA, you can monitor message queues, databases, or APIs, and feed information on their usage back into the built-in autoscaler. The built-in autoscaler can then scale your workload properly all the way from hundreds to zero running pods. We'll be using KEDA's RabbitMQ message queue integration for this tutorial, as RabbitMQ strikes a good balance between being lightweight, configurable, and dependable.

As part of this tutorial, we'll set up a Killercoda scenario with a Kubernetes cluster running KEDA, RabbitMQ, and a message producer (such as a Python script). The tutorial will cover different modes of autoscaling, including no scaling, CPU-based HorizontalPodAutoscaler, KEDA ScaledObject, and test different configurations of the KEDA setup. By the end, you should be able to set up KEDA on a Kubernetes cluster, integrate it with a message queue such as RabbitMQ, and reason about when it's warranted or not.

**Relevance**

This tutorial is relevant to the field of DevOps as it aims to teach you about how to scale resources in a Kubernetes cluster for better reliability, throughput, and resource utilization. 
