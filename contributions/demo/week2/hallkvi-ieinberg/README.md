# Assignment Proposal

## Title

Enforcing version consistency between identical package dependencies in monorepos

## Names and KTH ID

- Hampus Hallkvist (hallkvi@kth.se)
- Isak Einberg (ieinberg@kth.se)

## Deadline

- Week 2

## Category

- Demo

## Description

We intend to demonstrate how to enforce version consistency for identical package dependencies in a monorepository, highlighting the benefits and detailing the corresponding implementation. In this demonstration, we will set up three simple web-apps using npm, with overlapping dependencies. We will then create a CI script that performs a tree search across the entire monorepository to compare package versions among the projects. If a mismatch is detected, the CI pipeline will fail, prompting the user to align the version with the rest of the repository. We intend to use a "majority rules" approach, meaning that the version used by most projects will be considered as the correct one, and any attempt to introduce a different version will trigger a failure or warning.

**Relevance**

When working with monorepositories, which store multiple projects in a single repository, one has to be cautious with overlapping dependencies between those projects. These overlaps can cause inconsistencies and conflicts in how different parts of the repository use shared libraries. To avoid these problems, it's important to ensure that all projects within the monorepository use the same version of shared dependencies. This approach maintains consistency throughout the codebase, simplifies dependency management, and ensures that there are no conflicting version of the same dependency.
