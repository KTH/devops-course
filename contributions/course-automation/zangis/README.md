# Course automation: Verify pull request content changes

## Members

Ralfs Zangis (zangis@kth.se)
GitHub: https://github.com/bubriks

## Proposal
Ensuring that pull requests can be approved only if the formatting requirements are met. 

## Description
- Check changed .md file contents (contains: task name, members, and description)
- Verify that the member names (from README.md) are represented in the containing folder name
- Confirm that file structure follows the rules (no changes outside members folder in the selected category)
- Inform user if any checks have failed (for more details on what has failed check build)

## Final solution

### Overview:
Code testing the validity of markdown files and the change location is expected to be run on pull requests.
This solution should allow for relatively easy future updates requiring few modifications, as the most complex part is handled by the referenced GitHub action.

### Info about the solution:
To confirm that the file structure follows rules and all changes are within a specific folder a separate python file was created (This was done since this part of the task is unique for this specific problem) and it is called verify_location.py.

For file content validation a GitHub action was created [file content checker](https://github.com/marketplace/actions/file-content-checker). (More detailed description of it can be found following the provided link).

The second python file (verify_folder_names.py)  is used to ensure that the contents presented in the markdown file are represented in the folder names (for example last names of members and category titles).

### Getting started:
To get started a YML file is provided and it showcases how all of the aforementioned solutions can be used in tandem (this file is supposed to be placed inside the workflow folder and it assumes that the python files are located inside the tool folder). To modify the preferred file contents simply change the JSON used within the YML file. Remember that the JSON is composed of regex expressions by which file lines must abide by.