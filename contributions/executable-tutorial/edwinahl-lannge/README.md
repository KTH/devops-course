# Assignment Proposal

## Title
Storing secrets locally using OpenBao

## Names and KTH ID

  - Edwin Ahlstrand (edwinahl@kth.se)
  - Lukas Lannge (lannge@kth.se)

## Deadline
- Task 3

## Category
- Executable tutorial

## Description
The tutorial teaches how to setup and store secrets locally in an OpenBao container. The steps taken during the tutorial are: 
1. Access a database using a password stored as plaintext in a python program
2. Scan the python file using detect-secrets (pip module)
3. Setup OpenBao docker container
4. Store secret in OpenBao
5. Update the python program to use the secret from OpenBao instead of plaintext

**Relevance**
In terms of DevSecOps, security must be managed by the team developing the product. By using OpenBao as a local docker container, a team can manage secrets safely and locally.

## Tutorial link
- Tutorial: https://killercoda.com/ahllan/scenario/scenario1
- Repo: https://github.com/EdwinAhl/DD2482-Executable-tutorial
