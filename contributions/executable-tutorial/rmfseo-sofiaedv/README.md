# Assignment Proposal

## Title

REST API Fuzzing using Schemathesis

## Names and KTH ID

- Rafael Oliveira (rmfseo@kth.se)
- Sofia Edvardsson (sofiaedv@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

As software solutions increasingly turn to web-based stacks, it becomes
paramount to include comprehensive API testing within CI pipeline processes. We
believe that performing automated testing of API endpoints, in a continuous
fashion, is of great benefit to any project used by consuming clients and so it
is very relevant for (aspiring) developers to get a sense of how one might do
that in a systematic fashion.

Thus, we propose creating an executable tutorial that can pedagogically
introduce developers unacquainted with these techniques to a specific workflow
that they might use later in their professional lives. In particular, we wish to
introduce learners to the [Schemathesis](https://schemathesis.io) tool, which
allows for automated fuzzing of REST APIs based on an OpenAPI contract document.

We will include a simple sample project with non-obvious logic errors, guide the
user to run Schemathesis and explore the potential vulnerabilities it detects,
as well as show them how to use the information reported to easily fix or
mitigate the problems in question.

**Relevance**

Automated fuzzing, especially in this particular context of REST APIs, is at the
heart of automated testing, which we have discussed in week 2 of this course and
is essential to allow for effective Continuous Integration without compromising
robustness. Our proposed tutorial hopes to demonstrate how to use a tool like
Schemathesis as a key component in a testing pipeline to complement
human-written and human-driven tests to ensure all stakeholders have confidence
in the system's continuous reliability.

**Submission**

Our tutorial is available
[here](https://killercoda.com/rafdev/scenario/rest-fuzzing-with-schemathesis),
with the corresponding source code in
[this](https://github.com/RafDevX/schemathesis-tutorial-devops) repository.
