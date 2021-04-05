# Course Automation: Upvote other students’ work
 
## Members

- [Dina Lerjevik](https://github.com/dmariel) (lerjevik@kth.se)
- [Anders Renström](https://github.com/Renstrom) (renstr@kth.se)
 
## Introduction
 
We have integrated a functionality that enables students to upvote other students' work. This facilitates for students to fulfill the criteria: "The task is praised by the other students of this course", which is currently one of the criteria for "Course Automation".
 
## Description of functionality
 
* When a student includes the label `Upvote - Course Automation` in a PR to the DevOps Course-repository:
 1. An issue `Upvote projects - Course Automation` is created, if no such issue already exists. The issue body includes a description of how to use the functionality, directed to the students. Furthermore, a “Top-list” that is going to show the most upvoted projects is incorporated to the issue, in the form of a comment.
 2. Next, a comment is automatically added to the issue thread. The comment includes: the title of the student's PR, a link to the PR and a link to the repository. This information enables other students to read about the project.
1. The student recieves a comment on their PR, stating that a comment has been added to the issue `Upvote projects - Course Automation` (including a link to the issue).
* This enables other students to upvote their classmates projects, by inserting :thumbsup: on the comments in the issue `Upvote projects - Course Automation`.
* The upvotes are collected and visualized in the “Top-list”, which is sheduled to be automatically updated every 5 minutes.

## Using the functionality

This section describes how the functionality is installed on a repository. We recommend following this guide when introducing the functionality to future courses:

1. Include a `.github/workflows` directory to the repository
2. In this folder, create a file and add the contents of the `upvote.yml` file to it
3. Specify the path to the repository that you want the script to run from on `line 13` of the `upvote.yml` file
4. Create a label `Upvote - Course Automation`
5. Now the functionality is installed and ready to use!
 
## Criteria fulfilled 

We believed that we have fulfilled the following criteria:
 
* Deadline before April 6, 2021 (in order to be useful for the course)
1. Yes, PR submitted on April 5.
* The automation task produces a PR status or issue / PR comment and points to a generated page with valuable additional information
2. Yes, please see the section `Description of functionality` above.
* The automation task is reusable in other courses
3. Yes, any course that uses GitHub. Please see the section `Using functionality` for more information.
* The task runs on a standard platform (GitHub Action)
4. Yes, the solution uses the GitHub Action platform.
* The code for the task is available and the repo is well documented.
5. Yes, please see repository [here]()

Furthermore, we hope that the following criteria will be fulfilled: "The task is praised by the other students of this course", this is hard to determine since our functionality is to be launched just now. However, so far, we have recieved positive feedback when we've mentioned the idea to other students.   