# GitHub label bot

* **Group members:** Joakim Croona (jcroona@kth.se), Simon Larsén
  (slarse@kth.se)
* **Concept:** A GitHub App (bot) that labels issues based on explicit markup
  in the issue body.
* **Use case:** The idea is to allow any user to label an issue with a set of
  labels that a repo owner has explicitly specified without giving the user
  write access to the repo
  [(as is otherwise required to label issues)](https://help.github.com/en/articles/applying-labels-to-issues-and-pull-requests).
  Consider for example the DevOps course repo. It would be beneficial to be
  able to allow students to label issues with for example `question` or
  `collaboration_wanted`, but not e.g. `grading`.
* **Additional details:** We want to try using AWS lambda for deploying the
  GitHub App, and are aiming for full continuous delivery. Right now, we plan
  to use AWS Lambda for the core application, and DynamoDB for storing allowed
  repo labels. This may change if we run into issues.
* **Example issue body:**

```
Hi! I need a project partner for the open project.

:label: collaboration_wanted
```
This would result in the bot labeling the issue with `collaboration_wanted`
(iff that is an allowed tag for the repo). We have a few different ideas going
for exactly how to configure the permitted labels for a repo, including opening
a "special" issue or using a configuration file.
