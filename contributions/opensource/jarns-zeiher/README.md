# Assignment Proposal

## Title
Feature contribution to the Robot Framework

## Names and KTH ID
  - Jonathan Arns (jarns@kth.se)
  - Fabian Zeiher (zeiher@kth.se)

## Deadline
- Task 2

## Category
- Open source

## Description

The [Robot Framework][https://github.com/robotframework/robotframework] is a test automation and RPA framework
that is used for automated acceptance and frontend testing. The framework comes with its own extensible test
definition language. We would like to contribute a new command line option to the tool's main command that allows users
to only selectively parse files in their test suite for faster performance. This feature is described in more detail by
[this issue][https://github.com/robotframework/robotframework/issues/4687].


**Relevance**

Being a test automation framework, the robot framework is without question closely related to devops.
We also think that, while on the surface this might seem like a very simple feature, it will be a very difficult piece of
engineering, simply because the robot framework is a humongous codebase of over 140000 lines of code.
Digging into it deep enough to know where to make changes for this feature will be hard in itself.

**Submission**

Our submission is bundled in [this PR](https://github.com/robotframework/robotframework/pull/4735) on the public repository
of the robot framework.
We implemented an additional command line option for the robot framework cli that allows the user to filter test data
by simple patterns, matching filenames, before tests are parsed and executed. This is useful for performance optimization
of CI pipelines in project with large test suites.
This feature was initially proposed by the project's maintainer in [this issue][https://github.com/robotframework/robotframework/issues/4687].

While this PR is not merged at the time of this submission, we expect it to be merged in the future, since we followed
opensource best practices and the contribution guidelines of the project. We also had a detailed conversation with the
project's maintainer to specify the changes that we would make (this can be found on the issue linked above).
