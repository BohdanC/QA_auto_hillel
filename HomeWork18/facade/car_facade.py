import allure

from facade.facade_base import FacadeBase


class CarFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure.step("Creating simple car Audi TT with own mileage")
    def create_car(self, mileage):
        self._garage_page.get_add_car_button().click()
        self._garage_page.get_add_mileage_field().fill_field(mileage)

    @allure.step("Clicking blue button to add/refactor car")
    def click_blue_button(self):
        self._garage_page.get_blue_button().click()

    @allure.step("deleting car")
    def delete_car(self):
        self._garage_page.get_refactor_car_button().click()
        self._garage_page.get_red_button().click()
        self._garage_page.get_red_confirmed_button().click()

    @allure.step("refactoring car")
    def refactor_car(self, mileage):
        self._garage_page.get_refactor_car_button().click()
        self._garage_page.get_add_mileage_field().fill_field(mileage)

    def check_add_car(self):
        return self._garage_page.get_car_added_alert().is_displayed()

    def check_delete_car(self):
        return self._garage_page.get_car_deleted_alert().is_displayed()

    def check_refactor_car(self):
        return self._garage_page.get_car_updated_alert().is_displayed()

    def log_out(self):
        return self._garage_page.get_log_out_button().click()