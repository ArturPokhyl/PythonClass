import allure

from locators.login_page_locators import LoginPageLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Wait fir visible of registration form")
    def wait_for_visible_of_registration_form(self):
        self.wait_for_element_to_be_visible(LoginPageLocators.block_login_form)

    @allure.step("Set email {1}")
    def set_email(self, keys_to_send):
        self.send_keys(LoginPageLocators.input_email, keys_to_send)

    @allure.step("Set password {1}")
    def set_password(self, keys_to_send):
        self.send_keys(LoginPageLocators.input_password, keys_to_send)

    @allure.step("Click at button 'Login'")
    def click_login_button(self):
        self.click_element(LoginPageLocators.btn_login)
