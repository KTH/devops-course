#python
from github import Github
import time
import aPDF

#Constants
REPO_ID = 337456664 #Used to find which repo to look at
REPO_NAME = "daTest"
TOKEN = "" #Used by Github library to find User
USER = Github(TOKEN) #This is the user that is nav Github
def test():
    # using an access token
    #REMOVE THIS!
    
    for repo in g.get_user().get_repos():
        if repo.name == "daTest":
            print("I found daTest")
            #repo.create_issue(title="test repo hopefully this is right")
            print(str(repo.get_pulls().totalCount))
            
            #print(dir(repo))
     
def findTheRepo():
    repo = USER.get_repo(REPO_ID)
    if repo.name == REPO_NAME:
        return repo
    else:
        raise Exception("Repo ID and repo name does not match")
def getPDFsFromPullObj(pulls):
    myList = []
    for pull in pulls:
        files = pull.get_files()
        if files.totalCount > 0:
            for file in files:
                if ".pdf" in file.filename:
                    #We have found a report, add to list with obj
                    newPDF = aPDF.aPDF(file.filename, file.raw_url, file.sha, pull)
                    myList.append(newPDF)
    return myList

def checkFiles(myPull):
    files = myPull.get_files()
    if files.totalCount > 0:
        for file in files:
            if ".pdf" in file.filename:
                return True
    return False
    
def removeWrongPRs(aList):
    returnList = []
    #pr is a Finalized thingy & is a essay & has not yet a comment from me:
    for pull in aList:
        if "final" in pull.title.lower() and \
        ("essay" in pull.body.lower()  or "essay" in pull.title.lower() ) and \
        checkFiles(pull):
            for comment in pull.get_comments():
                if "Hemingway" in comment.body:
                    #A hemingway comment was found, nogo
                    print("This pull request " + str(pull.title) + " was not added to list")
                    continue
            #No Hemingway in any comment means that I need to write a comment for this pull
            returnList.append(pull)
            print("This pull request " + str(pull.title) + " was added to list")
    return returnList

#Find repo
currentRepo = findTheRepo()

#Code for creating issue: results = pull.create_issue_comment("Hemingway")

#Start loop:
while True:
    print("New Loop")
    #Get all pull requests
    allPRs = currentRepo.get_pulls()
    #Remove all pull requests that are unrelated to this bot
    validPRs = removeWrongPRs(allPRs)
    
    print("These posts need hemingway comments:")
    for item in validPRs:
        print("\t" + str(item.number) + "," + item.title)
    
    #Find all valid pdf's and give them to me, with their pull obj
    pdfsAndPulls = getPDFsFromPullObj(validPRs)
    print("These files need to be Hemingway'd")
    for item in pdfsAndPulls:
        print(item.name)
    #Sleep 30 seconds
    print("Sleeping")
    time.sleep(10)





    
