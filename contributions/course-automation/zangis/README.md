# Course automation: Verify pull request content changes

## Members

Name: Ralfs Zangis Zangis
Email: zangis@kth.se
GitHub: https://github.com/bubriks

## Proposal
Ensuring that pull request can be approved only if the formatting requirements are met. 

## Description
- Check changed .md file contents (contains: task name, members, and description)
- Verify that the member names (from README.md) are represented in the containing folder name
- Confirm that file structure follows the rules (no changes outside members folder in the selected category)
- Disallow pull request approval if any checks have failed

-------------------------------
Example markdown file provided in: EXAMPLE_README.md
Based on example markdown file it should be saved in: course-automation/bar-lastname/ (members folder last names can be in other orders, but both must be present)