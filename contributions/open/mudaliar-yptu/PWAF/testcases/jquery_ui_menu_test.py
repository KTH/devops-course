""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 20-May-18
"""
from pages.jquery_ui_menu_page import JQueryUIMenuPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class JQueryUIMenuTest(DriverManager):
    def test_jquery_menu(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("JQuery UI Menus")

        jquery_menu_page = JQueryUIMenuPage(self.driver)
        jquery_menu_page.verify_jquery_menu()
