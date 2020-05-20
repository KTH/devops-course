"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class CheckboxPageTestFirefox(DriverManagerFirefox):
    def test_checkboxpage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Checkboxes").select_checkbox(2)

@attr(group=['kth'])
class CheckboxPageTestFirefox(DriverManagerChrome):
    def test_checkboxpage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Checkboxes").select_checkbox(2)
