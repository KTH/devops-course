# Open-source contribution proposal: Contributor Scoreboard
## Members
Kalle Meurman (kallem@kth.se) Github: Wizkas0

Markus Wesslen (mwesslen@kth.se) Github: m4reko

## Proposal
We would like to create an open-source project from scratch. Our idea is to create a github action/ workflow, 
that scores contributors to a repository based on user-defined rulesets. A rule might for instance be that 
commits should link to an issue. Each contributor would then have a score of (commits with linked issues)/(total commits) 
and this score would be kept in a scoreboard (perhaps as a pinned issue).

The point of this is to encourage good practices in contributors, which would improve workflow.

The scope of this project is potentially very large, as there are many rules of varying degrees of complexity 
that different projects might have. Our goal is, however, not to implement every rule one can think of, 
but to build the underlying infrastructure and implement a couple of general rules (Like the above mentioned example). 
The project could then be extended in the future, to include more complex rules, if there is demand for it.

We believe that this project is suitable for the open-source category, as it is not generally useful for the course-repo, 
but could be useful for many different projects.

*I (Kalle) have to note that I have already submitted a course-automation contibution (a github action that automatically labels pull requests).
Would this project be considered to be overlapping, since both are github actions, or are they dissimilar enough? I really like this idea and would like to pursue it.*
