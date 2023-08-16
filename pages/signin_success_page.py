from pages.base_page import BasePage
from pages.signin_success_page_locator import SignInSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignInSuccessPage(BasePage):
    def sign_in_success_lbl(self):
        lbl_signin_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, SignInSuccessPageLocators.SIGNIN_SUCCESS_LBL).text
        return lbl_signin_success_txt
