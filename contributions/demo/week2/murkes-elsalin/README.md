# Assignment Proposal
 
## Title
CI Pipeline with Integration Testing Against a Real Database
 
## Names and KTH ID
- Felicia Murkes — (murkes@kth.se)
- Elsa Linnéusson — (elsalin@kth.se)
## Deadline
Week 2
 
## Category
Demo
 
## Description
The demo will demonstrate a basic CI pipeline with two levels of tests: integration tests alongside unit tests. 
We will build a simple shopping list app backed up by a MySQL database as an external service. 
The CI pipeline (GitHub Actions) will run on every push/PR.

We will focus on why multiple levels of testing are essential and why unit tests may not be enough. 
Unit tests typically run against mocked or simulated data, so they can pass even when the underlying logic has a 
flaw that only appears when interacting with real data or real databases' behaviour, such as constraints, data types, or case-sensitivity, 
that a mock won't enforce. Code can look fine in isolation but fail when interacting with other components.

**Relevance**
Continuous Integration is a core DevOps practice: automatically testing every change catches problems early, before they reach production.
Running multiple levels of tests matters because some bugs won't surface until the code interacts with external services.
