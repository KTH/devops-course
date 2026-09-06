# Assignment Proposal

## Title

Automated Dependency Management and Package Updates with Renovate

## Names and KTH ID

* Rami Khedair (khedair@kth.se)
* Dawa Arkhang (arkhang@kth.se)

## Deadline

Week 6

## Category

Demo

## Description

Software projects rely on external packages that require continuous updates. Managing these manually leads to security vulnerabilities, outdated packages, and unnecessary effort.

This demo showcases how Renovate automates dependency management by monitoring repositories, detecting outdated packages, and creating Pull Requests for updates.

The demo covers scanning dependencies, CI validation, categorizing updates by impact (patch, minor, major), policy-based automerging, lock-file maintenance, and update grouping.

**Relevance**

Dependency maintenance is a key DevOps practice. Renovate replaces manual checking with continuous automated detection, shifting maintenance into standard Git/CI workflows. Automated testing provides immediate feedback before changes are integrated, maintaining stability while reducing technical debt.

**Demo Plan (can be changed)**

1. **Problem:** Show manual update overhead using a repository with outdated dependencies.
2. **Setup:** Show Renovate configuration rules (schedules, grouping, automerge rules).
3. **Detection:** Show Renovate identifying dependencies and generating PRs with changelogs.
4. **CI Validation:** Run automated build and test pipelines on the generated PR.
5. **Update Policy:** Highlight automerging for safe patch/minor updates versus manual review for major breaking changes.
6. **Live Experiment (Extra):** Modify a dependency version live to demonstrate Renovate detecting it, opening a PR, and triggering CI.
