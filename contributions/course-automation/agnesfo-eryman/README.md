# Course automation proposal: check criterion for groups with 3 students.

## Members
Agnes Forsberg (agnesfo@kth.se) 
github: agnesforsberg

Elin Ryman (eryman@kth.se) 
github: rymane

### Group rules in this course regarding groups with 3 student.
"We recommend 2 students. Three is also possible for ambitious essays, demos or contribution to open-source."

## Proposal
Since a group of 3 students has some extra criterion to fulfill than the regular group of 1-2 students, 
we want to simplify the TAs job in deciding whether the criterion is met. We would like to create a Github Action 
that automatically adds a label to the pull request when the group consists of 3 students. This is for the TA to know 
which pull requests should be ambitious enough. We will also check that the pull request submitted is regarding essays, 
demos or contributions to open-source since those categories are the only allowed for 3 students. 
The Github Action should create a PR comment with information about if 3 students are ok for the chosen category.

We aim to fulfill the following criterion: 

|                                             | Yes | No | Remarkable  |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes | **No** | n-a|
|The automation task produces a PR status or issue / PR comment | **Yes**, PR comment and adds a label | No | Points to a generated page with valuable additional information |
|The automation task is reusable | **Yes (next year for this course)** | No | In other courses than this one |
|The task runs on a standard platform | **Yes**, will use Github action | No | Other platforms (e.g. Moodle, Canvas) |
|The task is praised by the other students of this course | Yes | No | n-a |
|The code for the task is available | **Yes**, will use a public repo | No | **Well documented repo** |