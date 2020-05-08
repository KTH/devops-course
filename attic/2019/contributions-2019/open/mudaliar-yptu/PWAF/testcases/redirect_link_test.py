""" 
@author: Yi-Pei, Tu
@email: yptu@kth.se
@date: 24-Apr-19
"""
from pages.redirect_link_page import RedirectLinkPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from nose.plugins.attrib import attr

@attr(group=['kth'])
class RedirectLinkTestFirefox(DriverManagerFirefox):
    def test_redierct_link(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Redirect Link")

        redirect_link_page = RedirectLinkPage(self.driver)
        redirect_link_page.verify_redirect_link_page()
        redirect_link_page.verify_redirect_link()
        redirect_link_page.verify_redirect_link_status_code(200)
        redirect_link_page.verify_redirect_link_status_code(301)
        redirect_link_page.verify_redirect_link_status_code(404)
        redirect_link_page.verify_redirect_link_status_code(500)

@attr(group=['kth'])
class RedirectLinkTestChrome(DriverManagerChrome):
    def test_redierct_link(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Redirect Link")

        redirect_link_page = RedirectLinkPage(self.driver)
        redirect_link_page.verify_redirect_link_page()
        redirect_link_page.verify_redirect_link()
        redirect_link_page.verify_redirect_link_status_code(200)
        redirect_link_page.verify_redirect_link_status_code(301)
        redirect_link_page.verify_redirect_link_status_code(404)
        redirect_link_page.verify_redirect_link_status_code(500)