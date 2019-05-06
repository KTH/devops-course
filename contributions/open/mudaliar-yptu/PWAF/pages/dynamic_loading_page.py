"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Dynamically Loaded Page Elements"
        self.sub_header_1 = "Example 1: Element on page that is hidden"
        self.sub_header_2 = "Example 2: Element rendered after the fact"
        self.xpath_heading = "//h3"
        self.xpath_sub_heading = "//h4"
        self.xpath_link = "//a[contains(text(),'%s')]"
        self.xpath_btn = "//button"
        self.xpath_loading = "//div[@id='loading']"
        self.xpath_finsh = "//div[@id='finish']"
        self.txt_finsh = "Hello World!"

    def verify_dynamic_loading_page(self):
        """
        This method is to verify Dynamically Loaded Page Elements page.

        return: instance of Dynamically Loaded Page Elements page
        rtype: Dynamically Loaded Page ElementsPage instance
        """

        logging.info("## Verifying Dynamically Loaded Page Elements page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Dynamically Loaded Page Elements page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def click_on_link(self, link):
        self.services.wait_for_element(self.xpath_link % link)
        self.driver.find_element_by_xpath(self.xpath_link % link).click()
        self.services.wait_for_element(self.xpath_sub_heading)
        sub_heading = self.driver.find_element_by_xpath(self.xpath_sub_heading)
        actual_heading = sub_heading.text
        if 'Example 1' in link:
            assert actual_heading == self.sub_header_1, "Actual '%s' should be same as expected '%s'" % (
                actual_heading, self.sub_header_1)
        else:
            assert actual_heading == self.sub_header_2, "Actual '%s' should be same as expected '%s'" % (
                actual_heading, self.sub_header_2)

    def display_hidden_element(self):

        self.services.wait_for_element(self.xpath_btn)

        self.services.assert_element_present(self.xpath_finsh)
        self.services.assert_element_visibility(self.xpath_finsh, False)

        self.driver.find_element_by_xpath(self.xpath_btn).click()

        self.services.wait_for_element_visible(self.xpath_loading)
        self.services.assert_element_present(self.xpath_loading)

        self.services.wait_for_element_invisible(self.xpath_loading)
        self.services.assert_element_visibility(self.xpath_loading, False)

        self.services.assert_element_visibility(self.xpath_finsh)
        actual_txt = self.driver.find_element_by_xpath(self.xpath_finsh).text
        assert actual_txt == self.txt_finsh, "Actual '%s' should be same as expected '%s'"%(actual_txt, self.txt_finsh)

    def render_new_element(self):

        self.services.wait_for_element(self.xpath_btn)

        self.services.assert_element_is_not_present(self.xpath_finsh)

        self.driver.find_element_by_xpath(self.xpath_btn).click()

        self.services.wait_for_element_visible(self.xpath_loading)
        self.services.assert_element_present(self.xpath_loading)

        self.services.wait_for_element_invisible(self.xpath_loading)
        self.services.assert_element_visibility(self.xpath_loading, False)

        self.services.assert_element_present(self.xpath_finsh)
        self.services.assert_element_visibility(self.xpath_finsh)
        actual_txt = self.driver.find_element_by_xpath(self.xpath_finsh).text
        assert actual_txt == self.txt_finsh, "Actual '%s' should be same as expected '%s'"%(actual_txt, self.txt_finsh)