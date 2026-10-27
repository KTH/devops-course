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

**Submission**

- Pull request: https://github.com/monero-project/monero-site/pull/2724
- Tracking issue: https://github.com/monero-project/monero-site/issues/2723

**What we built.** monero-site (getmonero.org) is a Jekyll site built into 15 languages by a `jekyll-multiple-languages-plugin` pipeline and deployed via GitHub Actions and Netlify. Its CI built and published the site but never *validated* it, so broken internal links reached production and were fixed reactively, one PR at a time. We added a `link-check` CI job that builds the site and runs [lychee](https://github.com/lycheeverse/lychee) over the generated `_site/`, failing the build on broken internal links, with the configuration in `lychee.toml`. The job passes the target project's own CI on the pull request.

**System reasoning.** The check runs as a separate job alongside the existing build workflows: it does a full `jekyll build` and then validates the output.

**Design decisions.**
- *Internal, root-relative links only, offline.* External links are not gated because a third-party site being down should never fail our CI. lychee's `--offline` resolves root-relative links against `_site` with no network calls necessary.
- *Baseline, not a mass fix.* Links already broken on `master` are listed in `lychee.toml` (and catalogued in issue #2723), so the gate lands without a simultaneous content cleanup and blocks only newly introduced broken links.
- *`failIfEmpty`.* Guards against the check silently passing while validating nothing.
- *Tool choice.* We first tried html-proofer, which silently reported zero links on the CI runner (a false "pass"); then htmltest, which worked but has had no release in roughly four years; and settled on lychee which is an actively maintained tool, really fastand can be run via the official `lycheeverse/lychee-action`.

**Relevance.** This turns a recurring manual chore, i.e. hunting broken links on the project's primary public face, into an automated quality gate on every pull request with no new accounts or secrets, strengthening the project's existing CI/CD.

**Reflection.** The hardest part was that the failure modes only appeared on the CI runner, not locally: html-proofer's HTML5 parser returned zero links there, which a self-check (fail if too few links are examined) helped to flag for. To extend this we would gate in-page anchors and images once their large pre-existing backlogs are cleaned up, cover the translated mirrors, and check absolute self-links (currently treated as external). We would also follow up with PRs fixing the baselined links in #2723.

**Process and status.** We followed the project's C4 contribution workflow: opened issue #2723 describing the problem, then a pull request referencing it from a fork. Per the monero-site maintainer policy, pull requests are not merged for at least 168 hours, so a merge is expected after the course deadline; we will respond to any maintainer feedback.
