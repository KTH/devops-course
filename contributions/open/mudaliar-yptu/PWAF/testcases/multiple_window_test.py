"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
from pages.multiple_window_page import MultipleWindowsPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class MultipleWindowsTest(DriverManager):
    def test_multiple_windows(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Multiple Windows")

        multiple_window = MultipleWindowsPage(self.driver)
        multiple_window.verify_multiple_windows_page()
        multiple_window.verify_next_window_txt()
