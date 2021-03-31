# Course automation: Verify pull request content changes

## Members

Ralfs Zangis (zangis@kth.se)
GitHub: https://github.com/bubriks

## Proposal
Ensuring that pull requests can be approved only if the formatting requirements are met. 

## Description
- Check changed .md file contents (contains: task name, members, and description)
- Verify that the member names (from README.md) are represented in the containing folder name
- Confirm that file structure follows the rules (no changes outside members folder in the selected category)
- Inform user if any checks have failed (for more details on what has failed check build)

-------------------------------
Code testing validity of markdown files and the change location is run only on pull-requests.

Example markdown file provided in EXAMPLE_README.md
Based on the example markdown file its containing directory should be: course-automation/bar-lastname/ (members folder last names can be in other orders, but both must be present)