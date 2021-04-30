# Open-source: Meta-data Report of Github Repo (Proposal: #1237)

## Members: 
 Henrik Kultala (kultala@kth.se)  
 GitHub: [hengque](https://github.com/hengque)

 Eleonora Borzi (borzi@kth.se)  
 GitHub: [EleonoraBorzis](https://github.com/EleonoraBorzis)

## Proposal
We would like to create our own open-source project, where we create a tool that is used to get specific information about a repo. 
This would be made into a Github action that you can run on your repo, for instance once every week. 
The action would give a quick overview of the state of activity and complexity in the repo, and could help indicate if changes should be made to make the project more approachable. It could function as guidance in the development stages, but also remind you later on if quality is degrading.

## Tools:
- Github Actions    
- Docker
- Lizard
- Github API

## Implementation:
The action can be found on the public repo: https://github.com/EleonoraBorzis/repo-activity-report-action/

We created a github action that can be used to analyse the activity and the Code Complexity of a repo. It is wrapped in a Docker container, allowing it to easily be used by other workflows. When triggered, a python script will run, making calls to the GitHub API to measure activity and utilizing [lizard](https://pypi.org/project/lizard/) for measuring code complexity.

The action has three inputs:
- github-token: The GitHub secret token that gives access to several git functions. It also increases the limit of GitHub API calls. 
- repo-name: The full name of the repo that is being analysed.
- issue-number: The number of the issue where the user wants the report to be commented.

The user can decide how the action will be triggered, for example a new pull request or at a set day every month. The action will post a comment on the issue with the issue number given by the user. The data posted on the action is: 
- The number of unreviwed issues 
- A list of unreviwed issues
- The number of unreviwed pull requests 
- A list of unreviwed pull requests 
- Average time until PR/Issue closed
- Average time of how long PR/Issues that are still open have been open
- Average time until pull request is commented on by collaborator
- Average time opened for pull requests without collaborator comments
- Lizard output (ex. NLOC, CCN, token, PARAM, length, etc)

## Known limitations:  
API call limit: The GitHub API puts a limit on how many get requests can be sent in a given time frame (the maximum amount of API request is 1000 requests per hour). This action sends one request for every 100 issues and pull request, one request for every 100 issue and pull request comments and one request for every 100 pull request review comments. Thus, if this total exceeds the API limit, not all requested information will be gathered by the action.

## Improvements:  
One improvement could be to include commmit reviews in the analysis. We chose not to include them 
since it is not the most common way to review a PR and it would increase the the number of API calls. 
