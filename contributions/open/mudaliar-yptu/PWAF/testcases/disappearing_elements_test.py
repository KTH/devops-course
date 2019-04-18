""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
from pages.disappearing_elements_page import DisappearingElementsPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class DisappearingElementsTest(DriverManager):
    def test_disappearing_elements_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Disappearing Elements")

        disappearing = DisappearingElementsPage(self.driver)
        actual_tabs = disappearing.get_list_of_all_tabs()
        print "Tabs: %s" % actual_tabs
        assert "Home" in actual_tabs, "'Home' should be present in %s" % actual_tabs
        disappearing.verify_tab_disappear("Gallery")
