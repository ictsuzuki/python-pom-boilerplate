from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_TEXTFIELD = (By.ID, 'user-name')
    PASSWORD_TEXTFIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    HOME_TITLE = (By.CSS_SELECTOR, '.title')
