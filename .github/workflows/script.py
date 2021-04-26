import os, re
from github import Github 
import sys


g = Github(login_or_token=sys.argv[1])
repo = g.get_repo("Hilaire-Bouaddi/devops-course")
#print(repo.name)

#THIS SECTION FINDS THE PRs THAT ARE FEEDBACKED

path_to_feedback = "contributions/feedback/"
feedback_folders_names = list(filter(lambda name: os.path.isdir(path_to_feedback+name), os.listdir(path_to_feedback)))
feedbacked = [] # this will be the list of feedbacked PR 

for name in feedback_folders_names:
    files = os.listdir(path_to_feedback+name)
    
    if len(files) == 1 and files[0][-3:].lower()==".md":
        markdown = files[0]
        content = open(path_to_feedback+name+"/"+markdown, encoding="utf-8").read()
        results = re.search("#[0-9]+", content)

        if results:
            feedbacked.append(results.group())

print(feedbacked)


#THIS SECTION FINDS THE PRs THAT WILL BE FEEDBACKED 


#THIS SECTION APPLIES THE LABELS

pr_number = feedbacked[0][1:]
pr = repo.get_pull(1)
pr_labels = pr.labels

print(pr.title)
print(pr_labels)