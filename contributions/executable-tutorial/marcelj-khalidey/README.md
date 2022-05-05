# Assignment Proposal

## Title

Massively cutting server costs for model training with spot instances on Azure.

## Names and KTH ID

- Marcel Juschak (marcelj@kth.se)
- Khalid El Yaacoub (khalidey@kth.se)

## Deadline

Task 3

## Category

Executable Tutorial

## Description

Training a machine learning (ML) model is one of the core components of MLOps, e.g. for continuous deployment. However, training a model can require high-end hardware resources over many days which in turn leads to high monetary costs. Spot instances on cloud platforms like Azure are servers that can be rented for usually 10% to 25% of the original price. As a downside, access to the instance may be withdrawn at any point after a 30 second notice. Model training can take advantage of spot instances by checkpointing the training state so that training can be resumed from a checkpoint after termination and restart of the server.

In this tutorial we will show how to create a docker container that trains an ML model with checkpointing and resumes training after random termination + automatic restart of the Azure spot instance.

**Final Submission**: [Tutorial repo](https://github.com/Neproxx/cloud-training)
