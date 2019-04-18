"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
from pages.file_down_loading_page import FileDownLoadingPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class FileDownLoadingTest(DriverManager):
    def test_file_downloading_functionality(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("File Download")

        file_download = FileDownLoadingPage(self.driver)
        file_download.verify_file_downloader_page()
        file_download.verify_file_downloading("shank.txt")
