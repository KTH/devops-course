""" 
@author: Yi-Pei, Tu
@email: yptu@kth.se
@date: 23-Apr-19
"""
from pages import dynamic_controls_page
from pages.key_presses_page import KeyPressesPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class KeyPressesTestFirefox(DriverManagerFirefox):

    def test_key_presses(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Key Presses")

        key_presses_page = KeyPressesPage(self.driver)
        key_presses_page.verify_key_presses_page()

        key_presses_page.verify_key_presses()

@attr(group=['kth'])
class KeyPressesTestChrome(DriverManagerChrome):

    def test_key_presses(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Key Presses")

        key_presses_page = KeyPressesPage(self.driver)
        key_presses_page.verify_key_presses_page()

        key_presses_page.verify_key_presses()