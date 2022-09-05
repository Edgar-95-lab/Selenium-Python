# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# Web Drivers ==> Edge
ser = Service("msedgedriver.exe")
op = webdriver.EdgeOptions()
driver = webdriver.Edge(service=ser, options=op)
driver.maximize_window()
driver.get('https://www.google.com.mx')
time.sleep(2)

# Web Elements
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")