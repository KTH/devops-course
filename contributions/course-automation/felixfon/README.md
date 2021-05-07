# Course automation: Generate Summary Readme on Category Folders

## Members

Félix Fonteneau (felixfon@kth.se)
GitHub: [FelixFonteneau](https://github.com/FelixFonteneau)

## Proposal

I would like to create an automation that  generate a summary readme for each category folder, based on the content of the contributions, and update when new project

For this, I will do a a Github action on pushes that:

- Check if a new contribution folder is pushed in one category folder or an update in these folders
- Retrieve the information of the contribution (e.g. the contributors, the status, a summary (if possible)... )
- Update the readme of the contribution directory (demo or essay)


## Goal

I plan to get the following of the criteria. 

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) |~~Yes~~ |	**No** |	n-a|
|The automation task produces a PR status or issue / PR comment	| **Yes**	|~~No~~	|~~Points to a generated page with valuable additional information~~|
|The automation task is reusable	|**Yes (next year for this course)**|	~~No~~	|In other courses than this one (if they have the same group formation structure)|
|The task runs on a standard platform	|**Yes (Github action)**	| ~~No~~ |	~~Other platforms (e.g. Moodle, Canvas)~~|
|The task is praised by the other students of this course|	**Yes**|	~~No~~|	n-a|
|The code for the task is available	|**Yes (public repo)**|	~~No~~	|**Well documented repo**|

## Submission

You can see the details of the doc, implementation and a demo are available [here](https://github.com/FelixFonteneau/readme-Generation-for-Devops-Course).

