import requests

from core.config_reader import ConfigReader
from core.models.User import User


class APIHelper:
    def __init__(self):
        self.base_url = ConfigReader().get_base_url() + "/api"

    @staticmethod
    def get_session():
        return requests.session()

    def registration(self, user: User(), session):
        registration_data = {
            "name": user.name,
            "lastName": user.last_name,
            "email": user.email,
            "password": user.password,
            "repeatPassword": user.password,
        }
        print(self.base_url)
        print(f"{self.base_url}/auth/signup")
        print(registration_data)
        return session.post(f"{self.base_url}/auth/signup", json=registration_data)

    def login(self, user: User(), session):
        login_dict = {
            "email": user.email,
            "password": user.password,
            "remember": False,
        }
        login_result = session.post(url=f"{self.base_url}/auth/signin", json=login_dict)
        if login_result.status_code != 200:
            raise AssertionError(
                f"Failed to sign in for deleting. Status code: {login_result.status_code}"
            )
        return login_result

    def delete(self, session):
        delete_result = session.delete(url=f"{self.base_url}/users/")
        if delete_result.status_code != 200:
            raise AssertionError(
                f"Failed to delete user. Status code: {delete_result.status_code}"
            )
        print("\n User was deleted")
        return delete_result

    def get_cars(self, session):
        result = session.get(url=f"{self.base_url}/cars")
        if result.status_code != 200:
            raise AssertionError(
                f"Failed to get cars. Status code: {result.status_code}"
            )
        return result
