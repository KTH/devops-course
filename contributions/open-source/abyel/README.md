# Assignment Proposal

## Title

Open-source contribution to Mergify software bot, adding action to revert changes

## Names and KTH ID

- Abyel Tesfay (abyel@kth.se)

## Deadline

Task 5

## Category

Contribution to open-source

## Description

[Mergify](https://github.com/Mergifyio/mergify-engine) is an automation tool that automates pull requests actions e.g. merging. The repository would benefit DevOps as it can be used to 
automate manual work that is often required when handling each pull request. A common example is merging a PR if enough 
reviewers have approved it and the PR passes all CI checks. The project has an active community with 272 stars and over 4000 commits.

The authors have expressed their wish for an action that reverts commits in pull requests, i will contribute to this by adding a file which handles the _revert_ action
in their directory of actions. This will contribute to a growing number of actions the tool can perform and hopefully a way for deveopers to automate reverts to 
e.g previous stable commits.
