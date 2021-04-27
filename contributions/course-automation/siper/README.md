# Course automation: Automatic validation and labeling

## Members

Simon Persson (siper@kth.se)
GitHub: altaired


## Submission

The action can be found at [https://github.com/altaired/devops-label](https://github.com/altaired/devops-label). The code is documented, tested and more information can be found in the repository itself.

The action does the following:
* Checks that only a single category is modified on each checked PR
* Checks that only a single folder in that category is modified
* That the naming structure of the authors folder holds, e.g 'name1-name2'
* If the PR is a proposal or not and assign a label if it is a proposal
* Fetches statistics of all pull requests with the proposal label and updates a provided issue with stats

In order to include the action in this repository, all details can be found in the repository above. A suggested configuration file is included in this directory as well (see [here](/contributions/course-automation/siper/config.yml)), the issue number has to be set though. Simply create an issue with an appropriate title and add the issue number in the configuration file where it currently says `<ISSUE_NUMBER>`. The version to use of this action is the latest (currently @v1.3).

Below is an example of how to use the action.
```
name: Validate and label PR
  id: vlpr
  uses: altaired/devops-label@v1.3
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    configuration-path: .github/config.yml
```

I recomend triggering it on each pull request, even if this does not update the stats when a PR is merged. As pull requests are made and updated regularly this should not be a problem.






