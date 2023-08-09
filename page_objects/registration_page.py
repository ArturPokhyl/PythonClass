from locators.registration_page_locators import RegistrationLocators
from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    def wait_for_visible_of_registration_form(self):
        self.wait_for_element_to_be_visible(RegistrationLocators.block_reg_form)

    def set_name(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_name, keys_to_send)

    def set_last_name(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_last_name, keys_to_send)

    def set_email(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_email, keys_to_send)

    def set_password(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_password, keys_to_send)

    def set_retry_password(self, keys_to_send):
        self.send_keys(RegistrationLocators.input_retry_password, keys_to_send)

    def click_register_button(self):
        self.click_element(RegistrationLocators.btn_register)
