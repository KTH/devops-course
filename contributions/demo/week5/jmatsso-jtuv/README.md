# Assignment Proposal

## Title

Using Pulumi Policy as Code to enforce rules on IoC managed cloud resources.

## Names and KTH ID

  - Johannes Matsson (jmatsso@kth.se)
  - Jonatan Tuvstedt (jtuv@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

The goal of this assignment is to demonstrate Pulumi's Policy as Code solution by showing a Policy for Cloud Storage (either Google cloud storage or AWS S3) in action. For this we will have a Pulumi CrossGuard policy for cloud storage and non compliant cloud storage resource created and managed by pulumi. We will first show the non compliant cloud storage in the cloud, then demonstrate that the CrossGuard Policy does not approve it. After that we will live fix the storage before finally showing it passing the Policy as Code check and being deployed.

**Relevance**

Infrastructure as code is an important topic in devops as being able to use code instead of manually managing disparate resources through online control centers is difficult, annoying and hard to have an overview of. But it is still easy to create unsafe or bad cloud resources with IaC, and therefore having a Policy as Code checks to enforce Policy compliance allows you to further integrate your IoC into your CI/CD pipeline.