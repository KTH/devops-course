# Assignment Proposal

## Title
Improving the API for a built-your-own PaaS platform

## Names and KTH ID
  - Emil Karlsson (emilk2@kth.se)

## Deadline
- Task 1

## Category
- Open source

## Description
https://github.com/cloudfoundry/korifi

Korifi is a relatively newly built open-source "build you own" PaaS platform. It acts as a higher abstraction built on top of Kubernetes, but adds a lot more in terms of certificate management, ingress controllers, user management, command-line tools etc. 

This proposal aims to improve the API for Korifi.

**Relevance**\
Korifi is related to IaC and CD as it allows a developer to simplify their DevOps by facilitating them with various tools to spin up and manage apps. Thus, contributing to Korifi's API has direct effect on any DevOps engineer using the platform. 


Submission:
The final pr can found here: [https://github.com/cloudfoundry/korifi/pull/2371](https://github.com/cloudfoundry/korifi/pull/2371)

I implemented a route in the Korifi API that allows fetching packages connected to an deployed app. On top of it, both unit and end-to-end tests were written. These tests had to be refactored after the maintainers made changes to the API. Communication with a maintainer was done too in order to get the PR merged correctly, and their guidelines were followed. 