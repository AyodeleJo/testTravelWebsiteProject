from selenium import webdriver
import pytest as pytest


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def user_name_password():
    username = "ayodele.h.joseph@gmail.com"
    password = "Mypassword1."
    return [username, password]


@pytest.fixture(scope="function")
def username_password():
    user_name = "ayo21"
    password = "pass123"
    return [user_name, password]


@pytest.fixture(scope="function")
def contact_info():
    fname = "Margot"
    lname = "speed"
    phone = "123456778"
    email = "margotSpeed@gmail.com"
    return [fname, lname, phone, email]


@pytest.fixture(scope="function")
def mailing_info():
    address = "73, lively street"
    city = "Ottawa"
    province = "Ontario"
    postal_code = "K1V L26"
    return [address, city, province, postal_code]
