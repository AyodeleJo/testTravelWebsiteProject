from selenium.webdriver.common.by import By


class SignInPageLocators:
    SIGN_IN_LINK = (By.LINK_TEXT, "sign-in")
    USER_NAME_TEXT_BOX = (By.NAME, "userName")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    SUBMIT_BUTTON = (By.NAME, "submit")
