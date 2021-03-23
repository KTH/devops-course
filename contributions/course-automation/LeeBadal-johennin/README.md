# Automatic duplicate proposal detection
## Members
Lee Badal (badal@kth.se)

GitHub: [@LeeBadal](https://github.com/LeeBadal)

Johan Henning (johennin@kth.se)

GitHub [@johennin](https://github.com/johennin)

## Proposal
We plan to create a github action that validates that no previous/similar proposals have been made before.

To verify that the PR is a proposal we intend to test the folder structure or validate that a proposal label is assigned (if  https://github.com/KTH/devops-course/pull/949 is implemented)
We will then run a semantic analysis comparator to previous PR(Title and description) proposals and notify the user/TA's by writing a comment if they are above a certain threshold of similarity or if manual revision by a TA is required. (In this case the URLs to the similar PR will be provided)

## Proposed tools
 * Github Actions
 * [NLTK](https://www.nltk.org/)
