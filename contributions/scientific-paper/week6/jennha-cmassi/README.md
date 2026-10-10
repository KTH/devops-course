# Assignment Proposal

## Title

SpiderScan: Practical Detection of Malicious NPM Packages Based on Graph-Based Behavior Modeling and Matching

## Names and KTH ID

  - Christopher Massi (cmassi@kth.se)
  - Jennifer Ha (Jennha@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

Modern software development relies heavily on third-party packages and dependencies, making package ecosystems an attractive target for software supply chain attacks. Malicious packages can be difficult to detect because individual behaviors, such as accessing files or communicating over a network, can occur in both legitimate and malicious software.

The paper we have chosen to present, “SpiderScan: Practical Detection of Malicious NPM Packages Based on Graph-Based Behavior Modeling and Matching”, presents an approach for detecting malicious packages in the npm ecosystem. Instead of considering suspicious API calls only in isolation, SpiderScan models their relationships using behavior graphs that capture control flow and data dependencies. It then matches suspicious behavior against known malicious behavior patterns and uses additional verification to reduce false positives.

During the presentation we cover the problem of malicious packages, explain SpiderScan’s graph-based approach and evaluation. Discuss its DevSecOps and dependency-management implications, and critically compare its limitations with related approaches such as ProfMal and MalGuard.

**Relevance**

Third-party dependencies are an important part of modern DevOps pipelines, but they also introduce software supply chain security risks. Detecting malicious dependencies before they can compromise development, build, or deployment environments is therefore relevant to DevSecOps. SpiderScan addresses this problem by providing an automated approach for analyzing npm packages and identifying potentially malicious behavior.
