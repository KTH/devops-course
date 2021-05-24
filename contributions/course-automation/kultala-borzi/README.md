
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

The action interprets the pull request and if it does not look like a student project proposal it posts a comment stating that. If it looks like a proposal then it checks whether the email addresses in the README and the folder name correspond with each other. If they don't this is posted as a comment and it fails the check, otherwise a comment is posted with information regarding if the group composition is allowed and the check fails or passes depending on the outcome.

Some typical scenarios that can occur:
1. The pull request does not add exactly one README file under *contributions/*. In this case, it could be a TA that created the pull request. The action will only post a comment about the submission probably not being from a student and then end with a pass. 
2. The KTH email-addresses in the README and the name of the folder do not match. The action will post a comment saying that it's not valid if it's a student project proposal, and will fail the check on the PR. 
3. The size of the group is not allowed. The action will fail the pull request and post a comment regarding this. 
4. The members have worked together more than the maximum allowed times. The action will fail the pull request and post a comment regarding this. 
5. The pull request satisfied all the requirements. Then this action will post a comment saying this and end with a pass.

For a more in-depth showcase of different scenarios see the dedicated repository: https://github.com/hengque/group-validity-action-example 

Exception case: One case that the action will fail is when a TA adds one single README file in a folder under *contributions/*. It is hard to discern this case with the case when students adds a README file in their folders, so we have decided to fail the pull request to give feedback to students.  

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
