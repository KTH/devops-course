"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
@date: 21-Apr-19
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class InfiniteScrollPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Infinite Scroll"
        self.xpath_heading = "//h3"

    def verify_infinite_scroll_page(self):
        """
        This method is to verify infinite scroll page.

        return: instance of Infinite scroll page
        rtype: Infinite scroll Page instance
        """
        logging.info("## Verifying Infinite Scroll page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Infinite Scroll page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_infinite_scroll(self, itr):
        """
        This method is to verify infinite scroll.
        """
        scroll_flag = False
        count = 0
        for i in range(0, itr):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            count += 1

        if count == itr:
            scroll_flag = True

        assert scroll_flag is True, "Infinite Scroll is happening"
