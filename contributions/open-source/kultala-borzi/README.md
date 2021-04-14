# Open-source proposal: Meta-data Report of Github Repo 

## Members: 
 Henrik Kultala (kultala@kth.se)  
 GitHub: [hengque](https://github.com/hengque)

 Eleonora Borzi (borzi@kth.se)  
 GitHub: [EleonoraBorzis](https://github.com/EleonoraBorzis)

## Proposal
We would like to create our own open-source project, where we create a tool that is used to get specific information about a repo. 
Some KTH courses (such as this one) have labs/projects where students have to work on open source projects that fulfil some specific criteria. 
Finding a repo that is adequate can take some time and can be rather frustrating for those unaccustomed to scouring the open-source world. 
We want to shorten the time spent looking for repos fulfilling certain criteria by quickly giving users an analysis of the “responsiveness” of the repo. 
This includes statistics such as the average response time of a repo owner/contributor commenting on or merging a pull request, 
and how many pull requests have not been reviewed yet (that is, have not been commented on). 

The idea is to create a tool that takes as a parameter an URL to a GitHub repo and outputs a report with the following data:

### Category 1:
- Average time it takes for an Issue/PR to be closed
- Average response time of a contributor on an Issue/PR (for example it takes on average one month to receive a comment on an Issue/PR)
- List of what open issues have received a comment from the owner/contributors
- How many pull requests have not been reviewed yet
- NLOC using the tool Lizard
- Complexity using the tool Lizard

### Category 2:
- Number of stars
- Name of the owner
- The date when the repo was created
- Which language (English, Chinese, etc) and programming languages are used in the repo
- Number of open issues/PR
- Number of commits
- The date of the last commit 
- License 
- If there is a contributions.md

The first category is the most interesting one since that information is not immediately obvious when opening a repo. 
The data of the second category is rather easy to quickly find manually, but it is included in case one wishes to utilize this script in 
some bigger automation where repo URL:s are fed into it without the user browsing the repos first. 


## Tools:
- Python
- Github API
- Lizard

## Implementation:
We will write a python script that interacts with the Github API. Since we want to present data from the tool Lizard, 
this must be downloaded beforehand (this will be included in the instructions). The script should be called from a terminal 
so the final output with the data will be displayed in the terminal or written in a file. A Bonus feature would be to give 
the user the possibility to customize what information should be reported, for example, only License and how many pull 
requests have not been reviewed yet.

## DevOps tie in:
First off, as described above, this tool helps reduce tedious, repetitive manual work that follows from being asked 
to find an open-source project with specific requirements. However, the owner of a repo would also benefit from this tool. 
They could run this on their own repo to get a quick overview of how active the repo is and make changes in the repo if needed. 
It can function as guidance in the development stages.  
