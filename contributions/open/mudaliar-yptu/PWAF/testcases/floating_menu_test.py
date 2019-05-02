""" 
@author: Yi-Pei, Tu
@email: yptu@kth.se
@date: 21-Apr-19
"""
from pages import dynamic_controls_page
from pages.floating_menu_page import FloatingMenuPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class FloatingMenuTestFirefox(DriverManagerFirefox):

    def test_floating_menu(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Floating Menu")

        floating_menu_page = FloatingMenuPage(self.driver)
        floating_menu_page.verify_floating_menu_page()

        floating_menu_page.verify_floating_menu()

@attr(group=['kth'])
class FloatingMenuTestChrome(DriverManagerChrome):

    def test_floating_menu(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Floating Menu")

        floating_menu_page = FloatingMenuPage(self.driver)
        floating_menu_page.verify_floating_menu_page()

        floating_menu_page.verify_floating_menu()