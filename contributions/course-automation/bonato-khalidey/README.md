# Assignment Proposal

## Title
Automatic email of PR merge success and calendar event.

## Names and KTH ID
  - Khalid El Yaacoub (khalidey@kth.se)
  - Simone Bonato (bonato@kth.se)

## Deadline

April 5th - Task 1

## Category

Course Automation

## Description

We designed a GitHub action that automatically generates an email confirmation that notifies the students with the details of their PR (title, description, deadline) and additional information (who and when accepted the PR), when it is merged in the main branch.

The github action does the following:

- On merge, parses the PR description and determine its details.
- Writes an email that contains a calendar event for the date of the deadline at 17pm if the deadline was written correctly in the body of the PR (it contains "task #"), otherwise it only includes the PR details and the info regarding who accepted the PR.
- Sends an email w/details to parsed addresses.

We thought it could be useful in order to give the students a confirmation that their request has been accepted and a further reminder about the deadline of their intended task.

  **_Final Submission_**

Here below you can find the links to the GitHub repo of the action, a link to the tutorial and demonstration that the action works, and finally the link to the GitHub marketplace page where we uploaded our action.

Repository for Github Action: https://github.com/khalidey/merge-checker

Link to Github marketplace: https://github.com/marketplace/actions/merge-checker

Link to the tutorial & demonstration that the action works: https://github.com/khalidey/merge-checker/blob/main/tutorial.md
