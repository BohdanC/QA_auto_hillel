from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage


class BotPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__bot_button: Button = None

    def get_bot_button(self):
        self.__bot_button = Button(self._driver.find_element(By.XPATH,
                                   "//button[@type='submit']"))

        return self.__bot_button