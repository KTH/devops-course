# Tutorial: How To Build Your Own Github Action
**Team members:**

- Keivan Matinzadeh keivanm@kth.se @keivanm
- Alexander Volminger alevol@kth.se @Volminger

**Topic:**
Github Actions: CI for Java with Maven

Github actions is a relatively new way of creating a workflows for your development cycle and it is gaining in popularity, especially since it has become a free feature for public repositories. It can be used to create CI/CD pipelines for a lot of different languages and infrastructure setups. Searching on the web we noticed that there are a lot of tutorialS about how to setup GitHub action that other people have built. But a lack of tutorials about how to build your own GitHub actions, and the ones that we found were quite basic. We would therefore like to make a tutorial explaining how to build a more complex CI GitHub action for Java with Maven.

We aim to lift GitHub Actions features such as:
- Using [secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) in your actions and storing them in a secure way in your repository
- Use of [environment variables](https://help.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables) in GitHub actions
- Use a [service container](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-postgresql-service-containers) in our GitHub action to run integration tests against our [Java application](https://help.github.com/en/actions/language-and-framework-guides/building-and-testing-java-with-maven). 
