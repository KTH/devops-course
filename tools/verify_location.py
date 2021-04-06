import sys
import re

CHANGE_LOCATION = "contributions/"
MARKDOWN = "README.md"

def get_change_location(changed_file):
    m = re.search('^' + CHANGE_LOCATION + '(.+)/(.+)/', changed_file)
    if m:
        return m
    else:
        sys.exit("Change performed in wrong folder: " + changed_file)

def verify_change_locations(changed_files, change_location):
    for change in changed_files:
        if(not change.startswith(change_location)):
            sys.exit("Change performed in wrong folder"
                "\nExpected path: " + change_location +
                "\nChange location: " + change)

def main(changes):
    changed_files = changes.split(" ")
    match = get_change_location(changed_files[0])
    verify_change_locations(changed_files, match.group())
    
    markdown_file = match.group() + MARKDOWN
    print(f"::set-output name=markdown::{markdown_file}")
    print(f"::set-output name=categoryfolder::{match.group(1)}")
    print(f"::set-output name=memberfolder::{match.group(2)}")

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])