from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.helpers.driver_helper import Driver


class BasePage:
    def __init__(self):
        self._driver = Driver().driver

    def click_element(self, locator):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(
                f"Element with locator {locator} not visible within {timeout} seconds."
            )
            return None

    def send_keys(self, locator, keys_to_send):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(keys_to_send)

    def select_option(self, locator, value):
        select_element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        select = Select(select_element)
        select.select_by_visible_text(value)

    def get_element_text(self, locator):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        return element.text
