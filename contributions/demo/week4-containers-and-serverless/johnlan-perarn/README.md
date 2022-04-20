- Edited after demo on the 12/4-22:
The repository we used for the demo can be found [here](https://github.com/ArnPellesGit/DD2482-Devops-Demo). The slides used can also be found in the same repository. 

# Assignment Proposal

## Title

A modern experience for CI/CD pipeline development.

## Names and KTH ID
  - [@johnlan](https://github.com/landeholt) John Landeholt (johnlan@kth.se)
  - [@perarn](https://github.com/ArnPellesGit) Per Arn (perarn@kth.se)

## Deadline

Task 2

## Category

Demo

## Description
When it comes to deciding where one should host applications, there are many things
to consider. Suppose that you've chosen a platform for hosting and You realize that You'd like to
change to another platform. This might be messy. Queue(cue) [Dagger](https://dagger.io/), a new SOTA tool which enables switching
of platforms and makes it more intuitive and extensive than a regular configuration language such as YAML.

In this demo we will show how you can create a local CI/CD pipeline for a general application.
This can be as advanced as needed really, but for this demo we'll show a simple TODO app.

The key perks of using a tool such as Dagger is that it is built to be portable, making it as
easy as possible for the developers to switch platforms. This is done by Dagger building Dockerfiles and living in the Docker container.
