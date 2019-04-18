""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 13-May-18
"""
from pages.challenging_dom_page import ChallengingDomPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class ChallengingDomPageTest(DriverManager):
    def test_challenging_dom_page(self):
        welcome_page = WelcomePage(self.driver)
        btn_lst = welcome_page.verify_welcome_page().click_on_link("Challenging DOM").get_list_of_all_buttons()

        challenging_dom_page = ChallengingDomPage(self.driver)
        challenging_dom_page.click_on_button(btn_lst[0])

        cell_txt = challenging_dom_page.get_cell_text(col_name='Sit')
        assert "Definiebas0" == cell_txt, "{actual} should be equal to {expected}.".format(actual=cell_txt,
                                                                                           expected="Definiebas0")
