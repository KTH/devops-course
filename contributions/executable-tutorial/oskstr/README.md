# Executable Tutorial: Deploying an API with a Custom Lambda Authorizer using Serverless

## Members
- [Oskar Strömberg](https://github.com/oskstr) (oskstr@kth.se)

## Proposal
I would like to create a tutorial for deploying (using [serverless](https://www.serverless.com/)) a simple service protected by a Custom Lambda Authorizer.

 - Create a simple Typescript service using an AWS Lambda function
 - Create a Custom Lambda Authorizer (itself an AWS Lambda) - authorizing against a separate service
 - Declare using `serverless.yml` that calls need to pass the authorizer to go through
 - Deploy to AWS using [serverless](https://www.serverless.com/)

When I have worked with this on a personal project I wasn't able to find anything on exactly this topic, they were mostly using JWT directly - which is fine when you're building something from scratch but wasn't possible in my case. I needed to validate API keys against a different service, but I still wanted the convenient caching provided by the Amazon API Gateway.

While it would probably look better and be more useful on Medium, I'll probably have to go with one of the browser platforms like Katacoda based on the grading criteria.

Question: Would it work if I create one version on Katacoda and one on Medium?