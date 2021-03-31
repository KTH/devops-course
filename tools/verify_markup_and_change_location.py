import sys
import re
from itertools import permutations

'''
Member: Class used for storing group member info

name- full name
email- email adress
github- link to github account

At this time only the name is used to extract the family name, with other
variables left for furture use.

'''
class Member:
    
    def __init__(self, name, email, github):
        self.name = name
        self.email = email
        self.github = github
    
    '''
    Extracts family name from name
    '''
    def get_family_name(self):
        return self.name.split(" ")[-1]

'''
CHANGE_LOCATION: constant variable used for defining location of changes
'''
CHANGE_LOCATION = "contributions/"
'''
CATEGORY: constant variable used for defining possible categories of work 
'''
CATEGORY = ["presentation",
            "essay",
            "demo",
            "open-source",
            "executable tutorial",
            "course automation",
            "feedback"]
'''
MARKUP: constant variable used for defining the name of a markdown file (it is
a must have within the member folder)
'''
MARKDOWN = "README.md"
'''
MAX_MEMBERS: constant variable used for defining the number of members allowed
in one group
'''
MAX_MEMBERS = 3

'''
Extracts lines from a file

Returns a list of non empty lines, with all leters transformed to lower case
'''
def get_lines_from_file(file_name):
    try:
        file = open(file_name, 'r')
        lines = file.read().lower().splitlines()
        lines = list(filter(None, lines))
        lines = [s.strip() for s in lines]
        return lines
    except:
        sys.exit("Cant open file: " + file_name)

'''
Transforms category string to valid folder name
'''
def category_to_folder_name(category):
    return category.replace(" ", "-") + "/"

'''
Gets line from lines iff the current line starts with the necassary text, 
otherwise, depending on the "necassary" variable either None will be returned
or exit will be performed.
'''
def get_expected_content(lines, text, necassary = True):
    if(len(lines) != 0 and lines[0].startswith(text)):
        return lines.pop(0)
    else:
        if necassary:
            sys.exit("Expected, but not found: " + text)
        else:
            return None

'''
Returns the first group of search using regex if it was succesful, otherwise,
exit will be performed.
'''
def verify_content(regex, line):
    m = re.search(regex, line)
    if m:
        return m.group(1)
    else:
        sys.exit("Wrong formating for line: " + line)

'''
Verifies that the lines read from a markdown file are following the necassary
format.
'''
def check_markdown(lines):
    members = []
    category_folder = ""
    
    # Title is must have
    txt = "# {}:"
    found = False
    for t in CATEGORY:
        line = get_expected_content(lines, txt.format(t), False)
        if line != None:
            category_folder = CHANGE_LOCATION + category_to_folder_name(t)
            found = True
            break
    if(not found):
        sys.exit("Bad task name")
    
    # Members are must have
    get_expected_content(lines, "## members")
    
    while(True):
        # Name is must have
        start_with = "name:"
        line = get_expected_content(lines, start_with)
        name = verify_content("^" + start_with +
                              " ([a-z]+( [a-z]+)* [a-z]+)$", line)
        
        # Email is must have
        start_with = "email:"
        line = get_expected_content(lines, start_with)
        email = verify_content("^" + start_with + " ([a-z]+@kth.se)$", line)
        
        #GitHub is optional
        start_with = "github:"
        line = get_expected_content(lines, start_with, False)
        if line != None:
            github = verify_content("^" + start_with +
                                    " (https://github.com/[a-z]+)$", line)
        else:
            github = None
            print("Github not provided")
            
        members.append(Member(name, email, github))
        
        
        if(len(lines) == 0):
            sys.exit("Proposal section is missing")
        
        #leave loop if see that next section starts
        if lines[0].startswith("##"):
            break
    
    # Proposal is must have
    get_expected_content(lines, "## proposal")
    
    if(len(members) > MAX_MEMBERS):
        sys.exit("Too many members")
        
    return (category_folder, members)

'''
Verify that the location where markdown file is strored is correct, this is
done based on markdown file info and it returns location of folder where
members should have been working in.
'''
def get_member_directory(category_folder, markdown_file, members):
    lastNames = [m.get_family_name() for m in members]
    perms = ['-'.join(p) for p in permutations(lastNames)]
    
    markdown = category_folder + "{}/" + MARKDOWN
    
    for i in perms:
        if(markdown_file == markdown.format(i)):
            return markdown_file
    
    sys.exit("Markup file in wrong folder, expected location: " +
             markdown.format(perms[0]))

'''
Gets users markdown file location, based one changed file location 
'''
def get_markdown_file_location(file_location):
    m = re.search('^(' + CHANGE_LOCATION + '.+/.+/)', file_location)
    if m:
        return m.group(1) + MARKDOWN
    else:
        sys.exit("Change performed in wrong folder")

'''
Ensure all changes are done within the provided folder
'''
def verify_change_location(changed_files, folder):
    for change in changed_files:
        if(not change.startswith(folder)):
            sys.exit("Change performed outside users folder")

'''
Main entry point for the program
'''
def review_changes(changes):
    #Creates list of changed files from string
    changed_files = changes.split(" ")
    
    #Gets location of the markup file based on the location of the first change
    markdown_file = get_markdown_file_location(changed_files[0])
    
    #Verifies that markdown file contains the necassary info
    lines = get_lines_from_file(markdown_file)
    (category_folder, members) = check_markdown(lines)
    
    #Get directory where all changes had to be made
    member_directory = get_member_directory(category_folder, markdown_file,
                                            members)
    
    #Verify that no changes are made outside specific directory
    verify_change_location(changed_files, member_directory)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])