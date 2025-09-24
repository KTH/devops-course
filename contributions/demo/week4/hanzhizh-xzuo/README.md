# Assignment Proposal

## Title

Blue-Green Deployment of AI Models Based on MLflow

## Names and KTH ID

  - Hanzhi Zhang (hanzhizh@kth.se)
  - Xu Zuo (xzuo@kth.se)

## Deadline

Week 4

## Category

Demo

## Description

This project highlights the use of MLflow in a Blue-Green deployment of an Iris classification AI model. Instead of focusing only on traffic switching, we demonstrate how MLflow supports the end-to-end lifecycle of the model: training and packaging with MLflow Models, versioning and promotion with the Model Registry, and experiment tracking with the Tracking Server. Rollback and health checks go beyond service availability by validating model functionality and performance through MLflow. In this way, the project showcases how MLflow enhances Blue-Green deployment by integrating model management, monitoring, and lifecycle control.

There are several differences from the similar topic in previous years. Our demo mainly focuses on traffic switching in production and visual control via a load balancer, by running two different model versions on two separate deployments and switching traffic between them. The previous demo, however, switches model versions in the MLflow Registry, which means it runs different versions of the model within a single virtual machine.

**Relevance**

In this project, we demonstrate how the Blue-Green deployment strategy can be applied to AI model deployment using MLflow. By running two versions of the Iris classification model in parallel (Blue and Green), we can safely switch traffic between them, test new models in production, and roll back instantly if needed. This directly reflects DevOps principles such as continuous delivery, automation, reliability, and rapid feedback, showing how modern MLOps practices align with core DevOps methodologies.
