# Assignment Proposal

## Title

Automated Preview Deployments of Web Applications

## Names and KTH ID

- Mathias Magnusson (mathm@kth.se)
- Kevin Wenström (kevinwe@kth.se)

## Deadline

- Week 3

## Category

- Demo

## Description

This is a demonstration of automatically creating a preview deployment of a web application for each
pull request in a repository. When pull requests are made the branch will be deployed on a subdomain
unique to the pull request which will be torn down when the pull request is merged or closed. For
this, we will use GitHub actions for kicking the pipeline off,
[Nomad](https://developer.hashicorp.com/nomad) for orchestrating the deployments, and
[traefik](https://traefik.io/traefik) for proxying the traffic on the subdomain to the correct
deployment. Each preview deployment will also get its own copy of a PostgreSQL database.

**Relevance**

Preview environments allow everyone involved in the software development process to quickly and
early evaluate changes to an application, by not just looking at the code, but also seamlessly
assess its behaviour in a production-like environment. Notably, this allows non-developers to take
part earlier in the development process.
