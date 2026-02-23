import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..base.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ( NoSuchElementException,TimeoutException,ElementClickInterceptedException,ElementNotInteractableException,StaleElementReferenceException,WebDriverException)



class CustomerManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # self.wait = WebDriverWait(driver, 10)

    # Locators
    MENU = (By.XPATH, "//i[@class='bx bx-grid-alt bx-sm pt-1']")
    CUSTOMER_MANAGEMENT = (By.XPATH, "//ul[@class='list-unstyled list-group notification navs module-wise']//a[@routerlinkactive='active'][normalize-space()='Customer Management']")
    ADD_NEW_BUTTON = (By.XPATH, "//button[contains(text(),'Add New')]")
    CUSTOMER_NAME = (By.XPATH, "//input[@formcontrolname='customerName']")
    PARENT_COMPANY = (By.XPATH, "//input[@formcontrolname='parentCompany']")
    ADDRESS = (By.XPATH, "//input[@formcontrolname='address']")
    DEPARTMENT = (By.XPATH, "//input[@formcontrolname='department']")
    SUBSIDIARY = (By.XPATH, "//input[@formcontrolname='subsidiary']")
    LOCATION = (By.XPATH, "//input[@formcontrolname='location']")
    PHONE_NUMBER = (By.XPATH, "//input[@formcontrolname='phoneNumber']")
    EMAIL_ADDRESS = (By.XPATH, "//input[@formcontrolname='emailAddress']")
    COMMENTS = (By.XPATH, "//input[@formcontrolname='comments']")
    CONTACT_NAME = (By.XPATH, "//input[@formcontrolname='contactName']")
    CONTACT_PHONE = (By.XPATH, "//input[@formcontrolname='contactPhone']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    DROPDOWN_SEARCH = (By.XPATH,"//select[@id='mat-input-1']")
    SEARCH_INPUT = (By.XPATH,"//div[@class='filter-grid ng-star-inserted']//div[@class='search-text position-relative']//input[@class='form-control search-input mb-1 ng-untouched ng-pristine ng-valid']")

    def navigate_to_customer_management(self):
        time.sleep(5)
        self.driver.find_element(*self.MENU).click()
        self.driver.find_element(*self.CUSTOMER_MANAGEMENT).click()
        print("Navigated to Customer Management page successfully.")
        time.sleep(2)

    def create_customer(self, test_data):
        self.navigate_to_customer_management()
        self.driver.find_element(*self.ADD_NEW_BUTTON).click()
        time.sleep(2)
        # Fill in customer detail
        self.driver.find_element(*self.CUSTOMER_NAME).send_keys(test_data[0])
        self.driver.find_element(*self.PARENT_COMPANY).send_keys(test_data[1])
        self.driver.find_element(*self.ADDRESS).send_keys(test_data[2])
        self.driver.find_element(*self.DEPARTMENT).send_keys(test_data[3])
        self.driver.find_element(*self.SUBSIDIARY).send_keys(test_data[4])
        self.driver.find_element(*self.LOCATION).send_keys(test_data[5])
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(test_data[6])
        self.driver.find_element(*self.EMAIL_ADDRESS).send_keys(test_data[7])
        self.driver.find_element(*self.COMMENTS).send_keys(test_data[8])
        self.driver.find_element(*self.CONTACT_NAME).send_keys(test_data[9])
        print("Customer details filled in successfully.")

    def search_parameter(self,testdata):
        try:
        # Navigate to Customer Management page
            self.navigate_to_customer_management()
            print("Navigated to Customer Management page for search parameter.")
            dropdown = self.driver.find_element(*self.DROPDOWN_SEARCH)
            select = Select(dropdown)
            select.select_by_value("customerName")
            input_value=self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
            input_value.send_keys(testdata[0])
            print("Search parameter filled in successfully.",testdata[0])
            time.sleep(5)
        except  ElementNotInteractableException as e:
            print("Element not found:", e)


