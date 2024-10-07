# Assignment Proposal

## Title

Kubernetes secrets with Sealed Secrets

## Names and KTH ID

  - Amin Nouiser (anouiser@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

Managing Kubernetes secrets can be challenging, especially when the infrastructure is defined in code in a public git repository. By default, Kubernetes secrets are only base64 encoded but not encrypted which is not sufficiently secure. Sealed Secrets is a tool that allows secrets to be encrypted by the developer and remain so until they reach the cluster. 

In this demo, I will begin by demonstrating how secrets can be distributed without Sealed Secrets to illustrate the security risk. I will then introduce Sealed Secrets and demonstrate how it solves this problem and makes the distribution more secure.

**Relevance**

This demo is relevant to DevOps as it addresses secure secret management in Kubernetes which is a key principle in DevSecOps.