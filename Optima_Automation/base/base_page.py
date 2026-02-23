import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    WebDriverException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.logger = logging.getLogger(__name__)
        self.actions = ActionChains(self.driver)

    def go_to_url(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Navigated to URL: {url}")
        except WebDriverException as e:
            self.logger.error(f"Failed to navigate to URL {url}: {e}")
            raise


    def get_text(self, by, locator):
        try:
            element = self.find_element(by, locator)
            text = element.text.strip()
            self.logger.info(f"Text from element {locator}: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Error getting text from {locator}: {e}")
            raise

    def is_element_visible(self, by, locator):
        try:
            visible = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            self.logger.warning(f"Element not visible: {locator}")
            return False

    def wait_until_clickable(self, by, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            self.logger.info(f"Element is clickable: {locator}")
        except TimeoutException as e:
            self.logger.error(f"Element not clickable: {locator}")
            raise

    def wait_for_element_disappear(self, by, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until_not(
                EC.presence_of_element_located((by, locator))
            )
            self.logger.info(f"Element disappeared: {locator}")
        except TimeoutException:
            self.logger.warning(f"Element did not disappear: {locator}")

    def scroll_to_element(self, by, locator):
        try:
            element = self.find_element(by, locator)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)
            self.logger.info(f"Scrolled to element: {locator}")
        except Exception as e:
            self.logger.error(f"Error scrolling to element {locator}: {e}")
            raise

    def scroll_down(self, pixels=500):
        try:
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
            self.logger.info(f"Scrolled down by {pixels} pixels.")
        except Exception as e:
            self.logger.error(f"Error scrolling down: {e}")
            raise

    def scroll_up(self, pixels=500):
        try:
            self.driver.execute_script(f"window.scrollBy(0, -{pixels});")
            self.logger.info(f"Scrolled up by {pixels} pixels.")
        except Exception as e:
            self.logger.error(f"Error scrolling up: {e}")
            raise

    def hover_over_element(self, by, locator):
        try:
            element = self.find_element(by, locator)
            self.actions.move_to_element(element).perform()
            self.logger.info(f"Hovered over element: {locator}")
        except Exception as e:
            self.logger.error(f"Error hovering over element {locator}: {e}")
            raise

    def press_key(self, key):
        try:
            self.actions.send_keys(key).perform()
            self.logger.info(f"Pressed key: {key}")
        except Exception as e:
            self.logger.error(f"Error pressing key {key}: {e}")
            raise

    def wait_for_page_load(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            self.logger.info("Page load complete.")
        except TimeoutException:
            self.logger.warning("Page did not load within timeout.")

    def get_title(self):
        try:
            title = self.driver.title
            self.logger.info(f"Page title: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Error getting title: {e}")
            raise

    def get_current_url(self):
        try:
            url = self.driver.current_url
            self.logger.info(f"Current URL: {url}")
            return url
        except Exception as e:
            self.logger.error(f"Error getting current URL: {e}")
            raise

    def close_browser(self):
        try:
            self.driver.quit()
            self.logger.info("Browser closed.")
        except Exception as e:
            self.logger.error(f"Error closing browser: {e}")
            raise


