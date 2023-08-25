import allure

from core.models import Car
from facades.base_facade import BaseFacade


class GarageFacade(BaseFacade):

    def __init__(self):
        super().__init__()

    @allure.step("Add car {1} to garage")
    def add_car_to_garage(self, car: Car):
        self.garage.wait_for_page_load()
        self.garage.click_add_car_button()
        self.add_car.wait_for_page_load()
        self.add_car.set_car_brand(car.car_brand)
        self.add_car.set_car_model(car.car_model)
        self.add_car.set_car_mileage(car.mileage)
        self.add_car.click_add_button()
