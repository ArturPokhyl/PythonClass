from core.helpers.driver import Driver
from page_objects.add_car_page import AddCarPage
from page_objects.garage_page import GaragePage
from page_objects.index_page import IndexPage
from page_objects.login_page import LoginPage
from page_objects.registration_page import RegistrationPage


class BaseFacade:
    def __init__(self):
        self.driver = Driver.driver
        self.indexPage = IndexPage()
        self.registrationPage = RegistrationPage()
        self.login = LoginPage()
        self.garage = GaragePage()
        self.add_car = AddCarPage()
