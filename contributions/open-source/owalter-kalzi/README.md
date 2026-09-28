# Assignment Proposal



## Title



Migrating legacy integration tests in Moby



## Names and KTH ID



- Oscar Walter (owalter@kth.se)

- Hasan Kalzi (kalzi@kth.se)



## Deadline



- Task 3



## Category



- Open source

## Description


[Moby](https://github.com/moby/moby) is an open-source container engine project used by Docker. Its legacy `integration-cli` test suite is deprecated, and [issue #50159](https://github.com/moby/moby/issues/50159) tracks the migration to the newer test suites.

We plan to migrate five tests related to creating images from containers:

- `TestContainerAPICommit`
- `TestContainerAPICommitWithLabelInConfig`
- `TestCommitChange`
- `TestCommitChangeLabels`
- `TestCommitPausedContainer`

Together, these tests cover preservation of filesystem changes and the configured command, labels supplied during a commit, configuration changes, label overrides without changing the source container, and preservation of a container’s paused state.

We will first investigate the existing tests, check for equivalent coverage and coordinate through the migration issue to avoid duplicating work. We will then migrate the tests to Moby’s API integration suite using the Go client and existing test helpers.

The migration involves replacing command-line setup and checks with API calls, preserving the relevant assertions, and adapting container lifecycle handling, cleanup and platform conditions. We will run the migrated tests, document the results and remove the replaced legacy tests once their coverage is preserved.

We will submit an upstream pull request and address maintainer feedback, with the goal of having it merged. Our contribution summary will explain our implementation choices, testing results and any changes made during review.

If another contributor takes one of the selected tests before we start, we will substitute another suitable test from the migration issue, as agreed with the teaching assistant.


**Relevance**



This contribution supports automated testing and continuous integration in a container engine used in DevOps workflows. It preserves regression coverage for container commits while helping Moby move away from deprecated testing infrastructure.

