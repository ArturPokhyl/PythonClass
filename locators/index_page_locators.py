from selenium.webdriver.common.by import By


class IndexPageLocators:
    btn_sign_up = (By.XPATH, "//button[contains(text(), 'Sign up')]")
    btn_sign_in = (By.XPATH, "//button[contains(@class, 'header_signin')]")
