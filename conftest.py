import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def set_up():
    print("test start")

    yield
    print("test finish")
    # driver.quit()