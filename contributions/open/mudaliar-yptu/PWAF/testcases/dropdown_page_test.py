"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class DropdownPageTestFirefox(DriverManagerFirefox):
    def test_dropdown_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dropdown")

    def test_select_value_in_dropdown(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dropdown").select_dropdown_option("Option 1")

@attr(group=['kth'])
class DropdownPageTestChrome(DriverManagerChrome):
    def test_dropdown_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dropdown")

    def test_select_value_in_dropdown(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dropdown").select_dropdown_option("Option 1")
