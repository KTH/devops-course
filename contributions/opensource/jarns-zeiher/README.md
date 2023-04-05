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
