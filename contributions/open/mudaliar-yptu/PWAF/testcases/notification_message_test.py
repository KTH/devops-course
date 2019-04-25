"""
@author: Kartik Mudaliar
@email: mudaliar@kth.se
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager
from pages.notification_message_page import NotificationMessagePage
from nose.plugins.attrib import attr


@attr(group=['kth'])
class NotificationMessagePageTest(DriverManager):
    def test_notification_message_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Notification Messages")

        notification_message_page = NotificationMessagePage(self.driver)
        notification_message_page.verify_notification_message_page()
        notification_message_page.verify_notification_message()

