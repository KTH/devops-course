# Demo: CD of Node Express App on Google Cloud with designated release branch using GitHub actions

In this demo, we will demonstrate how to create a continuous deployment workflow using GitHub Actions that automate deployment of a simple Express server to Google App Engine (GAE), a fully managed, serverless platform for developing and hosting web applications at scale. We will go through the following:
1. How to create a project on Google Cloud
2. How to deploy the Express server to Google App Engine (GAE)
3. How to create a CD workflow to automate deployment using GitHub Actions

## Members

Kalle Pettersson (kalpet@kth.se)  
GitHub: [KallePettersson](https://github.com/KallePettersson)

Anders Nilsson (andnil5@kth.se)  
GitHub: [andnil5](https://github.com/andnil5)

## Screencast link
[YouTube link](https://www.youtube.com/watch?v=lY5Uj_VzClc).

## GitHub repository
[GitHub link](https://github.com/KallePettersson/Continous-Deployment-on-gCloud).

## Motivation

The motivation for why this demo matters to DevOps is twofold.
- It shows how to deploy an application on Google Cloud, which increases productivity and flexibility, frees up developers by taking away the demands of managing infrastructure, and provides automatic scaling.
- It demonstrates how to create a continuous deployment workflow using GitHub actions, one of DevOps' cornerstones.

## Take home message

Make sure to **NOT** commit your `gcloud_secret.json` file to GitHub. This could give malicious actors remote access to your Google Cloud account.

## Grading - We strive to meet the following grading criteria

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The demonstration is clearly motivated (why it matters for Devops?) | X |  | |
|The video is sublime (eg visually appealing) | X |  |  |
|There is a code repo to run the demo  | X |  | X |
|The video must contain subtitles which are clear and in proper English | X |  |  |
|The video includes a take-home message | X |  |  |
