# Course automation: Generate Summary Readme on Category Folders

## Members

Félix Fonteneau (felixfon@kth.se)
GitHub: [Félix](https://github.com/FelixFonteneau)

## Proposal

I would like to create an automation that  generate a summary readme for each category folder, based on the content of the contributions, and update when new project

For this, I will do a a Github action on pushes that:

- Check if a new contribution folder is pushed in one category folder or an update in these folders
- Retrieve the information of the contribution (e.g. the contributors, the status, a summary (if possible)... )
- Update the readme of the contribution directory (demo or essay)
