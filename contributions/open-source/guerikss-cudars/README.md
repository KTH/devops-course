# Assignment Proposal

## Title

Adding an automated link-checking CI gate to the Monero website (monero-site)

## Names and KTH ID

  - Harry Eriksson (guerikss@kth.se)
  - Jēkabs Čudars (cudars@kth.se)

## Deadline

- Task 3

## Category

- Open source contribution

## Description

[monero-site](https://github.com/monero-project/monero-site) is the source of [getmonero.org](https://www.getmonero.org), the official website of Monero, one of the largest privacy-focused cryptocurrency projects. It is a Jekyll static
site and it is very actively maintained (hundreds of merged pull requests, commits on most days, and an active review community of core maintainers).

Its GitHub Actions pipeline (`.github/workflows/ci.yml`) builds the site on every push and pull request, but it never validates links in the webpages. As a consequence, broken links can and does reach production and are repeatedly fixed by hand, one pull request at a time (for example the recently merged (searching for "fix link" garners a a slew of results in the commit history).

We will add a continuous quality-automation gate that closes this gap:

- A CI job that runs [HTMLProofer](https://github.com/gjtorikian/html-proofer)
  against the built `_site/`, failing the build on broken internal links,
  missing images, and dead anchors.
- Relative link checking will be blocking while external link checking (which is
  inherently flaky, since third-party sites can go down without warning) will be kept out of the blocking job, but will be documented. This keeps CI trustworthy rather than randomly red.

When finished, we will first open an issue describing the gap, follow the repository's contribution workflow, submit an upstream pull request, and address maintainer feedback with the goal of getting it merged. Our contribution summary will explain the architecture of the site's build, justify our design decisions (what to block on, how to handle pre-existing failures via a documented ignore-list plus an upstream issue), and reflect on the review.

If the maintainers prefer a narrower or different scope, we will naturally adjust our pull request.

**Relevance**

This contribution brings continuous verification to a CI pipeline that currently
builds an artifact without checking it. It turns a recurring manual task: hunting down broken links on the project's primary public face, into an automated quality gate that runs on every pull request, catching regressions before they ship. It strengthens the project's existing CI/CD and requires no external accounts or secrets, so it runs the same way on contributor forks and upstream.
