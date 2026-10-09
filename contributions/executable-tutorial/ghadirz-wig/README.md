# Assignment Proposal

## Title

Advanced GitHub Actions: Caching, Matrix Builds, and Reusable Workflows

## Names and KTH ID

- Hossein Ghadirzadeh (ghadirz@kth.se)
- Alexander Wigren (wig@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

This executable tutorial teaches three intermediate GitHub Actions techniques by having the learner apply them to a small starter repository provided as a GitHub template: dependency caching, matrix builds, and reusable/callable workflows.

The learner forks the template repository, which contains a minimal CI workflow with no caching and a single build target. Working entirely in the browser (GitHub's web editor and the Actions tab), they will:

1. Add `actions/cache` to the workflow and compare run time before and after.
2. Turn the single build target into a build matrix (multiple OS / language versions) and observe the parallel matrix runs.
3. Extract the shared steps into a reusable workflow (`workflow_call`) and call it from the main workflow, so the same CI logic can be reused across repositories.

Each step includes an explanation of what it does and why it is needed, and the tutorial states its intended learning outcomes at the start.

**Relevance**

Caching, matrix builds, and reusable workflows are standard techniques for keeping CI pipelines fast and maintainable as a project grows, and they directly address the continuous-integration themes covered in this course. Learning to compose CI logic into reusable, callable workflows also reflects a core DevOps principle: treating pipeline configuration itself as maintainable, DRY code rather than copy-pasted YAML.

Link to our tutorial: [Advanced GitHub Actions tutorial](https://github.com/hosseinghzadeh/advanced-github-actions-tutorial)
