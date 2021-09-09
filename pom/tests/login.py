import unittest

from pom.pages.home_page import HomePage
from pom.pages.login_page import LoginPage
from pom.tests.base_test import BaseTest
from pom.utils.data import Data


class Login(BaseTest, unittest.TestCase):
    def test_login(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        data = Data()

        login_page.do_login(data.user, data.password)
        self.assertIn("PRODUCTS", home_page.get_title_text())
