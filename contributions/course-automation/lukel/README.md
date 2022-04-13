# Assignment Proposal

## Title

Add a shell script (`mpr`, for "make pull request") which when invoked from CLI creates a new PR for students to the
devops course repository. This script will live in a new directory (`/scripts`) in the root of the devops repo.

## Names and KTH ID

- Luke LeVasseur (lukel@kth.se)

## Deadline

Task 2: April 19, 17h Stockholm time

## Category

Course automation

## Description

`mpr` will simplify the PR creation flow for students. This shell script will incorporate pushing the most recent commit
to its remote branch in the forked repo copy, opening a new PR in the devops repo, and applying the template PR
Description.

Students will be able to run `mpr` from their command line, which will prompt them for a PR title. After they write the
title and hit enter, the script will run some git commands and open up the "create pull request" web UI with the
template for the title auto-filled based on the CLI input. Students will still need to update the description of the PR
with details from their readme, but this will simplify the PR creation process for students (
currently `local commit, remote push, edit PR through git web UI, input title and desc, create pr`, will
be `local commit, mpr, input desc, create pr`)

Additionally, I could see this automation contribution as a first step in a new class of shell scripts designed to
automate student workflows. For example, I regularly use a `rebase`
alias (`git stash && git checkout origin/master && git pull && git checkout - && git rebase origin/master && git stash pop`)
which could also be valuable to student workflows within the devops repo.

Submission:
Shell Script URL in Standalone Repository: https://github.com/luuuk/devops-course/blob/2022/scripts/mpr.sh
