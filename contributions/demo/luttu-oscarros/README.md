# pre-commit git hook for tests on touched modules

## Group members

- Johan Luttu (luttu@kth.se)
- Oscar Rosquist (oscarros@kth.se)

## Description

An attempt to reduce the workload on CI systems could be to prevent the occurance of errors that quickly can be caught locally on developers' machines. This can be achieved by manually running tests before anything is pushed. One way to automate this could be to use a pre-commit git hook that runs the tests when a commit is made. However, commits should be fast. If commiting becomes slow it might encourage developers to commit more sparingly, which is undesirable. A way to reduce the time it takes to run the tests could be to limit the amount of code to be tested.

For our pre-commit git hook we're only going to run tests on modules that belong to the files that have been touched. In a large codebase this could significantly affect the time it takes for the tests to run.

For the demo we're going to run our hook on an Android codebase. The hook will fire off static analysis tools such as PMD, SpotBugs (new FindBugs) and checkstyle. If a certain argument is given to the commit as a flag, unit tests and mutation tests will run as well.
