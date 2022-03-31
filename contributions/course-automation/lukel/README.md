# Assignment Proposal

## Title

Add a shell script (`mpr`, for "make pull request") which when invoked from CLI creates a new PR for students.

## Names and KTH ID

- Luke LeVasseur (lukel@kth.se)

## Deadline

Task 2: April 19, 17h Stockholm time

## Category

Course automation

## Description

`MPR` will simplify the PR creation flow for students. This shell command will incorporate pushing the most recent
commit to its remote branch in the forked repo copy, opening a new PR in the devops repo, and applying the template PR
Description.

Additionally, I could see this automation contribution as a first step in a new class of shell scripts designed to
automate student workflows. For example, I regularly use a `rebase`
alias (`git stash && git checkout origin/master && git pull && git checkout - && git rebase origin/master && git stash pop`)
which could also be valuable to student workflows within the devops repo.