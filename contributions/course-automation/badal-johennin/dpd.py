import os
import spacy
from github import Github
all_readme = []
nlp = spacy.load('en_core_web_md')
stopwords = nlp.Defaults.stop_words
stopwords |= {"#",} ##add additional to default stopwords

## Preprocess the current readme's into a list of all_readme's

for root, dirs, files in os.walk("/home/runner/work/devops-course/devops-course/", topdown=True):
    #print(root,dirs,files)
    
    if (root.count("/")==5 and not("presentation" in root)) or (root.count("/")==6 and ("presentation" in root)):
        print(root,files)
        if "README.md" in files:
            current_readme = open(root+"/README.md")
            string = "".join(current_readme.readlines())
            temp_string = []
            for word in string.split():
                if not(word in stopwords):
                    temp_string.append(word)
            all_readme.append(" ".join(temp_string)) ##joining without space yields better results?

    

check = nlp(all_readme[4])

for readme in all_readme:
    x = nlp(readme)
    print(check.similarity(x))

#GITHUB_TOKEN = os.environ('GITHUB_TOKEN')
g = Github(GITHUB_TOKEN)
ref = os.environ('GITHUB_REF')
repo = "johennin/devops-course"
pr = repo.get_pull(ref)
pr.create_issue_comment('test')
