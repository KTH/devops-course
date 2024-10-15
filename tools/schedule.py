#!/usr/bin/python3
# automate the preparation of the schedule
# usage ./schedule.py week4

import subprocess

# get current date and time
import datetime
import re
import sys

# get output of command ls

# get output of command ls
# and store it in a variable

WEEK=sys.argv[1]

output = subprocess.getoutput("git log --oneline contributions/presentation/"+WEEK+" contributions/demo/"+WEEK+"/ contributions/scientific-paper/"+WEEK+"/").split("\n")
output.reverse()

def get_title(content):
    lines = content.split("\n")
    for idx in range(len(lines)):
        line = lines[idx]
        if line.startswith("## Title"):
            if len(lines[idx+1].strip())>0:
                # return next line
                return lines[idx+1]
            if len(lines[idx+2].strip())>0:
                # return next line
                return lines[idx+2]
    return "No title found"


for i in output:
    # print(i)
    # get pull request id from commit message
    # get commit message
    commit_message = i
    # get pull request id
    pull_request_id = re.findall(r"[(]#([0-9]+)[)]", commit_message)
    if len(pull_request_id) == 0:
        continue
    # print( pull_request_id )



    # parse git output
    # get commit hash
    commit_hash = i.split(" ")[0]
    # get list of files in the commit using git command
    files = [x for x in subprocess.getoutput(f"git diff-tree --no-commit-id --name-only -r {commit_hash}").split("\n") if ".md" in x.lower() and ("presentation" in x or "demo" in x or "scientific-paper" in x ) and WEEK in x]
    # print the commit hash
    #print(commit_hash)
    # get content of first file
    # and print it
    for file in files:
        content  = subprocess.getoutput(f"git show {commit_hash}:{file}")
        # parse content as markdown
        title = get_title(content)
        print(f"1. [{title}](https://github.com/KTH/devops-course/pull/{pull_request_id[0]})")   
                






