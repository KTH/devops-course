# Tutorial: Serverless Applications on Heroku

## Members

Axel Pettersson (axp@kth.se)
GitHub: [Ackuq](https://github.com/Ackuq)

Felix Seifert (fseifert@kth.se)
Github: [felix-seifert](https://github.com/felix-seifert)

## Description

Heroku is a webservice where users can run simple web applications for free for a limited number of hours per month. The obvious approach is to run serverless applications which are billed per second. However, Heroku does not offer the option to deploy serverless applications of-the-shelf.

We found a way on how to use Heroku's One-off Dynos, which are not addressable via HTTP requests, to process Functions-as-a-Service via providing arguments via environment variables. This approach is mentioned on the web only a single time. We want to create a tutorial on how to use Heroku to deploy a serverless application. This tutorial requires interaction with both Heroku and GitHub and goes through every major step in making it possible, as well as providing a frontend UI you can use to test your own serverless functions or even use to build your own frontend.

The tutorial is present both in the GitHub repository linked below and in generated tutorial website, created with GitHub pages. In addition to a tutorial which needs local execution, we also deployed an adapted version of the tutorial on Katacoda (required attention that everything gets executed correctly). To accompany the tutorial, a Medium article was created to hopefully make the tutorial gain more public traction.

## GitHub Repository

[https://github.com/felix-seifert/serverless-on-heroku](https://github.com/felix-seifert/serverless-on-heroku)

## Generated Tutorial Website

[https://felix-seifert.github.io/serverless-on-heroku/](https://felix-seifert.github.io/serverless-on-heroku/)

## Katacoda Tutorial

[https://www.katacoda.com/ackuq/scenarios/serverless-on-heroku](https://www.katacoda.com/ackuq/scenarios/serverless-on-heroku)

## Accompanying Medium Article

[https://axel-84042.medium.com/going-serverless-on-heroku-using-one-off-dynos-79b6fd85705a](https://axel-84042.medium.com/going-serverless-on-heroku-using-one-off-dynos-79b6fd85705a)

## Easter Egg Hint

<details> 
  <summary>Click me for hint</summary>
  ⭐
</details>
