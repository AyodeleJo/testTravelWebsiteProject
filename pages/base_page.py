from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))

    def find_element(self, locator_type_and_locator_tuple):
        return self.driver.find_element(*locator_type_and_locator_tuple)

    # def drop_down(self, locator_type_and_locator_tuple):

    # country_drop_down = self.driver.find_element(locator_type_and_locator_tuple)
    # drop_down_select = Select(country_drop_down)
    # drop_down_select.select_by_index(2)
    # return self.driver.find_element(locator_type_and_locator_tuple)
