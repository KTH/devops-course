
# Course automation: Send notification to all team members when a new PR-comment is made

## Members
Ayub Atif (aatif@kth.se)
GitHub: [ayubatif](https://github.com/ayubatif)

Isac Arvidsson (isacarv@kth.se)
Github: [isacarvid](https://github.com/isacarvid)

## Proposal

We want to send a notification via email to all PR group members when a new comment on a proposal-PR has been made(new comment, approved, request changes). The problem arises as only the author of the PR would receive a notification normally, leaving the other members without knowledge of needed changes. Thereby providing an improvment to the course automation experience.

The requirements for the actions are:

-   When a proposal-PR is commented it triggers github actions.
-   Parse README.md to find all members.
-   Include PR-status and title of PR.
-   Include the new comment.
-   Send email to all group members.
