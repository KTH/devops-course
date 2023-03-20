# Assignment Proposal

## Title
Automated Switch Validation with P4 Models

## Names and KTH ID
  - Afruz Bakhshiyeva (afruz@kth.se)
  - Luis Jira (lcjira@kth.se)

## Deadline


- Week 2

## Category
- Presentation

## Description
This presentation will focus on how automated switch validation is currently achieved at Google as explained in this [research paper]{https://dl.acm.org/doi/abs/10.1145/3544216.3544220} and the preceding [talk at ONF Connect 19]{https://www.youtube.com/watch?v=VoUKAIg4zNE}.
The basic idea is that a formal specification in P4 is used to program a virtual switch and a hardware fixed-function network switch. Both receive the same network traffic and their output is compared. A difference in output then means that an error occurred at some stage in the process.


### Relevance
With software-defined networking and programmable switches becoming more and more common in datacenter networks, automated tests are necessary to ensure availability and correctness of the network.
