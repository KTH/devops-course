# Assignment Proposal

## Title

CI job for live counting active participation

## Names and KTH ID

- Björn Thiberg (bthiberg@kth.se)

## Deadline

- Deadline 1

## Category

- Open source

## Description

This document is 1. a task proposal for introducing a script and a GitHub Actions workflow to track lecture participation, and 2. the description of the PR which implementatis this. Very meta.

The structure of both script and workflow YAML file is based on the already existing workflow for updating the Statistics of Student Registrations. It has a similar structure, can be run locally in the same way, and uses the same dependencies.

How it's supposed to work:

GitHub actions workflow
- The workflow is triggered on new issue comments, and proceeds if the issue title is “Lecture participation tracker 2024”.
- track_participation.py is run

Python script (`track_participation.py`):
- Fetches all comments to the issue from the GitHub API
- If the author is a collaborator, or the comment is outside the commenting window (5 hours from the start of each lecture), the comment is ignored.
- Valid comments are stored in a dictionary, with keys for each student who has commented.
- The script generates a markdown table, similar to the one for tracking tasks, which displays the lectures each student has attended.
- The issue description is updated with this markdown table and a timestamp.

I have tested that (in a copy of the repo):
- the workflow triggers correctly when a new comment is added to the tracker.
- comments made by collaborators are ignored as expected.
- comments made outside of the allowed window are not counted.
- valid comments update the participation tracker in the issue.
- timezones work as expected (don't quote me on this)

I have not tested for more than two unique students/commenters, as would be the case in "production".

Updating for newer years should only require changing the lecture dates constant in the Python code and the issue title in the YAML file. 

Closes #2459

**Relevance**

This contribution sets up a CI job for a repository for a course in DevOps.
