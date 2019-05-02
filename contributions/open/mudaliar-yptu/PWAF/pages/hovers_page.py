"""
@author: Prerna Pal
@email: prerna.chanchal13@gmail.com
@date: 20-May-18
"""
import logging

from selenium.webdriver.common.action_chains import ActionChains

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class HoversPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Hovers"
        self.xpath_heading = "//h3"
        self.xpath_image = "//div[@class='figure']"
        self.xpath_image_1 = self.xpath_image + "[1]//img"
        self.xpath_image_2 = self.xpath_image + "[2]//img"
        self.xpath_image_3 = self.xpath_image + "[3]//img"
        self.xpath_image_1_caption = self.xpath_image + "[1]//div[@class='figcaption']"
        self.xpath_image_2_caption = self.xpath_image + "[2]//div[@class='figcaption']"
        self.xpath_image_3_caption = self.xpath_image + "[3]//div[@class='figcaption']"

    def verify_hovers_page(self):
        """
        This method is to verify Hovers page.

        return: instance of Hovers page
        rtype: HoversPage instance
        """

        logging.info("## Verifying Hovers page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Hovers page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_hovers_functionality(self):
        image_1 = self.driver.find_element_by_xpath(self.xpath_image_1)
        image_2 = self.driver.find_element_by_xpath(self.xpath_image_2)

        self.services.assert_element_visibility(self.xpath_image_2_caption, False)

        action_chain = ActionChains(self.driver)
        action_chain.move_to_element(image_1).perform()
        from time import sleep
        sleep(1)

        action_chain.move_to_element(image_2).perform()
        from time import sleep
        sleep(1)

        self.services.is_element_visible(self.xpath_image_2_caption)
