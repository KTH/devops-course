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
        sys.exit("Cant open file: " + file_name)

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


def get_expected_content(lines, text, necassary = True):
    '''
    Gets contents if it was expected.
    
    Gets line from lines iff the current line starts with the provided text, 
    otherwise, depending on the "necassary" variable either None will be
    returned or exit will be performed.
    
    Args:
        lines: Lines read from file.
        text: String value indicating how line should start.
        necassary: Boolean used to decide if line must start with text.
        
    Returns:
        Line.
    '''
    if(len(lines) != 0 and lines[0].startswith(text)):
        return lines.pop(0)
    else:
        if necassary:
            sys.exit("Expected, but not found: " + text)
        else:
            return None

def verify_content(regex, line):
    '''
    Verifies contents of line.
    
    Returns the first group of search using regex if it was succesful,
    otherwise, exit will be performed.
    
    Args:
        regex: Regex formated string value.
        line: text to search using regex.
        
    Returns:
        first group found.
    '''
    m = re.search(regex, line)
    if m:
        return m.group(1)
    else:
        sys.exit("Wrong formating for line: " + line)

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
    txt = "# {}:"
    found = False
    for t in CATEGORY:
        line = get_expected_content(lines, txt.format(t), False)
        if line != None:
            category_folder = CHANGE_LOCATION + category_to_folder_name(t) + "/"
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
    
    sys.exit("Markup file in wrong folder, expected location: " +
             markdown.format(perms[0]))

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
        sys.exit("Change performed outside users folder")

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
            sys.exit("Change performed outside users folder")

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