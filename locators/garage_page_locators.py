from selenium.webdriver.common.by import By


class GaragePageLocators:
    btn_add_car = (By.XPATH, "//*[@class='panel-page']//button[contains(text(), 'Add car')]")
    block_empty_page = (By.XPATH, "//*[@class='panel-page_empty panel-empty']")
    block_car = (By.XPATH, "//*[@class='car jumbotron']")
    block_car_name = (By.XPATH, "//*[@class='car_name h2']")
    input_miles = (By.NAME, "miles")
