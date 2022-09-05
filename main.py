# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# Web Drivers ==> Edge
ser = Service("C:/WebDrivers/msedgedriver.exe")
op = webdriver.EdgeOptions()
driver = webdriver.Edge(service=ser, options=op)
driver.maximize_window()
driver.get('https://demo.guru99.com/selenium/newtours/')
time.sleep(5)

# Web Elements
# user_box = driver.find_element(By.NAME, "userName")
# user_box = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input")
user_box = driver.find_element(By.CSS_SELECTOR, "body > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(3) > form > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]")
# pass_box = driver.find_element(By.NAME, "password")
pass_box = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input")
submit_button = driver.find_element(By.NAME, "submit")
register_link = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")


# Web UI Keywords
user_box.send_keys('user')
pass_box.send_keys('password')
# submit_button.click()
register_link.click()
time.sleep(2)

registration_form_link = driver.find_element(By.LINK_TEXT, "registration form")
assert registration_form_link.text.__eq__("registration form")
print("Assert 1 is passed")
assert registration_form_link.tag_name == "a"
print("Assert 2 is passed")