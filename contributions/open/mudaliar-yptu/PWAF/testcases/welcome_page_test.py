"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class WelcomePageTest(DriverManager):
    def test_welcomepage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page()
