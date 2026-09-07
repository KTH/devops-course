# Assignment Proposal

## Title

Automated Regression Testing of a Real-Time Threat-Detection Pipeline

## Names and KTH ID

- Einar Harri (eharri@kth.se)
- Christopher Massi (cmassi@kth.se)


## Deadline

- Week 2

## Category

- Demo

## Description

We propose a live demonstration of automated regression testing in Kinetic
Ranger, a real-time RF threat-detection prototype. The system consists of a
synthetic signal source, feature extraction, state estimation, alerting logic,
a FastAPI backend, a WebSocket connection, and a web-based dashboard.

During the demonstration, we will use a deterministic recorded scenario to
test the behavior of the detection pipeline. We will introduce a configuration
or implementation change that causes an incorrect alert decision, demonstrate
how an automated test detects the regression, and then show the pipeline
working correctly after the problem is fixed.

We created this software together with our other group members as part of the Drone Defence Hackaton 2026 held at KTH Innovation with their partner companies. 
See link to repository below:
https://github.com/einhar1/DDH2026-Kinetic-Ranger
