# Assignment Proposal

## Title

Setup and use tools to improve your commit messages

## Names and KTH ID
  - Corentin Guilloteau (corgui@kth.se)

## Deadline

Task 3

## Category

Executable tutorial 

## Description

Writing good commit messages is very important in a team project, but it can be a hard task. This is why commit conventions exist in order to help developers. 
In the executable tutorial, I want to create a step-by-step tutorial on how to setup a good environment to enforce the use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) in a project.

If I have enough time, I could also describe how using a commit convention can be useful in a CI/CD pipeline for automatic changelog and version number generation for example.

I plan to use [Husky](https://github.com/typicode/husky) to handle hooks, [commitlint](https://github.com/conventional-changelog/commitlint#config) and [commitizen](https://github.com/commitizen/cz-cli) to enforce conventional commit and [standard-version](https://github.com/conventional-changelog/standard-version) for automatic changelog generation.
