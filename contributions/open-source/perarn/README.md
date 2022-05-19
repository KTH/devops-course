# Assignment Proposal

## Title

Contributing to [gosec](https://github.com/securego/gosec) - a Golang Security Checker

## Names and KTH ID
  - Per Arn (perarn@kth.se)

## Deadline

Task 4

## Category

Contribution to open-source

### Description
The [gosec](https://github.com/securego/gosec) repository hosts a neat program which analyzes Golang code for known security vulnerabilites.
It scans the GO AST to inspect the source code for issues.

As of writing this, the repo has 6.1k stars, 101 contributors, 759 commits and issues and PRs seem to come up quite frequently.

The reason for me choosing this repo is due to my [previous contribution](https://github.com/securego/gosec/commit/ea5d31f7f5cd942dbc4c9cdad74c2c1d1eab1ed2) to this project,
where I've had my contributions merged to the repo. I find security very interesting and
seeing how this would be part of DevSecOps, it made sense to me to pick this repo.

I went through the different issues posted and saw one that I thought was interesting, [link here](https://github.com/securego/gosec/issues/598). The issue describes a feature that some user would want to have implemented, where it is possible for the user
to write the log from checking source code to different files and different formats.
It had the labels "help-wanted" and "enhancement" so I figured I'd give it a go. There had been
prior discussion on how the feature should be implemented which I intend to follow.

**EDIT AFTER PROPOSAL HAS BEEN MERGED INTO DEVOPS 2022 BRANCH:**

I've written a piece of code which handles what the issue was describing - I added a flag which
if enabled, converts the JSON output to any other format such as text or yaml.

The [PR](https://github.com/securego/gosec/pull/814) has yet to be merged but I expect it to be sooner or later
since I've had previous PR's there merged.

In my opinion, my contributions fulfills the following devops Open Source criteria:
* Documentation - I've edited the README to properly describe the new feature, and I added code documentation where needed.
* Feat - the contribution adds a new feature - I've added a feature that a user asked for.
* Difficulty - although my code is not a difficult piece of engineering, understanding the code base was a mess
and took far longer than I care to admit.

I expect to have the PR merged, but it is not as of writing this.
