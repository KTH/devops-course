""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class DynamicControlsTest(DriverManager):
    def test_drag_and_drop_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Drag and Drop").drag_a_to_b()
        import time
        time.sleep(5)

