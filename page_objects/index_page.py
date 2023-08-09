from locators.index_page_locators import IndexPageLocators
from page_objects.base_page import BasePage


class IndexPage(BasePage):
    def click_sign_up_button(self):
        self.click_element(IndexPageLocators.btn_sign_up)

    def click_sign_in_button(self):
        self.click_element(IndexPageLocators.btn_sign_in)
