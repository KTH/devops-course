# Tutorial: Serverless Applications on Heroku

## Members

Axel Pettersson (axp@kth.se)
GitHub: [Ackuq](https://github.com/Ackuq)

Felix Seifert (fseifert@kth.se)
Github: [felix-seifert](https://github.com/felix-seifert)

## Description

Heroku is a webservice where users can run simple web applications for free for a limited number of hours per month. The obvious approach is to run serverless applications which are billed per second. However, Heroku does not offer the option to deploy serverless applications of-the-shelf.

We found a way on how to use Heroku's One-off Dynos, which are not addressable via HTTP requests, to process Functions-as-a-Service via providing arguments via environment variables. This approach is mentioned on the web only a single time. We want to create a tutorial on how to use Heroku to deploy a serverless application. This tutorial requires interaction with both Heroku and GitHub and goes through every major step in making it possible, as well as providing a frontend UI you can use to test your own serverless functions or even use to build your own frontend.

the tutorial is present both in the GitHub repository linked below and in generated tutorial website, created with GitHub pages. To accompany this tutorial, a Medium article was created to hopefully make the tutorial gain more public traction.

## Link to GitHub repository

https://github.com/felix-seifert/serverless-on-heroku

## Link to generated tutorial website

https://felix-seifert.github.io/serverless-on-heroku/

## Accompanying Medium article

https://axel-84042.medium.com/going-serverless-on-heroku-using-one-off-dynos-79b6fd85705a

## Easter egg hint

<details> 
  <summary>Click me for hint</summary>
  ⭐
</details>
