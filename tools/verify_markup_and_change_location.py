import sys
import re
from itertools import permutations

class Member:
    def __init__(self, name, email, github):
        self.name = name
        self.email = email
        self.github = github
    
    def getLastName(self):
        return self.name.split(" ")[-1]

CHANGE_LOCATION = "devops-course/contributions/"
CATEGORY = ["presentation",
            "essay",
            "demo",
            "open-source",
            "executable tutorial",
            "course automation",
            "feedback"]
MARKUP = "README.md"
MAX_MEMBERS = 3

def getLinesFromFile(fileName):
    try:
        file = open(fileName, 'r')
        lines = file.read().lower().splitlines()
        lines = list(filter(None, lines))
        lines = [s.strip() for s in lines]
        return lines
    except:
        sys.exit("Cant open file: " + fileName)

def categoryToFolderName(category):
    return category.replace(" ", "-") + "/"

def checkMD(lines):
    members = []
    category_folder = ""
    
    # Title is must have
    txt = "# {}:"
    if(len(lines) != 0):
        line = lines.pop(0)
        found = False
        
        for t in CATEGORY:
            if(line.startswith(txt.format(t))):
               category_folder = categoryToFolderName(t)
               found = True
               break;
        if(not found):
            sys.exit("Bad task name")
    else:
        sys.exit("No task name")
    
    # Members are must have
    if(len(lines) != 0 and lines[0] == "## members"):
        lines.pop(0)
    else:
        sys.exit("Members section is missing")
    
    while(True):
        # Name is must have
        if(len(lines) != 0 and lines[0].startswith("name:")):
            line = lines.pop(0)
            if(not re.match("^name: [a-z]+( [a-z]+)* [a-z]+$", line)):
                sys.exit("Wrong name")
            name = line.partition(": ")[2]
        else:
            sys.exit("Name was expected")
        
        # Email is must have
        if(len(lines) != 0 and lines[0].startswith("email:")):
            line = lines.pop(0)
            if(not re.match("^email: [a-z]+@kth.se$", line)):
                sys.exit("Wrong email")
            email = line.partition(": ")[2]
        else:
            sys.exit("Email was expected")
        
        #GitHub is optional
        github = None
        if(len(lines) != 0 and lines[0].startswith("github:")):
            line = lines.pop(0)
            if(not re.match("^github: https://github.com/[a-z]+$", line)):
                sys.exit("Wrong github")
            github = line.partition(": ")[2]
            
        members.append(Member(name, email, github))
        
        if(len(lines) == 0):
            sys.exit("Proposal section is missing")
        
        if(lines[0] == "## proposal"):
            break
    
    if(len(members) > MAX_MEMBERS):
        sys.exit("Too many members")
    elif (len(members) == 0):
        sys.exit("Too few members")
        
    return (category_folder, members)

# Verify that the location is correct based on markup file info and return member work folder
def getMemberDirectory(category_folder, markupFile, members):
    lastNames = [m.getLastName() for m in members]
    perms = ['-'.join(p) for p in permutations(lastNames)]
    
    markup = CHANGE_LOCATION + category_folder + "{}/" + MARKUP
    
    for i in perms:
        if(markupFile == markup.format(i)):
            return markupFile
    
    sys.exit("Markup file in wrong folder, expected location: " + markup.format(perms[0]))

# Gets users markup file location
def getMarkupFileLocation(fileLocation):
    print(fileLocation)
    m = re.search('(' + CHANGE_LOCATION + '.+/.+/)', fileLocation)
    if m:
        return m.group(1) + MARKUP
    else:
        sys.exit("Change performed in wrong folder")

# Ensure all changes are within the members folder
def verifyChangeLocation(changes, member_directory):
    for change in changes:
        if(not change.startswith(member_directory)):
            sys.exit("Change performed outside users folder")

def reviewChanges(changes):
    changed_files = changes.split(" ")
    markupFile = getMarkupFileLocation(changed_files[0])
    
    (category_folder, members) = checkMD(getLinesFromFile(markupFile))
    member_directory = getMemberDirectory(category_folder, markupFile, members)
    verifyChangeLocation(changed_files, member_directory)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])