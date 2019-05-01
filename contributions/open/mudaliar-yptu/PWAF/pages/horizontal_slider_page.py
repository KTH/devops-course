"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
@date: 21-Apr-19
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

from selenium.webdriver.common.action_chains import ActionChains


class HorizontalSliderPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Horizontal Slider"
        self.xpath_heading = "//h3"
        self.xpath_slider = "//input[@type='range']"
        self.xpath_slider_output = "//span[@id='range']"

    def verify_horizontal_slider_page(self):
        """
        This method is to verify Horizontal slider page.

        return: instance of Horizontal slider page
        rtype: Horizontal Slider Page instance
        """
        logging.info("## Verifying Horizontal Slider page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Horizontal Slider page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_horizontal_slider(self, opt):
        """
        This method is to verify horizontal slider.
        """
        offset = 100
        action = ActionChains(self.driver)
        slider = self.driver.find_element_by_xpath(self.xpath_slider)
        action.click_and_hold(slider).move_by_offset(offset, 0).release().perform()
        slider_output = self.driver.find_element_by_xpath(self.xpath_slider_output)
        actual = slider_output.get_attribute('innerHTML')
        assert actual == opt, "Selected value {0}, should be same as expected value {1}".format(actual, opt)
