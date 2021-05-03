# GitHub action to show what is available for feedback 

## Member

Hilaire Bouaddi, bouaddi@kth.se [https://github.com/Hilaire-Bouaddi]

## Rationale 

It takes some minutes to check if a contribution we are interested in will receive feedback or not. This can generate frustration.
The aim of the proposal is to automate the labelization of PR to mark the ones that can be feedbacked. 

## Proposal

I would like to try to create a GitHub Action. This action would:
- get the URL of every merged PR for contributions in either essay or executable tutorial. 
- for every URL 
  - if the URL is referenced in a contribution for feedback, put the label "feedbacked" to the PR, delete other labels "feedbackable" and "feedback claimed"
  - else if the URL is referenced in a feedback PR that waits to be merged, put the label "feedback claimed" to the PR, delete other labels "feedbackable" and "feedbacked"
  - else put the label "feedbackable" to the PR, delete other labels "feedback claimed" and "feedbacked"

### Legend 
* "feedbackable": nobody claimed the feedback for this task yet
* "feedback claimed": a PR is waiting to be merged for the feedback of this contribution
* "feedbacked": the feedback for this contribution has been claimed
