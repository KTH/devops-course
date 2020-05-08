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

Screencast: [CI/CD Pipeline with GitHub, Travis-CI and Heroku](https://www.youtube.com/watch?v=Wj4VUcCAink&fbclid=IwAR0Ek4q_CeogVzsz5v_F0TsIYZ6MRP5wnzE2ND9LXgQpFYQrOpy6lbCf_Rc)  
GitHub Repo: [Demo app](https://github.com/AristotelisKotsias/dd2482-DevOpsDemo)