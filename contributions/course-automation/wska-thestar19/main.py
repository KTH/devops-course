#python
from github import Github
import time
import aPDF
import urllib.request
import subprocess
import hemingway
import sys

#Constants
REPO_ID = 337456664 #Used to find which repo to look at
REPO_NAME = "daTest"
TOKEN = "" #Used by Github library to find User
     
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
def runCommand(command):
    return subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )    
def removeWrongPRs(aList):
    returnList = []
    #pr is a Finalized thingy & is a essay & has not yet a comment from me:
    for pull in aList:
        doAdd = True
        if "final" in pull.title.lower() and \
        ("essay" in pull.body.lower()  or "essay" in pull.title.lower() ) and \
        checkFiles(pull):
            for comment in pull.get_issue_comments():
                if "hemingway" in comment.body.lower():
                    #A hemingway comment was found, nogo
                    print("This pull request " + str(pull.title) + \
                    " was not added to list")
                    doAdd = False
                    break
            #No Hemingway in any comment means that I need to write a comment for this pull
            if doAdd:
                returnList.append(pull)
                print("This pull request " + str(pull.title) + " was added to list")
    return returnList

#take in arguments
if len(sys.argv) < 1:
    if len(TOKEN) < 10:
        print("No token in main AND no token in arguments, exiting")
        raise Exception("No token given, please pass as arg or set in main")
    else:
        print("Using token from main, do not git push this")
else:
    if len(sys.argv[1]) > 0:
        TOKEN = sys.argv[1]

#Create user that will navigate Github
USER = Github(TOKEN)

#Find repo
currentRepo = findTheRepo()

#Code for creating issue: results = pull.create_issue_comment("Hemingway")

#Start loop:
while True:
    #Get all pull requests
    allPRs = currentRepo.get_pulls()
    
    #Remove all pull requests that are unrelated to this bot
    validPRs = removeWrongPRs(allPRs)
    if len(validPRs) < 1:
        print("Debug: No posts found, please add some in daTest")
    else:
        print("These posts need hemingway comments:")
        for item in validPRs:
            print("\t" + str(item.number) + "," + item.title) 
        
    #Find all valid pdf's and give them to me, with their pull obj
    PDFobj = getPDFsFromPullObj(validPRs)
    
    #Download PDF's and convert to txt
    for item in PDFobj:
        #Download a PDF using link
        onlyName = item.name.split("/").pop()
        item.nameOfFile = onlyName
        fileName = urllib.request.urlretrieve(item.url, "PDF/" + str(onlyName))
        #Save path of download to obj
        item.path = "PDF/" + str(onlyName)
    
    #Convert to txt
    for item in PDFobj:
        #Remove .pdf from filename
        runCommand("python3 Tools/pdf2txt.py " + item.path + " > Text/" + item.nameOfFile.replace(".pdf",".txt"))
        #Save txt to obj
        f = open("Text/" + item.nameOfFile.replace(".pdf",".txt"), "r+")
        allOfText = ""
        for line in f:
            allOfText = allOfText + line
        item.asText = allOfText
    #Send text to Hemingway
    for item in PDFobj:
        item.hemingwayReponse = hemingway.getHemingwayScore(item.asText)
    #Make PR request
    #This is right now buggy if commit includes more than one file
    for item in PDFobj:
        results = item.pull.create_issue_comment(item.hemingwayReponse)
    #Sleep 30 seconds
    print("Sleeping---------------------------------")
    time.sleep(20)





    
