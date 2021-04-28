# Deploying scheduled functions on Kubernetes using Kubeless

## Members

Simon Persson, siper@kth.se

GitHub: altaired


Martijn Atema, atema@kth.se

GitHub: atema

## Proposal

This tutorial will guide one through how to create a K8 cluster and deploy a scheduled serverless function using Kubeless. 
The scheduled function will call an another service on the K8 cluster, with the purpose of demonstrating how this can be used to 
perform routine tasks such as backups and archiving automatically. We plan to use Katacoda to be able to run the tutorial with a bash terminal.

## Submission

Here is the initial submission for proposal #1134.

Our tutorial can be run in the browser, and is available [here](https://www.katacoda.com/siper/scenarios/scheduled-kubeless).

The source of the tutorial can be found in the repository [altaired/katacoda-scenarios](https://github.com/altaired/katacoda-scenarios).

## Grading Criteria We Aim For

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) | **✓ Yes** | No | **✓ In the browser** |
|If local execution, runs on Linux | Yes | No | Easy to setup and run  |
|The tutorial gives enough background | **✓ Yes** | No | Comprehensive background |
|The tutorial is easy to follow  | **✓ Yes** | No | **✓ Well documented** |
|The tutorial is original, no such tutorial exists on the web | **✓ Yes** | No | The teaching team never heard about it |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) | **✓ Yes** | No | Subtle and fun |
|The tutorial is successful (attracts comments and success) | **✓ Yes** | No | 🙏 Lively discussion |
|The language is correct | **✓ Yes** | No | Interesting narrative  |
