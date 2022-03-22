# Github action to check word count in submitted essays

## Member

Daniel Gustafsson, danielg8@kth.se [https://gtihub.com/halvtomat]

## Rationale

It is probably annoying for TAs to have to check the word count in each individual essay submisison. 

The goal of this proposal is to automate this task and make life easier for TAs.

## Proposal

Create a GitHub Action which does the following on all essay pull requests:

- Get changed/new pdf file

- Count the words in this changed/new pdf file

- Check if the word count is in the interval defined by environment variables


