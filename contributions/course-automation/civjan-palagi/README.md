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
