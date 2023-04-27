from label import Label
from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__login_label: Label = None

    def get_user_label(self):
        self.__login_label = Label(self._driver.find_element(By.XPATH,
                                   "//li/a[text()='John Smith']"))

        return self.__login_label.get_text()