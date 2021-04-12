# Course Automation: Upvote other students’ work
 
## Members
- [Dina Lerjevik](https://github.com/dmariel) (lerjevik@kth.se)
- [Anders Renström](https://github.com/Renstrom) (renstr@kth.se)
 
## Proposal
 
We would like to integrate a functionality that enables students to upvote other students' work. This would facilitate for students to fulfill the criteria: "The task is praised by the other students of this course", which is currently one of the criteria for "Course Automation".
 
The action should perform the following:
 
* When a specific label is included in a PR, create a comment on an issue with details from the Course Automation-folder (README-title and URL to project repository).
* A comment is added to the PR when a comment has been added to the issue. A link to the issue-comment is included.
* This enables people to upvote projects, by interting :thumbsup: on the comments.
* The upvotes are collected and visualized in a table, in the form of a “Top-list”.
 
We aim to fulfill the following criteria:
 
* Deadline before April 6, 2021 (in order to be useful for the course)
* The automation task produces a PR status or issue / PR comment and points to a generated page with valuable additional information
* The automation task is reusable in other courses
* The task runs on a standard platform (GitHub Action)
* The task is praised by the other students of this course
* The code for the task is available and the repo is well documented