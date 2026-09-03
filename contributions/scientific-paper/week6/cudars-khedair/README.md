# Assignment Proposal

## Title

ARGUS: A Framework for Staged Static Taint Analysis of GitHub Workflows and Actions

## Names and KTH ID

  - Jēkabs Čudars (cudars@kth.se)
  - Rami Khedair (khedair@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

The paper selected was published at the 32nd USENIX Security Symposium (USENIX Security 2023) https://www.usenix.org/conference/usenixsecurity23/presentation/muralee.

CI/CD automation platforms such as GitHub actions, GitLab CI, Travis CI etc. are a modern part of software development on which large amount of projects rely on. With these platforms new dependencies and code complexity has been introduced resulting in new vulnerabilities. 
Currently, securing pipeline requires oversight over non-linear workflow execution and handling 3rd party interactions with actions. The current authors purpose - `ARGUS`, taint analysis designed to catch GitHub actions code injections. In contrast, to existing solutions ARGUS models non-linear workflows into graphs uses taint analysis summary to catch vulnerabilities across the GitHub Action Jobs supporting composite and JavaScript actions types. Authors ran their analysis tool over 2.7 million workflows and managed to find critical vulnerabilities (manually verified) in 4307 of them.

During the presentation we plan to deep dive into the method applied in the taint analysis, provide architecture overview and discuss the key finding of the paper.

**Relevance**

GitHub actions is one of the core CI/CD automation platforms in DevOps. This paper directly assesses the security layer of CI/CD pipelines , showing that vulnerabilities in workflows are pervasive and can compromise the entire software supply chain. 

Understanding and detecting these risks is essential for anyone designing or maintaining DevOps pipelines.