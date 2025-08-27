# Assignment Proposal

## Title

Setting up a CI pipeline with GitHub Webhooks and REST API feedback

## Names and KTH ID

- Harald Hamrin Reinhed (haraldhr@kth.se)
- Ludwig Flod (lflod@kth.se)

## Deadline

- Week 2

## Category

- Demo

## Description

The demo will show how to implement a simple Continuous Integration (CI) workflow from scratch using GitHub webhooks and the GitHub REST API.  
The workflow will cover the following steps:  
1. Setting up a GitHub webhook that triggers on new commits or pull requests.  
2. Implementing a lightweight server that listens for webhook events.  
3. Running automated build and test commands on the triggered event.  
4. Reporting the results of the build back to GitHub by updating the commit status or posting a comment through the REST API.  

The demo will be performed live by pushing both failing and successful commits to show the feedback loop in action.
The idea is to give a general idea of how to implement it, so some functions will be pre-written.

**Relevance**

This proposal is directly relevant to CI, as it demonstrates the fundamentals of Continuous Integration: automatic builds, testing, and feedback triggered by version control events. The example makes visible how CI tools GitHub Actions work under the hood, and highlights the importance of automation, integration, and rapid feedback in modern software development workflows.
