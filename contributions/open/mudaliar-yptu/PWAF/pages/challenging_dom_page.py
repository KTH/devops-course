"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 13-May-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ChallengingDomPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Challenging DOM"
        self.xpathHeading = "//h3"
        self.xpathButton = "//a[contains(@class,'button') and text()='%s']"
        self.xpathButtons = "//a[contains(@class,'button')]"
        self.xpathTableHeader = "//div[@class='large-10 columns']/table/thead/tr/th"
        self.xpathTableCell = "//div[@class='large-10 columns']/table/tbody/tr[%s]/td[%s]"

    def verify_challenging_dom_page(self):
        """
        This method is to verify Challenging DOM page.

        return: instance of Challenging DOM page
        rtype: ChallengingDomPage instance
        """

        logging.info("## Verifying Challenging DOM page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on Challenging DOM page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def get_list_of_all_buttons(self):
        """
        This function is to get the list of all buttons present on page.
        :return: list of button
        """
        self.services.wait_for_element(self.xpathButtons)
        buttons_ele = self.driver.find_elements_by_xpath(self.xpathButtons)

        btn_lst = []
        for btn in buttons_ele:
            btn_lst.append(btn.text)

        return btn_lst

    def click_on_button(self, btn_text):
        """
        This function is to click on the desired button by given text present on button.
        :param btn_text: string
        """
        xpath = self.xpathButton % btn_text
        print(xpath)
        self.services.wait_for_element(xpath)
        self.driver.find_element_by_xpath(xpath).click()

    def get_column_index(self, col_name):
        '''
        This function is to get the index of the column name present on the table header.
        :param col_name: col name
        :return: index
        '''

        self.services.wait_for_element(self.xpathTableHeader)
        header_eles = self.driver.find_elements_by_xpath(self.xpathTableHeader)

        index = 0
        lst = []
        for header in header_eles:
            index += 1
            h_txt = header.text.strip()
            lst.append(h_txt)
            if col_name == h_txt:
                return index

        assert index == 0, "Given col name '{0}' is not present in {1}.".format(col_name, lst)

    def get_cell_text(self, row_index=1, col_name=None):
        """
        This function is to get the cell text by row index & cell index
        :param row_index: row index in number
        :param col_name: column name in string
        :return: cell text.
        """

        col_index = self.get_column_index(col_name)
        xpath = self.xpathTableCell % (str(row_index), str(col_index))
        self.services.wait_for_element(xpath)

        return self.driver.find_element_by_xpath(xpath).text
