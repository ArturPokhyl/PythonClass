import allure

from locators.registration_page_locators import RegistrationLocators
from page_objects.base_page import BasePage


class RegistrationPage(BasePage):

    @allure.step("Wait fir visible of registration form")
    def wait_for_visible_of_registration_form(self):
        self.wait_for_element_to_be_visible(RegistrationLocators.block_reg_form)

    @allure.step("Set name {1}")
    def set_name(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_name, keys_to_send)

    @allure.step("Set last name {1}")
    def set_last_name(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_last_name, keys_to_send)

    @allure.step("Set email {1}")
    def set_email(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_email, keys_to_send)

    @allure.step("Set password {1}")
    def set_password(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_password, keys_to_send)

    @allure.step("Set retry password {1}")
    def set_retry_password(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_retry_password, keys_to_send)

    @allure.step("Click at button 'Register'")
    def click_register_button(self):
        self.click_element(RegistrationLocators.btn_register)
