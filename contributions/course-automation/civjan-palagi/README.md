# Assignment Proposal

## Title

Proposal Verifications - Category and Presentation/Demo Date

## Names and KTH ID
  - Brad Palagi (palagi@kth.se)
  - Ben Civjan (civjan@kth.se)

## Deadline

Task 1

## Category

Course Automation

## Description

We will create a script to enforce the submission rules of the course.

These include:
1. Ensuring that students are not partners with the same person for more than two projects
2. Ensuring that students are not working alone for more than two projects
3. Ensuring that a student is not choosing the same topic (ex. Testing & CI, Containers & Serverless, etc.) for two different tasks
4. Making sure that a student has not done more a task (ex. presentation, essay, etc.) more than once

The check will be triggered when a new proposal PR is created. If there is any problem, the check will fail.


***Final Submission***

The link to our GitHub action repository is [here](https://github.com/bencivjan/enforce-submission-rules-action).

To demonstrate functionality, we have included a variety of tests through different types of simulated pull requests. The history of these tests can be seen in the 'Actions' tab of our repository. 

In order to facilitate these tests we created a *contributions* directory inside our repo with the same structure as KTH/devops-course. By integrating our GitHub action with the contributions folder, we hope to provide a good example for how our program could be used within the devops-course in the future.

The README of our repository outlines the functionality of the action, how to integrate it into a project, the most important aspects of the yml file, as well as the tests we ran to validate functionality. We also included some suggestions of submission standardization for the devops course in the future so that our script can be most effective.
