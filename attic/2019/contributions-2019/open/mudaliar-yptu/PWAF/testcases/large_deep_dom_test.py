""" 
@author: Yi-Pei, Tu
@email: yptu@kth.se
@date: 23-Apr-19
"""
from pages.large_deep_dom_page import LargeDeepDomPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class LargeDeepDomTestFirefox(DriverManagerFirefox):

    def test_key_presses(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Large & Deep DOM")

        large_deep_dom_page = LargeDeepDomPage(self.driver)
        large_deep_dom_page.verify_large_deep_dom_page()

        large_deep_dom_page.verify_large_deep_dom_no_sibling()
        large_deep_dom_page.verify_large_deep_dom_table()

@attr(group=['kth'])
class LargeDeepDomTestChrome(DriverManagerChrome):

    def test_key_presses(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Large & Deep DOM")

        large_deep_dom_page = LargeDeepDomPage(self.driver)
        large_deep_dom_page.verify_large_deep_dom_page()

        large_deep_dom_page.verify_large_deep_dom_no_sibling()
        large_deep_dom_page.verify_large_deep_dom_table()