# Assignment Proposal 

### Title 
Fixing unnoticed commits of unstaged changes with bump in Commitizen 
### Names and KTH ID 
- Marcus Alström (maals@kth.se) 
- Omid Fattahi Mehr (omidfm@kth.se) 

### Deadline 
Task 3 

### Category 
Open source 

### Description 
Commitizen is an open source release management tool, that automatically creates commits in a standard way and updates versioning. It is actively used and popular with 2.5k stars with an active community. Bump is a tool within Commitizen that allows automated updating of the version of the project, which is managed by version provider files, such as pyproject.toml or Cargo.toml. Bump will automatically update the version of the project within the version file, it will add all tracked files to staging, create a changelog, and commit these files with a git tag corresponding to the new version. 

The problem: There has been an ongoing [issue](commitizen/commitizen#1194) where the project has been bumped up with uncommitted changes that could go unnoticed. This could lead to breaking changes being included in the new version of the project. 

Our first idea was to simply abort any bump if there were unstaged changes. However, after a short discussion with one of the maintainers we agreed that the best solution would be to only add the version files and let any unstaged changes remain unstaged. 



Before starting, we took time to: 
- Understand the tool and Commitizen's source code.
- Set up Commitizens development environment ensuring everything is working correctly. 

Solved the issue by: 
- Finding a way to retrieve the version files for all the different version providers 
- Updating the corresponding source code file that handles the bump command to only add and commit the version files 
- Updating documentation 
- Adding relevant test cases 
- Making sure our test coverage has not dropped 
- Formatting all the changes according to Commitizens standard 

[Our pull request can be found here](https://github.com/commitizen-tools/commitizen/pull/1261) and we are currently awaiting review from the maintainers. 


**Relevance**
Commitizen is a tool with an important application in managing commits and versioning, which is an important part of DevOps (especially in CI/CD pipelines) and helps teams structure their commits and be on track. First, automation is key in DevOps, and so Commitizen provides a structured and consistent approach to creating commit messages that are consistent and easy to follow. In addition it can analyze commits to determine the next version and automatically change the version of a project and create tags, changelogs, and releases. Some tools in DevOps, such as Jenkins work well with structured commit messages and can do actions based on certain patterns. Also, an important aspect in DevOps is good communication between developers, which can be more easily facilitated by using standardized commit messages.
