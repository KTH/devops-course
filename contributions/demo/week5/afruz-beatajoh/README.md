# Assignment Proposal

## Title

Infrastructure as Code in Jenkins

## Names and KTH ID

  - Beata Johansson (beatajoh@kth.se)
  - Afruz Bakhshiyeva (afruz@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

Configuration as Code (CaC) demonstration of Jenkins jobs with the JobDSL plugin and Jcasc.

The demo will consist of setting up a docker container running Jenkins with these plugins and show how DSL files are used for configuring jobs as code in Jenkins. We will also show how the deployment of an entire Jenkins instance can be done with Jcasc.

Hopefully we can demo an example which highlights why configuring Jenkins with DSL files is important.

https://hub.docker.com/r/tomdesinto/jenkins-dsl-ready/
https://medium.com/preply-engineering/jenkins-omg-275e2df5d647

**Relevance**

Jenkins is a commonly used tool for building and automating tests in the form of Jenkins jobs. The CaC way of thinking simplifies maintaining and restoring jobs which contains errors. This becomes important when projects manage a large numbers of jobs. It can also be relevant for teams to re-deploy entire Jenkins instances in the infrastructure.
