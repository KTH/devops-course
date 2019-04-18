"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
import logging
from time import sleep

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FileUpLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "File Uploader"
        self.xpathHeading = "//h3"
        self.xpathChooseFile = "//input[@id='file-upload']"
        self.xpathUploadBtn = "//input[@id='file-submit']"
        self.xpathUploadedFiles = "//div[@id='uploaded-files']"

    def verify_file_uploader_page(self):
        """
        This method is to verify File Uploader page.

        return: instance of File Uploader page
        rtype: File UploaderPage instance
        """

        logging.info("## Verifying File Uploader page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on File Uploader page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_uploaded_file(self):
        self.driver.find_element_by_xpath(self.xpathChooseFile).send_keys(
            "E:\\eclipse\\selLearning\\download\\menu.pdf")

        sleep(2)
        self.services.assert_and_click_by_xpath(self.xpathUploadBtn)
        self.services.wait_for_element(self.xpathUploadedFiles)
        assert "menu.pdf" == self.services.get_text_by_xpath(self.xpathUploadedFiles)
