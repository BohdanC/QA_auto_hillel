from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:
    driver = None

    @staticmethod
    def get_firefox_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = webdriver.Firefox()
            return Driver.driver
        else:
            return Driver.driver

    @staticmethod
    def get_chrome_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = webdriver.Chrome()
            return Driver.driver
        else:
            return Driver.driver