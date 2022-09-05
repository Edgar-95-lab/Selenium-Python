# Imports
import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from Pages.PageIndex import *
from Pages.FlightPage import *
from Pages.PageRegister import *
from Helpers.data import *
from Helpers.xmlReader import *


# Web Drivers ==> Edge
class newtoursTest(unittest.TestCase):
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
        self.driver.get(self.configuration.obtener_datos("url"))
        self.driver.execute_script("window.open('https://www.google.com.mx')")
        self.my_tabs = self.driver.window_handles
        self.page_index = PageIndex(self.driver)
        self.flight_page = FlightPage(self.driver)
        self.page_register = PageRegister(self.driver)

    # @unittest.skip("Se excluye TestCase Dropdowns")
    def test_dropdowns(self):
        my_data = test_data()
        self.page_index.click_register()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        self.flight_page.select_country_by_index(5)
        time.sleep(1)
        self.flight_page.select_country_by_value(my_data.country)
        self.flight_page.verify_country("MEXICO")
        self.flight_page.verify_not_country("ITALY")

    # @unittest.skipIf(2 > 1, "Si la condición = True, se ejecuta el TestCase actual (test_login)")
    def test_login(self):
        self.page_index.login("User", "Password")
        self.page_register.verify_registration_from()

    # @unittest.skipUnless(sys.platform.startswith("Linux"), "Sólo es para linux")
    def test_login_by_tabs(self):
        self.page_index.login_by_tab("User", "Password")

    def test_switch_navigation(self):
        self.driver.switch_to.window(self.my_tabs[1])
        self.driver.get("https://jmeter.apache.org/download_jmeter.cgi")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()