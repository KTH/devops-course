# Assignment Proposal

## Title

Security and vulnerability scanning using Trivy

## Names and KTH ID

- William Nordwall (wcvno@kth.se)
- Elsa Linnéusson (elsalin@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description
Our executable tutorial will demonstrate how to detect security issues or dependency vulnerabilities in your code.
The tutorial will run on Killercoda and will guide the user through how to use Trivy to detect issues.
It starts off with some Python code which has exposed secrets and vulnerable dependencies. The user will then be told how to run a command on this code to find these issues.
In order to proceed to the next step, the user must address all problems discovered by Trivy.
Once the issues are fixed we will help the user set these checks up in the CI pipeline so that they do not have to check manually each time they push new code.
Once the user has fixed the issues and set up a CI which runs Trivy, the tutorial is completed.


**Relevance**
This is related to dependency management and DevSecOps as it helps the user ensure that their code is secure.
It also utilizes a CI pipeline to help automate this process, which is a core part of DevOps.
