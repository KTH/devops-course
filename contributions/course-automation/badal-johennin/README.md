## Automatic Duplicate Detection for Pull Requests Proposals
### Members
Lee Badal (badal@kth.se)

GitHub: [@LeeBadal](https://github.com/LeeBadal)

Johan Henning (johennin@kth.se)

GitHub [@johennin](https://github.com/johennin)

## Submission
The action and code can be found either in the KTH DevOps repo or in our [fork](https://github.com/johennin/devops-course). 
Link to the files in the fork: [dpd.py](https://github.com/johennin/devops-course/blob/final_version/contributions/course-automation/badal-johennin/dpd.py) and [dpd.yml](https://github.com/johennin/devops-course/blob/final_version/.github/workflows/dpd.yml)

## Features

- On any pull request labeled `proposal`, the script will execute
- The script checks all README files in the controbutions folder agenst the README in the pull request and compares the similarities using [spaCy](https://spacy.io/usage/linguistic-features/#vectors-similarity) word vector semantic analysis
- If similarity is over a predefined threshold (can be changed but it is sensitive) it will fail the check and the output can be found in the actions log under `run check`
- Only checks for student READMEs in the folder `contributions`

## Installation
This tool was specifically tailored for the course DevOps DD2482 at KTH and the respective repository. Which means that it only works for that specific folder structure and naming. The implementation assumes the dpd.yml in the workflow folder and the dpd.py in contributions/course-automation/badal-johennin. This can be customized with minor changes to dpd.yml. For a detailed view check out the branch [final_version](https://github.com/johennin/devops-course/tree/final_version) in our fork.

If this tool is to be reused in other years of DD2482 respecifying the path to the dpd.py file is required.
If any tasks are added or changed this can be added in the dpd.py file.

## Examples
Here is a example output of a submission that was similar to another and therefore failed. By simply pressing the details which is highlighted in the picture below it will display all necessary information.

![failed1](https://i.imgur.com/89lnQHo.png)

![failed2](https://i.imgur.com/YgSoyya.png)

Here is an example of a 99.4% similarity score of 2 README files which result in a fail:

![similar1](https://i.imgur.com/H0bbDmE.png)

