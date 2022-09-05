import time
import unittest

from selenium.webdriver.common.by import By

class PageRegister:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.registration_form_link = (By.LINK_TEXT, "registration form")

    def verify_registration_from(self):
        tc = unittest.TestCase('__init__')
        self.driver.implicitly_wait(5)
        registration_link = self.driver.find_element(*self.registration_form_link)
        tc.assertEqual(registration_link.text, "registration form")
        print("Assert 1 is passed ==> TestCase Login")
        tc.assertEqual(registration_link.tag_name, "a")
        print("Assert 2 is passed ==> TestCase Login")