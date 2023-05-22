from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.textbox import TextBox
from controls.label import Label



class GaragePage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._my_profile_button = None
        self._add_car_button = None
        self._add_mileage_field = None
        self._add_car_brand = None
        self._add_car_model = None
        self._blue_button = None
        self._red_button = None
        self._car_added_alert = None
        self._car_updated_alert = None
        self._car_deleted_alert = None
        self._refactor_car_button = None
        self._red_confirmed_button = None
        self._log_out_button = None

    def get_my_profile_button(self):
        self._my_profile_button = Button(self._driver.find_element(By.ID, "userNavDropdown"))
        return self._my_profile_button

    def get_add_car_button(self):
        self._add_car_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Add car' and @class='btn btn-primary']"))
        return self._add_car_button

    def get_add_mileage_field(self):
        self._add_mileage_field = TextBox(self._driver.find_element(By.XPATH, "//input[@id='addCarMileage']"))
        return self._add_mileage_field

    def get_add_brand_field(self):
        self._add_car_brand = Button(self._driver.find_element(By.ID, "addCarBrand"))
        return self._add_car_brand

    def get_add_model_field(self):
        self._add_car_model = Button(self._driver.find_element(By.ID, "addCarModel"))
        return self._add_car_model

    def get_blue_button(self):
        self._blue_button = Button(self._driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[2]"))
        return self._blue_button

    def get_car_added_alert(self):
        self._car_added_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Car added']"))
        return self._car_added_alert

    def get_car_updated_alert(self):
        self._car_updated_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Car updated']"))
        return self._car_updated_alert

    def get_car_deleted_alert(self):
        self._car_deleted_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Car removed']"))
        return self._car_deleted_alert

    def get_refactor_car_button(self):
        self._refactor_car_button = Button(self._driver.find_element(By.XPATH, "(//button[@class='car_edit btn btn-edit'])[1]"))
        return self._refactor_car_button

    def get_red_button(self):
        self._red_button = Button(self._driver.find_element(By.XPATH, "//button[@class='btn btn-outline-danger']"))
        return self._red_button

    def get_red_confirmed_button(self):
        self._red_confirmed_button = Button(self._driver.find_element(By.XPATH, "//button[@class='btn btn-danger']"))
        return self._red_confirmed_button

    def get_log_out_button(self):
        self._log_out_button = Button(self._driver.find_element(By.XPATH, "//a[@class='btn btn-link text-danger btn-sidebar sidebar_btn']"))
        return self._log_out_button