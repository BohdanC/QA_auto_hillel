from selenium import webdriver
from selenium.webdriver.common.by import By
from locators_constants import LocatorsConstants
import time


def test_admin_demo_positive():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.get("https://admin-demo.nopcommerce.com/")
    time.sleep(10)
    driver.find_element(By.XPATH, LocatorsConstants.BOT_CHECK_XPATH).click()
    time.sleep(3)
    driver.find_element(By.XPATH, LocatorsConstants.EMAIL_FIELD_XPATH).send_keys('admin@yourstore.com')
    driver.find_element(By.XPATH, LocatorsConstants.PASSWORD_FIELD_XPATH).send_keys('admin')
    driver.find_element(By.XPATH, LocatorsConstants.SUBMIT_BUTTON_XPATH).click()
    user = driver.find_element(By.XPATH, LocatorsConstants.LOGGED_IN_CHECK_XPATH)
    assert user.is_displayed()
