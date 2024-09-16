# Assignment Proposal

## Title

Measuring frequency of deployments

## Names and KTH ID

- Tobias Ljunggren (tljun@kth.se)
- Josef Lindkvist (joslindk@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

The organization DORA comes out with the state of DevOps every year. Additionally, they provide a standard set of DevOps metrics used for evaluating process performance and maturity. These metrics provide information about how quickly DevOps can respond to changes, the average time to deploy code, the frequency of iterations, and insight into failures.

This demo will demonstrate how to easily and automatically measure frequency of deployments. The demo will utilise GitHub actions webhooks and a serverless rest API (AWS lambda) connected to a database (MongoDB). The demo will mainly focus on the GitHub actions webhooks, how to parse the payloads, and which events can trigger. It will not be about setting up AWS lambda.  

_Relevance

Github actions are commonly used to have autonomy and create personalised workflows for the deployment processes. This demo can be used for any project regardless of if the application is hosted on vercel, heroku, AWS, etc.

https://www.atlassian.com/devops/frameworks/dora-metrics
