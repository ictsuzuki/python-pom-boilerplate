from pom.pages.base_page import BasePage
from pom.utils.locators import *

class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def do_login(self, email, passord):
        email_text_field = self.find_element(LoginPageLocators.USERNAME_TEXTFIELD)
        password_text_field = self.find_element(LoginPageLocators.PASSWORD_TEXTFIELD)
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)

        self.typeText(email_text_field, email)
        self.typeText(password_text_field, passord)
        self.click(login_button)

