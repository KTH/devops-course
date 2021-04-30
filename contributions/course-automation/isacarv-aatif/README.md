
# Course automation: Email notification for proposal-PR new comments

## Members
Ayub Atif (aatif@kth.se)
GitHub: [ayubatif](https://github.com/ayubatif)

Isac Arvidsson (isacarv@kth.se)
Github: [isacarvid](https://github.com/isacarvid)

## Submission
We have made a GitHub action to send notifications via email to the contributors of a PR on the KTH/devops repository. The action triggers a GitHub PR review, which helps students know if their proposals are approved or need changes. The notification is activated via a keyword in the PR readme (eg. #Notify).

The action can be found here:https://github.com/marketplace/actions/pr-review-norification

The source code can be found on this link: https://github.com/isacarvid/PR-review-notification


We are aiming to fulfill the following criteria with our submission including 6 'yes' and two 'remarkable'.

|                                             | Yes | Remarkable  |
|-------------------------------------------- | ----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes (submitted April 5) | n-a|
|The automation task produces a PR status or issue / PR comment | Not quite (evaluates PR diff, parses contact info, and generates a notification email) | The action does not point to a generated page with valuable additional information |
|The automation task is reusable | Yes (next year for this course) | Action can be used in other courses where contributor mails are stored in their README.md |
|The task runs on a standard platform | Yes (Github action) | We did not use Canvas or Moodle |
|The task is praised by the other students of this course | Yes | n-a |
|The code for the task is available | Yes (public repo) | Well documented repo with clear README.md as well as instructions alongside the latest GitHub actions marketplace release |

