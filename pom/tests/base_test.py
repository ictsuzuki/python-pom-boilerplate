import unittest

from selenium import webdriver


class BaseTest():
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/tsuzuki/Documents/drivers/chromedriver")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()