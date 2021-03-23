# Course automation: Checking link validity to slides for all presentations

## Members

Ralfs Zangis (zangis@kth.se)
GitHub: [Ralfs](https://github.com/bubriks)

## Proposal
My wish is to resolve the issue described in #916
With the task being: "Check that there is a valid link to the slides for all presentations."

## Proposed Solution
1. When creating/editing a pull request that is about presentation (for example PR name contains specific word)
2. Locate all URLs within the description
3. Verify their validity (can be accessible and possibly file is of a specific type: ppt, pptx, pdf, ...)
4. Display verification results on the pull request
