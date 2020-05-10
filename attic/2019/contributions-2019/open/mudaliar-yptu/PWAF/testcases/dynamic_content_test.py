""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
from pages import dynamic_controls_page
from pages.dynamic_content_page import DynamicContentPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class DynamicControlsTestFirefox(DriverManagerFirefox):

    def test_dynamic_content(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Content")

        dynamic_content_page = DynamicContentPage(self.driver)
        dynamic_content_page.verify_dynamic_content_page()

        dynamic_content_page.verify_dynamic_images_texts()

@attr(group=['kth'])
class DynamicControlsTestChrome(DriverManagerChrome):

    def test_dynamic_content(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dynamic Content")

        dynamic_content_page = DynamicContentPage(self.driver)
        dynamic_content_page.verify_dynamic_content_page()

        dynamic_content_page.verify_dynamic_images_texts()