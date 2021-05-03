# Course automation proposal: check criterion for groups with 3 students.

## Members
Agnes Forsberg (agnesfo@kth.se) 
github: agnesforsberg

Elin Ryman (eryman@kth.se) 
github: rymane

## Group rules in this course regarding groups with 3 student.
"We recommend 2 students. Three is also possible for ambitious essays, demos or contribution to open-source."

## Proposal
Since a group of 3 students has some extra criterion to fulfill than the regular group of 1-2 students, 
we want to simplify the TAs job in deciding whether the criterion is met. We would like to create a Github Action 
that automatically adds a label to the pull request when the group consists of 3 students. This is for the TA to know 
which pull requests should be ambitious enough. We will also check that the pull request submitted is regarding essays, 
demos or contributions to open-source since those categories are the only allowed for 3 students. 
The Github Action should create a PR comment with information about if 3 students are ok for the chosen category.

## Submission
This GitHub action looks at pull requests and checks if the number of studens is appropriate for the task. If the group size is 3 a comment will be added to the pull request regarding this is an acceptable task for that group size. Since the course has a requirement that groups of 3 need a remarkable submission our action also adds a label to the pull request if the group has 3 students so that the TAs can take a more careful look at the proposal.

### Link to action repo
https://github.com/rymane/group-of-3-action

## Validation
We have created pull requests to check the different use cases and make sure that they work.
- [Test group of 3 students with valid task](https://github.com/rymane/group-of-3-action/pull/15)
- [Test group of 3 students with unvalid task](https://github.com/rymane/group-of-3-action/pull/17)
- [Test group of 2 students](https://github.com/rymane/group-of-3-action/pull/16)

## Testing
The directory **contributions** is made for testing. It contains 2 additional directories, named after valid tasks in the course. To test, perform these steps:

1. Checkout a new testing branch
2. Change something in one of the test files
3. Commit and push the changes
4. Create a new pull request

This will trigger the workflow, and a comment will be written on the pull request. If the test was made on a "submission" with 3 names, a "GroupOfThree" label will also be added to the pull request. If the group size is change to 2 in a later stage, the "GroupOfThree" label is removed.

We think we have fulfilled the following criterion: 


|                                             | Yes | No | Remarkable  |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes | **No** | n-a|
|The automation task produces a PR status or issue / PR comment | **Yes**, PR comment and adds a label | No | Points to a generated page with valuable additional information |
|The automation task is reusable | **Yes (next year for this course)** | No | In other courses than this one |
|The task runs on a standard platform | **Yes**, will use Github action | No | Other platforms (e.g. Moodle, Canvas) |
|The task is praised by the other students of this course | Yes | No | n-a |
|The code for the task is available | **Yes**, will use a public repo | No | **Well documented repo** |

