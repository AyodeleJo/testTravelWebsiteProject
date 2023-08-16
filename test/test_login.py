from test_utils import *
from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from pages.sign_in_page import SignInPage
from pages.signin_success_page import SignInSuccessPage
from resources.constants import TEST_SITE_URL


class TestLogin:
    #  Test case 1 (Registering the users)

    def test_register_new_user(self, driver, username_password, contact_info, mailing_info):
        index_page = IndexPage(driver)

        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_first_name(contact_info)
        register_page.wait_and_type_last_name(contact_info)
        register_page.wait_and_type_phone_number(contact_info)
        register_page.wait_and_type_email(contact_info)

        register_page.wait_and_type_address(mailing_info)
        register_page.wait_and_type_city(mailing_info)
        register_page.wait_and_type_state(mailing_info)
        register_page.wait_and_type_postal(mailing_info)
        # register_page.click_country_btn()

        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password(username_password)
        register_page.click_submit_btn()

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"

    def test_sigin_in_user(self, driver, username_password):
        sign_in_page = SignInPage(driver)
        sign_in_page.wait_and_click_signin_btn()

        sign_in_page.wait_and_type_user_name(username_password)
        sign_in_page.wait_and_type_password(username_password)
        sign_in_page.click_submit_btn()

        sign_in_success_page = SignInSuccessPage(driver)
        sign_in_success_page_lbl = sign_in_success_page.sign_in_success_lbl()
        assert sign_in_success_page_lbl == "Login Successfully", "test failed"


