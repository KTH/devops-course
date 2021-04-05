
# Course Automation: Checking legal group composition

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

    - This is also assumed to mean “all members of the group” and not “two members”; i.e. if there are three members then all three members’ email address should be included in the folder name.

## Proposal
When a new project is proposed, the readme and the folder name are checked for the names of the group members. The group validity is checked against the rules stated above and a comment with the results is posted on the PR. It also checks that the name of the folder is correct in relation to the email addresses in the readme.

## Tools:
Github Actions   
Bonus: Status Check on GitHub  
Docker

## Implementation:
The action can be found on the public repo: https://github.com/EleonoraBorzis/group-validity-action

We decided to use Docker to make it more accessible to the public. The action will post a comment on the PR depending on what requirements are met and what type of scenario the pull request is. 
In this action there can be the following scenarios:
1. The pull request is not from a fork. Then this action will end early with a pass and not do anything else.
2. The pull request does not add exactly one README file. In this case, it could be a TA that created the pull request so to not interfere, the action will post a comment about the submission probably not being from a student. The action will then end with a pass. 
3. The KTH mail addresses in the README and the name of the folder does not match. The action will post a comment saying that it's not valid if it's a student project proposal and will fail the check on the PR. 
4.  The size of the group is not allowed. The action will fail the pull request and post a comment regarding this. 
5.  The members have worked together more than the maximum number. The action will fail the pull request and post a comment regarding this. 
6.  The pull request satisfied all the requirements. Then this action will post a comment saying this and end with a pass..

Exception case: One case that the action will fail is when a TA adds one single README file in a folder under contributions/. It is hard to discern this case with the case when students adds a README file in their folders, so we have decided to fail the pull request to give feedback to students.  

The requirements that we think we have achieved are: 
|                                             | Yes | No | Remarkable  |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes |  | |
|The automation task produces a PR status or issue / PR comment | Yes | |  |
|The automation task is reusable | Yes (next year for this course) |  | |
|The task runs on a standard platform | Yes (Github action) | | |
|The code for the task is available | Yes (public repo) | | Well documented repo |

Improvements:
One improvement could be to use a secondary action that discern when the pull request is from a student proposal or from a TA. This would help us to give the proper feedback to the pull request. 
