# Assignment Proposal

## Title

Automated Dependency Management and Package Updates with Renovate

## Names and KTH ID

* Rami Khedair ([khedair@kth.se](mailto:khedair@kth.se))
* Dawa Arkhang ([arkhang@kth.se](mailto:arkhang@kth.se))

## Deadline

Week 6

## Category

Demo

## Description

Software projects rely on external packages that require continuous updates. Managing these manually can lead to security vulnerabilities, outdated dependencies, and unnecessary effort.

This demo showcases how **Renovate** automates dependency management across different languages and project structures. We will demonstrate Renovate using **Java and Node.js** projects.

The demo will cover:

* **Java:** a backend project using external dependencies.
* **Node.js:** a monorepo containing both a backend and frontend.

We will also demonstrate CI validation, update grouping, lock-file maintenance, and different policies for patch, minor, and major updates.

**Relevance**

Dependency maintenance is a key DevOps practice. Renovate replaces manual dependency checking with continuous automated detection and integrates updates directly into the Git/CI workflow.

Using three different ecosystems and a cross-project dependency demonstrates how Renovate can automate dependency management beyond a single repository or programming language.

**Demo Plan (can be changed)**

1. **Problem:** Show outdated dependencies and the effort required to maintain them manually.

2. **Setup:** Show the Renovate configuration, including schedules, grouping, automerge rules, and update policies.

3. **Java:** Demonstrate Renovate detecting outdated Maven dependencies and creating Merge Requests.

4. **Node.js:** Demonstrate dependency updates in a monorepo containing a backend and frontend.

5. **CI Validation:** Show CI pipelines automatically building and testing Renovate-generated Merge Requests.

6. **Update Policy:** Demonstrate automerging safe patch/minor updates while keeping major updates for manual review.

7. **Live Experiment (Extra):** Trigger a dependency update during the demo and show the complete Renovate → Merge Request → CI workflow.
