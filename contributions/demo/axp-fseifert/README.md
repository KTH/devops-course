# Video demo: Publishing a Java package to Maven Central using Github Actions

## Members

Axel Pettersson (axp@kth.se)
GitHub: [Ackuq](https://github.com/Ackuq)

Felix Seifert (fseifert@kth.se)
Github: [felix-seifert](https://github.com/felix-seifert)

## Proposal

In this demo we will show how to create a simple Java package and deploying it to Maven Central for distribution using Github Actions.

The action will:

-   run when commits are pushed to main branch
-   update the version of the artifact to be published
-   authenticate with Maven Central
-   use encrypted Github Secrets to securely handle authentication
