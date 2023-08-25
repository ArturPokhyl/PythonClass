import requests

from constans.api_path_constants import POST_SIGN_UP_USER, POST_SIGN_IN_USER, DELETE_USER, CARS
from constans.url_constants import DEFAULT_API_URL
from core.models.User import User


class APIHelper:
    def __init__(self):
        self.base_url = DEFAULT_API_URL

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
        print(f"{self.base_url}{POST_SIGN_UP_USER}")
        print(registration_data)
        return session.post(f"{self.base_url}{POST_SIGN_UP_USER}", json=registration_data)

    def login(self, user: User(), session):
        login_dict = {
            "email": user.email,
            "password": user.password,
            "remember": False,
        }
        login_result = session.post(url=f"{self.base_url}{POST_SIGN_IN_USER}", json=login_dict)
        if login_result.status_code != 200:
            raise AssertionError(
                f"Failed to sign in for deleting. Status code: {login_result.status_code}"
            )
        return login_result

    def delete(self, session):
        delete_result = session.delete(url=f"{self.base_url}{DELETE_USER}")
        if delete_result.status_code != 200:
            raise AssertionError(
                f"Failed to delete user. Status code: {delete_result.status_code}"
            )
        print("\n User was deleted")
        return delete_result

    def get_cars(self, session):
        result = session.get(url=f"{self.base_url}{CARS}")
        if result.status_code != 200:
            raise AssertionError(
                f"Failed to get cars. Status code: {result.status_code}"
            )
        return result
