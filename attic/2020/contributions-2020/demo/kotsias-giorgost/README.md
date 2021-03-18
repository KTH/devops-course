# Demo proposal

## Members
Aristotelis-Antonios Kotsias (kotsias@kth.se)  
Georgios Tagkoulis (giorgost@kth.se)

## Description
In the demo, we would like to demonstrate the full pipeline of CI/CD for a minimal application.
The idea is to have a client-server application using NodeJS/React, version controlled by git and 
hosted in GitHub. It will follow the GitHub flow, and it will be connected with Travis-CI. 
For every push to the remote repository, all tests will run (using the Mocha test framework) but only
when the pull requests will be merged to the master branch, the application will be deployed in Heroku.
The server, will have production, development and test mode (if possible).

Screencast: [CI/CD Pipeline with GitHub, Travis-CI and Heroku](https://www.youtube.com/watch?v=8RSjgaFlGc0&feature=youtu.be&fbclid=IwAR2wi50u_-U5JC3shF-Ol3PlfsMLSKmbPuenrHPdRrqlrsCEIPfdDXWsllk)  
GitHub Repo: [Demo app](https://github.com/AristotelisKotsias/dd2482-DevOpsDemo)