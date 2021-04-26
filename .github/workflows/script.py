import os, re

path_to_feedback = "contributions/feedback/"
feedback_folders_names = list(filter(lambda name: os.path.isdir(path_to_feedback+name), os.listdir(path_to_feedback)))

feedbacked = []

for name in feedback_folders_names:
    files = os.listdir(path_to_feedback+name)
    
    if len(files) == 1 and files[0][-3:].lower()==".md":
        markdown = files[0]
        content = open(path_to_feedback+name+"/"+markdown, encoding="utf-8").read()
        results = re.search("#[0-9]+", content)

        if results:
            feedbacked.append(results.group())

print(feedbacked)

from github import Github 

g = Github(login_or_token="access_token")

import sys
print(sys.argv[1])