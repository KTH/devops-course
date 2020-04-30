# CI/CD tutorial using Github and Declarative Multibranch pipeline on Jenkins

## Contributors
George Rezkalla - rezkalla@kth.se @georgewbar

## Description

This is a `Katacoda` tutorial that goes in detail through how to create a `Multibranch pipeline` (using `Multibranch pipeline` plugin) on `Jenkins`. In particular, the following points are covered:

1. Background on DevOps, CI/CD, and Jenkins, and Jenkins `Multibranch pipeline`. Morover, information about the pre-requisites, the execution environment, and the sample `Java` app on the Github repo for this tutorial.
1. How to install Jenkins on Ubuntu 16.04 environment (on Katacoda).
1. How to create a Github organization and fork the repo that will be used for this tutorial.
1. How to create a `personal access token` on Github in order to use it in Jenkins so that Jenkins can change the commit status on Github.
1. How to configure the `Multibranch pipeline` on Jenkins to communicate with Github and create the `Multibranch pipeline` using the `Jenkinsfile` in the Github repo. Moreover, explanation of the `Declarative` syntax in the `Jenkinsfile` is explained. Moreover, the `Multibranch pipeline that is created` consists of `Build`, `Test` and `Deliver` stages together with how to archive test cases and use artifacts. Furthermore, `Docker` is used as the execution environment for the `Multibranch` pipeline.
1. How to configure a Github webhook on the Github repo to communicate with `Jenkins`. Also, how to configure branch rules for `master` branch on Github branch to only allow merging builds that pass on Jenkins and that are code reviewed by at least one person.
1. How to invite a collaborator with `Write` role to the Github repo.
1. How to clone the repo, introduce an error in the code and push to Github on another branch than master, and see `Jenkins` detect the push on Github on another branch. Also, how to create a `pull request` and see that the merging is blocked until all the conditions configured on Github are met. Moreover, an explanation of the different parts of the `Jenkins` GUI is provided.
1. How to fix the error again, push the repo again, and see that Jenkins passes. Then, how submit code review for the code, and then how to merge the pull request.
1. At last, some fun facts are provided at the end of the tutorial.

This tutorial is considered original because the background information and the steps of the tutorial itself did not exist in only one place. The information is spread across different places in all over the Internet. In particular, there is no one tutorial that tries to combine in one tutorial all information about how to configure different settings in Github and Jenkins using clear steps and illustrations/images (i.e. no tutorial explains in one place e.g. how to configure Github webhooks, how to configure collaboration rules on branches on Github, how to create `personal access token` on Github, and where to use this token in Jenkins, how to find the webhook URL of Jenkins, etc).

As a beginner in Jenkins, it took time for me to find and gather all this information and do a tutorial that combines all of these elements in an end-to-end CI/CD pipeline.

## Criteria I aim to fulfill

* The TA can successful execute all the commands of the tutorial (mandatory).
* The tutorial gives enough background.
* The tutorial is easy to follow.
* The tutorial is original, no such tutorial exists on the web.
* The tutorial contains fun facts or easter eggs.
* The tutorial is doable in the browser without a local environment (the tutorial is on https://www.katacoda.com/)

## Tutorial link on Katacoda

The link for this tutorial on Katacoda is [https://www.katacoda.com/georgerezkalla/scenarios/jenkins-multibranch-pipeline](https://www.katacoda.com/georgerezkalla/scenarios/jenkins-multibranch-pipeline).
