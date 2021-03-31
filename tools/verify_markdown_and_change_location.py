import sys
import re
from itertools import permutations

class Member:
    '''
    Member
    
    Holds information about each member
    '''
    
    def __init__(self, name, email, github):
        """
        Initialize Member class.
        
        Sets up Member variables.
        
        Args:
            name: Group members full name.
            email: Group members email address.
            github: Link to group members github page.
        """
        self.name = name
        self.email = email
        self.github = github
    
    
    def get_family_name(self):
        '''
        Gets family name.
        
        Extracts family name from name.
        
        Returns:
            family name.
        '''
        return self.name.split(" ")[-1]

"""
Verify markdown and change location module.

Verifies that data provided within markdown file is sufficient and correct, 
while also ensuring that no changes have been performed outside dedicated 
member folder.

Attributes:
    CHANGE_LOCATION: Defines location where changes can take place.
    CATEGORY: List of possible categories for work.
    MARKDOWN: Necassary markdown file name (must be present in member folder).
    MAX_MEMBERS: Variable defining maximum team size.
"""

CHANGE_LOCATION = "contributions/"
CATEGORY = ["presentation",
            "essay",
            "demo",
            "open-source",
            "executable tutorial",
            "course automation",
            "feedback"]
MARKDOWN = "README.md"
MAX_MEMBERS = 3

def inform_user(text):
    '''
    Informs user of issue.
    
    Showcases the provided text before exiting.
    
    Args:
        text: Informative text regarding issue.
    '''
    sys.exit("\nEncountered Problem:" +
             "\n" + text + "\n")

def get_lines_from_file(file_name):
    '''
    Gets lines from file
    
    Extracts lines from a list of non empty lines, with all leters transformed
    to lower case.
    
    Args:
        file_name: Name of the file to be read.
        
    Returns:
        List of lines.
    '''
    try:
        file = open(file_name, 'r')
        lines = file.read().lower().splitlines()
        lines = list(filter(None, lines))
        lines = [s.strip() for s in lines]
        return lines
    except:
        inform_user("Cant open file: " + file_name)

def category_to_folder_name(category):
    '''
    Converts category to folder name
    
    Transforms category string to valid folder name.
    
    Args:
        category: Text to be transformed.
        
    Returns:
        Folder name.
    '''
    return category.replace(" ", "-")


def search_line(lines, regex, info, necassary = True):
    '''
    Searches line.
    
    Returns Match from lines iff the current line can find something by searching
    using regex, otherwise, depending on the "necassary" variable either None
    will be returned or exit will be performed.
    
    Args:
        lines: Lines read from file.
        regex: Regex formated string value.
        necassary: Boolean used to decide if line must start with text.
        
    Returns:
        Match (allowing for extaction of data based on query).
    '''
    if(len(lines) != 0):
         m = re.search(regex, lines[0])
         if m:
             lines.pop(0)
             return m
         else:
             if necassary:
                 inform_user("Problem retreiving line for: " + info +
                             "\nExpression to sattisfy: " + regex +
                             "\nCurrent line formating: " + lines[0])
    else:
        if necassary:
            inform_user("Out of lines, cannot sattisfy regex expression: " + regex)

def check_markdown(lines):
    '''
    Checks markdown files contents.
    
    Verifies that the lines read from a markdown file are following the
    necassary format.
    
    Args:
        lines: Lines read from file.
        
    Returns:
        Expected category folder and group members.
    '''
    members = []
    category_folder = ""
    
    # Title is must have
    txt = "^# {}:.*$"
    found = False
    for t in CATEGORY:
        search_result = search_line(lines, txt.format(t), "Title", False)
        if search_result != None:
            category_folder = CHANGE_LOCATION + category_to_folder_name(t) + "/"
            found = True
            break
    if(not found):
        inform_user("Bad task name")
    
    # Members are must have
    search_line(lines, "^## members$", "Members")
    
    while(True):
        # Name and Email is must have
        regex = "^([a-z]+( [a-z]+)* [a-z]+) (\([a-z]+@kth.se\))$"
        match = search_line(lines, regex, "Name and Email")
        name = match.group(1)
        email = match.group(2)
        
        #GitHub is optional
        regex = "^github: (https://github.com/[a-z]+)$"
        match = search_line(lines, regex, "Github", False)
        github = None
        if match:
            github = match.group(1)
            
        members.append(Member(name, email, github))
        
        if(len(lines) == 0):
            inform_user("Missing proposal section")
        
        #leave loop if see that next section starts
        if lines[0].startswith("##"):
            break
    
    # Proposal is must have
    search_line(lines, "^## proposal$", "Proposal")
    
    if(len(members) > MAX_MEMBERS):
        inform_user("Too many members")
        
    return (category_folder, members)

def get_member_directory(category_folder, markdown_file, members):
    '''
    Gets member directory path.
    
    Verify that the location where markdown file is strored is correct, this is
    done based on markdown file info and it returns location of folder where
    members should have been working in.
    
    Args:
        category_folder: Path to directory where all changes should be present.
        markdown_file: Path to markdown file.
        members: List of group members.
        
    Returns:
        Path inside which all changes should be performed.
    '''
    lastNames = [m.get_family_name() for m in members]
    perms = ['-'.join(p) for p in permutations(lastNames)]
    
    markdown = category_folder + "{}/" + MARKDOWN
    
    for i in perms:
        if(markdown_file == markdown.format(i)):
            return category_folder + i
    
    inform_user("Markdown file in wrong group member folder"
                "\nExpected: " + markdown.format(perms[0]) +
                "\nFound: " + markdown_file)

def get_markdown_file_location(file_location):
    '''
    Gets markdown files location.
    
    Gets users markdown file location, based single changed file path. 
    
    Args:
        file_location: Path to one of the changed files.
        
    Returns:
        Expected markdown file path.
    '''
    m = re.search('^(' + CHANGE_LOCATION + '.+/.+/)', file_location)
    if m:
        return m.group(1) + MARKDOWN
    else:
        inform_user("Change performed in wrong path: " + file_location)

def verify_change_location(changed_files, folder):
    '''
    Verify change locations
    
    Ensure that all changes are done within the provided folder.
    
    Args:
        changed_files: List of files changed.
        folder: Directory that should contain all changes.
    '''
    for change in changed_files:
        if(not change.startswith(folder)):
            inform_user("Change performed in wrong path"
                "\nExpected path: " + folder +
                "\nChange location: " + change)

def review_changes(changes):
    '''
    Review changes
    
    Main entry point for the program.
    
    Args:
        changes: Text value indicating changed file locations separated by
        single space.
    '''
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