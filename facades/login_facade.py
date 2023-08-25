import allure

from constans.url_constants import DEFAULT_URL
from core.models import User
from facades.base_facade import BaseFacade


class LoginFacade(BaseFacade):

    def __init__(self):
        super().__init__()

    @allure.step("Login user {1}")
    def login_user(self, user: User):
        self.driver.get(DEFAULT_URL)
        self.indexPage.click_sign_in_button()
        self.login.wait_for_visible_of_registration_form()
        self.login.set_email(user.email)
        self.login.set_password(user.password)
        self.login.click_login_button()
