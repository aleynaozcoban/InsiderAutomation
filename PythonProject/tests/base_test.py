
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from utils.screenshots import take_screenshot


class BaseTest(unittest.TestCase):
    base_url = 'https://useinsider.com/'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
        import sys
        exc_type, exc_value, _ = sys.exc_info()
        if exc_type is not None:
            take_screenshot(self.driver, self._testMethodName)


