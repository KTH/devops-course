#Hemingway python
from selenium import webdriver
import time
chromedriverPath = "./chromedrivers/chromedriver84.0.4147.30" # Driver depends on your chrome version. Mine is 84.0.4147.30. See https://chromedriver.chromium.org/downloads


def getElement(xpath, driver):
    return driver.find_element_by_xpath(xpath)

def getElementText(xpath, driver):
    return driver.find_element_by_xpath(xpath).text

def parseDataContent(dataContent): # Method for parsing through the datacontent and obtain the feedback on sentences #@TODO
    pass

def getHemingwayScore(text):
    if not(isinstance(text, str)): # Call with filepath
        file = open(text, "r") 
        text = file.read()
    
    driver = webdriver.Chrome(chromedriverPath) 
    driver.get("https://hemingwayapp.com/")

    # Finding and pasting
    hemingwaycontainer = '//*[@id=\"hemingway-container\"]/div[2]/div/div[2]/div/div/div'
    driver.find_element_by_xpath(hemingwaycontainer).click() # Click on the primary text container
    driver.find_element_by_xpath(hemingwaycontainer).clear() # Clear it of any default text
    driver.find_element_by_xpath(hemingwaycontainer).send_keys("") # Paste the text (string) to the container
    driver.find_element_by_xpath(hemingwaycontainer).send_keys(text) # Paste the text (string) to the container

    time.sleep(3) # Incase the hemingway editor needs a bit of time. Not sure if needed at all or if long enough. 

    # Gathering information
    gradeValue = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[1]/h4", driver)
    gradeWord = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[1]/p/p/strong", driver) 
    wordCount = int(getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[2]/div[1]/strong", driver)) - 133 # For some reason, the default value is not reset upon clear. The length of the default text is 133.
    adverbs = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[1]/strong", driver)
    passiveVoice = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[2]/strong", driver)
    complexWords = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[3]/strong", driver)
    hardReadability = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[4]/strong", driver)
    veryHardReadability = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[5]/strong", driver)

    # WIP/#@TODO. Returning the graded sentences.
    #dataContentPath = "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div"
    #dataContent = getElement(dataContentPath, driver)
    #feedbackText = parseDataContent(dataContent)
    #print(dataContent)

    # Compile to readable format
    verdict = "Hemingway verdict\n   Grade Numeric:{}\n   Grade:{}\n   Wordcount:{}\n   Adverbs:{}\n   Passive Voice uses:{}\n   ComplexWords:{}\
        \n   Sentences that are hard to read:{}\n   Sentences that are very hard to read:{}"\
        .format(gradeValue, gradeWord, wordCount, adverbs, passiveVoice, complexWords, hardReadability, veryHardReadability)

    
    
    print(verdict)
    return verdict

getHemingwayScore("Testing more words for hemingway")

