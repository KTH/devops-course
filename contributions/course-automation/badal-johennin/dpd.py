import os
import spacy
from github import Github
import sys
import requests

import json

def get_req(api_url):
    headers = {'content-type': 'application/json'}
    response = requests.get(api_url,allow_redirects=False,headers=headers).json()

    return "/".join(response[0]['filename'].split("/")[:-1])



ref = sys.argv[1]
api_URL = f'https://api.github.com/repos/johennin/devops-course/pulls/{ref}/files'
filename = get_req(api_URL)

all_readme = []
nlp = spacy.load('en_core_web_md')
stopwords = nlp.Defaults.stop_words
stopwords |= {"#",} ##add additional to default stopwords

## Preprocess the current readme's into a list of all_readme's
cwd = os.path.abspath(os.getcwd())
cwd_search = "/".join(cwd.split("/")[:-2])
matches = ["week","course","presentation","contributions","feedback","executable","demo","essay","open-source"]

print("Start walk")
print("Listing all filepaths and files to compare")
for root, dirs, files in os.walk(cwd_search):
    #print(root,dirs,files)
    
    if not(any(x in root.split("/")[-1] for x in matches)) and not("attic" in root) and ("contributions" in root):

        if "README.md" in files:
            print(root,files)
            current_readme = open(root+"/README.md")
            string = "".join(current_readme.readlines())
            temp_string = []
            for word in string.split():
                if not(word in stopwords):
                    temp_string.append(word)
            if filename in root:
                check = " ".join(temp_string)
            else:
                all_readme.append((root," ".join(temp_string))) ##joining without space yields better results?
print(f'{len(all_readme)} READMEs found in repository')
    
if not(check):
    sys.exit("No readme in pull request")

print("Starting NLP check")
check = nlp(check)
failed = []
for fp,readme in all_readme:
    x = nlp(readme)
    similarity = check.similarity(x)
    if similarity >= 0.99:
        print(f'Current README is {similarity*100}% similar to the README on filepath: {fp} ')
        failed.append(similarity)


if failed:
    print(f'{len(failed)}/{len(all_readme)} checks failed')
    sys.exit("Similar README found in repository")
else:
    print(f'All checks have passed')


    


#GITHUB_TOKEN = os.environ('GITHUBTOKEN')
#g = Github(GITHUB_TOKEN)
#print(ref)
#print(g)
#repo = "johennin/devops-course"
#pr = repo.get_pull(ref)
#pr.create_issue_comment('test')
