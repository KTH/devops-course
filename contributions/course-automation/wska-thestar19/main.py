#python
from github import Github
import time
import aPDF
import urllib.request
import subprocess
import hemingway
import sys

#Constants
REPO_ID = 131834720 #Used to find which repo to look at
REPO_NAME = "devops-course"
TOKEN = "" #Used by Github library to find User, is sometimes set by argument

#The function uses the global "user" and returns the correct repo obj
def findTheRepo():
    repo = USER.get_repo(REPO_ID)
    if repo.name == REPO_NAME:
        return repo
    else:
        raise Exception("Repo ID and repo name does not match")

#The function takes a list of "pull" obj and returns it's PDF's
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

#The function takes a list of "pull" objs and returns if pull contains a pdf file
def checkFiles(myPull):
    files = myPull.get_files()
    if files.totalCount > 0:
        for file in files:
            if ".pdf" in file.filename:
                return True
    return False
#The function takes a os ubuntu command, runs it in a terminal and returns the results.
def runCommand(command):
    return subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
#Function takes a list of pulls and returns a list of pulls that should get a hemingway reponse    
def removeWrongPRs(aList):
    returnList = []
    #pr is a Finalized thingy & is a essay & has not yet a comment from me:
    for pull in aList:
        doAdd = None
        if checkFiles(pull):
            if "!hemingway" in pull.body:
                doAdd = True
            for comment in pull.get_issue_comments():
                if "hemingway verdict" in comment.body.lower():
                    #A hemingway comment was found, nogo
                    print("This pull request " + str(pull.title) + \
                    " was not added to list")
                    doAdd = False
                    break
                if "!hemingway" in comment.body.lower():
                    doAdd = True
            #No Hemingway in any comment means that I need to write a comment for this pull
            if doAdd:
                returnList.append(pull)
                print("This pull request " + str(pull.title) + " was added to list")
    return returnList

#Check if token is given as an argument
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

#Find repo that we should look at
currentRepo = findTheRepo()

#Get all pull requests from repo
allPRs = currentRepo.get_pulls()

#Remove all pull requests that are unrelated to this bot
validPRs = removeWrongPRs(allPRs)
if len(validPRs) < 1:
    print("Debug: No posts found, please add some in" + REPO_NAME)
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
    fileName = urllib.request.urlretrieve(item.url, str(onlyName))
    #Save path of download to obj
    item.path = str(onlyName)
    
#Convert to txt
for item in PDFobj:
    #Remove .pdf from filename
    print("python3 contributions/course-automation/wska-thestar19/pdf2txt.py " + item.path + " > " + item.nameOfFile.replace(".pdf",".txt"))
    print(runCommand("python3 contributions/course-automation/wska-thestar19/pdf2txt.py " + item.path + " > " + item.nameOfFile.replace(".pdf",".txt")))
    #Save txt to obj
    f = open(item.nameOfFile.replace(".pdf",".txt"), "r+")
    allOfText = ""
    for line in f:
        allOfText = allOfText + line
    item.asText = allOfText

#Send text to Hemingway
for item in PDFobj:
    print(item.asText)
    item.hemingwayReponse = hemingway.getHemingwayScore(item.asText)

#Make PR request
#This is right now buggy if commit includes more than one file
for item in PDFobj:
    theComment = "File: " + str(item.name) + "@" + item.url + "\n" + \
    item.hemingwayReponse + \
    "\n \nTo run this bot again, please delete this comment.\n \
    You might have to wait a while, or comment !hemingway again"
    results = item.pull.create_issue_comment(theComment)




    
