"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager
from pages.infinite_scroll_page import InfiniteScrollPage


class InfiniteScrollPageTest(DriverManager):
    def test_infinite_scroll_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Infinite Scroll")

        infinite_scroll_page = InfiniteScrollPage(self.driver)
        infinite_scroll_page.verify_infinite_scroll_page()
        infinite_scroll_page.verify_infinite_scroll(5)
