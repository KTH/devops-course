"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class WelcomePageTestFirefox(DriverManagerFirefox):
    def test_welcomepage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page()


@attr(group=['kth'])
class WelcomePageTestChrome(DriverManagerChrome):
    def test_welcomepage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page()
