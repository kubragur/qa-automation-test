# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from .base_page import BasePage

class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(),'Careers')]")

    def open_home_page(self):
        self.visit("https://useinsider.com/")
        self.accept_cookies()

    def go_to_careers(self):
        """Menüde Company üzerine gel ve Careers’a tıkla."""
        actions = ActionChains(self.driver)
        company_menu = self.wait.until(lambda d: d.find_element(*self.COMPANY_MENU))
        actions.move_to_element(company_menu).perform()
        self.click(self.CAREERS_LINK)
