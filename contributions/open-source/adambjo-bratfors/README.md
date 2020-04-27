# Upgrade Strongbox documentation to mkdocs-material-5.0.0

## Contributors

Adam Björnberg (adambjo@kth.se)
GitHub: adbjo

Robin Bråtfors (bratfors@kth.se)
GitHub: rbratfors


## Proposal

Migrate the [Strongbox documentation](https://strongbox.github.io/) to Material for MkDocs 5.

Solves this issue: https://github.com/strongbox/strongbox/issues/1715 

## Description

The following tasks will need to be carried out:

- Upgrade docker image so it uses the latest version ci-build-images/images/mkdocs/Dockerfile.mkdocs and installs the correct pip dependencies
- Make any necessary configuration changes
- Add support pymdownx.tabbed in markdown_extensions under mkdocs.yaml (this requires pymdown-extensions>=7.0)
- Search for todo: pymdownx.tabbed within the project to

## Ties to DevOps

- Strongbox is an **artifact repository** manager
- Docker image configuration (**containerization**)
- MkDocs is a **project documentation** generator

## Merged PRs
We worked on two separate repositories, here are the merged pull requests that detail our work:

https://github.com/strongbox/ci-build-images/pull/9

https://github.com/strongbox/strongbox-docs/pull/82
