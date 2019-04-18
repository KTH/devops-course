# GitHub label bot

* **Group members:** Joakim Croona (jcroona@kth.se), Simon Larsén
  (slarse@kth.se)

## Finished prototype: Labelbot
* **Repo URL:** [https://github.com/slarse/labelbot](https://github.com/slarse/labelbot)
    - See the README there for details!
* **Demo repo URL:** [https://github.com/jcroona/labelbot-demo](https://github.com/jcroona/labelbot-demo)
    - See [Example usage](https://github.com/slarse/labelbot#example-usage) for
      how to interact with the bot in the demo repo.
* **Group member contributions:**
    - slarse: Almost all contributions are visible in the Labelbot repo, so
      there is no need to list them here.
    - jcroona: Some contributions visible in the Labelbot repo. Has also done
      almost all of the work with getting AWS Lambda and the demo GitHub app up
      and running, which is not visible in the repo.
* **DevOpsy stuff about the project (apart from the product):**
    - Designed for AWS Lambda (i.e. "serverless", and only static state)!
    - TravisCI running the test suite with multiple versions of Python
      ([view on Travis](https://travis-ci.com/slarse/labelbot)).
    - Continuous deployment with Travis to AWS Lambda on specifically tagged
      commits (see the
      [end of this log](https://travis-ci.com/slarse/labelbot/jobs/193963421)
      for a deployment example). Any tag that matches a version number regex
      will be deployed to the AWS Lambda function that operates the demo bot.
    - [Release notes](https://github.com/slarse/labelbot/releases) generated
      from markup in commits (e.g. `[docs]` or `[feat]`). The quality of these
      notes is maybe questionable, as they essentially just reiterate commits,
      but at least they are sorted by category!
    - [Codecov](https://codecov.io/gh/slarse/labelbot) for coverage monitoring.
    - Automatically deployed documentation to
      [ReadTheDocs](https://labelbot.readthedocs.io)

## Original Proposal
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
