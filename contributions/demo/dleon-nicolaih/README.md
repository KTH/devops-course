# Demo
Screencast link: https://youtu.be/F1jmOZOFCLI

Repository: https://github.com/dieflo4711/devops_demo

## Members
Diego Leon (dleon@kth.se)
Nicolai Hellesnes (nicolaih@kth.se)

## Description
The demo is based on our CI/CD pipeline which uses a proof of concept web application which can perform division. This application was deployed in a Kubernetes cluster running on Google Kubernetes Engine. 

The pipeline starts when the developer pushes code to GitHub. Each commit automatically triggers a Travis-CI build which checks that the code successfully compiles and that all tests pass (there is one unit test for the division function). Once all the requirements are fulfilled, Travis-CI builds a new docker image and pushes it to Docker Hub. Travis-CI notifies Kubernetes, through Google Cloud SDK, of the new docker image available for deployment. Kubernetes then pulls the new image from Docker Hub. Lastly, Kubernetes deploys and manages the docker container.

![pipeline](https://media.discordapp.net/attachments/689574194035687474/702564112311517344/pipe.jpg)

## Motivation
CI/CD are important parts of DevOps. They bring automation, from integration and testing phases to delivery and deployment. Together they form the "CI/CD pipeline".

## Easter egg
Since the application is used for division, something interesting happens when the user divides a number by zero. The easter egg is presented at the end of the screencast.

