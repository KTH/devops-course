# Assignment Proposal

## Title

Detection as Code: Testing and Deploying Falco Runtime Security Rules in Kubernetes

## Names and KTH ID

- Vilhelm Prytz (vprytz@kth.se)
- Samouil Mosios (samouil@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

**Executable tutorial submission.** The tutorial is complete. Proposal: [#3087](https://github.com/KTH/devops-course/pull/3087).

Tutorial: https://killercoda.com/vilhelm/scenario/detection-as-code-with-falco

The tutorial runs on Killercoda's two-node Kubernetes playground and needs no local installation or account beyond Killercoda. A background setup script installs Falco, Falcosidekick and the Falcosidekick web UI with Helm, deploys a deliberately vulnerable web app, and creates a local Git repository for the detection rules whose Git hook runs a validate, deploy, test and rollback pipeline. The learner goes through six verified steps:

1. Baseline detection: exploit the app and see Falco's default rules flag the attack
2. The rules repository and pipeline
3. Write a custom rule together with a test, and ship it through the pipeline
4. Break it on purpose: push a broken rule and see the pipeline stop it
5. Tune a false positive with an exception, through the same pipeline
6. Close the loop: use the alert details to fix the app and confirm the attack no longer works
