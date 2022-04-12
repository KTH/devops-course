# Assignment Proposal

## Title

Add feature: Specifying Hyperparameter Ranges for AutoKeras Block "DataAugmentation"

## Names and KTH ID

- Nikolaos Smyrnioudis (nsmy@kth.se)
- Marcel Juschak (marcelj@kth.se)

## Deadline

Deadline for task 4

## Category

Contribution to open-source

## Description
AutoKeras is an AutoML tool that finds a close-to-optimal architecture and hyperparameter choice for a neural network given some boundaries for the search space. One preprocessing module "DataAugmentation" is currently missing the possibility to specify a range of values for its parameters instead of single ones. We are going to add this functionality to four arguments (the ones for which it makes sense). Since the issue states that every PR should only change one hyperparameter, our contribution will consist of four PRs.

This open-source contribution is interesting to us from multiple standpoints. Firstly, the package is designed to automate much of the ML model creation process. Because we contribute to it, we will spend time on understanding it. Secondly, the respository uses modern DevOps tools like VS code to work inside [development containers](https://code.visualstudio.com/docs/remote/containers). We are looking forward to learn this alternative development workflow and integrate it into our own.  

Autokeras repo: https://github.com/keras-team/autokeras <br>
Forked repo: https://github.com/NickSmyr/autokeras <br>

Issue to work on:<br>
https://github.com/keras-team/autokeras/issues/1420 <br>