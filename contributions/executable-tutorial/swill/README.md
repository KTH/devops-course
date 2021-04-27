# Tutorial Submission: Implementing AWS Lambda with AWS SES and invoking it with HTTP Request
## Members
- [Sebastian Williams](https://github.com/sfkwww) (swill@kth.se)

## Proposal

I would like to create a tutorial on how to setup the serverless microservice AWS Lambda. The example used in the tutorial will be triggered by AWS SES and then send a response to a specific email.

The main steps of the tutorial will be as follows:
- Setting up SES
- Creating the Lambda function
- Creating an API Gateway
- Configuring the permissions for the Lambda

Microservices such as AWS Lambda are commonly used within DevOps to build a single application as a set of small services.

## Submission for Feedback

Due to invoking AWS Lambda with SES requires a domain I opted to use an HTTP request as the lambda trigger instead.

The Katacoda tutorial can be found [here](https://www.katacoda.com/sfkwww/scenarios/aws-lambda-ses) and the repo can be found [here](https://github.com/sfkwww/katacoda-scenarios).

I hope to receive feedback from @oskstr as per #1164
