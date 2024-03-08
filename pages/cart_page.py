import time

import select

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage
from webdriver_manager.core import driver



class Cart_page(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    action = ActionChains(driver)



    """Locators"""

    phone_number = "//input[@class='wa-input wa-phone']"
    drop_down_country = "//select[@class='wa-select js-region-field']"
    select_town = "(//input[@autocomplete='off'])[2]"
    price_in_cart = "//div[@class='s-section-header wa-flex-box full-line middle']"
    quantity = "//i[@class='cart-qty']"



    """getters"""

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_drop_down_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drop_down_country)))

    def get_select_town(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_town)))


    def get_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_in_cart)))

    def get_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quantity)))


    """Actions"""

    def click_phone_number(self):
        self.get_phone_number().click()
        self.get_phone_number().send_keys(1234567890)
        print("Click phone_number")

    def select_country(self):
        self.get_drop_down_country().click()
        select = Select(self.get_drop_down_country())
        select.select_by_visible_text("Ингушетия республика")
        print("select drop menu")

    def input_town(self):
        self.get_select_town().click()
        self.get_select_town().send_keys("Назрань")
        print("input town")








    """methods"""

    def product_in_cart(self):
        self.get_current_url()
        self.click_phone_number()
        # self.make_text(self.get_quantity)
        print("in cart: " + self.make_text(self.get_quantity()) + " pieces")
        self.select_country()
        self.input_town()
        self.assert_check_word(self.get_price_in_cart(), 'Корзина')
        print("assert price good")

