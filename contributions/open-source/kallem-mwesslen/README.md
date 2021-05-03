# Open-source contribution proposal: Contributor Scoreboard
## Members
Kalle Meurman (kallem@kth.se) Github: [Wizkas0](https://github.com/Wizkas0)

Markus Wesslen (mwesslen@kth.se) Github: [m4reko](https://github.com/m4reko)

## Proposal
We would like to create an open-source project from scratch. Our idea is to create a Github action/workflow,
that scores contributors to a repository based on user-defined rulesets. Our action will build and update a scoreboard based on
output from other user defined, integrating actions. For instance, if a repo wants to score its users based on uploading working code, our action
could be run using the output of a CI-server action. The point of this is to encourage good practices in contributors,
which would improve workflow.

We will implement the scoreboard functionality in our main action, as well as an example integrating action,
which scores commits based on word count of their messages. The word count is a simplified measure of the usefulness of a commit message.

To enable others to create integrating actions, our scoreboard action will have a simple, well defined API.

We believe that this project is suitable for the open-source category, as it is not generally useful for the course-repo,
but could be useful for many different projects.

## Execution
Our open source project can be found [here](https://github.com/Wizkas0/repo-score).
