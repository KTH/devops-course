# Course automation: Verify pull request content changes

## Members

Ralfs Zangis (zangis@kth.se)
GitHub: https://github.com/bubriks

## Proposal
Ensuring that pull requests can be approved only if the formatting requirements are met. 

## Description
- Check changed .md file contents (contains: task name, members, and description)
- Verify that the member names (from README.md) are represented in the containing folder name
- Confirm that file structure follows the rules (no changes outside members folder in the selected category)
- Inform user if any checks have failed (for more details on what has failed check build)

## Final solution

### Overview
Code testing the validity of markdown files and the change location is expected to be run on pull requests.
This solution should allow for relatively easy future updates requiring few modifications, as the most complex part is handled by the referenced GitHub action.
[KTH course content verifier](https://github.com/bubriks/KTH-Course-content-verifier)

### Info about the solution

An example solution is provided and explained within the provided GitHub link and an aditional file for implementation is provided ("validation.yml"), this file only needs to be copied into the following folder for it to work: DevOps-course\.github\workflows. 

Since single action was necassary the functionality of the following actions is incorporated in this repository (in addition to logic related to folder naming):
- https://github.com/bubriks/string-verifier
- https://github.com/bubriks/file-content-checker

They were made to allow for usage of the implemented functions outside of this curse (As the provided solution could be considered specialized for the task at hand).

### Getting started:
Example of deployed solution can be found in: https://github.com/bubriks/devops-course/tree/course-automation-deployed

And tests performed by forking the deployed solotion can be seen here: https://github.com/bubriks/devops-course/pull/25 (with each commit being a separate test, read comments for more info)