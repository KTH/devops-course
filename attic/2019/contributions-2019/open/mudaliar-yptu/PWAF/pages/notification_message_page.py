"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
@date: 21-Apr-19
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class NotificationMessagePage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Notification Message"
        self.xpath_heading = "//h3"
        self.xpath_href = "//a[@href = '/notification_message']"
        self.xpath_notification_message = "//div[@id = 'flash']"

    def verify_notification_message_page(self):
        """
        This method is to verify Notification Message page.

        return: instance of Notification Message page
        rtype: Notification Message Page instance
        """
        logging.info("## Verifying Notification Message page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Notification Message page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_notification_message(self):
        """
        This method is to verify notification message.
        """
        href_button = self.driver.find_element_by_xpath(self.xpath_href)
        href_button.click()
        notification_message = self.driver.find_element_by_xpath(self.xpath_notification_message)
        actual = notification_message.get_attribute('innerHTML')
        assert "Action successful" or "Action unsuccesful, please try again" in actual, "Notification message appears"

