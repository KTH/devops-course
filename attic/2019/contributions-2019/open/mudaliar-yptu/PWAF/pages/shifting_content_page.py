"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
@date: 21-Apr-19
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ShiftingContentPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Shifting Content"
        self.xpath_heading = "//h3"
        self.xpath_menu = "//a[@href = '/shifting_content/menu']"
        self.xpath_image = "//a[@href = '/shifting_content/image']"
        self.xpath_list = "//a[@href = '/shifting_content/list']"

    def verify_shifting_content_page(self):
        """
        This method is to verify Shifting Content page.

        return: instance of Shifting Content page
        rtype: Shifting Content Page instance
        """
        logging.info("## Verifying Shifting Content page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Shifting Content page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_menu_random(self):
        """
        This method is to verify Shifting Menu element randomly.
        """
        href_menu = self.driver.find_element_by_xpath(self.xpath_menu)
        href_menu.click()
        href_random = self.driver.find_element_by_xpath("//a[@href = '/shifting_content/menu?mode=random']")
        href_random.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/menu?mode=random"
        assert current_url == expected_url, "Shifting of Menu elements happens randomly"

    def verify_menu_pixel_shift(self):
        """
        This method is to verify Shifting Menu element by 100 pixels.
        """
        href_random = self.driver.find_element_by_xpath("//a[@href = '/shifting_content/menu?pixel_shift=100']")
        href_random.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/menu?pixel_shift=100"
        assert current_url == expected_url, "Shifting of Menu elements happens by 100 pixels"

    def verify_menu_pixel_shift_random(self):
        """
        This method is to verify Shifting Menu element by 100 pixels.
        """
        href_random = self.driver.find_element_by_xpath("//a[@href = '/shifting_content/menu?mode=random&pixel_shift=100']")
        href_random.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/menu?mode=random&pixel_shift=100"
        assert current_url == expected_url, "Shifting of Menu elements happens by 100 pixels and randomly"

    def verify_image_random(self):
        """
        This method is to verify shifting of image randomly element.
        """
        href_menu = self.driver.find_element_by_xpath(self.xpath_image)
        href_menu.click()
        href_random = self.driver.find_element_by_xpath("//a[@href = '/shifting_content/image?mode=random']")
        href_random.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/image?mode=random"
        assert current_url == expected_url, "Shifting of image elements happens randomly"

    def verify_image_pixel_shift(self):
        """
        This method is to verify Shifting image element by 100 pixels.
        """
        href_random = self.driver.find_element_by_xpath("//a[@href = '/shifting_content/image?pixel_shift=100']")
        href_random.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/image?pixel_shift=100"
        assert current_url == expected_url, "Shifting of image elements happens by 100 pixels"

    def verify_image_pixel_shift_random(self):
        """
        This method is to verify Shifting image element by 100 pixels.
        """
        href_random = self.driver.find_element_by_xpath("//a[@href = '/shifting_content/image?mode=random&pixel_shift=100']")
        href_random.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/image?mode=random&pixel_shift=100"
        assert current_url == expected_url, "Shifting of image elements happens by 100 pixels and randomly"

    def verify_image_append(self):
        """
        This method is to verify appending image element.
        """
        href_random = self.driver.find_element_by_xpath("//a[@href = '/shifting_content/image?image_type=simple']")
        href_random.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/image?image_type=simple"
        assert current_url == expected_url, "Appending image element works"

    def verify_list(self):
        """
        This method is to verify list element.
        """
        href_menu = self.driver.find_element_by_xpath(self.xpath_list)
        href_menu.click()
        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/shifting_content/list"
        assert current_url == expected_url, "List elements keeps on randomly shifting"

