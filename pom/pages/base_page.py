from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeOut = 30

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((locator))
            )
            return element
        except:
            print('Element with locator id ' + locator + ' was not displayed')

    def typeText(self, web_element, string):
        try:
            web_element.send_keys(string)
        except:
            print("Unable to type text in next web element"+ web_element)

    def click(self, web_element):
        try:
            web_element.click()
        except:
            print("Unable to click in next web element "+ web_element)

