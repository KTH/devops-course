# Course automation: Verify pull request content changes

## Members

Ralfs Zangis (zangis@kth.se)
GitHub: [Ralfs](https://github.com/bubriks)

## Proposal
Ensuring that pull request can be approved only if the formatting requirements are met. 

## Description
- Check changed .md file contents (contains: task name, members, and description)
- Verify that the member names (from README.md) are represented in the containing folder name
- Confirm that file structure follows the rules (no changes outside members folder in the selected category)
- Disallow pull request approval if any checks have failed