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

This project showcases Blue-Green deployment of a Iris classification AI model using MLflow, running two model versions (Blue and Green) in parallel. A FastAPI load balancer enables seamless switching and rollback, while a Streamlit dashboard provides a simple interface for monitoring, testing, and controlling traffic between the models.

**Relevance**

In this project, we demonstrate how the Blue-Green deployment strategy can be applied to AI model deployment using MLflow. By running two versions of the Iris classification model in parallel (Blue and Green), we can safely switch traffic between them, test new models in production, and roll back instantly if needed. This directly reflects DevOps principles such as continuous delivery, automation, reliability, and rapid feedback, showing how modern MLOps practices align with core DevOps methodologies.
