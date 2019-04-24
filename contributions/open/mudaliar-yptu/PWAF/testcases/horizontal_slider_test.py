"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager
from pages.horizontal_slider_page import HorizontalSliderPage
from nose.plugins.attrib import attr

@attr(group=['kth'])
class HorizontalSliderPageTest(DriverManager):
    def test_horizontal_slider_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Horizontal Slider")

        horizontal_slider_page = HorizontalSliderPage(self.driver)
        horizontal_slider_page.verify_horizontal_slider_page()
        horizontal_slider_page.verify_horizontal_slider("5")
