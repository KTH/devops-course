"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DynamicControlsPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Dynamic Controls"
        self.xpath_heading = "//h4"
        self.xpath_btn = "//button[@type='button' and text()='%s']"
        self.xpath_checkbox = "//input[@type='checkbox']"
        self.xpath_loading = "//div[@id='loading']"

    def verify_dynamic_controls_page(self):
        """
        This method is to verify Dynamic Controls page.

        return: instance of Dynamic Controls page
        rtype: Dynamic ControlsPage instance
        """

        logging.info("## Verifying Dynamic Controls page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Dynamic Controls page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_removed_element(self):
        assert self.services.is_element_present(self.xpath_checkbox), "Checkbox element should be present."

        xpath_remove_btn = self.xpath_btn%"Remove"
        self.services.assert_element_present(xpath_remove_btn)
        remove_btn = self.driver.find_element_by_xpath(xpath_remove_btn)
        remove_btn.click()

        self.services.wait_for_element_visible(self.xpath_loading)
        self.services.assert_element_present(self.xpath_loading)

        self.services.wait_for_element_invisible(self.xpath_loading)
        self.services.assert_element_visibility(self.xpath_loading, False)

        self.services.assert_element_is_not_present(self.xpath_checkbox)
        self.services.assert_element_is_not_present(xpath_remove_btn)

    def verify_add_element(self):

        self.verify_removed_element()

        xpath_add_btn = self.xpath_btn % "Add"
        self.services.assert_element_present(xpath_add_btn)
        add_btn = self.driver.find_element_by_xpath(xpath_add_btn)
        add_btn.click()

        self.services.wait_for_element_visible(self.xpath_loading)
        self.services.assert_element_present(self.xpath_loading)

        self.services.wait_for_element_invisible(self.xpath_loading)
        self.services.assert_element_visibility(self.xpath_loading, False)

        self.services.assert_element_present(self.xpath_checkbox)
        self.services.assert_element_is_not_present(xpath_add_btn)