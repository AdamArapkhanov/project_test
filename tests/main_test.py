import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from base.base_page import BasePage
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwithes', ['enable-logging'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(r'C:\\Users\\Адам\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome(options=options, service=g)
    base_url = 'https://zetzet.ru/'
    driver.get(base_url)
    # driver.maximize_window()

    lp = Login_page(driver)
    lp.authorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.product_in_cart()






