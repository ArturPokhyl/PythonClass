import allure

from core.decorator_failed_tests import decorator_screenshot
from core.helpers.api_helper import APIHelper
from core.helpers.driver import Driver
from core.models.Car import Car
from core.models.User import User
from facades.garage_facade import GarageFacade
from facades.login_facade import LoginFacade
from page_objects.garage_page import GaragePage


@allure.suite("Garage tests")
@allure.feature("Add car to garage")
class TestGarage:
    def setup_method(self):
        self.user = User()
        self.car = Car()
        self.session = APIHelper().get_session()
        self.driver = Driver().get_chrome_driver()
        self.garage = GaragePage()
        self.login_facade = LoginFacade()
        self.garage_facade = GarageFacade()
        APIHelper().registration(self.user, self.session)

    @allure.description("Create car via WEB UI")
    @decorator_screenshot
    def test_add_car(self):
        self.login_facade.login_user(self.user)
        self.garage_facade.add_car_to_garage(self.car)
        self.garage.wait_for_car_visible()
        assert (
            self.garage.get_car_name() == f"{self.car.car_brand} {self.car.car_model}"
        )

    @allure.description("Create car via WEB UI and check it via API")
    @decorator_screenshot
    def test_garage_api(self):
        self.login_facade.login_user(self.user)
        self.garage_facade.add_car_to_garage(self.car)
        self.garage.wait_for_car_visible()
        APIHelper().login(self.user, self.session)
        cars = APIHelper().get_cars(self.session)
        assert cars.json()["status"] == "ok"
        assert cars.json()["data"][0]["brand"] == self.car.car_brand
        assert cars.json()["data"][0]["model"] == self.car.car_model
        assert cars.json()["data"][0]["mileage"] == int(self.car.mileage)

    def teardown_method(self):
        APIHelper().login(self.user, self.session)
        APIHelper().delete(self.session)
        Driver.close_driver()
