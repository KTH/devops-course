# Tutorial:  CI/CD for Java Maven using GitHub Actions
**Team members:**

- Keivan Matinzadeh keivanm@kth.se @keivanm
- Alexander Volminger alevol@kth.se @Volminger

**Topic:**
Github Actions: CI for Java with Maven

GitHub Actions is an exciting new feature that have the potential to replace a lot of your previous development pipelines. Say you want to send build status messages to through Slack? Or implement a whole CI/CD solution? GitHub Actions can do all of this, with everything still being inside your repository.

This tutorial will show you how to set up a CI/CD solution for a Java Maven project. The tutorial will start of with a simple GitHub Action that builds the Maven project and displays the result. More advanced topics will be gradually explored; such as the use of secrets in GitHub Actions and running integration tests against an external service. By the end of this tutorial you should have a GitHub Action that publish your tested Java application as a container image at Docker Hub.

We aim to lift GitHub Actions features such as:
- Using [secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) in your actions and storing them in a secure way in your repository
- Use of [environment variables](https://help.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables) in GitHub actions
- Use a [service container](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-postgresql-service-containers) in our GitHub action to run integration tests against our [Java application](https://help.github.com/en/actions/language-and-framework-guides/building-and-testing-java-with-maven). 


Link to tutorial: https://medium.com/@alexander.volminger/ci-cd-for-java-maven-using-github-actions-d009a7cb4b8f


## Grading Criteria
For the easter egg look inside the Java code, try running. If you need to take a look at https://hitchhikers.fandom.com/wiki/Deep_Thought

We also hope to fullfill that the tutorial is doable in the browser without a local environment, since it is possible to do all tasks in the GitHub web interface.
