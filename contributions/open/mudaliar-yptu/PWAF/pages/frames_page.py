"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FramesPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Frames"
        self.xpathHeading = "//h3"
        self.xpathLink = "//a[text()='%s']"
        self.xpathBottomFrame = "//frame[@name='frame-bottom']"
        self.xpathTopFrame = "//frame[@name='frame-top']"
        self.xpathLeftFrame = "//frame[@name='frame-left']"
        self.xpathMiddleFrame = "//frame[@name='frame-middle']"
        self.xpathRightFrame = "//frame[@name='frame-right']"

    def verify_multiple_windows_page(self):
        """
        This method is to verify Frames page.

        return: instance of Frames page
        rtype: Frames Page instance
        """

        logging.info("## Verifying Frames page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on Frames page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def click_on_link(self, lnk):
        self.services.assert_and_click_by_xpath(self.xpathLink % lnk)

    def verify_next_frame_txt(self):
        self.services.wait_for_element(self.xpathBottomFrame)
        top_frame = self.driver.find_element_by_xpath(self.xpathTopFrame)
        self.driver.switch_to.frame(top_frame)

        left_frame = self.driver.find_element_by_xpath(self.xpathLeftFrame)
        self.driver.switch_to.frame(left_frame)
        print self.services.get_text_by_xpath("//body")

        self.driver.switch_to_default_content()

        top_frame = self.driver.find_element_by_xpath(self.xpathTopFrame)
        self.driver.switch_to.frame(top_frame)

        middle_frame = self.driver.find_element_by_xpath(self.xpathMiddleFrame)
        self.driver.switch_to.frame(middle_frame)
        print self.services.get_text_by_xpath("//body")

