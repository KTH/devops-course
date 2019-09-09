"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager
from nose.plugins.attrib import attr

class AllTests(DriverManager):

    @attr(group=['smoke', 'reg'])
    def test_welcomepage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page()

    @attr(group=['smoke', 'reg', 'sanity'])
    def test_checkboxpage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Checkboxes").select_checkbox(2)

    @attr(group=['reg'])
    def test_dropdown_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dropdown")
