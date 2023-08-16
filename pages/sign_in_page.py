from pages.base_page import BasePage
from pages.sign_in_page_locator import SignInPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignInPage(BasePage):

    def wait_and_click_signin_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignInPageLocators.SIGN_IN_LINK).click()

    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignInPageLocators.USER_NAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def wait_and_type_password(self, username_and_pw_list):
        self.find_element(SignInPageLocators.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def click_submit_btn(self):
        self.find_element(SignInPageLocators.SUBMIT_BUTTON).click()
