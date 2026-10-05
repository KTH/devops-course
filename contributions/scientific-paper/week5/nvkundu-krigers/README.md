# Assignment Proposal

## Title

Deployability-Centric Infrastructure-as-Code Generation: Fail, Learn, Refine, and Succeed through LLM-Empowered DevOps Simulation

## Names and KTH ID

  - Nalin Kundu (nvkundu@kth.se)
  - Kristers Krigers (krigers@kth.se)

## Deadline

- Week 5

## Category

- Scientific paper

## Description

We want to present the FSE 2026 paper ["Deployability-Centric Infrastructure-as-Code Generation: Fail, Learn, Refine, and Succeed through LLM-Empowered DevOps Simulation"](https://dl.acm.org/doi/10.1145/3797142).

Large Language Models can generate Infrastructure-as-Code (IaC) templates, but syntactically correct IaC does not necessarily deploy successfully. The paper evaluates six LLMs and finds that only 20.8–30.2% of generated IaC templates successfully deploy on the first attempt. To address this, the authors introduce *IaCGen*, an iterative framework that verifies generated IaC, attempts real deployment, collects deployment errors, and provides this feedback to the LLM to refine the configuration. Using this feedback loop, IaCGen increases the proportion of deployable templates to 54.6–91.6% within 10 iterations. The paper also investigates limitations regarding user-intent alignment and security compliance.


**Relevance**

The paper is directly related to Infrastructure as Code and automated infrastructure deployment. It demonstrates how deployment feedback can be incorporated into LLM-based IaC generation, as it allows agentic tools to be used in modern DevOps workflows. 
