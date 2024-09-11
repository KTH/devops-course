# Assignment Proposal

## Title

Dynamic model rollbacks using MLflow

## Names and KTH ID

  - Björn Thiberg (bthiberg@kth.se)
  - Omid Fattahi Mehr (omidfm@kth.se)

## Deadline

- Week 4

## Category

- Demo

## Description

We will demonstrate how to implement and automate dynamic model rollbacks using MLflow’s Model Registry. 

We will look at a model in production, and simulate a model performance drop or condition (set by us) when deploying a new version of the model.

Based on this condition, we will then trigger a rollback to an earlier reliable model (using Python code and the MLFlow API).

The process will be verified and visualized using the MLflow GUI.

**Relevance**

Using version management, automatic deployment and automatic reactions based on feedback from the production environment are core parts of the devops philosophy for software development. 

By doing this in an MLOps context, we demonstrate how DevOps principles can be extended for use in MLOps.

There is no way to natively do this yet in MLflow, and there is even currently [an issue](https://github.com/mlflow/mlflow/issues/6180) on the main MLflow repository, showing that this is both difficult and relevant.
