# Video demo: Publishing a Java package to Maven Central using Github Actions

## Members

Axel Pettersson (axp@kth.se)
GitHub: [Ackuq](https://github.com/Ackuq)

Felix Seifert (fseifert@kth.se)
Github: [felix-seifert](https://github.com/felix-seifert)

## Description

In this demo we show how to create a simple Java package and deploying it to Maven Central for distribution using Github Actions.

We go through all of the configuration needed to make this possible, which includes configuring the `pom.xml` file, setting up GitHub secrets, and of course the GitHub Actions workflow.

The action will:

-   run when commits are pushed to main branch
-   execute tests on the code to be published
-   update the version of the artifact to be published
-   authenticate with Maven Central
-   use encrypted Github Secrets to securely handle authentication

## Why it matters to DevOps

Manually deploying new versions of software is both error prone and tedious, and also comes with a lot of extra work. By automating this process using CD (Continuos Deployment / Delivery) you can reliably publish new versions of your software, resulting in happier teams and customers.

## Video link

https://www.youtube.com/watch?v=8tLAKABP5ns

Subtitles for the video can be activated natively with the YouTube player.

## GitHub repository

https://github.com/Ackuq/maven-gh-deploy

## Easter egg hint

<details> 
  <summary>Click me for hint</summary>
  Do you realise how fast the cache can run?
</details>
