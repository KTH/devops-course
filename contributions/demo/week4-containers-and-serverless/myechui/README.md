# Assignment Proposal

## Title

Demonstration of Deploying Multiple API Servers with Docker and AWS Lambda

## Names and KTH ID

- Man Yin Edward CHUI (myechui@kth.se)

## Deadline

Task 2 (April 19)

## Category

Week 4: Containers & Serverless (April 12)

## Description

This demonstration would like to show: 

- How to dockerize multiple backend API servers (possibly written in different languages) under the same project at the same time.
- How to then deploy the docker to AWS lambda.

AWS Lambda is a serverless, event-driven service.
When a request is made to Lambda, it will invoke a function call to a function which correspond to an API call, then make the request accordingly.
In this demo, I would like to show how to deploy multiple backend API servers and demonstrate how they can possibly interact with each other (may be like a webhook) in the container.

Repository for the demo:
https://github.com/EDChui/docker-to-aws-demo
