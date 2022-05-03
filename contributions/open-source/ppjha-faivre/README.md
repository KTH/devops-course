# Assignment Proposal

## Title

Open source contribution on a [Lint Action](https://github.com/marketplace/actions/lint-action), an github action that shows linting errors and allows auto-fixing issues.

## Names and KTH ID
  - Philip Hamelink (ppjhad@kth.se)
  - Bastien Faivre (faivre@kth.se)
## Deadline

Task 2: April 19, 17h

## Category

Contribution to open-source

## Description

We want to add a feature mentioned in this [issue](https://github.com/wearerequired/lint-action/issues/426). Currently, this action allows to set 
auto-fixing linting errors for all linters. There has been a requested feature to only allow auto-fixing for certain linters, which we want to
add ourselves. The repo has 329 :star: and 509 commits. The community is quite active. The issue was requested 7 days ago, and the author responded and 
labeled the issue with "help_wanted" 2 days ago. 

We believe this satisfies the requirements for the open-source contribution assignment as linting code on commits is an invaluabe feature in DevOps.

Submission:

In our [pull request](https://github.com/wearerequired/lint-action/pull/439), we mention the issues we have had, and how we have come up with our final solution. We tested our new feature [here](https://github.com/phamelink/test-action-repo), where you can see the results from our action where we can specify which linters we want to automatically fix code issues.  

We believe we satisfy the following grading criteria:

|                                             | Yes | No | 
|-------------------------------------------- | ----|----|
|bug: The contribution fixes bugs | Yes :white_check_mark: | No | 
|documentation: The contribution improves documentation | Yes :white_check_mark: | No |
|feat: The contribution adds new features | Yes :white_check_mark: | No |
|difficulty: The contribution is a difficult piece of engineering | Yes :white_check_mark: | No | 
|conversation: There is an interesting engineering conversation with the maintainers | Yes | No | 
|merge: The contribution is merged in the main branch.| Yes | No | 

We believe we fixed a small bug. Before, when auto-fix was set, when linters did not support auto-fixing there was a warning that could not be prevented. This can now be avoided when the input <linter>_auto_fix is set to `false` for a non auto-fix supporting linter. 
  
We improved documentation by adding information about our new feature (since there are new inputs in our version), and we also added an example for our feature.
  
This contribution adds an obvious new feature as requested.
  
Finally, we believe that even though the final changes were minimal and quite simple, this contribution was quite challenging as we had to figure out exactly where and when we needed to add a condition. We went through many stages, most involving manipulations with git to avoid committing and pushing certain files as was tried [here](https://github.com/phamelink/lint-action/tree/implementation) or with this [script](https://github.com/phamelink/lint-action/blob/test-branch/t.sh), or even restore files to their original state done in this [commit](https://github.com/phamelink/lint-action/commit/1cd4c214d1daa2c129e0f04e988df579d4634e3f). 
