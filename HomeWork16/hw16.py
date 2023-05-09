import requests


class UserLogin:
    def __init__(self, email, password, remember):
        self.email = email
        self.password = password
        self.remember = remember


class UserRegister:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
  #      self.repeatPassword = repeat_password





class TestAuth:
    def setup_class(self):
        self.session = requests.session()


    def setup_method(self):
        self.user_register = UserRegister(name="Testname", last_name="Test_lastname", email="test@test.com",
                                          password="Password123", repeat_password="Password123")
        self.user_to_login = UserLogin("test@test.com", "Password123", False)



    def test_user_register(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")
        result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_register.__dict__)
        assert result.json()["status"] == "ok"

    def test_user_login(self):
        result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signin",
                                   json=self.user_to_login.__dict__)
        assert result.json()["status"] == "ok"

    def test_delete_user(self):
        result = self.session.delete("https://qauto2.forstudy.space/api/users")
        assert result.json()["status"] == "ok"



    def teardown_method(self):
        self.session.get("https://qauto2.forstudy.space/api/auth/logout")

    def teardown_class(self):
        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin",
                          json=self.user_to_login.__dict__)
        self.session.delete("https://qauto2.forstudy.space/api/users")
