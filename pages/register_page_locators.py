from selenium.webdriver.common.by import By


class RegisterPageLocators:
    # CONTACT INFO
    FIRST_NAME_TEXT_BOX = (By.NAME, "firstName")
    LAST_NAME_TEXT_BOX = (By.NAME, "lastName")
    PHONE_NUMBER_TEXT_BOX = (By.NAME, "phone")
    EMAIL_TEXT_BOX = (By.NAME, "userName")

    # MAILING INFO
    ADDRESS_TEXT_BOX = (By.NAME, "address1")
    CITY_TEXT_BOX = (By.NAME, "city")
    STATE_TEXT_BOX = (By.NAME, "state")
    POSTAL_CODE_TEST_BOX = (By.NAME, "postalCode")
    #COUNTRY_BTN = (By.NAME, "country")

    # USERNAME AND PASSWORD
    USER_NAME_TEXT_BOX = (By.ID, "email")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    CONFIRM_PASSWORD_TEXT_BOX = (By.NAME, "confirmPassword")
    SUBMIT_BUTTON = (By.NAME, "submit")
