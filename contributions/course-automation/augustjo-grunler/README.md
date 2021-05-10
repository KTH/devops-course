# Course automation: Check Feedback Requirements

## Members
August Jönsson: 

Github: Augustjon  
KTH.se: augustjo

Daniel Grünler:

Github: Grunler  
KTH.se: grunler

## Proposal:
We plan on making a Github action that automates part of the evaluation for the feedback task. 
This will include checks to see that the feedback exceeds the minimum word limit of 500 words, that it meets deadline requirements and that there are pointers to additional material.
We will also implement the possible checks for a remarkable submission, such as the feedback surpassing 1000 words or being submitted within 24 hours.

## Submission

We have created a [Github Action](https://github.com/Augustjon/Feedbackcheck-action) that can be used to automate some part of the evaluation of the feedback task. When people in the course give feedback to their fellow students, that feedback has to pass certain requirements. We have focused on 2 of these requirements: 
1. The feedback is substantiated meaning that the word count is at least 500 words, and if the word count is above 1000 then the feedback is considered remarkable. The Github Action uses input variables so that the limits can be modified in future course offerings as required. 
2. The feedback should be submited 4 days before the submission deadline of the task. As this deadline might also be subject to change in future course offerings we decided to let the course administration set the deadline for the **feedback** as an input to the Github Action.

## Action location

Repo: https://github.com/Augustjon/Feedbackcheck-action

Marketplace: https://github.com/marketplace/actions/check-feedback

## Usage
### Inputs
The inputs of the actions are:
| Name                | Description                                                                                                    | Required |
|---------------------|----------------------------------------------------------------------------------------------------------------|----------|
| repo-token          | The token is necessary in order to create comments on the PR and get access to data from github                | True     |
| minimal-wordcount   | The minimal wordcount required to pass the check                                                               | True     |
| remakarble-wordcount| The word count limit for remarkable feedback                                                                   | True     |
| deadline            | The deadline of the feedback task. The format of the deadline should be in ISO8601                             | True     |


###  Example workflow file
To use the action you may create a file in your project (example `.github/workflows/feedbackcheck.yml`) and include these lines of code.
````yml
name: Feedback-check
on:
  pull_request:
    paths:
      - '**/feedback/**/README.md'
jobs:
  action:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: check feedback
      id: feedback
      uses: Augustjon/Feedbackcheck-action@v1
      with:
        repo-token: ${{secrets.GITHUB_TOKEN}}
        minimal-wordcount: 500
        remarkable-wordcount: 1000
        deadline: '2021-04-27T23:59Z'
````

The yaml might be changed to trigger the action on other events or to specify certain branches or paths.

### Course-specific
The action triggers on a PR when the files that are modified matches this path in the devops structure `**/feedback/**/README.md`. 
This means that if someone adds their feedback in the README (which they should) of their folder in the feedback folder, this action will trigger and check the requirements. After the feedback is checked by the action the action will produce a pr comment on the person submiting feedback's PR stating whether the feedback is sufficient or not.

