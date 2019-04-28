"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
"""
from pages.welcome_page import WelcomePage
from pages.shifting_content_page import ShiftingContentPage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class ShiftingContentPageTestFirefox(DriverManagerFirefox):
    def test_shifting_menu_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Shifting Content")

        shifting_content_page = ShiftingContentPage(self.driver)
        shifting_content_page.verify_shifting_content_page()
        shifting_content_page.verify_menu_random()
        shifting_content_page.verify_menu_pixel_shift()
        shifting_content_page.verify_menu_pixel_shift_random()

    def test_shifting_image_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Shifting Content")

        shifting_content_page = ShiftingContentPage(self.driver)
        shifting_content_page.verify_shifting_content_page()
        shifting_content_page.verify_image_random()
        shifting_content_page.verify_image_pixel_shift()
        shifting_content_page.verify_image_pixel_shift_random()
        shifting_content_page.verify_image_append()

    def test_shifting_list_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Shifting Content")

        shifting_content_page = ShiftingContentPage(self.driver)
        shifting_content_page.verify_shifting_content_page()
        shifting_content_page.verify_list()


@attr(group=['kth'])
class ShiftingContentPageTestChrome(DriverManagerChrome):
    def test_shifting_menu_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Shifting Content")

        shifting_content_page = ShiftingContentPage(self.driver)
        shifting_content_page.verify_shifting_content_page()
        shifting_content_page.verify_menu_random()
        shifting_content_page.verify_menu_pixel_shift()
        shifting_content_page.verify_menu_pixel_shift_random()

    def test_shifting_image_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Shifting Content")

        shifting_content_page = ShiftingContentPage(self.driver)
        shifting_content_page.verify_shifting_content_page()
        shifting_content_page.verify_image_random()
        shifting_content_page.verify_image_pixel_shift()
        shifting_content_page.verify_image_pixel_shift_random()
        shifting_content_page.verify_image_append()

    def test_shifting_list_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Shifting Content")

        shifting_content_page = ShiftingContentPage(self.driver)
        shifting_content_page.verify_shifting_content_page()
        shifting_content_page.verify_list()