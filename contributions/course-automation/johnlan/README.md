# Assignment Proposal

## Title

Automatic verification for mandatory parts of course-automation final

## Names and KTH ID

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


Submission


Link to action repo

https://github.com/landeholt/dd2482-course-automation

__Validation__

- [Pull request #8](https://github.com/landeholt/dd2482-course-automation/pull/8)


__Testing__

Please check through the test folder, or the readme solution.

I think I have fulfilled the following criterion: 


__Changelog__

- changed title from "Meta course-automation" to "Mandatory sanity checker for DD2482"
- changed installation documentation separating the two registries (GH Marketplace & PyPi)
- Removed takeaways, as it didn't provide any valuable insight to the project
- Added a Rationale section, such that a background to the creation of this action is based on
- Changed "Validation links" to "Possible outcomes"
- Added Inputs section, explaining what data is needed to make the action work as intented
- Created a flowchart (figure) of the action and appended the illustration to the README
- Published the action to Github Marketplace


|                                             | Yes | No | 
|-------------------------------------------- | ----|----|
|timeliness: the automation is done before the first task deadline (in order to be useful for the course) | **Mandatory** | - |
|repo: the code for the task is available in a public repo  | **Mandatory**| - | 
|outcome: the automation task produces a PR status or an issue / PR comment | **Yes** | No |
|reuse: the automation task is reusable (next year for this course) | **Yes** | No | 
|platform: the task runs on a standard platform (eg Github action) | **Yes** | No | 
|doc: the repo is documented with a good readme | **Yes**  | No | 
|figure: the README is illustrated with at least an informative figure (eg a flowchart) | **Yes** | No | 
|availability: The action is available on a market place (Github Marketplace, Azure Marketplace, etc.) | **Yes** | No | 
