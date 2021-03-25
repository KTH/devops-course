
# Course automation: Email notification for proposal-PR new comments

## Members
Ayub Atif (aatif@kth.se)
GitHub: [ayubatif](https://github.com/ayubatif)

Isac Arvidsson (isacarv@kth.se)
Github: [isacarvid](https://github.com/isacarvid)

## Proposal

We want to send a notification via email to all PR group members when a new comment on a proposal-PR has been made. The problem arises as only the author of the PR would receive a notification normally, leaving the other members without knowledge of needed changes. Thereby providing an improvment to the course automation experience.

The requirements for the actions are:

-   When a proposal-PR is commented it triggers github actions.
-   Parse README.md to find all members.
-   Include title of PR.
-   Include the new comment.
-   Send email to all group members.

Note: The student can set on/off the notification (it will be off by default). This way, students who don't want to be notified are not going to receive email alerts.
