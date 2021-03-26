# Course automation: Post metadata information for demo links

## Members

William Skagerström (wska@kth.se) (@wska)
Alexander Kruger (alekru@kth.se) (@thestar19)
## Proposal

We would like to propose a task that will parse and links to demo-showcases and publishes metadata-information about the video in a short table-summary. We are thinking of making initially making it work with youtube and its API, but if a correponding API solution exists for Vimeo we may include that aswell.


This will thus be a bot that:
* Parses updates in the demo section.
* Looks for updates to the link section in the readme (such as a youtube.com link).
* Takes the link and queries relevant APIs for metadata information.
* Summarizes the data in a table and posts it back to the issue. Could also update tags if neccesary. 
