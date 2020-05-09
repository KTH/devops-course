""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 13-May-18
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox
from nose.plugins.attrib import attr

@attr(group=['kth'])
class CheckboxPageTestFirefox(DriverManagerFirefox):
    def test_context_menu_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Context Menu").perform_right_click()
