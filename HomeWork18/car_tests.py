from models.register_post_model import RegisterPostModel
from models.car_post_model import CarPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from facade.login_facade import LoginFacade
from facade.car_facade import CarFacade





class TestCars:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.login_facade = LoginFacade()
        self.garage_facade = CarFacade()
        self.session = requests.session()
        register_user = RegisterPostModel("Jon", "Snow", "test@test.mail", "Qwerty123", "Qwerty123")
        created_car = CarPostModel(1, 1, 1000)
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user.__dict__)
        self.session.post("https://qauto2.forstudy.space/api/cars", json=created_car.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.login_facade.open_login_form()
        self.login_facade.set_email_and_password_and_click_login_button("test@test.mail", "Qwerty123")


    def test_add_car(self):
        self.garage_facade.create_car(100)
        self.garage_facade.click_blue_button()
        assert self.garage_facade.check_add_car()

    def test_delete_car(self):
        self.garage_facade.delete_car()
        assert self.garage_facade.check_delete_car()

    def test_refactor_car(self):
        self.garage_facade.refactor_car("\b\b\b\b\b\b100020")
        self.garage_facade.click_blue_button()
        assert self.garage_facade.check_refactor_car()



    def teardown_method(self):
        self.garage_facade.log_out()


    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")

