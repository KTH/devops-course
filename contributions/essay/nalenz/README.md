# Assignment Proposal

## Title

Large-scale JavaScript error tracking

## Names and KTH ID

- Julian Nalenz (nalenz@kth.se)

## Deadline

Task 3 (2022-05-03)

## Category

Essay

## Description

Continuous error tracking and monitoring are highly relevant for all applications, especially when they are cloud-based. In this essay, error tracking in the JavaScript/React/Node.js ecosystem should be discussed, using the example of [Sentry](https://sentry.io/).

Firstly, this essay will give an in-depth introduction into how exceptions in JavaScript work (in both synchronous and asynchronous code), which properties characterize an exception (e.g. exception name, stacktrace), how exceptions can be grouped (exception fingerprinting and Sentry's standard configuration for that) and how based on all this, exception tracing can work when using many distributed microservices (e.g. using the `X-Request-ID` HTTP header). In the end, this essay will also give an overview of how Sentry can be integrated into other tools, e.g. sending a Slack message when an exception happens.
