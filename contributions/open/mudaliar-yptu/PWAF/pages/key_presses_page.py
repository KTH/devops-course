"""
@author: Yi-Pei Tu
@email: yptu@kth.se
@date: 24-Apr-19
"""
import logging

from utility.services import Services
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class KeyPressesPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Key Presses"
        self.xpath_heading = "//h3"
        self.xpath_result = "//*[@id='result']"
        self.send_keys = {'ENTER': Keys.ENTER, 'A': 'a' }

    def verify_key_presses_page(self):
        """
        This method is to verify Key Presses page.

        return: instance of Key Presses page
        rtype: Key Presses Page instance
        """
        logging.info("## Verifying Key Presses page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Key Presses page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_key_presses(self):
        """
        This method is to verify Key Presses after input.
        The result should be the same as the input
        """
        for result, key in self.send_keys.items():
            ActionChains(self.driver).send_keys(key).perform()
            self.services.wait_for_element(self.xpath_result)
            key_result = self.services.get_text_by_xpath(self.xpath_result)
            assert key_result == "You entered: %s" % result, "The result should be %s after input" % result
        