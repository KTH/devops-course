# Executable Tutorial: Setting up a Jenkins CI/CD pipeline for deploying to Docker Hub

In this tutorial you will learn how to setup a simple CI/CD pipeline in Jenkins. Jenkins will be configured to listen to pushes to a GitHub repository containing a node.js project. Jenkins will fetch the new code, run tests on it which if successful, will trigger Jenkins to build a docker image from the project and publish the image to Docker Hub.

Read the [tutorial here](https://christophergustafson.medium.com/creating-a-jenkins-ci-cd-pipeline-45bf747643b5). (Note: We were not able to have it show up as two authors in medium, so Christopher is currently the author and Fredrik is mentioned at the beginning of the article, as we both contributed to this project)


## Members

Christopher Gustafson (chrigu@kth.se)
Github: [ChristopherGustafson](https://github.com/ChristopherGustafson)

Fredrik Björkman (fbjorkma@kth.se)
Github: [fbjorkman](https://github.com/fbjorkman)

## Easter eggs

The tutorial contains two small easter eggs for you to find (these can only be found if you are using the [premade node project](https://github.com/ChristopherGustafson/tutorial-app) for the tutorial, and not your own).

<details> 
  <summary>Click here for some hints about where to find them.</summary>
    <ul>
        <li>What does these tests really check?</li>
        <li>What would happen if we typed "npm run starwars" as a third command in our CI configuration? (Check the logs of the last CI build afterwards)</li>
</details>
