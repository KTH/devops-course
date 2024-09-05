# Assignment Proposal

## Title

Deployment and rollbacks with Kubernetes

## Names and KTH ID

  - Robin Claesson (robcla@kth.se)
  - Simon Hocker (hocker@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

We want to give a demo for how you can configure a Kubernetes cluster. We will start with giving a short introduction into the world of microservice and container architecture, then dive straight into Kubernetes and its purposes.

We will then begin the demo by showing a configuration file for a Kubernetes cluster, and then start it up, showing how the cluster represents the configuration. Following that, we demonstrate how to increase the replicas of a pod to scale with demand. 

We will then update the configuration to change the version of one of the pods and show how the cluster is updated. This new version will contain a bug, and to fix this we will show how to use the rollback feature of Kubernetes to go back to the previous working version, then deploy a corrected version without the bug.  

**Relevance**

Kubernetes a modern system for deploying containers in a micro service architecture. As applications grew to hold many complex containers across numerous servers, the system would become too complex for mainstream services to keep up. Problems arose consisting of how to coordinate, schedule and communicate between such an abundance of containers, how to scale them, etc. Google introduced Kubernetes to solve these problems.