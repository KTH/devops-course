""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
from pages import dynamic_controls_page
from pages.dynamic_controls_page import DynamicControlsPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class DynamicControlsTestFirefox(DriverManagerFirefox):

    def test_removing_element_from_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Controls")

        dynamic_controls_page = DynamicControlsPage(self.driver)
        dynamic_controls_page.verify_removed_element()

    def test_adding_element_from_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Controls")

        dynamic_controls_page = DynamicControlsPage(self.driver)
        dynamic_controls_page.verify_add_element()

@attr(group=['kth'])
class DynamicControlsTestChrome(DriverManagerChrome):

    def test_removing_element_from_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Controls")

        dynamic_controls_page = DynamicControlsPage(self.driver)
        dynamic_controls_page.verify_removed_element()

    def test_adding_element_from_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Controls")

        dynamic_controls_page = DynamicControlsPage(self.driver)
        dynamic_controls_page.verify_add_element()