from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@id='flexCheckDefault']")
    LOGIN_BUTTON = (By.XPATH, "//div[@class='mb-3 d-grid']")
    LOGOUT_LINK = (By.XPATH, "//a[@href='/logout']")


    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.REMEMBER_ME_CHECKBOX).click()
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # def logout(self):
    #     self.driver.find_element(*self.LOGOUT_LINK).click()
