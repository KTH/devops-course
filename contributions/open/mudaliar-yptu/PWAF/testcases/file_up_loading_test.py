"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
from pages.file_up_loading_page import FileUpLoadingPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class FileUpLoadingTestFirefox(DriverManagerFirefox):
    def test_file_uploading_functionality(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("File Upload")

        file_upload = FileUpLoadingPage(self.driver)
        file_upload.verify_file_uploader_page()
        file_upload.verify_uploaded_file()

@attr(group=['kth'])
class FileUpLoadingTestChrome(DriverManagerChrome):
    def test_file_uploading_functionality(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("File Upload")

        file_upload = FileUpLoadingPage(self.driver)
        file_upload.verify_file_uploader_page()
        file_upload.verify_uploaded_file()
