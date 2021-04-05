
# Course Automation Proposal: Checking legal group composition

## Members: 
 Henrik Kultala (kultala@kth.se)  
 GitHub: [hengque](https://github.com/hengque)

 Eleonora Borzi (borzi@kth.se)  
 GitHub: [EleonoraBorzis](https://github.com/EleonoraBorzis)


## Group rules for this course:
- Max 3 persons in a group 

- You cannot be with the same persons for more than 2 projects.

- You can work alone on one or at most two projects.

- When you send a pull request for registration, please follow the name convention of using the email addresses of two members to create the folder: email-email. 
    - This is assumed to be the same email addresses as specified in the readme. 

    - This is also assumed to mean “all members of the group” and not “two members”; i.e. if there are three members then all three mbemers’ email address should be included in the folder name.

## Proposal
When a new project is proposed, the readme and the folder name are checked for the names of the group members. The group validity is checked against the rules stated above and a comment with the results is posted on the PR. It also checks that the name of the folder is correct in relation to the email addresses in the readme.

## Tools:
Github Actions   
Bonus: Status Check on GitHub  
Docker

## Implementation:
The action can be found on the public repo: https://github.com/EleonoraBorzis/group-validity-action

We decided to use Docker to make it more accessible to the public. The action will post a comment on the PR depending on what requirements are met and what type of scenario the pull request is. 
In this action the are three scenarios:
1. The pull request does not contain a README file. In this case, it could be a TA that created the pull request so to not interfere, the action will post the comment "There wasn't exactly one readme added under collaborations/ . This is assumed not to be a student submission." The action will not fail the pull request. 
2. The accounts in the README and the name of the folder does not match. The following will be posted as a comment on the PR "The ID:s constituting the folder name did not match with the email addresses in the README file. If this is a student submission, please revise the pull request." The action will fail the check on the PR. 
3.  The size of the group is not allowed. The action will fail the pull request and print the following comment "The group size is 4, but the maximum allowed group size is 3. This group is thus not allowed."
4.  The members have worked together more than the maximum number allowed, the following will be posted on the PR as a comment "A and B appears to have worked together 10 times, while the maximum allowed is 2. Consequently they may not work together here". The action will fail the pull request. 
5.  The pull request satisfies all the requirements and the following will be commented on the pull request "The ID:s constituting the folder name matched with the email addresses in the README file. The group consisting of  A and B appears to have worked together 2 times. Maximum group size allowed: 3. Maximum number of collaborations 2. The group composition is allowed.

The requirements that we think we have achieved are: 
|                                             | Yes | No | Remarkable  |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes |  | |
|The automation task produces a PR status or issue / PR comment | Yes | |  |
|The automation task is reusable | Yes (next year for this course) |  | |
|The task runs on a standard platform | Yes (Github action) | | |
|The code for the task is available | Yes (public repo) | | Well documented repo |
