from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.set_page_load_timeout(10)

driver.get("http://google.com")
time.sleep(5)
driver.find_element_by_name("q").send_keys("Kartik Mudaliar")
time.sleep(5)
driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()



