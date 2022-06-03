# Assignment Proposal

## Title

Contributing to [better-npm-audit](https://github.com/jeemok/better-npm-audit)

## Names and KTH ID
  - Max Persso (maxper@kth.se)

## Deadline

Task 5

## Category

Contribution to open-source

### Description
NPM is a package manager for Node.js which is a hugely popular back end runtime environment for Javascript code. Node.js provides the framework for Javascript code to be executed outside of the web browser, allowing for quick and easy development of backend services. In order to validate the safety of applications built on potentially thousands of packages NPM provides the NPM audit command. The NPM audit command scans the project and reports known issues and security vulnerabilities. The audit command however has undergone several revisions and changes over the years, favoring a minimalistic report style. This choice has created a need for more extensive options and output from the audit command.

The [better-npm-audit](https://github.com/jeemok/better-npm-audit) is an open source repository which allows for extended output and configuration of the npm audit command. I will solve an open issue where the developer has asked for help, allowing users to write configuration files in the yaml format for the improved audit command. Given that yaml is a very popular configuration langauge for DevOps-related tools and projects it will help expand the range of users that can use this tool in their CI/CD pipelines.

The repository has 81 stars, 218 commits and an active community as other students in this course have had conversations with the developer and have contributed to the repository as part of this course.

Final Submission
[Adding yaml support](https://github.com/jeemok/better-npm-audit/pull/79)
