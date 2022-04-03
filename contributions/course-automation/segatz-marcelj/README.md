# Assignment Proposal

## Title

_Automatic comparison of proposals with previous contributions_

## Names and KTH ID
  - Fabian Segatz (segatz@kth.se)
  - Marcel Juschak (marcelj@kth.se)

## Deadline

Deadline for Task 1

## Category

Course Automation

## Description

As the course is repeatedly taught, more and more brilliant contributions from previous students are accumulated that can be leveraged to enhance the quality of new students' contributions.

We will create a Github Action that compares the title of an assignment proposal to the selected student works of previous years and create reading suggestions for good contributions on similar topics. In addition, we will check whether a comparison with **all previously merged** pull requests leads to an even more useful result. The output of the action will be given as a comment to the pull request. We anticipate that this will help students that feel overwhelmed to gain a quick overview of the field and show what approaches are particularly suitable for this kind of topic. Furthermore, this supports the TAs in assessing whether the proposal is too similar to previous ones.

**FINAL SUBMISSION**

| Link | Description |
| -----| ----------- |
| [Repository](https://github.com/Neproxx/similar-contributions) | Repository for Github Action |
| [Marketplace](https://github.com/marketplace/actions/similar-contributions) | Link to Github marketplace |
| [Test environment](https://github.com/fsegatz/devops-course/tree/similar-contributions) | Fork of course repository for testing |
| [Example #1](https://github.com/fsegatz/devops-course/pull/4) | Example shows good use-case. The significant keywords in the title get used to build the recommendation list |
| [Example #2](https://github.com/fsegatz/devops-course/pull/6) | Another good use-case. However, this time without any outstanding contributions that could be matched |
| [Example #3](https://github.com/fsegatz/devops-course/pull/5) | Example to show limitations. "Toggle", "feature" and "fit" are probably not the most significant keywords. The action has an input parameter that can be used to specify keywords that should be filtered (See readme of repository) |
