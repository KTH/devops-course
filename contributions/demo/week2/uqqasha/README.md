# Assignment Proposal

## Title

Integrating Robocop Analysis Report in SonarQube

## Names and KTH ID

  - Uqqasha Ijaz (uqqasha@kth.se)

## Deadline

- Week 2

## Category

- Demo

## Description

I intend to demonstrate how you can import Robocop analysis report into your SonarQube project. Robocop is a static code analysis tool for Robot Framework code. Robot Framework is a generic open-source test automation framework. SonarQube is the most popular static code analysis tool which supports 29 programming languages. However, SonarQube does not support Robot Framework language out-of-the-box. 

In this demonstration, I will first create a few functional tests using Robot Framework Browser library. Then, I will perform the static code analysis of Robot Framework code using Robocop and generate Report. Finally, this Report will be imported to SonarQube server.

Stretch Goal: Achieve all of these steps in an automated way using GitHub Actions.

**Relevance**

Integrating Robocop analysis into SonarQube is highly relevant to DevOps, particularly in the area of test automation. By incorporating Robocop’s static analysis of Robot Framework tests into SonarQube, teams can automatically detect code quality issues early in the development cycle, even for technologies not natively supported by SonarQube. This integration enhances the DevOps feedback loop.