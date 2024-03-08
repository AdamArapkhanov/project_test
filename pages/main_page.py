import time

from selenium.webdriver import ActionChains, Keys
from webdriver_manager.core import driver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Main_page(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    action = ActionChains(driver)


    """locators"""

    catalog_button = "//div[@class='aside-title open-cat']"
    dom_decor_button = "(//a[@href='/category/dom-i-dekor/'])[2]"
    garniture_button = "//a[@href='/category/mir-xiaomi/naushniki-i-garnitura/']"
    price_min = "//input[@name='price_min']"
    price_max = "//input[@name='price_max']"
    add_to_cart = "(//input[@value='Добавить в корзину'][1])"
    check_word_name_product = "//span[@itemprop='name']"
    check_price_product = "//span[@class='price nowrap']"
    enter_to_cart = "//i[@class='cart-icon']"
    choose_product = "(//img[@class='lazy loaded'])[2]"
    dishes_button = "(//a[@href='/category/dom-i-dekor/dlya-kukhni/'])[3]"




    """getters"""

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_dom_decor_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dom_decor_button)))

    def get_garniture_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.garniture_button)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_choose_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_product)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_check_word_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_word_name_product)))

    def get_check_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_price_product)))

    def get_enter_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_to_cart)))

    def get_dishes_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dishes_button)))

    """actions"""

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog_button")

    def move_dom_decor_button(self):
        self.action.move_to_element(self.get_dom_decor_button())
        print("move dom_decor_button")

    def click_dom_decor_button(self):
        self.get_dom_decor_button().click()
        print("Click dom_decor_button")

    def set_price_min(self):
        self.get_price_min().send_keys(500)
        print("insert price min done")

    def set_price_max(self):
        self.get_price_max().send_keys(10000)
        print("insert price max done")
        time.sleep(5)
        self.action.send_keys(Keys.RETURN)
        print("press enter done")

    def click_choose_product(self):
        self.get_choose_product().click()
        print("Click choose_product")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Click add_to_cart")

    def click_dishes_button(self):
        self.get_dishes_button().click()
        print("Click dishes_button")

    def click_enter_to_cart(self):
        self.get_enter_to_cart().click()
        print("Click enter_to_cart")

        """methods"""

    def select_product(self):
        self.get_current_url()
        self.click_catalog_button()
        self.move_dom_decor_button()
        self.click_dom_decor_button()
        self.set_price_min()
        self.set_price_max()
        self.click_choose_product()
        self.click_add_to_cart()
        self.value_price = self.get_check_price_product().text
        # self.click_enter_to_cart()
        # self.click_dishes_button()
        self.get_screenshot()
        self.click_enter_to_cart()
