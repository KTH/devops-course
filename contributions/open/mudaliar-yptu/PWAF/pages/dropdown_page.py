"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 16-Apr-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
from selenium.webdriver.support.select import Select
from time import sleep


class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Dropdown List"
        self.xpath_heading = "//h3"
        self.xpath_dropdown = "//select[@id='dropdown']"

    def verify_dropdown_page(self):
        """
        This method is to verify Dropdown page.

        return: instance of Dropdown page
        rtype: DropdownPage instance
        """

        logging.info("## Verifying Dropdown page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Dropdown page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def select_dropdown_option(self, opt):
        """
        This method is to select value in dropdown.
        @param opt: visible text
        type opt: string
        """
        select = Select(self.driver.find_element_by_xpath(self.xpath_dropdown))

        #select.select_by_index(1)
        #select.select_by_value("2")
        
        select.select_by_visible_text(opt)
        sleep(1)
        actual = select.first_selected_option.text
        assert actual == opt, "Selected value {0}, should be same as expected {1}".format(actual, opt)
