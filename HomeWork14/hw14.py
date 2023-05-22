from driver import Driver
from main_page import MainPage
from login_page import LoginPage
from bot_page import BotPage



class TestLoginToSite:

    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.driver.maximize_window()
        self.bot_page = BotPage()
        self.login_page = LoginPage()
        self.main_page = MainPage()


    def setup_method(self):
        self.driver.get("https://admin-demo.nopcommerce.com/")

    def test_get_login_check(self):
        # if self.bot_page.get_bot_button().is_enabled():
        #     self.bot_page.get_bot_button().click()
        # else:
        #     pass
        self.login_page.get_login_textbox().send_keys('admin@yourstore.com')
        self.login_page.get_password_textbox().send_keys('admin')
        self.login_page.get_login_submit_button().click()
        result = self.main_page.get_user_label()
        assert result == "John Smith"

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.quit()
