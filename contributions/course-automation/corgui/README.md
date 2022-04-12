# Assignment Proposal

## Title

Automatic deletion of teammate request

## Names and KTH ID

-   Corentin Guilloteau (corgui@kth.se)

## Deadline

Task 2

## Category

Course Automation

## Description

This course uses a Github repository issue to allow students to find a teammate. The problem here is that is requires
the students to update or remove their comment on this issue when they have found a teammate. The aim here is to
automate this task.

The automation should perform the following :

-   Run for each new pull request having a label corresponding to an assignment
-   Check if the emails of the author of the task are included in a comment on the teammate finding issue
-   If so, add edit the first comment found by appending `AUTO EDIT: Teammate found`and mentioning the identified users
    to notify them, and comment the PR with a reference to the comment
