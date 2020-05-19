"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
"""
from pages.welcome_page import WelcomePage
from pages.infinite_scroll_page import InfiniteScrollPage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class InfiniteScrollPageTestFirefox(DriverManagerFirefox):
    def test_infinite_scroll_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Infinite Scroll")

        infinite_scroll_page = InfiniteScrollPage(self.driver)
        infinite_scroll_page.verify_infinite_scroll_page()
        infinite_scroll_page.verify_infinite_scroll(5)

@attr(group=['kth'])
class InfiniteScrollPageTestChrome(DriverManagerChrome):
    def test_infinite_scroll_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Infinite Scroll")

        infinite_scroll_page = InfiniteScrollPage(self.driver)
        infinite_scroll_page.verify_infinite_scroll_page()
        infinite_scroll_page.verify_infinite_scroll(5)
