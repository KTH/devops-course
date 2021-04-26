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
            feedbacked.append(int(results.group()[1:]))

print(feedbacked)


#THIS SECTION FINDS THE PRs THAT WILL BE FEEDBACKED 



#THIS SECTION CREATES LABELS IF THEY DON'T EXIST IN THE REPO
labels_repo = [l.name for l in repo.get_labels()]

label_names = ["feedbackable", "feedback claimed", "feedbacked"]
colors = ["FFDC73", "97B1F3", "3D5BA5"]
for i in range(3):
    if label_names[i] not in labels_repo:
        repo.create_label(label_names[i], colors[i])

#THIS SECTION APPLIES THE LABELS


for pr in repo.get_pulls(state="closed"):
    if pr.is_merged(): # we are only interested in merged pull requests
        pr_labels = pr.labels
        for label in pr_labels:
            if label.name in label_names:
                pr.remove_from_labels(label)
        
        if pr.number in feedbacked:
            pr.add_to_labels("feedbacked")
        else:
            pr.add_to_labels("feedbackable")