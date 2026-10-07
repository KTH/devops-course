# Assignment Proposal

## Title

Adding a CI test stage and smoke tests to Hugin (hugin-native)

## Names and KTH ID

  - Harry Eriksson (guerikss@kth.se)
  - Jēkabs Čudars (cudars@kth.se)

## Deadline

- Task 3

## Category

- Open source contribution

## Description

[hugin-native](https://github.com/kryptokrona/hugin-native) is the React Native
mobile client for Hugin, a private and secure chat application in the Kryptokrona
ecosystem (1,200+ commits, actively maintained). Its GitHub Actions pipeline
builds and signs an Android APK and publishes draft GitHub Releases on tags, but
it currently runs no automated tests or linting.

We will add a continuous-testing stage to the project's CI together with its
first smoke tests:

- A GitHub Actions workflow that runs on pull requests and pushes to `master`:
  install dependencies, run `npm run lint` (ESLint), and run `npm test` (Jest).
- An initial smoke test that renders the root `<App />` component with React
  Native Testing Library and asserts it mounts without crashing.
- An Android emulator boot smoke test that launches the built APK and verifies the main screen appears.

We will first study the existing build/release workflows and the app's
bootstrapping. We will also follow the repository's conventions and submit an upstream pull request, addressing maintainer feedback with the goal of getting it merged. Our contribution summary will explain our implementation choices, the testing results, and any changes made during review.

If the maintainers prefer a different scope (for example a lint-only gate first,
or a specific set of units to cover), we will of course adjust our PR.

**Relevance**

This contribution brings continuous testing and fast feedback to a pipeline that currently ships signed release artifacts without verifying them. A smoke test catches if changes has broken the app completely in the CI and turns it into an automated quality gate on every pull request. It strengthens the project's existing CI/CD without requiring any external accounts or secrets.
