# Tutorial: How To Build Your Own Github Action
**Team members:**

- Keivan Matinzadeh keivanm@kth.se @keivanm
- Alexander Volminger alevol@kth.se @Volminger

**Topic:**
Github Actions: CI for Java with Maven

Github actions is a relatively new way of creating a workflows for your development cycle and it is gaining in popularity, especially now since it has become a free feature for public repositories. It can be used to create CI/CD pipelines for a lot of different languages and infrastructure setups. Searching on the web we noticed that there are tutorialS about how use setup GitHub action that other people have built. But a lack of tutorials about how to build your own GitHub actions, and the ones that we found were quite basic. We would therefore like to make a tutorial explaining how to build a more complex CI GitHub action for Java with Maven.
We aim to lift GitHub Actions features such as:
-  Using secrets in your actions and storing them in a secure way in your repository
- Use of environment variables in GitHub actions
- Use a service container in our GitHub action to run integration tests against our Java application. 
