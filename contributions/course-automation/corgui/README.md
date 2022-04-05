# Assignment Proposal

## Title

Automatic deletion of teammate request

## Names and KTH ID

-   Corentin Guilloteau (corgui@kth.se)

## Deadline

Task 1

## Category

Course Automation

## Description

This course uses a Github repository issue to allow students to find a teammate. The problem here is that is requires
the students to update or remove their comment on this issue when they have found a teammate. This aim here is to
automate this task.

The automation should perform the following :

-   Run for each new pull request having a label corresponding to an assignment
-   Check if the author of the pull request has commented the teammate finder issue
-   If so, remove its comment on this issue
