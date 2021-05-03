# Course-automation: Automatic labels

## Members

Kalle Meurman (kallem@kth.se)
GitHub: [Kalle](https://github.com/Wizkas0)

Måns Andersson (manande@kth.se)
GitHub: [Måns](https://github.com/mansand1)

## Proposal
Action that automatically adds labels to issues, pull-requests, etc. based on keywords in message.

Original proposal pull request: https://github.com/KTH/devops-course/pull/932

# Submission
We have created our own Github action that adds labels to a pull request based on 
keywords within the title of the pull request. The code is available publicly at
https://github.com/Wizkas0/PR-LabelGenerator. In the repo both the code and 
documentation (README) can be found.

The keywords and corresponding labels to be added are specified in the workflow .yml file
as a JSON object. As a part of this pull request we have added the file `./github/workflows/label-generator.yml`.
If this pull request gets merged the action will hopefully become functional instantly and 
start adding labels to pull requests.

Here are the suggestions for keyword/label pairs that we think are reasonable based on 
the labels that are already used in the course:

```
{
"presentation":"presentation",
"essay":"essay",
"demo":"demo",
"executable tutorial":"tutorial",
"open-source contribution":"contribution_to_open_source",
"contribution to open-source":"contribution_to_open_source",
"course automation":"course_automation",
"feedback":"feedback",
"proposal":"proposal",
"submission":"final_submission"
}
```

For example this would mean that if the PR title contains the phrase "course automation"
the label `course_automation` will be added. We will gladly take suggestions for changing the
keywords/labels and adding additional labels.

### Grading
According to our own assessment, we have satisfied four criteria and two of those at a remarkable level.
|  Criteria                                 | Yes | No | Remarkable  |Motivation|
|-------------------------------------------- | ----|----|-------------|-------------|
|The automation task produces a PR status or issue / PR comment | `Yes` | | | When the action is run, the targeted pull request receives a `pending` status, and when the job is completed, it receives a `successful` status. If any labels are added by the action, this shows up in the pull request as `github-actions[bot] added the <something> label` . |
|The automation task is reusable | `Yes (next year for this course)` |  | `In other courses than this one` | Our action can be reused in both this course and others (and unrelated projects) by simply editing the `keyword-dict` input in the workflow .yml file to include the appropriate key-words/phrases and labels for the course/ course-run. |
|The task runs on a standard platform | `Yes (Github action)` | |  | Our action is a Github action.|
|The code for the task is available | `Yes (public repo)` | | `Well documented repo` | Our source code is a available at https://github.com/Wizkas0/PR-LabelGenerator and the action is available on the Github marketplace at https://github.com/marketplace/actions/pr-labelgenerator with thorough instructions for how to implement it. The source code is also well documented.|
