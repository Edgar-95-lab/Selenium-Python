# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.service import Service

# Web Drivers ==> Edge
ser = Service("msedgedriver.exe")
op = webdriver.EdgeOptions()
driver = webdriver.Edge(service=ser, options=op)
driver.maximize_window()
driver.get('https://demo.guru99.com/selenium/newtours/')
time.sleep(5)

# Web Elements
driver.find_element(By.LINK_TEXT, "REGISTER").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(1)
country_dropdown = Select(driver.find_element(By.NAME, "country"))
country_dropdown.select_by_index(5)
time.sleep(2)
country_dropdown.select_by_value("MEXICO")