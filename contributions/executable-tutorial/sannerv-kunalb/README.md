# Assignment Proposal

## Title

Setting up Continous Testing and Integration using Gradle and Github Actions

## Names and KTH ID
- Filip Sannervik (sannerv@kth.se)
- Kunal Bhatnagar (kunalb@kth.se)

## Deadline

Task 1

## Category

Executable tutorial

## Description

Gradle is a build automation tool that is used in the development process with everything from compilation to testing and deployment. It can be used cross-language and is very versatile, it systemises the delivery of your software. Combining the test functionalities of Gradle with Github Actions we can setup a simple yet powerful CI/CD Pipeline

We will create a Katacoda tutorial which teaches the student how to setup this automated build environment through interactive steps.

***SUBMISSION***

We created an executable tutorial with Katacoda which teaches how to setup a Gradle project for build and test automation. It also teaches how to add unit and integration tests, and how to combine this with GitHub actions to create a CI/CD pipeline. It also explains the basics of how Maven can be combined with gradle to publish a Gradle artifact to a Maven repository.

It consists of the following parts:

* Introduction to Gradle
* Introduction to GitHub Actions
* Setting up a project with Gradle
* Adding unit and integration tests
* Setting up CI pipeline with GitHub actions
* Brief explanation of how Gradle can be combined with Maven to publish an artifact to a Maven repository

***SUBMISSION LINKS***

* [Link to Katacoda Tutorial](https://www.katacoda.com/filipsannervik/scenarios/ci-gradle-github)
* [Link to Katacoda Repo](https://github.com/ZerooCoool/katacoda-scenarios)

***Changelog***

* Step 1: Added why we chose Gradle and discussed alternatives
* Step 2: Added why we chose Github actions and discussed alternatives
* Step 3: New step added, so previous step 3 and above have now increased with one. This new step explains the difference between unit and integration testing and why both are neccessary.
* Step 6: Added more explaining text for the scripts provided.
* Step 7: Added more explainations, also clearified that we will not add the script and data to publish our Gradle artifact to a Maven repository, but explain how you could add this to the build file to show that Gradle can be used with other tools.
* Fixed grammar and spelling mistakes throughout the tutorial
