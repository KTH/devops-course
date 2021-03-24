# Course automation: Verify pull request content changes

## Members

Ralfs Zangis (zangis@kth.se)
GitHub: [Ralfs](https://github.com/bubriks)

## Proposal
Ensuring that pull request can be approved only if the formatting requirements are met. 
For example: files and folders follow correct naming schema and the contents of .md files contain the necessary information, such as task name, members (who correspond to folder name), and description

## Description
1. When creating/editing a pull request tests are run
2. Check changed .md file contents
3. Verify that the member names are represented in the containing name
4. Confirm that file structure follows the rules (no changes outside permitted folders: 7 task categories)
5. Disallow pull request approval if any checks failed
