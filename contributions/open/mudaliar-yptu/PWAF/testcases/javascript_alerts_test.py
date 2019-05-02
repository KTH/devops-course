"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManagerFirefox, DriverManagerChrome
from pages.javascript_alerts_page import JavaScriptAlertsPage
from nose.plugins.attrib import attr


@attr(group=['kth'])
class JavaScriptAlertsPageTestFirefox(DriverManagerFirefox):
    def test_javascript_alert(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("JavaScript Alerts")

        javascript_alerts_page = JavaScriptAlertsPage(self.driver)
        javascript_alerts_page.verify_javascript_alerts_page()
        javascript_alerts_page.verify_javascript_alert()

    def test_javascript_confirm(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("JavaScript Alerts")

        javascript_alerts_page = JavaScriptAlertsPage(self.driver)
        javascript_alerts_page.verify_javascript_alerts_page()
        javascript_alerts_page.verify_javascript_confirm()

    def test_javascript_prompt(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("JavaScript Alerts")

        javascript_alerts_page = JavaScriptAlertsPage(self.driver)
        javascript_alerts_page.verify_javascript_alerts_page()
        javascript_alerts_page.verify_javascript_prompt("Test")


@attr(group=['kth'])
class JavaScriptAlertsPageTestChrome(DriverManagerChrome):
    def test_javascript_alert(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("JavaScript Alerts")

        javascript_alerts_page = JavaScriptAlertsPage(self.driver)
        javascript_alerts_page.verify_javascript_alerts_page()
        javascript_alerts_page.verify_javascript_alert()

    def test_javascript_confirm(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("JavaScript Alerts")

        javascript_alerts_page = JavaScriptAlertsPage(self.driver)
        javascript_alerts_page.verify_javascript_alerts_page()
        javascript_alerts_page.verify_javascript_confirm()

    def test_javascript_prompt(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("JavaScript Alerts")

        javascript_alerts_page = JavaScriptAlertsPage(self.driver)
        javascript_alerts_page.verify_javascript_alerts_page()
        javascript_alerts_page.verify_javascript_prompt("Test")
