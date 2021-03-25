# Course automation: Automatic validation and labeling

## Members

Simon Persson (siper@kth.se)
GitHub: altaired


## Proposal

I plan to make a github action that automatially asigns labels depending on the category of the proposal and a "proposal" label (if it is a new proposal). The action should also validate the folder naming structure and that a README file is included properly. This would allow the TA's to easily filter out what PR:s to check.

In order to achive this, the following will have to be done:
* Validate the folder structure and README on each push
* Check on each PR what file / files has been modified, to determine what category the PR is related to. Also check if files that should't have been modified are  included and if that's the case, return an error to the user.
* Assign the appropriate labels
* Report back the status if the PR is following the required structure.
* Create a report showing statistics over the number of proposals.
