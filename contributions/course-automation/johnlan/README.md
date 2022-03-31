# Assignment Proposal

## Title

Automatic verification for mandatory parts of course-automation final

## Names and KTH ID

-   John Landeholt (johnlan@kth.se)
-   John Landeholt (johnlan@kth.se)

## Deadline

Deadline to complete task 1: April 5, 17h Stockholm time

## Category

Course Automation 

## Description

In order to alleviate __redundant work__ for this course TAs I propose to automate verification of the following mandatory parts for ["course-automation"](https://github.com/KTH/devops-course/blob/2022/grading-criteria.md#course-automation):

-   timeliness: the automation is done before the __first task__ deadline (in order to be useful for the course)
        The first task deadline should be a set as a variable that can be changed for each year. If the final pull request to this repo is after __first task__, the pull request should become invalid.
-   repo: the code for the task is available in a public repo
        Check through the `readme.md` for a github-url and check whether the repo is public or not

The automation should perform the following :

-   Run for each new pull request that is the course automation task
-   Check if it is a final submission (i.e has a repo-link)
    - if final: check if it is before __first task__ deadline and if repo is __public__
    - if not final: check if it is before __first task__
-   Give feedback accordingly to the pull request

