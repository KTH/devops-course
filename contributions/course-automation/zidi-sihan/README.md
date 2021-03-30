# Course automation: Checking link validity in the course github text descriptions

## Members

Chen, Zidi: zidi@kth.se, https://github.com/Chen-Zidi
Chen, Sihan sihanc@kth.se, https://github.com/Spycsh


## Proposal

We want to check the validity of the deadlinks in the course github 
text descriptions, for example, readme files. Because sometimes 
the links might be not accessible or out of date.


## Proposed solution

After finding a broken link, our idea is:
- to create a github action and whenever there is a pull request, the action should automatically parse the children or descendant pages under the course website (KTH/devops-course) to find all the broken links
- to show the detail information (time of when the action find the broken link, the corresponding commit log and who writes this dead link, using git blame maybe) of all the broken links in a list of one issue
