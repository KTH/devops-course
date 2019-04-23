# CI/CD pipeline with automatic deployment 

## Group Member
Stephan Horsthemke (hors@kth.se)
Yi-Pei Tu (yptu@kth.se)

In this demo, we want to use kubernetes on AWS(https://aws.amazon.com/eks/) to design a CI/CD pipeline.
This pipeline connects to git repositories, tests automatically and builds new images in case of successfull tests. New images are automatically deployed in the cluster. Ultimately we want to have a setup in which we only push a change to the master of the repository and, in case the code is alright, the new version will automatically run in the cluster. We will also consider development, testing, and production enviroment to fit the real process in industry.

To reach this we want to first evaluate some CI/CD tools like travis(https://travis-ci.org/) and circleCI (https://circleci.com/) to then create the demo with our favorite solution.


source:
https://kubernetes.io/docs/setup/turnkey/aws/
https://kubernetes.io/
