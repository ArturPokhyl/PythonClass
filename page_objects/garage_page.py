from locators.garage_page_locators import GaragePageLocators
from page_objects.base_page import BasePage


class GaragePage(BasePage):
    def wait_for_page_load(self):
        self.wait_for_element_to_be_visible(GaragePageLocators.block_empty_page)
        self.wait_for_element_to_be_visible(GaragePageLocators.btn_add_car)

    def click_add_car_button(self):
        self.click_element(GaragePageLocators.btn_add_car)

    def wait_for_car_visible(self):
        self.wait_for_element_to_be_visible(GaragePageLocators.block_car)

    def get_car_name(self):
        return self.get_element_text(GaragePageLocators.block_car_name)

    def get_miles(self):
        return self.get_element_text(GaragePageLocators.input_miles)
