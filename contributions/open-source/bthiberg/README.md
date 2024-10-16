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

Concerns issue #2459 in this repo.

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

Updating for newer years should only require changing the lecture dates and issue number in the JSON config file.

**Relevance**

This contribution would set up a CI job for a repository for a course in DevOps. Highly relevant!
