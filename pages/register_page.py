from pages.base_page import BasePage
from pages.register_page_locators import RegisterPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class RegisterPage(BasePage):
    # contact info
    def wait_and_type_first_name(self, con_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.FIRST_NAME_TEXT_BOX).send_keys(
            con_information[0])

    def wait_and_type_last_name(self, con_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.LAST_NAME_TEXT_BOX).send_keys(
            con_information[1])

    def wait_and_type_phone_number(self, con_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.PHONE_NUMBER_TEXT_BOX).send_keys(
            con_information[2])

    def wait_and_type_email(self, con_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.EMAIL_TEXT_BOX).send_keys(
            con_information[3])

        # mailing info

    def wait_and_type_address(self, mail_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.ADDRESS_TEXT_BOX).send_keys(
            mail_information[0])

    def wait_and_type_city(self, mail_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.CITY_TEXT_BOX).send_keys(
            mail_information[1])

    def wait_and_type_state(self, mail_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.STATE_TEXT_BOX).send_keys(
            mail_information[2])

    def wait_and_type_postal(self, mail_information):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.POSTAL_CODE_TEST_BOX).send_keys(
            mail_information[3])

        #  def click_country_btn(self):
        # self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.COUNTRY_BTN).click()

        # username and password

    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.USER_NAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def type_password(self, username_and_pw_list):
        self.find_element(RegisterPageLocators.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def type_confirm_password(self, username_and_pw_list):
        self.find_element(RegisterPageLocators.CONFIRM_PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def click_submit_btn(self):
        self.find_element(RegisterPageLocators.SUBMIT_BUTTON).click()
    # This is a test
