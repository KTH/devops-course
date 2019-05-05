"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class MultipleWindowsPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Opening a new window"
        self.xpathHeading = "//h3"
        self.cssLink = "div.example > a"

    def verify_multiple_windows_page(self):
        """
        This method is to verify Multiple Windows page.

        return: instance of Multiple Windows page
        rtype: Multiple Windows Page instance
        """

        logging.info("## Verifying Multiple Windows page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on Multiple Windows page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_next_window_txt(self):
        self.driver.find_element_by_css_selector(self.cssLink).click()

        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                assert "New Window" == self.driver.title
