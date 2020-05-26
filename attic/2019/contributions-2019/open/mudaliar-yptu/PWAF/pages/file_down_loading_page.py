"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FileDownLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "File Downloader"
        self.xpathHeading = "//h3"
        self.xpathLink = "//a[text()='%s']"

    def verify_file_downloader_page(self):
        """
        This method is to verify File Downloader page.

        return: instance of File Downloader page
        rtype: File DownloaderPage instance
        """

        logging.info("## Verifying File Downloader page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on File Downloader page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_file_downloading(self, link):

        self.services.assert_and_click_by_xpath(self.xpathLink%link)


