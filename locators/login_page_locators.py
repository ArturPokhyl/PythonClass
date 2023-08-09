from selenium.webdriver.common.by import By


class LoginPageLocators:
    block_login_form = (By.XPATH, "//app-signin-modal")
    input_email = (By.ID, "signinEmail")
    input_password = (By.ID, "signinPassword")
    btn_login = (By.XPATH, "//button[text()='Login']")
