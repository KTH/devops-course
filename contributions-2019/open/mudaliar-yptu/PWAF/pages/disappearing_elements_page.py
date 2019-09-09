"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DisappearingElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Disappearing Elements"
        self.xpathHeading = "//h3"
        self.xpathTabs = "//ul//li//a"
        self.xpathTabByText = self.xpathTabs + "[text()='%s']"

    def verify_disappearing_elements_page(self):
        """
        This method is to verify Disappearing Elements page.

        return: instance of Disappearing Elements page
        rtype: ChallengingDomPage instance
        """

        logging.info("## Verifying Disappearing Elements page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on Disappearing Elements page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def get_list_of_all_tabs(self):
        """
        This function is to get the list of all tabs present on page.
        :return: list of button
        """
        self.services.wait_for_element(self.xpathTabs)
        tabs_ele = self.driver.find_elements_by_xpath(self.xpathTabs)

        tab_lst = []
        for btn in tabs_ele:
            tab_lst.append(btn.text)

        return tab_lst

    def verify_tab_disappear(self, tab_name):
        """
        This function is to tab disappearance.
        :param tab_name: string
        """
        xpath = self.xpathTabByText % tab_name
        print(xpath)

        while (True):
            self.driver.refresh()
            if not self.services.is_element_present(xpath):
                logging.info("# Tab '%s' is not present." % tab_name)
                break
            logging.info("# Tab '%s' is present." % tab_name)

        assert not self.services.is_element_present(xpath), "Tab '%s' should not present." % tab_name
