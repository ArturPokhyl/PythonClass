import time


class User:
    def __init__(self):
        self.name = "John"
        self.last_name = "Dou"
        self.email = f"test{int(time.time())}@test.com"
        self.password = "Test11223344"
