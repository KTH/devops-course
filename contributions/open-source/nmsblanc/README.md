# Assignment Proposal

## Title

Cross-task pipeline validation for weekly student registrations

## Names and KTH ID

- Nolan Blanc (nmsblanc@kth.se)

## Deadline

- Task 3

## Category

- Open source

## Description

This contribution aims to improve the course repository's GitHub Actions pipeline by adding a cross-task validation between the `demo` and `scientific-paper` contributions.

Currently, the pipeline checks whether the members of a contribution are correctly registered in Canvas and whether the README follows the expected format. However, it does not check whether a student is participating in two incompatible tasks during the same week.

The proposed improvement will verify that a student cannot participate in both a `demo` and a `scientific-paper` for the same week. For example, if a student is registered in a `demo/week3` contribution, the pipeline should reject another contribution containing the same student in `scientific-paper/week3`.

The validation will take into account:

- Contributions already merged into the repository.
- Other open pull requests targeting the course branch.
- The current pull request, which must be excluded when searching for existing conflicts.
- Conflicts between members of the same group, based on the group names in the contribution directory structure.

If a conflict is detected, the pipeline will fail and add an explanatory comment to the pull request identifying the student, the week, the conflicting task categories, and the relevant pull requests.

I would like to submit a PR adding this verification in https://github.com/algomaster99/github-canvas-integration-devops/blob/fix/replace-presentation-with-project/update_task.py

**Relevance**

This contribution is relevant to DevOps because it improves the automation and reliability of the project's CI/CD process. Instead of relying on manual checks, the pipeline will automatically validate cross-task constraints whenever a contribution is submitted or updated.

I am currently working alone because this issue in the pipeline was discovered on this morning. I did not have time to find a partner before starting the work. The implementation is relatively small and focused, since it mainly involves querying open pull requests and comparing the participating members and weeks.