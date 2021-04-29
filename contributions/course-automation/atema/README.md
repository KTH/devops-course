# Course automation: Checking essay requirements

## Members

Martijn Atema (atema@kth.se)
GitHub: [Atema](https://github.com/Atema)

## Proposal

I want to create a GitHub action (on pull requests) that automatically checks whether the word count and plagarism are within defined boundaries.

In order, this action should:

- Determine if the pull request concerns an essay submission
- Find the submitted pdf file
- Check the word count within the file
- Submit the file to a plagiarism check service
- Report the status on the PR
