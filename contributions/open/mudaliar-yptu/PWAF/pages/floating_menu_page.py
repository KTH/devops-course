"""
@author: Yi-Pei Tu
@email: yptu@kth.se
@date: 21-Apr-19
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FloatingMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Floating Menu"
        self.xpath_heading = "//h3"
        self.xpath_menu = "//*[@id='menu']"
        self.css_attr = "position"
        self.css_value = "absolute"

    def verify_floating_menu_page(self):
        """
        This method is to verify Floating Menu page.

        return: instance of Floating Menu page
        rtype: Floating Menu Page instance
        """
        logging.info("## Verifying Floating Menu page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Floating Menu page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_floating_menu(self):
        """
        This method is to verify Floating Menu after scrolling.
        The menu should always be on the top.
        """
        # the position should be absolute for floating
        css_floating = self.services.get_css_by_xpath(self.xpath_menu, self.css_attr)
        assert css_floating == self.css_value, "The attribute of position should be %s" % self.css_value
        
        # after scrolling, the y value should be different
        before_scrolling = self.services.get_position_by_xpath(self.xpath_menu)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.services.wait_for_element(self.xpath_menu)
        after_scrolling = self.services.get_position_by_xpath(self.xpath_menu)
        assert before_scrolling.get("y") != after_scrolling.get("y"), "The position should be different after scrolling"
        