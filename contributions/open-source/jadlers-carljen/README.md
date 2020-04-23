# Open source contribution: Jenkins integration for Home Assistant

## Contributors

- Jacob Adlers (jadlers@kth.se)
- Carl Jensen (carljen@kth.se)

## Proposal

Develop an integration for Home Assistant to get information from a Jenkins
CI/CD server.

## Description

This integration would make it possible for users of the home automation system
Home Assistant to get information about pipelines. Information we would like to
include is some of the following:

- Job-status (success/failed)
- Execution time
- Link to the build and/or commit on git
- Branch
- Time of execution

This would allow end-users of the integration to create automations, for
example, to announce a failing build on speakers around their home or set the
colour of a lamp based on events from their Jenkins server.

We're planning to use the Generic Webhook trigger plugin that is supported in
Jenkins. This might however not be the final use if another solution which will
make the integration easier/better is found.

## Motivation

An interface for using Home assistant to communicate with Jenkins has not yet
been created (as far as we can tell). The interface could be a fun way to
visualize relevant diagnostics from Jenkins as well as a good way to learn more
about, and contribute to, the open source community. 
