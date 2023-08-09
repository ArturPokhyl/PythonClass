from selenium.webdriver.common.by import By


class AddCarPageLocators:
    select_car_brand = (By.ID, "addCarBrand")
    select_car_model = (By.XPATH, "//*[@id = 'addCarModel']")
    input_car_mileage = (By.ID, "addCarMileage")
    btn_add = (By.XPATH, "//app-add-car-modal//button[@class = 'btn btn-primary']")
