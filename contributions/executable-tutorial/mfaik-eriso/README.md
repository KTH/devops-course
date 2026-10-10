# Assignment Proposal

## Title

Executable Tutorial: "Ship It" — Continuous Delivery vs. Continuous Deployment with Blue-Green Releases

## Names and KTH ID

- Mostafa Faik (mfaik@kth.se)
- Erik Söderlund (eriso@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

We propose an executable tutorial on KillerCoda that teaches the difference between Continuous Delivery and Continuous Deployment by guiding the learner through the creation and operation of a real CI/CD pipeline directly in the browser — without requiring accounts or cloud credentials.

The learner runs a small web service, "Demo Shop," on a disposable Ubuntu VM with Docker and nginx. The tutorial is structured into 9 guided steps, covering the following:

1. The service and its environments: manual deployment and observability.
2. Continuous Integration: every change is built and tested.
3. Production and deployment strategies: why blue-green.
4. Continuous Delivery: the manual gate.
5. Continuous Deployment: remove the gate.
6. The safety net: a bad release never reaches users.
7. Dark launches and instant rollback.
8. Continuous Integration for real: every commit triggers the pipeline.
9. Reflection: when, when not, and for whom.

The tutorial is grounded in the course material, including The Top 10 Adages in Continuous Deployment (Parnin et al.), the DigitalOcean introduction to CI/CD, and the Wikipedia articles on continuous delivery, continuous deployment, blue-green deployment, and deployment environments.

### Relevance

Continuous Delivery and Continuous Deployment are core DevOps practices: they automate the path from commit to production, shorten feedback loops, and turn releases from risky events into routine operations. This tutorial lets the learner experience exactly that tension hands-on: deploying more often while keeping failures away from users.

The tutorial touches several fundamental DevOps themes:

- Automation: the full test → build → version → deploy pipeline runs as code, with every step inspectable.
- Fast feedback and telemetry: health checks, version endpoints, and smoke tests gate every release (Adage 1: telemetry drives decisions).
- Deployment ≠ release: blue-green slots, a manual approval gate, and dark launches show how releasing to users is a separate, deliberate decision.
- Resilience: a broken release is aborted automatically, and rollback restores the previous version in about a second — because the old artifact is never destroyed.
- Culture and judgment: the final step reflects on when full automation is appropriate and when human approval is the right choice — recognizing that DevOps is not "automate everything," but "automate where it is safe."

### Links

- Scenario: https://killercoda.com/1mitox2/scenario/ship-it
- Repository: https://github.com/MiTO-X2/Continuous-Deployment-Bluegreen
