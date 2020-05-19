"""
@author: Yi-Pei, Tu
@email: yptu@kth.se
@date: 24-Apr-19
"""
import logging

from selenium.webdriver.common.action_chains import ActionChains
from requests import get
from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class RedirectLinkPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Redirection"
        self.xpath_heading = "//h3"
        self.xpath_here = "//*[@id='redirect']"
        self.xpath_status = "//*[@id='content']/div/ul/li/a[text()=%d]"
        
    def verify_redirect_link_page(self):
        """
        This method is to verify Redirect Link page.

        return: instance of Redirect Link page
        rtype: Redirect Link instance
        """

        logging.info("## Verifying Redirect Link page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Redirect Link page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_redirect_link(self):
        # click the redirect button
        self.services.assert_and_click_by_xpath(self.xpath_here)
        self.services.wait_for_element_visible(self.xpath_status % 200)

    def verify_redirect_link_status_code(self, status_code):
        href = self.services.get_href_by_xpath(self.xpath_status % status_code)
        self.services.assert_and_click_by_xpath(self.xpath_status % status_code)
        request = get(href)
        assert request.status_code == status_code, "Actual status code should be %d" % status_code
        # go back to previous page
        self.driver.back()
        self.services.wait_for_element_visible(self.xpath_status % status_code)
        