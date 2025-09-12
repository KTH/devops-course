# Assignment Proposal

## Title

DeepTest: Automated Testing of Deep-Neural-Network-driven Autonomous Cars

## Names and KTH ID

- Reza Hosseini (rezahos@kth.se)
- Gustav Nordström (gnords@kth.se)

## Deadline

- Week 4

## Category

- Scientific paper

## Description

We will present “DeepTest: Automated Testing of Deep-Neural-Network-driven Autonomous Cars” (ACM/IEEE ICSE 2018)

The paper introduces DeepTest, a tool for systematically testing deep learning models used in autonomous driving. It uses neuron coverage to guide test generation, applies realistic image transformations (rain, fog, brightness, rotation) to create corner cases, and checks outputs with metamorphic relations instead of costly labels.

**Relevance**

This work is highly relevant for MLOps/AIOps. It demonstrates that traditional DevOps-style testing principles are relevant in the field of ML: neuron coverage (an equivalent to code coverage in software technology) as a gating metric, metamorphic checks as automated oracles, and synthetic test cases generation. These ideas map directly to continuous testing and monitoring which is a core topic within DevOps practices applied to AI.
