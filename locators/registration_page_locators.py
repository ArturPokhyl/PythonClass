from selenium.webdriver.common.by import By


class RegistrationLocators:
    block_reg_form = (By.XPATH, "//app-signup-modal")
    input_name = (By.ID, "signupName")
    input_last_name = (By.ID, "signupLastName")
    input_email = (By.ID, "signupEmail")
    input_password = (By.ID, "signupPassword")
    input_retry_password = (By.ID, "signupRepeatPassword")
    btn_register = (By.XPATH, "//button[text()='Register']")
