""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class DynamicLoadingsTest(DriverManager):
    def test_hidden_element_on_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Loading")

        dynamic_loading_page = DynamicLoadingPage(self.driver)
        dynamic_loading_page.click_on_link("Example 1")
        dynamic_loading_page.display_hidden_element()

    def test_new_element_rendered_on_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Loading")

        dynamic_loading_page = DynamicLoadingPage(self.driver)
        dynamic_loading_page.click_on_link("Example 2")
        dynamic_loading_page.render_new_element()
