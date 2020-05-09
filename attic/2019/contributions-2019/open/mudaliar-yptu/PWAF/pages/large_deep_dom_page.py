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


class LargeDeepDomPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Large & Deep DOM"
        self.xpath_heading = "//h3"
        self.js_no_siblings = "$('div.parent')"
        self.js_no_siblings_length = 52
        self.js_table = "$('td')"
        self.js_table_length = 2500
        

    def verify_large_deep_dom_page(self):
        """
        This method is to verify Large Deep Dom page.

        return: instance of Large Deep Dom page
        rtype: Large Deep Dom instance
        """
        logging.info("## Verifying Large Deep Dom page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Large Deep Dom page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_large_deep_dom_no_sibling(self):
        """
        This method is to verify Large Deep Dom with no sibling by executing jquery
        The result should be the same as the input
        """
        length_no_sibling = self.driver.execute_script("return %s.length"%self.js_no_siblings)
        assert length_no_sibling == self.js_no_siblings_length, "Actual depth of no siblings should be %d" % self.js_no_siblings_length

    def verify_large_deep_dom_table(self):
        """
        This method is to verify Large Deep Dom with table by executing jquery
        The result should be the same as the input
        """
        length_table = self.driver.execute_script("return %s.length"%self.js_table)
        assert length_table == self.js_table_length, "Actual depth of no siblings should be %d" % self.js_table_length

    