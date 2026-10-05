# Assignment Proposal

## Title

Automated model drift detection using Evidently

## Names and KTH ID

  - Jonathan Värild (varild@kth.se)
  - Alexander Runebou (alerun@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

For our tutorial, we will create an executable Google Colab notebook that shows how Evidently can detect data drift in an ML system and automatically trigger a workflow to retrain the model.

The tutorial starts with a classification model trained on a reference dataset. We will then simulate new production data where the distribution has changed (distribution drift). Evidently will compare the reference and current data and report if a significant drift has occurred. If so, the workflow will automatically train a new candidate model, evaluate it, and apply a quality gate. The candidate is only accepted if it satisfies set performance requirements. 

This tutorial demonstrates a simple MLOps feedback loop where we monitor, detect drift, retrain the model, evaluate, and finally promote/reject it.​

**Relevance**

The accuracy of ML systems can degrade even if the code remains untouched, since production data may change over time. Our tutorial shows how DevOps principles such as monitoring, automation, continuous validation, and controlled releases can be applied to the ML lifecycle.
