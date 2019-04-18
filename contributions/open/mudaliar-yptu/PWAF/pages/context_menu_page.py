"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 13-May-18
"""
import logging
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

from utility.services import Services


class ContextMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Context Menu"
        self.xpathHeading = "//h3"
        self.hot_spot = "//div[@id='hot-spot']"

    def verify_context_menu_page(self):
        """
        This method is to verify Context Menu page.

        return: instance of Context Menu page
        rtype: ContextMenuPage instance
        """

        logging.info('## Verifying context menu page ##')
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on Context Menu page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)
        return self

    def perform_right_click(self):
        self.services.wait_for_element(self.hot_spot)
        logging.info('## Find element on which right click need to perform. ##')
        hot_spot_ele = self.driver.find_element_by_xpath(self.hot_spot)

        actions = ActionChains(self.driver)
        actions.context_click(hot_spot_ele).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        sleep(2)
        alert = Alert(self.driver)
        alert.accept()
