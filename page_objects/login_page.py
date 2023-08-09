from locators.login_page_locators import LoginPageLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    def wait_for_visible_of_registration_form(self):
        self.wait_for_element_to_be_visible(LoginPageLocators.block_login_form)

    def set_email(self, keys_to_send):
        self.send_keys(LoginPageLocators.input_email, keys_to_send)

    def set_password(self, keys_to_send):
        self.send_keys(LoginPageLocators.input_password, keys_to_send)

    def click_login_button(self):
        self.click_element(LoginPageLocators.btn_login)
