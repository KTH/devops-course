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



[Moby](https://github.com/moby/moby) is an open source container engine project used in Docker and DevOps workflows. Its legacy `integration-cli` test suite is deprecated, and the project is migrating its tests.



[Issue #50159](https://github.com/moby/moby/issues/50159) tracks this migration. We plan to contribute by migrating two tests: `TestContainerAPICommit` and `TestContainerAPICommitWithLabelInConfig`.



We plan to contribute by:



1. Investigating the selected tests and checking for existing equivalent coverage.

2. Migrating the tests to Moby’s API integration suite using the Go client and existing test helpers.

3. Preserving the relevant assertions and adapting setup, cleanup, and platform conditions to the current framework.

4. Running the migrated tests and documenting the results.

5. Removing the replaced legacy tests.

6. Submitting a pull request and collaborating with the repository’s maintainers, addressing their feedback until the PR is merged.



**Relevance**



This contribution supports automated testing and continuous integration in a widely used container engine project. Migrating deprecated tests helps maintain regression coverage while reducing reliance on legacy testing infrastructure.

