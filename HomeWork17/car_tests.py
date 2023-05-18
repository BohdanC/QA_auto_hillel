from models.register_post_model import RegisterPostModel
from models.car_post_model import CarPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from time import time



class TestAuthentication:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        self.session = requests.session()
        register_user = RegisterPostModel("Jon", "Snow", "test@test.mail", "Qwerty123", "Qwerty123")
        created_car = CarPostModel(1, 1, 1000)
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user.__dict__)
        self.session.post("https://qauto2.forstudy.space/api/cars", json=created_car.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("test@test.mail")
        self.login_page.get_password_field().fill_field("Qwerty123")
        self.login_page.get_login_button().click()


    def test_add_car(self):
        self.garage_page.get_add_car_button().click()
        self.garage_page.get_add_mileage_field().fill_field("100")
        self.garage_page.get_blue_button().click()
        assert self.garage_page.get_car_added_alert().is_displayed()

    def test_delete_car(self):
        self.garage_page.get_refactor_car_button().click()
        self.garage_page.get_red_button().click()
        self.garage_page.get_red_confirmed_button().click()
        assert self.garage_page.get_car_deleted_alert().is_displayed()

    def test_refactor_car(self):
        self.garage_page.get_refactor_car_button().click()
        self.garage_page.get_add_mileage_field().fill_field("20")
        self.garage_page.get_blue_button().click()
        assert self.garage_page.get_car_updated_alert().is_displayed()



    def teardown_method(self):
        self.session.delete("https://qauto2.forstudy.space/api/cars/{1}")
        self.garage_page.get_log_out_button().click()


    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")

