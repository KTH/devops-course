# Assignment Proposal

## Title

Managing team secrets using Infisical and GitHub

## Names and KTH ID

  - Amin Nouiser (anouiser@kth.se)
  - Fauzan Helmi Sudaryanto (fhsu@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

Managing environment secrets is crucial, especially for developers working in teams. In this tutorial, we want to utilize [Infisical](https://infisical.com/) and GitHub to show the following scenario:

1. Start with a condition where secrets are committed in plaintext to a GitHub repository

2. How to set up Infisical's Secret Scanning to scan existing GitHub repository and prevent future vulnerabilities

3. How to securely set up secrets in Infisical

4. How to consume Infisical secrets in runtime and use it for your application

With this tutorial, we want to highlight the before (unmanaged/unsafe) vs after (managed/safe) condition. We plan to deliver our tutorial on [KillerCoda](https://killercoda.com).

Infisical is chosen in the tutorial as an open-source alternative to [HashiCorp Vault](https://www.hashicorp.com/en/products/vault) to manage secrets that teams can self-host. However, in this tutorial, we will use their cloud solution which has a Free plan that can be used for the scenario.

**Relevance**

Managing secrets is central to DevSecOps because it reduces the risk of credential leaks and aligns security with delivery workflows.
