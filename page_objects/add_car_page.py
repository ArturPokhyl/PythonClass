import allure

from locators.add_car_page_locators import AddCarPageLocators
from page_objects.base_page import BasePage


class AddCarPage(BasePage):
    @allure.step("Wait for 'Add car' page load")
    def wait_for_page_load(self):
        self.wait_for_element_to_be_visible(AddCarPageLocators.select_car_brand)
        self.wait_for_element_to_be_visible(AddCarPageLocators.select_car_model)
        self.wait_for_element_to_be_visible(AddCarPageLocators.input_car_mileage)

    @allure.step("Set car brand {1}")
    def set_car_brand(self, value: str):
        self.select_option(AddCarPageLocators.select_car_brand, value)

    @allure.step("Set car model {1}")
    def set_car_model(self, value: str):
        self.select_option(AddCarPageLocators.select_car_model, value)

    @allure.step("Set car mileage {1}")
    def set_car_mileage(self, value: str):
        self.send_keys(AddCarPageLocators.input_car_mileage, value)

    @allure.step("Click at button 'Add'")
    def click_add_button(self):
        self.click_element(AddCarPageLocators.btn_add)
