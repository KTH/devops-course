# Feedback Submission - Executable Tutorial: Deploying an API with a Custom Lambda Authorizer using Serverless

Feedback for [this](https://www.katacoda.com/oskstr/scenarios/lambda-authorizer-with-serverless) tutorial.

- Tutorial submission PR: [#1387](https://github.com/KTH/devops-course/pull/1387)
- Feedback proposal PR: [#1162](https://github.com/KTH/devops-course/pull/1162)

## Members
* Sebastian Williams - swill@kth.se

## Feedback

### Introduction
+ (+) The introduction provides a clear explanation of the different components that the tutorial will use, ensuring that the user has enough background information before beginning the tutorial.
+ (+) The project overview provides a nice outline of what the tutorial will cover which makes it easy to later understand how the steps are related to each other.
- (-) The image provided looks like a nice overview of the tutorial but without an explanation, it's mostly just confusing. Providing an explanation note underneath or something similar would be very helpful here.

### Step 1
+ (+) The setup is easy and straightforward, especially with the executable code snippets. They make it very easy to perform the commands and prevent accidental typos.
- (-) When installing `serverless` globally some errors are produced. While they don't appear to cause any harm, it would be nice to provide a note saying that it's ok to get errors, as users might get confused otherwise. Personally I was a bit confused when I first ran this command because of the errors, but since the rest of the steps worked out fine it seemed to be ok.

### Step 2 & 3
+ (+) The instructions are straightforward and the code is easy to understand and execute.
- (-) When running the curl request you sometimes have to click it twice for it to work properly, most likely a bug with Katacoda but could be worth writing a small note about it.

### Step 4
+ (+) How authorization can be handled is explained in a short and concise manner at the beginning of the step, with some examples of different alternatives that one can use.
+ (+) The execution results of the different API calls are explained in an easy and understandable manner at the end.
- (-) The policy JSON example is not in a code block, which makes it a bit harder to read.
- (-) The different curl calls at the end would be more readable and easier to execute if they were in executable code snippets.

### Step 5
+ (+) The easter egg was unexpected and fun! The link could perhaps be a regular link instead of a shortened link since some users might not want to click on shortened URLs that might be malicious.
- (-) The AWS configuration instructions are a bit unclear and could be confusing for new AWS users. Consider giving a more detailed explanation on how to create the IAM user and where to get the `AWS_ACCESS_KEY` & `AWS_SECRET_ACCESS_KEY`.
- (-) The endpoints at the end could be placed in code snippets to make it easier to execute them.


### Overall Feedback
+ (+) The language is very fun and engaging. I found myself enjoying reading through each step and experimenting with new material.
+ (+) Most steps are easy to follow and teach the user about the different components in a brief and concise way. Overall I had no trouble following the instructions and executing the tutorial.
- (-) Most code snippets seem to replace the entire file when using the copy to editor Katacoda function. Instead of using replace, appending code to the file would shorten the code snippets making the tutorial code changes more readable. To make this change simply change the data target from `replace` to `append`

## Changes based on Feedback
These are the changes I've made based on the feedback from @oskstr

- Added an example scenario of why using Lambda like this could be useful in the intro.
- Rewrote parts of step 2 to make it more clear.
- Add explanation on how to send emails to unverified email addresses.
- Added some more details to step 4 to reduce confusion.
- Added background information on what Lambda Triggers are.
- Added a link for instructions on invoking AWS Lambda on received emails.
