# Imports
import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from Pages.PageIndex import *
from Pages.FlightPage import *
from Pages.PageRegister import *
from Helpers.data import *
from Helpers.xmlReader import *


# Web Drivers ==> Edge, Chrome
class dressesTest(unittest.TestCase):
    def setUp(self):
        self.configuration = xmlReader()
        if self.configuration.obtener_datos('browser') == 'chrome':
            ser = Service("C:/WebDrivers/chromedriver.exe")
            op = webdriver.ChromeOptions()
            # op.add_argument("--headless")
            op.add_argument("--start-maximized")
            # op.add_argument("--window-size=1550,1550)
            self.driver = webdriver.Chrome(service=ser, options=op)
        else:
            ser = Service("C:/WebDrivers/msedgedriver.exe")
            op = webdriver.EdgeOptions()
            # op.add_argument("--headless")
            op.add_argument("--start-maximized")
            self.driver = webdriver.Edge(service=ser, options=op)
        # self.driver.maximize_window()
        self.driver.get(self.configuration.obtener_datos("urldresses"))
        self.page_index = PageIndex(self.driver)

    def test_order_dress_by_ascending_name(self):
        self.page_index.click_dresses("Product Name: Z to A", "screenshot3")

    def test_order_dress_by_descending_name(self):
        self.page_index.click_dresses("Product Name: A to Z", "screenshot4")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

