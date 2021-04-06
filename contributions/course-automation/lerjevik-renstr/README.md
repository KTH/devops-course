# Course Automation: Upvote other students’ work
 
## Members

- [Dina Lerjevik](https://github.com/dmariel) (lerjevik@kth.se)
- [Anders Renström](https://github.com/Renstrom) (renstr@kth.se)
 
## Introduction
 
We have integrated a functionality that enables students to upvote other students' work. This facilitates for students to fulfill the criteria: "The task is praised by the other students of this course", which is currently one of the criteria for "Course Automation".
 
## Description of functionality
 
* A student includes the label `Upvote - Course Automation` in a PR to the DevOps Course-repository.
  1. An issue `Upvote projects - Course Automation` is created, if no such issue already exists. The issue body includes a description of how to use the functionality, directed to the students. Furthermore, a “Top-list” that is going to show the most upvoted projects is incorporated to the issue, in the form of a comment.
  2. Next, a comment is automatically added to the issue thread. The comment includes: the title of the student's PR, a link to the PR and a link to the repository. This information enables other students to read about the project.
  3. The student recieves a comment on their PR, stating that a comment has been added to the issue `Upvote projects - Course Automation` (including a link to the issue).
* This enables other students to upvote their classmates projects, by inserting :thumbsup: on the comments in the issue `Upvote projects - Course Automation`.
* The upvotes are collected and visualized in the “Top-list”, which is sheduled to be automatically updated every 5 minutes.

## Using the functionality

Since this repository has not yet been merged to the KTH DevOps-course repository, a [simulation](https://github.com/dmariel/devops-course/tree/student-fork/contributions/course-automation/lerjevik-renstr) of the process has been performed, where a `student-fork` branch (corresponding to a student's course-automation fork) makes a labeled PR to the `2021` branch of this repository.

The results can be seen here:
* Example PR: https://github.com/dmariel/devops-course/pull/4
* Issue: https://github.com/dmariel/devops-course/issues/5

**The student creates a PR with the correct label:**

<img src="https://github.com/dmariel/devops-course/blob/course-automation/contributions/course-automation/lerjevik-renstr/images/creating_PR_with_label.png?raw=true" width="800">

**This enables the checks of the action to start running:**

<img src="https://github.com/dmariel/devops-course/blob/course-automation/contributions/course-automation/lerjevik-renstr/images/running_checks.png?raw=true" width="800">

**An issue is created if none already exists:**

<img src="https://github.com/dmariel/devops-course/blob/course-automation/contributions/course-automation/lerjevik-renstr/images/issue_created.png?raw=true" width="400">

**A comment linking to the issue is added to student's PR:**

<img src="https://github.com/dmariel/devops-course/blob/course-automation/contributions/course-automation/lerjevik-renstr/images/comment_added_to_PR.png?raw=true" width="800">

**Information about the student's course automation project is posted in the issue-thread:**

<img src="https://github.com/dmariel/devops-course/blob/course-automation/contributions/course-automation/lerjevik-renstr/images/issue_thread.png?raw=true" width="800">

**Other students can upvote the project by inserting a :thumbsup::**

<img src="https://github.com/dmariel/devops-course/blob/course-automation/contributions/course-automation/lerjevik-renstr/images/add_reaction.png?raw=true" width="800">

## Installation

This section describes how the functionality is installed on a repository. We recommend following this guide when introducing the functionality to future courses. **However, for the DevOps course, the only thing needed for the functionality to run is for the course-administrators to merge our PR and create a label `Upvote - Course Automation`.** 

1. Include a `.github/workflows` directory to the repository.
2. In the `.github/workflows` directory, create a file `upvote.yml` and add the contents of this [file](https://github.com/dmariel/devops-course/blob/course-automation/.github/workflows/upvote.yml) to it.
3. Specify the path to the repository that you want the script to run from on `line 16` of the `upvote.yml` file.
4. (Optional) Edit the label name on line `16`, if you want to adapt the code for other courses.
5. Create a file `ISSUE_TEMPLATE.md` in the `.github` directory. Use the following [template](https://github.com/dmariel/devops-course/blob/course-automation/.github/ISSUE_TEMPLATE.md). It's possible to adjust course name etc. in order to adapt the code for other courses.
6. Create a label `Upvote - Course Automation` (alternatively a label with the name you choose in step 4). 
7. Now the functionality is installed and ready to use!
 
## Criteria fulfilled 

We believed that we have fulfilled the following 5 criteria:
 
* The automation task produces a PR status or issue / PR comment 
    * Yes, please see the section `Description of functionality` above. Furthermore, the PR comment and the "Top-list" comment generated for the issue includes links to the generated issue or a comment. **Thus, we believe that the criteria for "Pass with distinction" is fulfilled.**
* The automation task is reusable
    * Yes, the task can be reused next year for the DevOps course. Moreover, the task can be used for other courses that use GitHub. **Thus, we believe that the criteria for "Pass with distinction" is fulfilled.** Please see the section `Installation` for more information.
* The task runs on a standard platform (GitHub Action)
    * Yes, the solution uses the GitHub Action platform.
* The code for the task is available
    * Yes, please see repository [here](https://github.com/dmariel/devops-course/tree/course-automation/.github). Furthermore, we believe that the repository is properly [documentated](https://github.com/dmariel/devops-course/edit/course-automation/contributions/course-automation/lerjevik-renstr/README.md). **Thus, we believe that the criteria for "Pass with distinction" is fulfilled.**
* The task is praised by the other students of this course
    * This is a bit difficult to determine since our functionality has not yet been launched. However, so far, we have recieved positive feedback when we've mentioned the idea to other students.   
