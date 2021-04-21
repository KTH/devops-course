# Course Automation: Checking Open-Source Requirements

## Members
- [Oskar Strömberg](https://github.com/oskstr) (oskstr@kth.se)
- [Sebastian Williams](https://github.com/sfkwww) (swill@kth.se)

## Proposal

We would like to create a GitHub action that would automatically check the requirements for an open-souce contribution.

The action should check that repo has:
- More than 10 stars
- More than 100 commits
- An active community
  - open to interpretation
  - provide stats on what has happened the last year (comments, PRs, commits)

We believe that checking that a project is related to DevOps may be too difficult for the purposes of this project.

## Final Submission
We have created a GitHub action at: https://github.com/sfkwww/milkyway

The action can be used to find a link to an open-source GitHub repository in a body of text, like a pull request, and 
get the following stats:
 - stars
 - watchers
 - contributors
 - forks
 - commits
 - commits last year
 - open issues
 
 The action can test that those stats satisfy some minimum requirement, e.g. 10 stars and 100 commits.
 
 With this pull request we have added a file at `.github/workflows/open-source-requirement.yml` that 
 would run this action whenever a pull request to `2021` gets the label `contribution_to_opensource`.
 
 The minimum requirements currently in place are:
 - stars: 10
 - watchers: 10
 - contributors: 10
 - forks: 1
 - commits: 100
 - commits last year: 10
 - open issues: 10
 
 If needed they can be changed or removed. The default requirement is 0. 
 
 The current workflow also uses `github-script` to comment a table of stats on the pull request.

An example would be:

>  [ rust-lang/rust ]
>  -----------------------
>  | Stat  |  Number |  Pass | 
>  |---|---|---|
>  |Stars ⭐              | 53440             | ✔️   |
>  |Commits 📦            | 141152           | ✔️ |
>  |Commits Last Year ⏱️  | 14472 | ✔️ |
>  |Watchers 👀           | 1489          | ✔️ |
>  |Contributors 🧑🏻‍🤝‍🧑🏻       | 4135      | ✔️ |
>  |Forks 🍴               | 7696             | ✔️ |
>  |Open Issues 🟢        | 7056       | ✔️ |

### Update according to change in grading criteria
In a proposed update [#1209](https://github.com/KTH/devops-course/pull/1209) to the grading criteria for this task there are two additional requirements.

1. Implemented in stand-alone repository (already done, no issue here)
2. Demonstrate that automation technique actually works, for example in fork of [KTH/devops-course](https://github.com/KTH/devops-course) (we have tested but haven't provided a link)

Here is a link to the Pull Request where we did our testing: [sfkwww/milkyway#2](https://github.com/sfkwww/milkyway/pull/2).

Here is a link to the actions invoked during said testing: [sfkwww/milkyway/actions](https://github.com/sfkwww/milkyway/actions).
