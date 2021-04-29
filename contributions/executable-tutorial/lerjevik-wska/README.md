# Executable tutorial: Secure a Python Flask app using Keycloak running in Docker
 
## Members
- [Dina Lerjevik](https://github.com/dmariel) (lerjevik@kth.se)
- [William Skagerström](https://github.com/wska) (wska@kth.se)

## Submission

**The tutorial is available [here](https://www.katacoda.com/wska/scenarios/add-login-to-python-flask-app-using-keycloak).** </br>
**The repository is available [here](https://github.com/wska/katacoda-scenarios/tree/main/add-login-to-python-flask-app-using-keycloak).**

The tutorial demonstrates how to secure a Python Flask app using Keycloak running in Docker.

The aim of our tutorial is to:

* Showcase how to set up a simple Flask app in Python 3
* Introduce Oauth2, OpenID Connect and Keycloak
* Showcase how to set up Keycloak and host it using Docker
* Expand the Flask app to allow interaction with the Keycloak server and use it for login procedures for certain endpoints
 
Note about originality: 

*We found an existing tutorial on Katacoda on this topic, however there are three major distinctions between that one and ours, please see below.*

* We use an image using Docker, instead of launching through the use of a standalone application. 
* Our tutorial is for a Python application using Flask instead of a NodeJS application.
* Additionally, we show how to redirect users to login via Keycloak and then redirect them back (versus for only showing how to get an access token and use it). 

## Grading criteria

We aim to fulfill the following criteria:

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory)* | **Yes** ✅| No | **In the browser** ✅|
|If local execution, runs on Linux | Yes | **No** ❌| Easy to setup and run  |
|The tutorial gives enough background | **Yes** ✅| No | **Comprehensive background** ✅|
|The tutorial is easy to follow  | **Yes** ✅ | No | **Well documented** ✅|
|The tutorial is original, no such tutorial exists on the web | **Yes** ✅ | No | The teaching team never heard about it |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs)** | **Yes** ✅ | No | **Subtle and fun** ✅|
|The tutorial is successful (attracts comments and success) | Yes | **No** ❌| Lively discussion |
|The language is correct | **Yes** ✅| No | **Interesting narrative** ✅ |

*The tutorial has been user tested by an external tester (mid-range programming level proficiency) and the test was sucessful. However, the Katacoda editor seems to have some trouble with saving sometimes, so if you ever recieve a JSON error at step 10, make sure that the code written in step 8 was saved and/or restart the Flask application. </br>
**We have included three easter eggs in our tutorial.
