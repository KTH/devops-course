# Assignment Proposal

## Title

GitOps and Continuous Reconciliation with Argo CD in Killercoda

## Names and KTH ID

* Georgi Tsonchev Hristov (georgith@kth.se)
* Sébastien Rivière (sebriv@kth.se)

## Deadline

* Task 2

## Category

* Executable tutorial

## Description

We propose an interactive, browser-based Killercoda tutorial demonstrating GitOps principles and automated reconciliation loops using **Argo CD** in a Kubernetes cluster.

The tutorial runs in a pre-configured, single-node Kubernetes (K3s) environment on Killercoda and requires no local installation or paid account. An automated background script installs Argo CD, exposes its Web UI, and prepares a sample Git repository containing declarative Kubernetes manifests (`Deployment` and `Service`).

During this ~15–20 minute scenario, learners will:
1. Connect Argo CD to the declarative Git repository and observe the initial synchronization in Argo CD's Web UI (`Synced` / `Healthy`).
2. Manually induce configuration drift using imperative `kubectl` commands (e.g., deleting the service or scaling deployment replicas to zero).
3. Observe how Argo CD flags the drift (`OutOfSync`) and automatically triggers self-healing to restore the cluster to the exact state declared in Git without human intervention.
4. Reflect on the design trade-offs and limitations of GitOps (e.g., pull-based architecture vs. traditional push pipelines, polling intervals, and secret management).

**Relevance**

This tutorial directly addresses **Week 5: Infrastructure as Code (IaC)**, specifically GitOps & Continuous Reconciliation Loops. Unlike traditional, push-based IaC tools (like Terraform or Ansible) where drift repair requires manual CLI invocation, this tutorial demonstrates an automated, continuous reconciliation engine running inside Kubernetes.
