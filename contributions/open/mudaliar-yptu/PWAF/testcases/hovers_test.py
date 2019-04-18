""" 
@author: Prerna Pal
@email: prerna.chanchal13@gmail.com
@date: 20-May-18
"""
from pages.hovers_page import HoversPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class HoversTest(DriverManager):
    def test_hover_functionality(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Hovers")

        hovers_page = HoversPage(self.driver)
        hovers_page.verify_hovers_functionality()
