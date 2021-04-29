# GitHub action to show what is available for feedback 

This submission corresponds to the following PR #1306. We now have a new member!

## Member 

Hilaire Bouaddi, bouaddi@kth.se [https://github.com/Hilaire-Bouaddi]

[NEW MEMBER] Kun Wu, kunwu@kth.se [https://github.com/Wkkkkk]

## Rationale 

It takes some minutes to check if a contribution we are interested in will receive feedback or not. This can generate frustration.
The aim of the proposal is to automate the labelization of PR to mark the ones that can be feedbacked. 

## The finished contribution 

This work resulted in a new workflow for the DevOps repository. This workflow named label.yml is in charge of labelling merged PRs.
This is the implemented behavior:
```
every time a push occures (including merge) to the 2021 branch / every time that a PR is created for the branch 2021:
    delete labels 'feedbacked', 'feedbacked claimed', 'feedbackable' from every PR
    add the label 'feedbacked' to all the valid PRs* that are referenced in a markdown file of the contributions/feedback folder
    add the label 'feedback claimed' to all the valid PRs* that are referenced in the body of open PRs
    add the label 'feedbackable' to all the other valid PRs*
```
*PRs that have the labels 'proposal' and either 'essay' or 'tutorial'.

Those are the following assumptions: 
* Every merged PR for a proposal of a contribution in an essay or an executable tutorial will get the labels 'proposal' and either 'essay' or 'tutorial'.
* Feedbacks have to mention both in their readme and in the body of the feedback PR the id of the PR of the contribution proposal that they want to feedback. 

Considering the number of students in the course, the script will make mistakes. Those mistakes will generally consist of setting the label to 'feedbackable' to merged PRs even if they will receive feedback because the feedback readme doesn't mention that PR. 

|                                             | Yes | No | Remarkable  |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes | :white_check_mark: No | n-a|
|The automation task produces a PR status or issue / PR comment | :white_check_mark: Yes | No | Points to a generated page with valuable additional information |
|The automation task is reusable | :white_check_mark: Yes (next year for this course) | No | In other courses than this one |
|The task runs on a standard platform | :white_check_mark: Yes (Github action) | No | Other platforms (e.g. Moodle, Canvas) |
|The task is praised by the other students of this course | Yes | No | n-a |
|The code for the task is available | :white_check_mark: Yes (public repo) | No | Well documented repo |