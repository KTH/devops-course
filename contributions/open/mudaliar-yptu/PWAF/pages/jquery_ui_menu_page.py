"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 20-May-18
"""
import logging

from selenium.webdriver.common.action_chains import ActionChains

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class JQueryUIMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "JQueryUI - Menu"
        self.xpath_heading = "//h3"
        self.xpath_enabled = "//ul[@id='menu']//li/a[text()='Enabled']"
        self.xpath_downloads = "//li/a[text()='Downloads']"
        self.xpath_file_option = "//li/a[text()='%s']"

    def verify_jquery_menu_page(self):
        """
        This method is to verify JQueryUI - Menu page.

        return: instance of JQueryUI - Menu page
        rtype: JQueryUI - MenuPage instance
        """

        logging.info("## Verifying JQueryUI - Menu page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on JQueryUI - Menu page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_jquery_menu(self, file_option="PDF"):
        enabled = self.driver.find_element_by_xpath(self.xpath_enabled)

        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(enabled).perform()
        self.services.wait_for_element_visible(self.xpath_downloads)

        download = self.driver.find_element_by_xpath(self.xpath_downloads)
        action_chains.move_to_element(download).perform()
        self.services.wait_for_element_visible(self.xpath_file_option % file_option)

        option = self.driver.find_element_by_xpath(self.xpath_file_option % file_option)
        action_chains.move_to_element(option).perform()
        self.services.assert_and_click_by_xpath(self.xpath_file_option % file_option)
