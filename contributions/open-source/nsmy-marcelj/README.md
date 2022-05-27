# Assignment Proposal

## Title

Add feature: Specifying Hyperparameter Ranges for AutoKeras Block "ImageAugmentation"

## Names and KTH ID

- Nikolaos Smyrnioudis (nsmy@kth.se)
- Marcel Juschak (marcelj@kth.se)

## Deadline

Deadline for task 4

## Category

Contribution to open-source

## Description

AutoKeras is an AutoML tool that finds a close-to-optimal architecture and hyperparameter choice for a neural network given some boundaries for the search space. One preprocessing module "ImageAugmentation" is currently missing the possibility to specify a range of values for its parameters and currently only accepts a single value per parameter. We are going to add this functionality to four arguments (the ones for which it makes sense). Since the issue states that every PR should only change one hyperparameter, our contribution will consist of four PRs.

This open-source contribution is interesting to us from multiple standpoints. Firstly, the package is designed to automate much of the ML model creation process. Because we contribute to it, we will spend time on understanding it. Secondly, the respository uses modern DevOps tools like [development containers](https://code.visualstudio.com/docs/remote/containers) in VS code. We are looking forward to learn this alternative development workflow and integrate it into our own.

Issue: https://github.com/keras-team/autokeras/issues/1420 <br>
Forked repo: https://github.com/NickSmyr/autokeras

**Final Submission**

Our four PRs that add the mentioned functionality have been merged and can be found here: [1710](https://github.com/keras-team/autokeras/pull/1710), [1714](https://github.com/keras-team/autokeras/pull/1714), [1715](https://github.com/keras-team/autokeras/pull/1715), [1716](https://github.com/keras-team/autokeras/pull/1716).
