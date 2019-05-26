"""
Selenium based Django test experiments.
"""

import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSeleniumCases:
    
    def setup_method(self, method):
        pass

    def test_selenium_basic(self):
        """
        Test external resource, run as:
        pytest -vv -rfsX -s tests/selenium_tests.py        
        """
        self.browser = webdriver.Chrome('/Users/matthewbrown/downloads/chromedriver-3')
        print(self.browser.get("https://docs.djangoproject.com/"))
        self.browser.quit()
