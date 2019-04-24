""" 
@author: Yi-Pei, Tu
@email: yptu@kth.se
@date: 21-Apr-19
"""
from pages import dynamic_controls_page
from pages.floating_menu_page import FloatingMenuPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager
from nose.plugins.attrib import attr

@attr(group=['kth'])
class FloatingMenuTest(DriverManager):

    def test_floating_menu(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Floating Menu")

        floating_menu_page = FloatingMenuPage(self.driver)
        floating_menu_page.verify_floating_menu_page()

        floating_menu_page.verify_floating_menu()