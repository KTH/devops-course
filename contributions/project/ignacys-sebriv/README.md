# Assignment Proposal

## Title

DevOps and LLMOps Pipeline for a Web-Based Quiz Application

## Names and KTH ID

* Ignacy Stepniewski (ignacys@kth.se)
* Sébastien Riviére (sebriv@kth.se)

## Deadline

11 October 2026

## Category

* Project

## Description

This project will extend an existing open-source web-based trivia application:

https://github.com/Jimike110/quizApp

and use it as the basis for implementing a complete DevOps workflow.

The application will be modified and extended with additional functionality, including an LLM-based component for generating quiz questions. The main focus of the project will be building an automated CI/CD workflow around the application and integrating LLM evaluation into this workflow.

- CI: GitHub Actions will be used to run the CI pipeline on pull requests and pushes. The pipeline will perform linting, automated unit and integration tests, and validate that the application can be successfully built.

- CD: After changes are merged to the main branch and all CI checks pass, the application will be automatically deployed. A failed test or quality check will prevent deployment.

- IaC: The deployment environment will be configured using Terraform to manage versions.

- Security automation: Dependabot will be used to automatically detect vulnerable or outdated dependencies and propose updates through pull requests.

- LLMOps: A LLM will be used to generate quiz questions while an automated evaluation stage will asses the generated content before using it by combining deterministic checks with quality oriented evaluation.

**Relevance**

The project is directly relevant to DevOps because its main focus is the automation of the software development and delivery lifecycle rather than only the functionality of the quiz application.

The project additionally connects traditional DevOps practices with the topic from Week 4. Changes to the LLM component or prompts will be treated similarly to changes in code: they will be evaluated automatically abeforee they can be deployes. This demonstrates how conventional CI/CD quality gates can be extended to software containing non-deterministic AI components.
