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

## Submission For Feedback
I have opted to only do a version for Katacoda for now. 

The tutorial can be found at [katacoda.com/oskstr/scenarios/lambda-authorizer-with-serverless](https://www.katacoda.com/oskstr/scenarios/lambda-authorizer-with-serverless)
and the repo can be found at [oskstr/katacoda-scenarios](https://github.com/oskstr/katacoda-scenarios).

Looking forward to feedback from @sfkwww as per [#1162](https://github.com/KTH/devops-course/pull/1162).

## Final Submission
The location of the tutorial is still the same but I have made the following changes:
- [6c9ebab](https://github.com/oskstr/katacoda-scenarios/commit/6c9ebab) Change verbatim text to code blocks 
- [084bc62](https://github.com/oskstr/katacoda-scenarios/commit/084bc62) Format policy snippet as JSON
- [563582d](https://github.com/oskstr/katacoda-scenarios/commit/563582d) Change from replace to append/insert
- [aea9485](https://github.com/oskstr/katacoda-scenarios/commit/aea9485) Fix typo
- [ed6f7ec](https://github.com/oskstr/katacoda-scenarios/commit/ed6f7ec) Add explanation to image
- [f59c842](https://github.com/oskstr/katacoda-scenarios/commit/f59c842) Add warning about error messages
- [f1d6222](https://github.com/oskstr/katacoda-scenarios/commit/f1d6222) Explain bug where command isn't being run
- [7109af6](https://github.com/oskstr/katacoda-scenarios/commit/7109af6) Make curl calls executable
- [64dda2c](https://github.com/oskstr/katacoda-scenarios/commit/64dda2c) Explain which header we are looking for
- [e0a040d](https://github.com/oskstr/katacoda-scenarios/commit/e0a040d) Explain how to set up an AWS user
- [9c0e73a](https://github.com/oskstr/katacoda-scenarios/commit/9c0e73a) Add more spacing
- [2444cbf](https://github.com/oskstr/katacoda-scenarios/commit/6c9ebab) Remove space that caused graphical bug
- [85ad312](https://github.com/oskstr/katacoda-scenarios/commit/6c9ebab) Increase expected time for scenario

Diff log: https://github.com/oskstr/katacoda-scenarios/compare/756b829...85ad312
