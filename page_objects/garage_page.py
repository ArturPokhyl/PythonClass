import allure

from locators.garage_page_locators import GaragePageLocators
from page_objects.base_page import BasePage


class GaragePage(BasePage):

    @allure.step("Wait for 'Garage' page load")
    def wait_for_page_load(self):
        self.wait_for_element_to_be_visible(GaragePageLocators.block_empty_page)
        self.wait_for_element_to_be_visible(GaragePageLocators.btn_add_car)

    @allure.step("Click at button 'Add car'")
    def click_add_car_button(self):
        self.click_element(GaragePageLocators.btn_add_car)

    @allure.step("Wait for visible of car")
    def wait_for_car_visible(self):
        self.wait_for_element_to_be_visible(GaragePageLocators.block_car)

    @allure.step("Get car name")
    def get_car_name(self):
        return self.get_element_text(GaragePageLocators.block_car_name)

    @allure.step("Get car miles")
    def get_miles(self):
        return self.get_element_text(GaragePageLocators.input_miles)
