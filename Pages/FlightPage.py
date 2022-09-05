import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FlightPage:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.country_dropdown = (By.NAME, "country")

    def select_country_by_index(self, index):
        Select(self.driver.find_element(*self.country_dropdown)).select_by_index(index)
        time.sleep(1)
        self.driver.get_screenshot_as_file("screenshots/screenshot1.png")

    def select_country_by_value(self, value):
        Select(self.driver.find_element(*self.country_dropdown)).select_by_value(value)
        time.sleep(1)
        self.driver.save_screenshot("screenshots/screenshot2.png")

    def verify_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertEqual(Select(self.driver.find_element(*self.country_dropdown)).first_selected_option.text.strip(), country)
        print("Assert 1 is passed ==> TestCase Flight")

    def verify_not_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertNotEqual(Select(self.driver.find_element(*self.country_dropdown)).first_selected_option.text.strip(), country)
        print("Assert 2 is passed ==> TestCase Flight")