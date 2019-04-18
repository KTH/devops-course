"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
from pages.file_up_loading_page import FileUpLoadingPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class FileUpLoadingTest(DriverManager):
    def test_file_uploading_functionality(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("File Upload")

        file_upload = FileUpLoadingPage(self.driver)
        file_upload.verify_file_uploader_page()
        file_upload.verify_uploaded_file()
