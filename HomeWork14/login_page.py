from button import Button
from textbox import Textbox
from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__login_textbox: Textbox = None
        self.__password_textbox: Textbox = None
        self.__login_submit_button: Button = None

    def get_login_textbox(self):
        self.__login_textbox = Textbox(self._driver.find_element(By.XPATH,
                                                            "//input[@id='Email']"))
        return self.__login_textbox

    def get_password_textbox(self):
        self.__password_textbox = Textbox(self._driver.find_element(By.XPATH,
                                                            "//input[@id='Password']"))
        return self.__password_textbox

    def get_login_submit_button(self):
        self.__login_submit_button = Button(self._driver.find_element(By.XPATH,
                                                            "//button[@type='submit']"))
        return self.__login_submit_button