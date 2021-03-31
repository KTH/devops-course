# Executable tutorial: Secure an API endpoint using Keycloak running in Docker
 
## Members
- [Dina Lerjevik](https://github.com/dmariel) (lerjevik@kth.se)
- [William Skagerström](https://github.com/wska) (wska@kth.se)

## Proposal
We would like to publish a tutorial on how to secure an API endpoint using Keycloak running in Docker and hosting it on Katacoda. 

The aim of our tutorial is to:

* Provide and explain a simple API (likely a basic API using Python and Flask)
* Educate about security, Oauth2, OpenID Connect and Keycloak
* Showcase how to set up Keycloak and host it using Docker
* Go through how to set up a realm and add users with different levels of security clearance
* Use the existing Keycloak realm to secure the previously introduced API, which will now require access tokens and the relevant security clearance
 
We found an existing tutorial on Katacoda on this topic, however we believe that this tutorial was very basic since it merely only covers how to obtain an access token and using it for an request, which is only a few steps of the whole process. 