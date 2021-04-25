# Open-source proposal: Meta-data Report of Github Repo 

## Members: 
 Henrik Kultala (kultala@kth.se)  
 GitHub: [hengque](https://github.com/hengque)

 Eleonora Borzi (borzi@kth.se)  
 GitHub: [EleonoraBorzis](https://github.com/EleonoraBorzis)

## Proposal
We would like to create our own open-source project, where we create a tool that is used to get specific information about a repo. 
This would be made into a Github action that you can run on your repo, for instance once every week. 
The action would give a quick overview of the state of activity and complexity in the repo, and could help indicate if changes should be made to make the project
more approachable. It could function as guidance in the development stages, but also remind you later on if quality is degrading. 

### Data to present:
- Average time it takes for an Issue/PR to be closed
- Average response time of a contributor on an Issue/PR (for example it takes on average one month to receive a comment on an Issue/PR)
- List of what open issues have received a comment from the owner/contributors
- How many pull requests have not been reviewed yet
- NLOC using the tool Lizard
- Complexity using the tool Lizard

## Tools:
- Python
- Github API
- Github actions
- Lizard

## Implementation:
We will create a Github action that posts the specified meta data in a given issue/pull request on the repo it is run on. The data will be gathered through a python script and the tool [lizard](https://github.com/terryyin/lizard) by getting the repo data through API calls to Github.
