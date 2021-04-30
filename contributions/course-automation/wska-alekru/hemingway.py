#Hemingway python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def getElementText(xpath, driver):
    return driver.find_element_by_xpath(xpath).text

def parseDataContent(dataContent): # Method for parsing through the datacontent and obtain the feedback on sentences #@TODO
    pass

def getHemingwayScore(text):
    if not(isinstance(text, str)): # Call with filepath
        raise TypeError("Text input is not of string type.")
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
    driver.get("https://hemingwayapp.com/")
    time.sleep(1)

    # Finding and pasting
    hemingwaycontainer = '//*[@id=\"hemingway-container\"]/div[2]/div/div[2]/div/div/div'
    driver.find_element_by_xpath(hemingwaycontainer).click() # Click on the primary text container
    driver.find_element_by_xpath(hemingwaycontainer).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    draftContainer = "//*[@id=\"hemingway-container\"]/div[2]/div/div[2]" # The container is converted into an alternative container when it is empty, so use this for the paste.
    driver.find_element_by_xpath(draftContainer).send_keys(text) # Paste the text (string) to the container

    time.sleep(3) # Incase the hemingway editor needs a bit of time. Not sure if needed at all or if long enough. 

    # Gathering information
    gradeValue = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[1]/h4", driver)
    gradeWord = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[1]/p/p/strong", driver) 
    wordCount = int(getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[2]/div[1]/strong", driver))
    adverbs = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[1]/strong", driver)
    passiveVoice = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[2]/strong", driver)
    complexWords = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[3]/strong", driver)
    hardReadability = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[4]/strong", driver)
    veryHardReadability = getElementText("//*[@id=\"hemingway-container\"]/div[1]/div[2]/div[3]/div[5]/strong", driver)

    # Compile to readable format
    verdict = "Hemingway verdict\n   Grade Numeric:{}\n   Grade:{}\n   Wordcount:{}\n   Adverbs:{}\n   Passive Voice uses:{}\n   ComplexWords:{}\
        \n   Sentences that are hard to read:{}\n   Sentences that are very hard to read:{}"\
        .format(gradeValue, gradeWord, wordCount, adverbs, passiveVoice, complexWords, hardReadability, veryHardReadability)

    print(verdict)
    driver.quit()
    return verdict