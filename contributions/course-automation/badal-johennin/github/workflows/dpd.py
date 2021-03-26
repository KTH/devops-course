import os
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
print(is_stop)
all_readme = []
depth = 0
for root, dirs, files in os.walk("../../../../", topdown=True):
    #print(root,dirs,files)
    
    if (root.count("/")==5 and not("presentation" in root)) or (root.count("/")==6 and ("presentation" in root)):
        print(root,files)
        if "README.md" in files:
            current_readme = open(root+"/README.md")
            string = "".join(current_readme.readlines())
            temp_string = []
            for word in string.split():
                if not(word.is_stop):
                    temp_string.append(word)
            all_readme.append("".join(temp_string))

    

#all_readme = ["".join(i) for i in all_readme]

print(len(all_readme))
nlp = spacy.load('en_core_web_md')
check = nlp(all_readme[4].replace("#",""))
#print(all_readme[0])

for readme in all_readme:
    #print(readme)
    x = nlp(readme.replace("#",""))
    print(check.similarity(x))
