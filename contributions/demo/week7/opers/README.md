# Assignment Proposal

## Title

Your secret is safe with me: How to store and use secrets in AWS's secret manager

## Names and KTH ID
  - Oscar Persson (opers@kth.se)

## Deadline

- Week 7

## Category

- Demo

## Description

This presentation will cover secret managers, discuss their usefulness and place in the world of Dev(Sec)Ops. During the presentation a simple example project will be shown, which integrates a stored secret within AWS secret manager, a comparison may be made to storing them locally, or not storing them at all, and the demo will show how to upload them to AWS. The demo will focus on the importance of keeping ones secrets secret.

**Relevance**

As a rising standard in DevOps, DevSecOps embraces the security aspect of development, bringing it into the pipeline. Vulnerabilities in code and third party dependencies is one thing, but it is also of utmost important to keep developer credentials, information, and secrets, well, secret as well. A known secret could expose more than any vulnerability or exploit ever could. While there are many tools that may be used in the case of a secret being pushed to services such as GitHub, detecting and removing such instances, one may also take preventative action to prevent this from happening. Security of this also comes in the way of keeping everything up to date, preventing possible attack vectors.