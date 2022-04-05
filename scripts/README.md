# Catalog of Scripts for Devops Course

This readme includes usage instructions & information for all scripts in this repo, written for the KTH DevOps Course.
Please try to keep it updated!

## **- `mpr` - Make Pull Request**

`mpr` simplifies the PR creation flow for students. This shell script incorporates pushing the most recent commit to its
remote branch in the forked repo copy, opens a new PR in the devops repo, and auto-inserts the contents of the changed
readme into the PR description.

You can run mpr from your command line - first, it will prompt you to input or confirm (it infers this info) your Github
username. Next, it will prompt you for a PR title. After they write the title and hit enter, the script will ask for a
file path to the changed README file, and if the file exists, auto-add it as the pull-request body. Users will then be
taken to the Github "Compare Branches" screen, where they can open their auto-populated PR draft with a single mouse
click.