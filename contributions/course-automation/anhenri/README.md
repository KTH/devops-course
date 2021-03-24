# Course automation: Checking Demo Video Link

## Member

Andreas Henriksson (anhenri@kth.se)
GitHub: [heeenkie](https://github.com/heeenkie)

## Proposal

I want to create a GitHub action (on pull requests) that automatically checks whether the youtube link to the demovideo exists and that it is valid.

In order, this action should:

- Determine if the pull request concerns an demo submission
- Find the submitted readme file
- Check that the link exists and is valid
- Report the status on the PR
