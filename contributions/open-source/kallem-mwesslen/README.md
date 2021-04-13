# Open-source contribution proposal: Contributor Scoreboard
## Members
Kalle Meurman (kallem@kth.se) Github: Wizkas0

Markus Wesslen (mwesslen@kth.se) Github: m4reko

## Proposal
We would like to create an open-source project from scratch. Our idea is to create a github action/ workflow, 
that scores contributors to a repository based on user-defined rulesets. Our action will build and update a scorboard based on
output from user defined actions. For instance, if a repo wants to score its users based on uploading working code, our action
would be run using the output of a CI-server action. The point of this is to encourage good practices in contributors, 
which would improve workflow.



We will implement the scoreboard functionality in our main action, as well as an example integrating action, 
which scores commits based on word count. The word count is a simplified measure of the usefulness of a commit message.

We believe that this project is suitable for the open-source category, as it is not generally useful for the course-repo, 
but could be useful for many different projects.

