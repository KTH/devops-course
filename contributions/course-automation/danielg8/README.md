# Assignment Proposal

## Title

*Automatic labeling of PRs*

## Names and KTH ID

- Daniel Gustafsson (danielg8@kth.se) 

## Deadline

Task 1

## Category

Course automation

## Description

Currently all pull requests needs to be manually labeled by the course TAs.
Because this is tedious to do, some pull requests don't get labeled and are therefore harder to sort or search for.

I want to solve this by creating a GitHub Action that searches for keywords in pull requests and labels the pull request accordingly.

**Final Submission**

This is implemented as a GitHub Action in [this repository](https://github.com/halvtomat/KTH-DevOps-AutoLabeller)

To demo the functionality, 4 pull requests from the original devops-course repo has been copied (without names and email) to the repo and labeled by the bot.
