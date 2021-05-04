# GitHub action to show what is available for feedback 

This submission corresponds to the following PR #1306. We now have a new member!

## Member 

Hilaire Bouaddi, bouaddi@kth.se [https://github.com/Hilaire-Bouaddi]

[NEW MEMBER] Kun Wu, kunwu@kth.se [https://github.com/Wkkkkk]

## Rationale 

It takes some minutes to check if a contribution we are interested in will receive feedback or not. This can generate frustration.
The aim of the proposal is to automate the labelization of PR to mark the ones that can be feedbacked. 

## The finished contribution 

Link to the workflow: https://github.com/Hilaire-Bouaddi/devops-course/blob/2022/.github/workflows/label-feedbackable.yml 

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

## The demonstration repository 

You can see the result of the workflow on this repository (forked from the course): https://github.com/Hilaire-Bouaddi/devops-course/pulls?q=is%3Apr+is%3Aclosed 

The branch used for the demonstration is the 2022 branch.

Let's look closely on the Pull Requests #11, #12 and #13. Those Pull Requests are propositions to contribute either in Executable Tutorial or Essay. This work makes the hypothesis that this kind of pull requests will both have the label "proposal" and the label "tutorial"/"essay". We can also see that the feedback contribution #14 has been merged. In the readme of the feedback, #11 is mentioned. This is why the workflow will mark #11 as "feedbacked". 

Then, we can see on the repo that a PR is open. This PR references #12 in its body. This is why the PR#12 is marked as "feedback claimed". 

Finally, the PR #13 is neither mentioned in a PR body nor in a readme, it is then "feedbackable".