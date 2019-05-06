"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 17-May-18
"""
import logging

from selenium.webdriver.common.action_chains import ActionChains

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DragAndDropPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Drag and Drop"
        self.xpath_heading = "//h3"
        self.xpath_a_box = "//div[@id='column-a']/header"
        self.xpath_b_box = "//div[@id='column-b']/header"

    def verify_drag_and_drop_page(self):
        """
        This method is to verify Drag and Drop page.

        return: instance of Drag and Drop page
        rtype: Drag and DropPage instance
        """

        logging.info("## Verifying Drag and Drop page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Drag and Drop page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def drag_a_to_b(self):
        ele_a = self.driver.find_element_by_xpath(self.xpath_a_box)
        location = ele_a.location
        size = ele_a.size
        print(location)
        print(size)
        ele_b = self.driver.find_element_by_xpath(self.xpath_b_box)
        location = ele_b.location
        size = ele_b.size
        print(location)
        print(size)
        # {'y': 91.0, 'x': 430.0}
        # {'width': 116.0, 'height': 16.0}
        x_coordinate = int(location['x']) + int((size['width'] / 2))
        print("x_coordinate: %d" % x_coordinate)
        y_coordinate = int(location['y'])
        print("y_coordinate: %d" % y_coordinate)
        action_chain = ActionChains(self.driver)
        #action_chain.drag_and_drop(ele_a, ele_b).perform()
        # action_chain.move_to_element(ele_a).click_and_hold(ele_a).move_to_element(ele_b).perform()
        #action_chain.drag_and_drop_by_offset(ele_a, x_coordinate, y_coordinate).perform()
        #action_chain.click_and_hold(ele_a).move_to_element(ele_b).perform()
        #action_chain.click_and_hold(ele_a).move_by_offset(x_coordinate, y_coordinate).perform()
        #action_chain.click_and_hold(ele_a).move_to_element_with_offset(ele_b, size['width'], y_coordinate).perform()
        #action_chain.click_and_hold(ele_a).move_to_element(ele_b).release(ele_b).perform()
        import time
        for x in range(500, 700, 10):
            action_chain = ActionChains(self.driver)
            action_chain.click_and_hold(ele_a).move_by_offset(x, y_coordinate).perform()
            time.sleep(1)

