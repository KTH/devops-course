"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 16-Apr-18
"""
import logging

from pages.challenging_dom_page import ChallengingDomPage
from pages.checkbox_page import CheckboxPage
from pages.context_menu_page import ContextMenuPage
from pages.disappearing_elements_page import DisappearingElementsPage
from pages.drag_and_drop_page import DragAndDropPage
from pages.dropdown_page import DropdownPage
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.jquery_ui_menu_page import JQueryUIMenuPage
from utility.services import Services


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.title = "The Internet"
        self.xpath_link = "//a[text()='%s']"

    def verify_welcome_page(self):
        """
        This method is to verify Welcome page.

        return: instance of welcome page
        rtype: WelcomePage instance
        """

        logging.info('## Verifying home page ##')
        actual_title = self.driver.title
        logging.info('# Actual Title: %s' % actual_title)
        assert actual_title == self.title, "Actual title %s, should be same as %s" % (actual_title, self.title)
        return self

    def click_on_link(self, link_txt):
        """
        This method is to click on the links present on the welcome page.

        param link_txt: link text present on the Welcome page
        type link_txt: string

        return: returns the instance of the next navigating page.
        rtype: instance
        """

        logging.info("# Click on link '%s'" % link_txt)
        self.services.assert_and_click_by_xpath(self.xpath_link % link_txt)

        # Link Text: Checkboxes
        if link_txt == "Checkboxes":
            checkbox_page = CheckboxPage(self.driver)
            checkbox_page.verify_checkbox_page()
            return checkbox_page

        # Link Text: Dropdown
        if link_txt == "Dropdown":
            dropdown_page = DropdownPage(self.driver)
            dropdown_page.verify_dropdown_page()
            return dropdown_page

        # Link Text: Dropdown
        if link_txt == "Context Menu":
            context_menu_page = ContextMenuPage(self.driver)
            context_menu_page.verify_context_menu_page()
            return context_menu_page

        # Link Text: Challenging DOM
        if link_txt == "Challenging DOM":
            challenging_dom_page = ChallengingDomPage(self.driver)
            challenging_dom_page.verify_challenging_dom_page()
            return challenging_dom_page

        # Link Text: Disappearing Elements
        if link_txt == "Disappearing Elements":
            disappearing_elements_page = DisappearingElementsPage(self.driver)
            disappearing_elements_page.verify_disappearing_elements_page()
            return disappearing_elements_page

        # Link Text: Dynamic Controls
        if link_txt == "Dynamic Controls":
            dynamic_controls_page = DynamicControlsPage(self.driver)
            dynamic_controls_page.verify_dynamic_controls_page()
            return dynamic_controls_page

        # Link Text: Dynamic Loading
        if link_txt == "Dynamic Loading":
            dynamic_loading_page = DynamicLoadingPage(self.driver)
            dynamic_loading_page.verify_dynamic_loading_page()
            return dynamic_loading_page

        # Link Text: Dynamic Loading
        if link_txt == "Drag and Drop":
            drag_and_drop_page = DragAndDropPage(self.driver)
            drag_and_drop_page.verify_drag_and_drop_page()
            return drag_and_drop_page

        # Link Text: JQuery UI Menus
        if link_txt == "JQuery UI Menus":
            jquery_menu_page = JQueryUIMenuPage(self.driver)
            jquery_menu_page.verify_jquery_menu_page()
            return jquery_menu_page

        return self
