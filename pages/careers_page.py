from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CareersPage(BasePage):
  
    LOCATIONS_BLOCK = (By.XPATH, "//*[contains(., 'Our Locations')]")
    LIFE_AT_BLOCK   = (By.XPATH, "//*[contains(., 'Life at Insider')]")

    def scroll_to_bottom(self):
     
        last_height = 0
        while True:
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            last_height = new_height

    def check_blocks(self):
        self.scroll_to_bottom()
        assert self.is_visible(self.LOCATIONS_BLOCK), "Our Locations bloğu görünmüyor"
        assert self.is_visible(self.LIFE_AT_BLOCK), "Life at Insider bloğu görünmüyor"
