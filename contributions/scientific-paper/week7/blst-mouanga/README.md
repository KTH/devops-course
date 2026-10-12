# Assignment Proposal

## Title

Automating Dependency Updates in Practice: An Exploratory Study on GitHub Dependabot

## Names and KTH ID

  - Bogdan-Laurentiu Stefanescu (blst@kth.se)
  - Anders Mouanga (mouanga@kth.se)

## Deadline

Week 7

## Category

Scientific paper

## Description

We will present "Automating Dependency Updates in Practice: An Exploratory Study on GitHub Dependabot" by Runzhi He, Hao He, Yuxia Zhang, and Minghui Zhou, published in *IEEE Transactions on Software Engineering* (TSE 2023, DOI: [10.1109/TSE.2023.3278129](https://doi.org/10.1109/TSE.2023.3278129)).

Modern software engineering relies heavily on third-party libraries, but keeping dependencies up to date manually is labor-intensive and error-prone. GitHub integrated Dependabot to automate version bumps and patch security vulnerabilities, but its real-world effectiveness, developer adoption patterns, and failure modes remained largely unquantified at scale. The authors perform a large-scale empirical study combining quantitative data from thousands of GitHub repositories with qualitative surveys of software developers.

In the presentation we will:

- explain how Dependabot operates under the hood, demonstrating how configuration options (`schedule.interval`, `open-pull-requests-limit`, `ignore`) drive automated pull-request generation on a sample repository.
- present the core empirical findings: Dependabot adoption significantly reduces project technical lag (halving average lag from ~49 days down to ~25 days within 90 days), with ~35.7% of projects achieving zero technical lag.
- discuss developer friction and failure modes uncovered by the study, specifically "notification fatigue" (PR overload) and "update suspicion" (reluctance to merge automated PRs after a single broken build).
- highlight the role of CI/CD and test coverage: Dependabot's utility is bottlenecked by test suite quality, as developers rely almost entirely on passing automated tests to build trust in version bumps.
- critique the paper: address potential selection biases in the analyzed GitHub repositories and discuss the reliance on developer self-reporting in qualitative surveys.
- contrast Dependabot with alternative dependency bots (e.g., Renovate) and recent LLM-based automated program repair tools (e.g., BBCFixer / LLM agents) designed to automatically fix breaking API changes caused by dependency updates.

**Relevance**

Automated dependency management sits directly at the intersection of Continuous Integration and DevSecOps. Understanding the practical limitations of dependency bots helps teams design better CI guardrails, avoid developer burnout from bot noise, and manage supply chain security risks effectively.