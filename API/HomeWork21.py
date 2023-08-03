import time

import requests

BASE_URL = "https://qauto2.forstudy.space/api"


class User:
    def __init__(self):
        self.name = "John"
        self.last_name = "Dou"
        self.email = f"test{int(time.time())}@test.com"
        self.password = "Test11223344"


class TestProfileUser:
    def setup_method(self):
        self.user = User()
        self.session = requests.session()
        print("\n-----------<<START>>--------------")
        print(f"{self.user.email}")
        print(f"{self.user.password}")

    def _registration(self):
        registration_data = {
            "name": self.user.name,
            "lastName": self.user.last_name,
            "email": self.user.email,
            "password": self.user.password,
            "repeatPassword": self.user.password,
        }
        return self.session.post(f"{BASE_URL}/auth/signup", json=registration_data)

    def _login(self):
        login_dict = {
            "email": self.user.email,
            "password": self.user.password,
            "remember": False,
        }
        login_result = self.session.post(url=f"{BASE_URL}/auth/signin", json=login_dict)
        if login_result.status_code != 200:
            raise AssertionError(
                f"Failed to sign in for deleting. Status code: {login_result.status_code}"
            )
        return login_result

    def _delete(self):
        delete_result = self.session.delete(url=f"{BASE_URL}/users/")
        if delete_result.status_code != 200:
            raise AssertionError(
                f"Failed to delete user. Status code: {delete_result.status_code}"
            )
        print("\n User was deleted")
        return delete_result

    def test_registration(self):
        result = self._registration()
        assert result.status_code == 201
        assert result.json()["status"] == "ok"

    def test_login(self):
        self._registration()
        result = self._login()
        assert result.status_code == 200
        assert result.json()["status"] == "ok"

    def test_user(self):
        self._registration()
        self._login()
        result = self.session.get(f"{BASE_URL}/users/profile")
        assert result.status_code == 200
        assert result.json()["status"] == "ok"
        assert result.json()["data"]["name"] == self.user.name
        assert result.json()["data"]["lastName"] == self.user.last_name

    def teardown_method(self):
        self._login()
        self._delete()
        print("-----------<<FINISH>>--------------")
