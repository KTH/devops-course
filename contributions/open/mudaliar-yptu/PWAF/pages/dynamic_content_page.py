"""
@author: Yi-Pei Tu
@email: yptu@kth.se
@date: 21-Apr-19
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DynamicContentPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Dynamic Content"
        self.xpath_heading = "//h3"
        self.xpath_img = "//*[@id='content']/div[%d]/div[1]/img"
        self.xpath_text = "//*[@id='content']/div[%d]/div[2]"
        self.image_texts = []

    def verify_dynamic_content_page(self):
        """
        This method is to verify Dynamic Content page.

        return: instance of Dynamic Content page
        rtype: Dynamic Content Page instance
        """
        logging.info("## Verifying Dynamic Content page ##")
        self.services.wait_for_element(self.xpath_heading)
        actual_heading = self.services.get_text_by_xpath(self.xpath_heading)
        logging.info("# Actual heading on Dynamic Content page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def verify_dynamic_images_texts(self):
        """
        This method is to verify Dynamic Contents after reloading.
        Not all elements would change after reloading. Thus, only one change is acceptable. 
        """

        for index in range(1,4):
            xpath_img = self.xpath_img % index
            xpath_text = self.xpath_text % index
            self.image_texts.append({
                "img": self.services.get_src_by_xpath(xpath_img),
                "text": self.services.get_text_by_xpath(xpath_text)
                })
        
        self.services.reload_page()
        self.services.wait_for_element("//*[@id='content']")
        
        b_pass = False
        for index in range(3):
            content_img = self.services.get_src_by_xpath((self.xpath_img % (index+1)))
            content_text = self.services.get_text_by_xpath(self.xpath_text % (index+1))
            if content_img != self.image_texts[index]["img"] or content_text != self.image_texts[index]["text"]:
                b_pass = True
            
        assert b_pass is True, "After reloading, one of the image/text should be different" 
