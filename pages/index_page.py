from pages.base_page import BasePage
from pages.index_page_locator import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


# This is our super class
class IndexPage(BasePage):

    def wait_and_click_register_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.REGISTER_LINK).click()
