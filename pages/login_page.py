from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page(BasePage):
    def __init__(self, driver):
        super(). __init__(driver)


    """Locators"""

    login_button = "//a[@href='/login/']"
    user_name = "//input[@title='Логин']"
    password = "//input[@type='password']"
    enter_login_button = "//input[@type='submit']"
    check_word = "//div[contains(text(), 'Привет, Адам')]"
    cookie_button = "//button[@id='cookie-btn']"

    """getters"""

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_login_button)))

    def get_check_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_word)))

    def get_cookie_button(self):
        return WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    """actions"""

    def click_login_button(self):
        self.get_login_button().click()
        print("Click on login button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)

    def click_enter_login_button(self):
        self.get_enter_login_button().click()

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")

    def click_cookie_button(self):
        self.get_cookie_button().click()
        print("click cookie button done")

        """methods"""

    def authorization(self):
        self.get_current_url()
        self.click_cookie_button()
        self.driver.maximize_window()
        self.get_screenshot()
        self.click_login_button()
        self.input_user_name("nazran88@mail.ru")
        self.input_password("88nazran")
        self.click_enter_login_button()
        self.assert_check_word(self.get_check_word(), 'Привет, Адам')
        self.get_screenshot()