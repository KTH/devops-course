# Demo submission: Automated development pipeline for Chrome extensions

## Members:

Andreas Kärrby (karrby@kth.se)
Github: [andreaskth](https://github.com/andreaskth)

Henrik Kultala (kultala@kth.se)
Github: [hengque](https://github.com/hengque)

## Proposal/motivation

Original proposal PR is #1076 

## Submission

The video demo can be found at: https://www.youtube.com/watch?v=SKJYKNKyaqI  
**EDIT:** New video demo (after feedback) can be found at: https://www.youtube.com/watch?v=sTF_A4SPsh0

## What we did

- Created a Chrome extension that spawns easter eggs on websites, and lets the user collect these eggs ([available here](https://chrome.google.com/webstore/detail/easter-eggstension/lkeplkoegchdobbdodnocghcikijbnfm?hl=en)).
- Created a video demo showcasing an automated CI/CD pipeline for developing extensions for Google Chrome.
  - Work is done in feature branches, and tests are automatically run on commits.
  - Feature branches are merged into the dev-branch, representing an "unofficial" version of the extension, available to trusted testers. Tests are run on PRs to this branch.
  - For official releases (that appear for everyone), the dev-branch is merged into the main-branch.
- Subtitles are available (have to be manually activated by the viewer)
- Sources for all images are disclosed throughout the video, and in the video description.

## Grading criteria we are aiming for

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The demonstration is clearly motivated (why it matters for Devops?) | Yes 🐰 | No | Relates to a hard problem |
|The demonstration is difficult to do | Yes 🐣 | No | Relies on a non trivial infrastructure |
|The demonstration is original | Yes | No | The are less than 10 demos on the topic on Internet 🌷 |
|The video is sublime (eg visually appealing) | Yes | No | Excellent narrative 🐰 |
|The video contains an [easter egg](https://github.com/OrkoHunter/python-easter-eggs) | Yes | No | Related to the demo 🐣 |
|There is a code repo to run the demo  | Yes | No | Code repo with a solid readme |
|The video must contain subtitles which are clear and in proper English | Yes | No | Clearly understandable voice over 🌷 |
|The video includes a take-home message | Yes | No | Actionable takeaway 🐰 |
