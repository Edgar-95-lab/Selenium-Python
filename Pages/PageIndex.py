import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class PageIndex:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.user_box = (By.NAME, "userName")
        self.pass_box = (By.NAME, "password")
        self.register_link = (By.LINK_TEXT, "REGISTER")
        self.dresses_link = (By.LINK_TEXT, "DRESSES")
        self.sort_by = (By.ID, "selectProductSort")
        self.signin_link = (By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")

    def click_register(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.register_link).click()

    def click_dresses(self, value, no_screenshot):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.dresses_link).click()
        self.driver.execute_script("window.scrollTo(0,900)")
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element(*self.sort_by)).select_by_visible_text(value)
        time.sleep(2)
        self.driver.get_screenshot_as_file("screenshots/"+no_screenshot+".png")

    def login(self, user_name, password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.pass_box).send_keys(password)
        try:
            signin = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.signin_link))
        except:
            print("Element is not clickable")
        self.driver.find_element(*self.signin_link).click()

    def login_by_tab(self, user_name, password):
        self.driver.find_element(*self.user_box).send_keys(user_name + Keys.TAB + password + Keys.TAB + Keys.ENTER)