import time

from core.helpers.api_helper import APIHelper
from core.helpers.driver_helper import Driver
from core.models.Car import Car
from core.models.User import User
from page_objects.add_car_page import AddCarPage
from page_objects.garage_page import GaragePage
from page_objects.index_page import IndexPage
from page_objects.login_page import LoginPage
from page_objects.registration_page import RegistrationPage


class TestGarage:
    def setup_method(self):
        self.user = User()
        self.car = Car()
        self.session = APIHelper().get_session()
        self.driver = Driver().get_chrome_driver()
        self.indexPage = IndexPage()
        self.registrationPage = RegistrationPage()
        self.login = LoginPage()
        self.garage = GaragePage()
        self.add_car = AddCarPage()
        APIHelper().registration(self.user, self.session)

    def login_user(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.indexPage.click_sign_in_button()
        self.login.wait_for_visible_of_registration_form()
        self.login.set_email(self.user.email)
        self.login.set_password(self.user.password)
        self.login.click_login_button()

    def add_car_to_garage(self):
        self.garage.wait_for_page_load()
        self.garage.click_add_car_button()
        self.add_car.wait_for_page_load()
        self.add_car.set_car_brand(self.car.car_brand)
        self.add_car.set_car_model(self.car.car_model)
        self.add_car.set_car_mileage(self.car.mileage)
        self.add_car.click_add_button()

    def test_add_car(self):
        self.login_user()
        self.add_car_to_garage()
        self.garage.wait_for_car_visible()
        assert (
            self.garage.get_car_name() == f"{self.car.car_brand} {self.car.car_model}"
        )

    def test_garage_api(self):
        self.login_user()
        self.add_car_to_garage()
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
