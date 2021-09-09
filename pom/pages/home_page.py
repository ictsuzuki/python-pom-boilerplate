from pom.pages.base_page import BasePage
from pom.utils.locators import *

class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def get_title_text(self):
        title_label = self.find_element(LoginPageLocators.HOME_TITLE)
        return title_label.text



