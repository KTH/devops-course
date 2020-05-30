"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
@date: 21-Apr-19
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JavaScriptAlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "JavaScript Alerts"
        self.xpath_heading = "//h3"
        self.xpath_alert = "//button[@onClick = 'jsAlert()']"
        self.xpath_confirm = "//button[@onClick = 'jsConfirm()']"
        self.xpath_prompt = "//button[@onClick = 'jsPrompt()']"
        self.xpath_result = "//p[@id = 'result']"

    def verify_javascript_alerts_page(self):
        """
        This method is to verify JavaScript Alerts page.

        return: instance of JavaScript Alerts page
        rtype: JavaScript Alerts Page instance
        """
        logging.info("## Verifying JavaScript Alerts page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on JavaScript Alerts page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_javascript_alert(self):
        """
        This method is to verify javascript alert.
        """
        alert_button = self.driver.find_element_by_xpath(self.xpath_alert)
        alert_button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert "I am a JS Alert" in alert.text
        alert.accept()

    def verify_javascript_confirm(self):
        """
        This method is to verify javascript confirm.
        """
        confirm_button = self.driver.find_element_by_xpath(self.xpath_confirm)
        confirm_button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert "I am a JS Confirm" in alert.text
        alert.dismiss()

    def verify_javascript_prompt(self, txt):
        """
        This method is to verify javascript prompt.
        """
        prompt_button = self.driver.find_element_by_xpath(self.xpath_prompt)
        result_txt = self.driver.find_element_by_xpath(self.xpath_result)
        prompt_button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert "I am a JS prompt" in alert.text
        self.driver.switch_to.alert.send_keys(txt)
        assert "You entered: ", txt in result_txt.get_attribute('innerHTML')
        alert.accept()
